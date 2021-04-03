# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sampleGUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

import os
import ctypes.wintypes


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(839, 655)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.InputZone = QtWidgets.QVBoxLayout()
        self.InputZone.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.InputZone.setContentsMargins(-1, 0, -1, -1)
        self.InputZone.setSpacing(10)
        self.InputZone.setObjectName("InputZone")
        self.InputLabel = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.InputLabel.sizePolicy().hasHeightForWidth())
        self.InputLabel.setSizePolicy(sizePolicy)
        self.InputLabel.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.InputLabel.setFont(font)
        self.InputLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.InputLabel.setFrameShadow(QtWidgets.QFrame.Plain)
        self.InputLabel.setObjectName("InputLabel")
        self.InputZone.addWidget(self.InputLabel)
        self.LayoutInputType = QtWidgets.QHBoxLayout()
        self.LayoutInputType.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.LayoutInputType.setContentsMargins(-1, 0, -1, -1)
        self.LayoutInputType.setObjectName("LayoutInputType")
        self.ComboBoxSignal = QtWidgets.QComboBox(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ComboBoxSignal.sizePolicy().hasHeightForWidth())
        self.ComboBoxSignal.setSizePolicy(sizePolicy)
        self.ComboBoxSignal.setObjectName("ComboBoxSignal")
        self.ComboBoxSignal.addItem("")
        self.ComboBoxSignal.addItem("")
        self.ComboBoxSignal.addItem("")
        self.LayoutInputType.addWidget(self.ComboBoxSignal)
        self.InputZone.addLayout(self.LayoutInputType)
        self.gridInput = QtWidgets.QGridLayout()
        self.gridInput.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridInput.setVerticalSpacing(16)
        self.gridInput.setObjectName("gridInput")
        self.SpinBoxVolt = QtWidgets.QDoubleSpinBox(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SpinBoxVolt.sizePolicy().hasHeightForWidth())
        self.SpinBoxVolt.setSizePolicy(sizePolicy)
        self.SpinBoxVolt.setMaximum(999.99)
        self.SpinBoxVolt.setObjectName("SpinBoxVolt")
        self.gridInput.addWidget(self.SpinBoxVolt, 0, 1, 1, 1)
        self.labelf = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.labelf.setFont(font)
        self.labelf.setObjectName("labelf")
        self.gridInput.addWidget(self.labelf, 1, 0, 1, 1)
        self.ComboBoxFreq = QtWidgets.QComboBox(Form)
        self.ComboBoxFreq.setObjectName("ComboBoxFreq")
        self.ComboBoxFreq.addItem("")
        self.ComboBoxFreq.addItem("")
        self.gridInput.addWidget(self.ComboBoxFreq, 1, 2, 1, 1)
        self.labelV = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelV.sizePolicy().hasHeightForWidth())
        self.labelV.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.labelV.setFont(font)
        self.labelV.setObjectName("labelV")
        self.gridInput.addWidget(self.labelV, 0, 0, 1, 1)
        self.ComboBoxVolt = QtWidgets.QComboBox(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ComboBoxVolt.sizePolicy().hasHeightForWidth())
        self.ComboBoxVolt.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.ComboBoxVolt.setFont(font)
        self.ComboBoxVolt.setObjectName("ComboBoxVolt")
        self.ComboBoxVolt.addItem("")
        self.ComboBoxVolt.addItem("")
        self.gridInput.addWidget(self.ComboBoxVolt, 0, 2, 1, 1)
        self.SpinBoxFreq = QtWidgets.QDoubleSpinBox(Form)
        self.SpinBoxFreq.setMaximum(999.99)
        self.SpinBoxFreq.setObjectName("SpinBoxFreq")
        self.gridInput.addWidget(self.SpinBoxFreq, 1, 1, 1, 1)
        self.labeltheta = QtWidgets.QLabel(Form)
        self.labeltheta.setObjectName("labeltheta")
        self.gridInput.addWidget(self.labeltheta, 2, 0, 1, 1)
        self.ComboBoxTheta = QtWidgets.QComboBox(Form)
        self.ComboBoxTheta.setObjectName("ComboBoxTheta")
        self.ComboBoxTheta.addItem("")
        self.ComboBoxTheta.addItem("")
        self.ComboBoxTheta.addItem("")
        self.gridInput.addWidget(self.ComboBoxTheta, 2, 2, 1, 1)
        self.SpinBoxTheta = QtWidgets.QDoubleSpinBox(Form)
        self.SpinBoxTheta.setMaximum(999.99)
        self.SpinBoxTheta.setObjectName("SpinBoxTheta")
        self.gridInput.addWidget(self.SpinBoxTheta, 2, 1, 1, 1)
        self.labelDCinput = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.labelDCinput.setFont(font)
        self.labelDCinput.setObjectName("labelDCinput")
        self.gridInput.addWidget(self.labelDCinput, 3, 0, 1, 1)
        self.SpinBoxDCinput = QtWidgets.QSpinBox(Form)
        self.SpinBoxDCinput.setMinimum(5)
        self.SpinBoxDCinput.setMaximum(95)
        self.SpinBoxDCinput.setObjectName("SpinBoxDCinput")
        self.gridInput.addWidget(self.SpinBoxDCinput, 3, 1, 1, 1)
        self.InputZone.addLayout(self.gridInput)
        self.label_Sampling = QtWidgets.QLabel(Form)
        self.label_Sampling.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_Sampling.setFont(font)
        self.label_Sampling.setFrameShape(QtWidgets.QFrame.Box)
        self.label_Sampling.setObjectName("label_Sampling")
        self.InputZone.addWidget(self.label_Sampling)
        self.gridSampling = QtWidgets.QGridLayout()
        self.gridSampling.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridSampling.setObjectName("gridSampling")
        self.labelT = QtWidgets.QLabel(Form)
        self.labelT.setObjectName("labelT")
        self.gridSampling.addWidget(self.labelT, 0, 0, 1, 1)
        self.SpinBoxT = QtWidgets.QDoubleSpinBox(Form)
        self.SpinBoxT.setObjectName("SpinBoxT")
        self.gridSampling.addWidget(self.SpinBoxT, 0, 1, 1, 1)
        self.ComboBoxT = QtWidgets.QComboBox(Form)
        self.ComboBoxT.setObjectName("ComboBoxT")
        self.ComboBoxT.addItem("")
        self.ComboBoxT.addItem("")
        self.ComboBoxT.addItem("")
        self.gridSampling.addWidget(self.ComboBoxT, 0, 2, 1, 1)
        self.labelDC = QtWidgets.QLabel(Form)
        self.labelDC.setObjectName("labelDC")
        self.gridSampling.addWidget(self.labelDC, 1, 0, 1, 1)
        self.spinBoxDC = QtWidgets.QSpinBox(Form)
        self.spinBoxDC.setObjectName("spinBoxDC")
        self.gridSampling.addWidget(self.spinBoxDC, 1, 1, 1, 1)
        self.InputZone.addLayout(self.gridSampling)
        self.ButtonActualizar = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ButtonActualizar.sizePolicy().hasHeightForWidth())
        self.ButtonActualizar.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.ButtonActualizar.setFont(font)
        self.ButtonActualizar.setCheckable(False)
        self.ButtonActualizar.setObjectName("ButtonActualizar")
        self.InputZone.addWidget(self.ButtonActualizar)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.InputZone.addItem(spacerItem)
        self.horizontalLayout.addLayout(self.InputZone)
        self.LayoutGraph = QtWidgets.QVBoxLayout()
        self.LayoutGraph.setObjectName("LayoutGraph")
        self.GraphsWidget = QtWidgets.QTabWidget(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.GraphsWidget.sizePolicy().hasHeightForWidth())
        self.GraphsWidget.setSizePolicy(sizePolicy)
        self.GraphsWidget.setObjectName("GraphsWidget")
        self.OscTab = QtWidgets.QWidget()
        self.OscTab.setObjectName("OscTab")
        self.GraphsWidget.addTab(self.OscTab, "")
        self.EspecTab = QtWidgets.QWidget()
        self.EspecTab.setObjectName("EspecTab")
        self.GraphsWidget.addTab(self.EspecTab, "")
        self.LayoutGraph.addWidget(self.GraphsWidget)
        self.LayoutEtapas = QtWidgets.QGridLayout()
        self.LayoutEtapas.setHorizontalSpacing(32)
        self.LayoutEtapas.setVerticalSpacing(6)
        self.LayoutEtapas.setObjectName("LayoutEtapas")
        self.CheckBoxLAdraw = QtWidgets.QCheckBox(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CheckBoxLAdraw.sizePolicy().hasHeightForWidth())
        self.CheckBoxLAdraw.setSizePolicy(sizePolicy)
        self.CheckBoxLAdraw.setText("")
        self.CheckBoxLAdraw.setObjectName("CheckBoxLAdraw")
        self.LayoutEtapas.addWidget(self.CheckBoxLAdraw, 4, 3, 1, 1)
        self.label_15 = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_15.sizePolicy().hasHeightForWidth())
        self.label_15.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setAlignment(QtCore.Qt.AlignCenter)
        self.label_15.setObjectName("label_15")
        self.LayoutEtapas.addWidget(self.label_15, 4, 1, 1, 1)
        self.ButtonColorFAA = QtWidgets.QToolButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ButtonColorFAA.sizePolicy().hasHeightForWidth())
        self.ButtonColorFAA.setSizePolicy(sizePolicy)
        self.ButtonColorFAA.setText("")
        icon = QtGui.QIcon()
        # icon.addPixmap(QtGui.QPixmap("src/resources/assets/color.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap(os.getcwd() + '/assets/color.png'), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ButtonColorFAA.setIcon(icon)
        self.ButtonColorFAA.setObjectName("ButtonColorFAA")
        self.LayoutEtapas.addWidget(self.ButtonColorFAA, 2, 4, 1, 1)
        self.label_10 = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.LayoutEtapas.addWidget(self.label_10, 0, 1, 1, 1)
        self.CheckBoxFAAon = QtWidgets.QCheckBox(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CheckBoxFAAon.sizePolicy().hasHeightForWidth())
        self.CheckBoxFAAon.setSizePolicy(sizePolicy)
        self.CheckBoxFAAon.setText("")
        self.CheckBoxFAAon.setChecked(True)
        self.CheckBoxFAAon.setObjectName("CheckBoxFAAon")
        self.LayoutEtapas.addWidget(self.CheckBoxFAAon, 2, 2, 1, 1)
        self.label_7 = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.LayoutEtapas.addWidget(self.label_7, 1, 1, 1, 1)
        self.CheckBoxSHdraw = QtWidgets.QCheckBox(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CheckBoxSHdraw.sizePolicy().hasHeightForWidth())
        self.CheckBoxSHdraw.setSizePolicy(sizePolicy)
        self.CheckBoxSHdraw.setText("")
        self.CheckBoxSHdraw.setObjectName("CheckBoxSHdraw")
        self.LayoutEtapas.addWidget(self.CheckBoxSHdraw, 3, 3, 1, 1)
        self.checkBoxXINdraw = QtWidgets.QCheckBox(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBoxXINdraw.sizePolicy().hasHeightForWidth())
        self.checkBoxXINdraw.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.checkBoxXINdraw.setFont(font)
        self.checkBoxXINdraw.setText("")
        self.checkBoxXINdraw.setObjectName("checkBoxXINdraw")
        self.LayoutEtapas.addWidget(self.checkBoxXINdraw, 1, 3, 1, 1)
        self.label_12 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.LayoutEtapas.addWidget(self.label_12, 0, 2, 1, 1)
        self.label_9 = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.LayoutEtapas.addWidget(self.label_9, 0, 3, 1, 1)
        self.label_13 = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.LayoutEtapas.addWidget(self.label_13, 2, 1, 1, 1)
        self.CheckBoxLAon = QtWidgets.QCheckBox(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CheckBoxLAon.sizePolicy().hasHeightForWidth())
        self.CheckBoxLAon.setSizePolicy(sizePolicy)
        self.CheckBoxLAon.setText("")
        self.CheckBoxLAon.setChecked(True)
        self.CheckBoxLAon.setObjectName("CheckBoxLAon")
        self.LayoutEtapas.addWidget(self.CheckBoxLAon, 4, 2, 1, 1)
        self.ButtonColorLA = QtWidgets.QToolButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ButtonColorLA.sizePolicy().hasHeightForWidth())
        self.ButtonColorLA.setSizePolicy(sizePolicy)
        self.ButtonColorLA.setText("")
        self.ButtonColorLA.setIcon(icon)
        self.ButtonColorLA.setObjectName("ButtonColorLA")
        self.LayoutEtapas.addWidget(self.ButtonColorLA, 4, 4, 1, 1)
        self.ButtonColorFR = QtWidgets.QToolButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ButtonColorFR.sizePolicy().hasHeightForWidth())
        self.ButtonColorFR.setSizePolicy(sizePolicy)
        self.ButtonColorFR.setText("")
        self.ButtonColorFR.setIcon(icon)
        self.ButtonColorFR.setObjectName("ButtonColorFR")
        self.LayoutEtapas.addWidget(self.ButtonColorFR, 5, 4, 1, 1)
        self.CheckBoxSHon = QtWidgets.QCheckBox(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CheckBoxSHon.sizePolicy().hasHeightForWidth())
        self.CheckBoxSHon.setSizePolicy(sizePolicy)
        self.CheckBoxSHon.setText("")
        self.CheckBoxSHon.setChecked(True)
        self.CheckBoxSHon.setObjectName("CheckBoxSHon")
        self.LayoutEtapas.addWidget(self.CheckBoxSHon, 3, 2, 1, 1)
        self.CheckBoxFAAdraw = QtWidgets.QCheckBox(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CheckBoxFAAdraw.sizePolicy().hasHeightForWidth())
        self.CheckBoxFAAdraw.setSizePolicy(sizePolicy)
        self.CheckBoxFAAdraw.setText("")
        self.CheckBoxFAAdraw.setObjectName("CheckBoxFAAdraw")
        self.LayoutEtapas.addWidget(self.CheckBoxFAAdraw, 2, 3, 1, 1)
        self.ButtonColorSH = QtWidgets.QToolButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ButtonColorSH.sizePolicy().hasHeightForWidth())
        self.ButtonColorSH.setSizePolicy(sizePolicy)
        self.ButtonColorSH.setText("")
        self.ButtonColorSH.setIcon(icon)
        self.ButtonColorSH.setObjectName("ButtonColorSH")
        self.LayoutEtapas.addWidget(self.ButtonColorSH, 3, 4, 1, 1)
        self.label_11 = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.LayoutEtapas.addWidget(self.label_11, 0, 4, 1, 1)
        self.CheckBoxFRdraw = QtWidgets.QCheckBox(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CheckBoxFRdraw.sizePolicy().hasHeightForWidth())
        self.CheckBoxFRdraw.setSizePolicy(sizePolicy)
        self.CheckBoxFRdraw.setText("")
        self.CheckBoxFRdraw.setObjectName("CheckBoxFRdraw")
        self.LayoutEtapas.addWidget(self.CheckBoxFRdraw, 5, 3, 1, 1)
        self.ButtonColorXIN = QtWidgets.QToolButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ButtonColorXIN.sizePolicy().hasHeightForWidth())
        self.ButtonColorXIN.setSizePolicy(sizePolicy)
        self.ButtonColorXIN.setText("")
        self.ButtonColorXIN.setIcon(icon)
        self.ButtonColorXIN.setObjectName("ButtonColorXIN")
        self.LayoutEtapas.addWidget(self.ButtonColorXIN, 1, 4, 1, 1)
        self.CheckBoxFRon = QtWidgets.QCheckBox(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CheckBoxFRon.sizePolicy().hasHeightForWidth())
        self.CheckBoxFRon.setSizePolicy(sizePolicy)
        self.CheckBoxFRon.setText("")
        self.CheckBoxFRon.setChecked(True)
        self.CheckBoxFRon.setObjectName("CheckBoxFRon")
        self.LayoutEtapas.addWidget(self.CheckBoxFRon, 5, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.LayoutEtapas.addItem(spacerItem1, 3, 5, 1, 1)
        self.label_16 = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_16.sizePolicy().hasHeightForWidth())
        self.label_16.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_16.setFont(font)
        self.label_16.setAlignment(QtCore.Qt.AlignCenter)
        self.label_16.setObjectName("label_16")
        self.LayoutEtapas.addWidget(self.label_16, 5, 1, 1, 1)
        self.label_14 = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setObjectName("label_14")
        self.LayoutEtapas.addWidget(self.label_14, 3, 1, 1, 1)
        self.LayoutGraph.addLayout(self.LayoutEtapas)
        self.horizontalLayout.addLayout(self.LayoutGraph)

        self.retranslateUi(Form)
        self.GraphsWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.InputLabel.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">INPUT</span></p></body></html>"))
        self.ComboBoxSignal.setItemText(0, _translate("Form", "Coseno"))
        self.ComboBoxSignal.setItemText(1, _translate("Form", "3/2 Seno"))
        self.ComboBoxSignal.setItemText(2, _translate("Form", "Cuadrada"))
        self.labelf.setText(_translate("Form", "<html><head/><body><p align=\"center\">f</p></body></html>"))
        self.ComboBoxFreq.setItemText(0, _translate("Form", "kHz"))
        self.ComboBoxFreq.setItemText(1, _translate("Form", "Hz"))
        self.labelV.setText(_translate("Form", "<html><head/><body><p align=\"center\">V<span style=\" vertical-align:sub;\">P</span></p></body></html>"))
        self.ComboBoxVolt.setItemText(0, _translate("Form", "V"))
        self.ComboBoxVolt.setItemText(1, _translate("Form", "mV"))
        self.labeltheta.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-family:\'arial\',\'sans-serif\'; font-size:16px; font-weight:600; color:#202124; background-color:#ffffff;\">θ</span></p></body></html>"))
        self.ComboBoxTheta.setItemText(0, _translate("Form", "º"))
        self.ComboBoxTheta.setItemText(1, _translate("Form", "rad"))
        self.ComboBoxTheta.setItemText(2, _translate("Form", "π"))
        self.labelDCinput.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">DC [%]</span></p></body></html>"))
        self.label_Sampling.setText(_translate("Form", "<html><head/><body><p align=\"center\">SAMPLING</p></body></html>"))
        self.labelT.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">T</span></p></body></html>"))
        self.ComboBoxT.setItemText(0, _translate("Form", "s"))
        self.ComboBoxT.setItemText(1, _translate("Form", "ms"))
        self.ComboBoxT.setItemText(2, _translate("Form", "us"))
        self.labelDC.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">DC [%]</span></p></body></html>"))
        self.ButtonActualizar.setText(_translate("Form", "Actualizar"))
        self.GraphsWidget.setTabText(self.GraphsWidget.indexOf(self.OscTab), _translate("Form", "Osciloscopio"))
        self.GraphsWidget.setTabText(self.GraphsWidget.indexOf(self.EspecTab), _translate("Form", "Analizador de Espectros"))
        self.label_15.setText(_translate("Form", "   LA"))
        self.label_10.setText(_translate("Form", "Etapas"))
        self.label_7.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">X</span><span style=\" font-weight:600; vertical-align:sub;\">IN</span></p></body></html>"))
        self.label_12.setText(_translate("Form", "ON"))
        self.label_9.setText(_translate("Form", "Plot"))
        self.label_13.setText(_translate("Form", "   FAA"))
        self.label_11.setText(_translate("Form", "Color"))
        self.label_16.setText(_translate("Form", "<html><head/><body><p>   FR/X<span style=\" vertical-align:sub;\">OUT</span></p></body></html>"))
        self.label_14.setText(_translate("Form", "   S&H"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
