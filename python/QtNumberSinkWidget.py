# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QtNumberSinkWidget.ui'
#
# Created: Wed Dec  4 15:51:11 2013
#      by: PyQt4 UI code generator 4.10
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_NumberSinkWidget(object):
    def setupUi(self, NumberSinkWidget):
        NumberSinkWidget.setObjectName(_fromUtf8("NumberSinkWidget"))
        NumberSinkWidget.resize(664, 571)
        self.gridLayout = QtGui.QGridLayout(NumberSinkWidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.horizontalLayout_main = QtGui.QHBoxLayout()
        self.horizontalLayout_main.setSpacing(6)
        self.horizontalLayout_main.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.horizontalLayout_main.setContentsMargins(0, 0, -1, -1)
        self.horizontalLayout_main.setObjectName(_fromUtf8("horizontalLayout_main"))
        self.groupBox_data = QtGui.QGroupBox(NumberSinkWidget)
        self.groupBox_data.setMinimumSize(QtCore.QSize(0, 180))
        self.groupBox_data.setMaximumSize(QtCore.QSize(16777215, 200))
        self.groupBox_data.setObjectName(_fromUtf8("groupBox_data"))
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBox_data)
        self.gridLayout_2.setContentsMargins(0, 9, -1, -1)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.verticalLayout_data = QtGui.QVBoxLayout()
        self.verticalLayout_data.setObjectName(_fromUtf8("verticalLayout_data"))
        self.label_data = QtGui.QLabel(self.groupBox_data)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_data.setFont(font)
        self.label_data.setAlignment(QtCore.Qt.AlignCenter)
        self.label_data.setObjectName(_fromUtf8("label_data"))
        self.verticalLayout_data.addWidget(self.label_data)
        self.progressBar_data0 = QtGui.QProgressBar(self.groupBox_data)
        self.progressBar_data0.setEnabled(True)
        self.progressBar_data0.setMaximum(10000)
        self.progressBar_data0.setProperty("value", 240)
        self.progressBar_data0.setTextVisible(False)
        self.progressBar_data0.setObjectName(_fromUtf8("progressBar_data0"))
        self.verticalLayout_data.addWidget(self.progressBar_data0)
        self.progressBar_data1 = QtGui.QProgressBar(self.groupBox_data)
        self.progressBar_data1.setMaximum(10000)
        self.progressBar_data1.setProperty("value", 2400)
        self.progressBar_data1.setTextVisible(False)
        self.progressBar_data1.setObjectName(_fromUtf8("progressBar_data1"))
        self.verticalLayout_data.addWidget(self.progressBar_data1)
        self.gridLayout_2.addLayout(self.verticalLayout_data, 0, 0, 1, 1)
        self.horizontalLayout_main.addWidget(self.groupBox_data)
        self.GroupBox_options = QtGui.QGroupBox(NumberSinkWidget)
        self.GroupBox_options.setMinimumSize(QtCore.QSize(0, 180))
        self.GroupBox_options.setMaximumSize(QtCore.QSize(160, 200))
        self.GroupBox_options.setObjectName(_fromUtf8("GroupBox_options"))
        self.gridLayout_3 = QtGui.QGridLayout(self.GroupBox_options)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.verticalLayout_options = QtGui.QVBoxLayout()
        self.verticalLayout_options.setObjectName(_fromUtf8("verticalLayout_options"))
        self.checkBox_options_peak = QtGui.QCheckBox(self.GroupBox_options)
        self.checkBox_options_peak.setObjectName(_fromUtf8("checkBox_options_peak"))
        self.verticalLayout_options.addWidget(self.checkBox_options_peak)
        self.checkBox_options_avg = QtGui.QCheckBox(self.GroupBox_options)
        self.checkBox_options_avg.setObjectName(_fromUtf8("checkBox_options_avg"))
        self.verticalLayout_options.addWidget(self.checkBox_options_avg)
        self.horizontalLayout_avg = QtGui.QHBoxLayout()
        self.horizontalLayout_avg.setObjectName(_fromUtf8("horizontalLayout_avg"))
        self.label_avg = QtGui.QLabel(self.GroupBox_options)
        self.label_avg.setEnabled(False)
        self.label_avg.setObjectName(_fromUtf8("label_avg"))
        self.horizontalLayout_avg.addWidget(self.label_avg)
        self.lcdNumber_avg = QtGui.QLCDNumber(self.GroupBox_options)
        self.lcdNumber_avg.setEnabled(False)
        self.lcdNumber_avg.setFrameShape(QtGui.QFrame.NoFrame)
        self.lcdNumber_avg.setFrameShadow(QtGui.QFrame.Plain)
        self.lcdNumber_avg.setLineWidth(0)
        self.lcdNumber_avg.setMidLineWidth(0)
        self.lcdNumber_avg.setSmallDecimalPoint(True)
        self.lcdNumber_avg.setNumDigits(5)
        self.lcdNumber_avg.setDigitCount(5)
        self.lcdNumber_avg.setMode(QtGui.QLCDNumber.Dec)
        self.lcdNumber_avg.setSegmentStyle(QtGui.QLCDNumber.Flat)
        self.lcdNumber_avg.setProperty("value", 0.333)
        self.lcdNumber_avg.setObjectName(_fromUtf8("lcdNumber_avg"))
        self.horizontalLayout_avg.addWidget(self.lcdNumber_avg)
        self.verticalLayout_options.addLayout(self.horizontalLayout_avg)
        self.horizontalSlider_avg = QtGui.QSlider(self.GroupBox_options)
        self.horizontalSlider_avg.setEnabled(False)
        self.horizontalSlider_avg.setMaximum(10000)
        self.horizontalSlider_avg.setSingleStep(1)
        self.horizontalSlider_avg.setPageStep(1)
        self.horizontalSlider_avg.setProperty("value", 3333)
        self.horizontalSlider_avg.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_avg.setTickInterval(0)
        self.horizontalSlider_avg.setObjectName(_fromUtf8("horizontalSlider_avg"))
        self.verticalLayout_options.addWidget(self.horizontalSlider_avg)
        self.pushButton_hold = QtGui.QPushButton(self.GroupBox_options)
        self.pushButton_hold.setObjectName(_fromUtf8("pushButton_hold"))
        self.verticalLayout_options.addWidget(self.pushButton_hold)
        self.gridLayout_3.addLayout(self.verticalLayout_options, 0, 0, 1, 1)
        self.horizontalLayout_main.addWidget(self.GroupBox_options)
        self.horizontalLayout_main.setStretch(1, 10)
        self.gridLayout.addLayout(self.horizontalLayout_main, 0, 0, 1, 1)

        self.retranslateUi(NumberSinkWidget)
        QtCore.QObject.connect(self.checkBox_options_avg, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.label_avg.setEnabled)
        QtCore.QObject.connect(self.checkBox_options_avg, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.lcdNumber_avg.setEnabled)
        QtCore.QObject.connect(self.checkBox_options_avg, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.horizontalSlider_avg.setEnabled)
        QtCore.QObject.connect(self.pushButton_hold, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.pushButton_hold.setEnabled)
        QtCore.QObject.connect(self.horizontalSlider_avg, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), NumberSinkWidget.valueChangedFrac)
        QtCore.QObject.connect(self.pushButton_hold, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), NumberSinkWidget.buttonHoldClicked)
        QtCore.QObject.connect(self.checkBox_options_avg, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), NumberSinkWidget.activateAverage)
        QtCore.QObject.connect(self.checkBox_options_peak, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), NumberSinkWidget.activatePeakHold)
        QtCore.QObject.connect(NumberSinkWidget, QtCore.SIGNAL(_fromUtf8("setAverage(bool)")), self.checkBox_options_avg.setChecked)
        QtCore.QObject.connect(NumberSinkWidget, QtCore.SIGNAL(_fromUtf8("setPeakHold(bool)")), self.checkBox_options_peak.setChecked)
        QtCore.QObject.connect(NumberSinkWidget, QtCore.SIGNAL(_fromUtf8("setValueText(QString)")), self.label_data.setText)
        QtCore.QObject.connect(NumberSinkWidget, QtCore.SIGNAL(_fromUtf8("setRealBar(int)")), self.progressBar_data0.setValue)
        QtCore.QObject.connect(NumberSinkWidget, QtCore.SIGNAL(_fromUtf8("setImagBar(int)")), self.progressBar_data1.setValue)
        QtCore.QObject.connect(NumberSinkWidget, QtCore.SIGNAL(_fromUtf8("setBarRange(int,int)")), self.progressBar_data0.setRange)
        QtCore.QObject.connect(NumberSinkWidget, QtCore.SIGNAL(_fromUtf8("setBarRange(int,int)")), self.progressBar_data1.setRange)
        QtCore.QObject.connect(NumberSinkWidget, QtCore.SIGNAL(_fromUtf8("displayLcdNumberAvgValue(double)")), self.lcdNumber_avg.display)
        QtCore.QObject.connect(NumberSinkWidget, QtCore.SIGNAL(_fromUtf8("setSliderValue(int)")), self.horizontalSlider_avg.setValue)
        QtCore.QObject.connect(NumberSinkWidget, QtCore.SIGNAL(_fromUtf8("setRealBarVisible(bool)")), self.progressBar_data0.setVisible)
        QtCore.QObject.connect(NumberSinkWidget, QtCore.SIGNAL(_fromUtf8("setImagBarVisible(bool)")), self.progressBar_data1.setVisible)
        QtCore.QMetaObject.connectSlotsByName(NumberSinkWidget)

    def retranslateUi(self, NumberSinkWidget):
        NumberSinkWidget.setWindowTitle(_translate("NumberSinkWidget", "Form", None))
        self.groupBox_data.setTitle(_translate("NumberSinkWidget", "Qt Number Plot", None))
        self.label_data.setText(_translate("NumberSinkWidget", "Value", None))
        self.GroupBox_options.setTitle(_translate("NumberSinkWidget", "Options", None))
        self.checkBox_options_peak.setText(_translate("NumberSinkWidget", "Peak Hold", None))
        self.checkBox_options_avg.setText(_translate("NumberSinkWidget", "Average", None))
        self.label_avg.setText(_translate("NumberSinkWidget", "Avg Alpha:", None))
        self.pushButton_hold.setText(_translate("NumberSinkWidget", "Stop", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    NumberSinkWidget = QtGui.QWidget()
    ui = Ui_NumberSinkWidget()
    ui.setupUi(NumberSinkWidget)
    NumberSinkWidget.show()
    sys.exit(app.exec_())

