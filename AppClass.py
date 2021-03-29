import sys
from src.ui.sampleGUI import Ui_Form
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QColorDialog
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas, \
    NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
from src import Steps as Stepper
from src.backend.Signal import Signal
from src.backend.Sampler import Sampler
import numpy as np
import matplotlib.pyplot as plt

class AppClass(QtWidgets.QWidget):

    def __init__(self, parent=None): #instanciamos la clase
        super(AppClass,self).__init__(parent)

        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.GraphsWidget.setCurrentIndex(0)
        self.hideAll()

        # Testing
        # test = Sampler()
        # tValues = np.linspace(0, 1.1, 100000)
        # cosin = Signal(tValues)
        # cosin.gen_cosine(5, 5e3)
        # cosin.analize_fft()
        #
        # samp = Signal(tValues)
        # samp.gen_square(50, 50e3)
        # test.set_sampling_signal(samp)
        # test.set_input_signal(cosin)
        # test.activate_awesome_magical_signal_processing()

        # MY STUFF: cosas que necesito instanciar externas a Qt
        self.createBodePlotsCanvas()
        self.plot_list = Stepper.plot_list_specs()
        self.dumpling = Sampler()
        self.showSpecs(self.ui.ComboBoxSignal.currentText())

        # EVENT HANDLER: acciones a partir de la UI
        self.ui.ComboBoxSignal.currentIndexChanged.connect(self.change_ParamInputs)
        self.ui.ButtonActualizar.clicked.connect(self.process_input)
        #layouEtapas
        self.ui.CheckBoxFAAon.stateChanged.connect(lambda: self.toggleBypass('FAA'))
        self.ui.CheckBoxSHon.stateChanged.connect(lambda: self.toggleBypass('SH'))
        self.ui.CheckBoxLAon.stateChanged.connect(lambda: self.toggleBypass('LA'))
        self.ui.CheckBoxFRon.stateChanged.connect(lambda: self.toggleBypass('FR'))

        self.ui.checkBoxXINdraw.stateChanged.connect(lambda: self.toggleDraw('Xin'))
        self.ui.CheckBoxFAAdraw.stateChanged.connect(lambda: self.toggleDraw('FAA'))
        self.ui.CheckBoxSHdraw.stateChanged.connect(lambda: self.toggleDraw('SH'))
        self.ui.CheckBoxLAdraw.stateChanged.connect(lambda: self.toggleDraw('LA'))
        self.ui.CheckBoxFRdraw.stateChanged.connect(lambda: self.toggleDraw('FR'))
#        self.ui.CheckBoxXOUTdraw.stateChanged.connect(lambda: self.dict['Xout'].toggleDraw)

        self.ui.ButtonColorXIN.pressed.connect(lambda: self.selectColor('Xin'))
        self.ui.ButtonColorFAA.pressed.connect(lambda: self.selectColor('FAA'))
        self.ui.ButtonColorSH.pressed.connect(lambda: self.selectColor('SH'))
        self.ui.ButtonColorLA.pressed.connect(lambda: self.selectColor('LA'))
        self.ui.ButtonColorFR.pressed.connect(lambda: self.selectColor('FR'))
#        self.ui.ButtonColorXOUT.pressed.connect(lambda: self.selectColor('Xout'))

    def process_input(self):
        new_input = self.parse_input()
        if new_input['msg'] != 'ok':
            self.showmsg(new_input['msg'], 'red')
        else:
            new_sampling = self.parse_samp()
            if new_sampling['msg'] != 'ok':
                self.showmsg(new_sampling['msg'], 'red')
            else:
                self.process_signal(new_input, new_sampling)
                self.manage_plot()

    def process_signal(self, input_params, sample_params):
        self.dumpling.set_input_signal(input_params)
        self.dumpling.set_sampling_signal(sample_params)
        self.dumpling.activate_awesome_magical_signal_processing()

    def parse_input(self):
        """
               Parsea los datos cargados, en caso de estar correctamente cargados,
               crea un diccionario con el siguiente esqueleto:
               filtro = {'Type':..., 'V':X.xx, 'f':X.xx, 'phi':X.xx, 'DC':X%, 'msg':...}
        """
        signal = {}
        signal['type'] = self.ui.ComboBoxSignal.currentText()
        signal['V'] = self.ui.SpinBoxVolt.value() * (1 if self.ui.ComboBoxVolt.currentText() == 'V' else 1e-3)
        signal['f'] = self.ui.SpinBoxFreq.value() * (1 if self.ui.ComboBoxFreq.currentText() == 'Hz' else 1e3)
        signal['phi'] = (self.ui.SpinBoxTheta.value() * (1 if self.ui.ComboBoxTheta.currentText() == 'rad' else 180/np.pi)) if signal['type'] != 'Cuadrada' else None
        signal['DC'] = self.ui.SpinBoxDCinput.value() if signal['type'] == 'Cuadrada' else None
        signal['msg'] = 'ok'

        return signal

    def parse_samp(self):
        sample = {}

        if self.ui.ComboBoxT.currentText() == 's':
            multiplierT = 1
        elif self.ui.ComboBoxT.currentText() == 'ms':
            multiplierT = 1e-3
        else: #caso 'us'
            multiplierT = 1e-6

        sample['T'] = self.ui.SpinBoxT.value() * multiplierT
        sample['DC'] = self.ui.spinBoxDC.value()
        sample['msg'] = 'ok'

        return sample

    def change_ParamInputs(self):
        self.hideAll()
        signal = self.ui.ComboBoxSignal.currentText()
        self.showSpecs(signal)

    def manage_plot(self):
        w = self.ui.GraphsWidget.currentWidget()
        if w == self.ui.OscTab:
            axes = self.axes_osc
            canvas = self.canvas_osc
            plotter = self.oscplot
        else: #caso espectometro
            axes = self.axes_esp
            canvas = self.canvas_esp
            plotter = self.espplot
        axes.clear()
        axes.grid(which='both')
        plotter(axes, canvas)

    def oscplot(self, axes, canvas):
        temp_list = list(zip(self.plot_list.all_together,self.dumpling.nodeList)) #[(['name','color','draw'],Signal), ... ]
        for s in temp_list:
            if s[0][2]: #draw flag
                if s[0][1] is not None: #color var
                    axes.plot(s[1].tValues, s[1].yValues, label=s[1].description, color=self.formatColor(s[0][1]))
                else:
                    axes.plot(s[1].tValues, s[1].yValues, label=s[1].description)
        axes.set_xlabel('Eje X')
        axes.set_ylabel('Eje Y')
        axes.legend(loc='best')

        canvas.draw()

    def espplot(self, axes, canvas):
        pass


    def createBodePlotsCanvas(self):
        # creo una figura por pestaña
        self.figure_osc = Figure()
        self.figure_esp = Figure()
        # le creo un canvas a la figura
        self.canvas_osc = FigureCanvas(self.figure_osc)
        self.canvas_esp = FigureCanvas(self.figure_esp)
        # necesito algo donde poner el canvas
        plot_layout_osc = QtWidgets.QVBoxLayout()
        plot_layout_esp = QtWidgets.QVBoxLayout()
        # toolbar es la barra sobre el canvas, un verdadero amigo
        plot_layout_osc.addWidget(NavigationToolbar(self.canvas_osc, self))
        plot_layout_osc.addWidget(self.canvas_osc)
        plot_layout_esp.addWidget(NavigationToolbar(self.canvas_esp, self))
        plot_layout_esp.addWidget(self.canvas_esp)
        # tengo todos unidos, ahora lo agrego a ambas pesaña
        self.ui.OscTab.setLayout(plot_layout_osc)
        self.ui.EspecTab.setLayout(plot_layout_esp)
        # agregame el plot que sino nada tiene sentido
        self.axes_osc = self.figure_osc.add_subplot()
        self.axes_esp = self.figure_esp.add_subplot()

    def hideAll(self):
        # self.ui.labelf.setHidden(True)
        # self.ui.SpinBoxFreq.setHidden(True)
        # self.ui.ComboBoxFreq.setHidden(True)
        self.ui.labelV.setHidden(True)
        self.ui.SpinBoxVolt.setHidden(True)
        self.ui.ComboBoxVolt.setHidden(True)
        self.ui.labeltheta.setHidden(True)
        self.ui.SpinBoxTheta.setHidden(True)
        self.ui.ComboBoxTheta.setHidden(True)
        self.ui.labelDCinput.setHidden(True)
        self.ui.SpinBoxDCinput.setHidden(True)

    def showSpecs(self, type):
        if type == 'Cuadrada':
            self.ui.labelDCinput.setHidden(False)
            self.ui.SpinBoxDCinput.setHidden(False)
        else:
            self.ui.labelV.setHidden(False)
            self.ui.SpinBoxVolt.setHidden(False)
            self.ui.ComboBoxVolt.setHidden(False)
            self.ui.labeltheta.setHidden(False)
            self.ui.SpinBoxTheta.setHidden(False)
            self.ui.ComboBoxTheta.setHidden(False)

    #def manage_plot(self):

    def selectColor(self,who):
        colorDialog = QColorDialog()
        color = colorDialog.getColor()
        if color.isValid():
            self.plot_list.setColor(who,color)
            self.manage_plot()

    def formatColor(self, Qolor):
        Qolor = Qolor.getRgb()
        R = Qolor[0] / 255.0
        G = Qolor[1] / 255.0
        B = Qolor[2] / 255.0
        A = Qolor[3] / 255.0
        newColor = (R, G, B, A)

        return newColor

    def toggleDraw(self,who):
        self.plot_list.toggleDraw(who)
        self.manage_plot()


    def toggleBypass(self, who):
        toggles = {
            'FAA': self.dumpling.toggle_FAA_active,
            'SH': self.dumpling.toggle_sh_active,
            'LA': self.dumpling.toggle_switch_active,
            'FR': self.dumpling.toggle_recov_active
        }
        if who in toggles.keys():
            toggler = toggles[who]
            toggler()
            self.manage_plot()

    def showmsg(self,string,color):
        print(string)
# ------------------------------------------------------------
if __name__ == '__main__':
    MyFilterToolApp = QtWidgets.QApplication(sys.argv)
    MyFilterTool = AppClass()
    MyFilterTool.show()
    sys.exit(MyFilterToolApp.exec_())