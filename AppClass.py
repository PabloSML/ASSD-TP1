import sys
from src.ui.sampleGUI import Ui_Form
from PyQt5 import QtCore, QtGui, QtWidgets


class AppClass(QtWidgets.QWidget):

    def __init__(self, parent=None): #instanciamos la clase
        super(AppClass,self).__init__(parent)

        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.GraphsWidget.setCurrentIndex(0)



# ------------------------------------------------------------
if __name__ == '__main__':
    MyFilterToolApp = QtWidgets.QApplication(sys.argv)
    MyFilterTool = AppCLass()
    MyFilterTool.show()
    sys.exit(MyFilterToolApp.exec_())