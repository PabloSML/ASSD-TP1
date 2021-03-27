import sys
from src.ui.sampleGUI import Ui_Form
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QColorDialog
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas, \
    NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
from src import Steps as Stepper
import numpy as np

class AppClass(QtWidgets.QWidget):

    def __init__(self, parent=None): #instanciamos la clase
        super(AppClass,self).__init__(parent)

        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.GraphsWidget.setCurrentIndex(0)
        self.hideAll()

        # MY STUFF: cosas que necesito instanciar externas a Qt
        self.createBodePlotsCanvas()
        self.dict = {'Xin': Stepper.step(),
                     'FAA': Stepper.step(),
                     'SH':  Stepper.step(),
                     'LA':  Stepper.step(),
                     'FR':  Stepper.step(),
                     'Xout':Stepper.step()}

        self.showSpecs(self.ui.ComboBoxSignal.currentText())

        # EVENT HANDLER: acciones a partir de la UI
        self.ui.ComboBoxSignal.currentIndexChanged.connect(self.change_ParamInputs)
        #self.ui.ButtonActualizar.clicked.connect()
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

    def change_ParamInputs(self):
        self.hideAll()
        signal = self.ui.ComboBoxSignal.currentText()
        self.showSpecs(signal)
    def manage_plot(self):
        x = 1 # todo make me master
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
        # self.ui.labeltheta.setHidden(True)
        # self.ui.SpinBoxTheta.setHidden(True)
        # self.ui.ComboBoxTheta.setHidden(True)
        self.ui.labelDCinput.setHidden(True)
        self.ui.SpinBoxDCinput.setHidden(True)

    def showSpecs(self, type):
        if type == 'Cuadrada':
            self.ui.labelDCinput.setHidden(False)
            self.ui.SpinBoxDCinput.setHidden(False)

    #def manage_plot(self):

    def selectColor(self,who):
        colorDialog = QColorDialog()
        color = colorDialog.getColor()
        if color.isValid():
            self.dict[who].setColor(color)
            self.manage_plot()

# ------------------------------------------------------------
if __name__ == '__main__':
    MyFilterToolApp = QtWidgets.QApplication(sys.argv)
    MyFilterTool = AppClass()
    MyFilterTool.show()
    sys.exit(MyFilterToolApp.exec_())