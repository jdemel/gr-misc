# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QwtCompassWidget.ui'
#
# Created: Wed Dec  4 15:28:12 2013
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

class Ui_QwtCompassWidget(object):
    def setupUi(self, QwtCompassWidget):
        QwtCompassWidget.setObjectName(_fromUtf8("QwtCompassWidget"))
        QwtCompassWidget.setEnabled(True)
        QwtCompassWidget.resize(524, 452)
        self.gridLayout_2 = QtGui.QGridLayout(QwtCompassWidget)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.Compass = QwtCompass(QwtCompassWidget)
        self.Compass.setProperty("visibleBackground", True)
        self.Compass.setLineWidth(2)
        self.Compass.setFrameShadow(QwtDial.Plain)
        self.Compass.setObjectName(_fromUtf8("Compass"))
        self.gridLayout.addWidget(self.Compass, 0, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.retranslateUi(QwtCompassWidget)
        QtCore.QObject.connect(QwtCompassWidget, QtCore.SIGNAL(_fromUtf8("setCompassValue(double)")), self.Compass.setValue)
        QtCore.QMetaObject.connectSlotsByName(QwtCompassWidget)

    def retranslateUi(self, QwtCompassWidget):
        QwtCompassWidget.setWindowTitle(_translate("QwtCompassWidget", "Form", None))

from PyQt4.Qwt5 import QwtDial
from PyQt4.Qwt5 import QwtCompass

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    QwtCompassWidget = QtGui.QWidget()
    ui = Ui_QwtCompassWidget()
    ui.setupUi(QwtCompassWidget)
    QwtCompassWidget.show()
    sys.exit(app.exec_())

