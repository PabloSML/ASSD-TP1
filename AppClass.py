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

class AppClass(QtWidgets.QWidget):

    def __init__(self, parent=None): #instanciamos la clase
        super(AppClass,self).__init__(parent)

        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.GraphsWidget.setCurrentIndex(0)
        self.hideAll()

        # Testing
        test = Sampler()
        tValues = np.linspace(0, 1.1, 100000)
        cosin = Signal(tValues)
        cosin.gen_cosine(5, 5e3)
        cosin.analize_fft()

        samp = Signal(tValues)
        samp.gen_square(50, 50e3)
        test.set_sampling_signal(samp)
        test.set_input_signal(cosin)
        test.activate_awesome_magical_signal_processing()

        # MY STUFF: cosas que necesito instanciar externas a Qt
        self.createBodePlotsCanvas()
        self.dict = {'Xin': Stepper.step(),
                     'FAA': Stepper.step(),
                     'SH':  Stepper.step(),
                     'LA':  Stepper.step(),
                     'FR':  Stepper.step(),
                     'Xout':Stepper.step()}
        self.dumpling = Sampler()
        self.showSpecs(self.ui.ComboBoxSignal.currentText())

        # EVENT HANDLER: acciones a partir de la UI
        self.ui.ComboBoxSignal.currentIndexChanged.connect(self.change_ParamInputs)
        self.ui.ButtonActualizar.clicked.connect(self.process_input)
        #layouEtapas
        self.ui.CheckBoxFAAon.stateChanged.connect(self.dict['FAA'].toggleBypass)
        self.ui.CheckBoxSHon.stateChanged.connect(self.dict['SH'].toggleBypass)
        self.ui.CheckBoxLAon.stateChanged.connect(self.dict['LA'].toggleBypass)
        self.ui.CheckBoxFRon.stateChanged.connect(self.dict['FR'].toggleBypass)

        self.ui.checkBoxXINdraw.stateChanged.connect(self.dict['Xin'].toggleDraw)
        self.ui.CheckBoxFAAdraw.stateChanged.connect(self.dict['FAA'].toggleDraw)
        self.ui.CheckBoxSHdraw.stateChanged.connect(self.dict['SH'].toggleDraw)
        self.ui.CheckBoxLAdraw.stateChanged.connect(self.dict['LA'].toggleDraw)
        self.ui.CheckBoxFRdraw.stateChanged.connect(self.dict['FR'].toggleDraw)
        self.ui.CheckBoxXOUTdraw.stateChanged.connect(self.dict['Xout'].toggleDraw)

        self.ui.ButtonColorXIN.pressed.connect(lambda: self.selectColor('Xin'))
        self.ui.ButtonColorFAA.pressed.connect(lambda: self.selectColor('FAA'))
        self.ui.ButtonColorSH.pressed.connect(lambda: self.selectColor('SH'))
        self.ui.ButtonColorLA.pressed.connect(lambda: self.selectColor('LA'))
        self.ui.ButtonColorFR.pressed.connect(lambda: self.selectColor('FR'))
        self.ui.ButtonColorXOUT.pressed.connect(lambda: self.selectColor('Xout'))

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

    def process_signal(self, input, sample):
        #tValues = np.linspace(0, 2/input['f'], 100000) #quiero 2 periodos con queso extra
        self.dumpling.set_sampling_signal(sample)
        self.dumpling.set_input_signal(input)
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
        x = 1 # todo make me my master

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
        # self.ui.labelV.setHidden(True)
        # self.ui.SpinBoxVolt.setHidden(True)
        # self.ui.ComboBoxVolt.setHidden(True)
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
            self.ui.labeltheta.setHidden(False)
            self.ui.SpinBoxTheta.setHidden(False)
            self.ui.ComboBoxTheta.setHidden(False)

    #def manage_plot(self):

    def selectColor(self,who):
        colorDialog = QColorDialog()
        color = colorDialog.getColor()
        if color.isValid():
            self.dict[who].setColor(color)
            self.manage_plot()

    def showmsg(self,string,color):
        print(string)
# ------------------------------------------------------------
if __name__ == '__main__':
    MyFilterToolApp = QtWidgets.QApplication(sys.argv)
    MyFilterTool = AppClass()
    MyFilterTool.show()
    sys.exit(MyFilterToolApp.exec_())