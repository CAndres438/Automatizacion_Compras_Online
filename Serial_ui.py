# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Inicializar.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Serial(object):
    def setupUi(self, Serial):
        Serial.setObjectName("Serial")
        Serial.resize(491, 256)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/imagenes/imagenes/shul.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        Serial.setWindowIcon(icon)
        Serial.setStyleSheet("\n"
"color: rgb(30,29,29);\n"
"font: 75 8pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(30,29,29);")
        self.label = QtWidgets.QLabel(Serial)
        self.label.setGeometry(QtCore.QRect(10, 220, 471, 21))
        self.label.setStyleSheet("background-image: url(:/imagenes/imagenes/vita.png);\n"
"font: 8pt \"MS Shell Dlg 2\";\n"
"color: rgb(187, 181, 181);\n"
"text align:  center;")
        self.label.setObjectName("label")
        self.pushbigin = QtWidgets.QPushButton(Serial)
        self.pushbigin.setGeometry(QtCore.QRect(10, 10, 481, 201))
        self.pushbigin.setStyleSheet("background-image: url(:/imagenes/imagenes/logo.ico);\n"
"background-attachment: fixed;\n"
"background-position: center center;\n"
"background-size: cover;\n"
"background-repeat: no-repeat;\n"
"border-style:solid;\n"
"border-width:0px;\n"
"border-color: rgba(30,29,29);")
        self.pushbigin.setObjectName("pushbigin")
        self.serialtxt = QtWidgets.QTextEdit(Serial)
        self.serialtxt.setGeometry(QtCore.QRect(145, 180, 200, 25))
        self.serialtxt.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.serialtxt.setMouseTracking(True)
        self.serialtxt.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.serialtxt.setStyleSheet("border-style: solid;\n"
"font: 75 8pt \"MS Shell Dlg 2\";\n"
"border-width: 0px;\n"
"border-color: rgba(50,48,48);\n"
"background-color: rgba(50,48,48); \n"
"color: rgb(229, 9, 127);\n"
"border-radius: 10px;\n"
"padding-top:1px;\n"
"padding-left:10px;\n"
"padding-rigth:10px;\n"
"")

        self.serialtxt.setObjectName("serialtxt")

        self.retranslateUi(Serial)
        QtCore.QMetaObject.connectSlotsByName(Serial)

    def retranslateUi(self, Serial):
        _translate = QtCore.QCoreApplication.translate
        Serial.setWindowTitle(_translate("Inicializar", "Inicio"))
        self.label.setText(_translate("Inicializar", "                   Somnium 1.0, Windows Version/21 - automation technologies with Selenium "))
        self.pushbigin.setText(_translate("Inicializar", "PushButton"))
import an_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Serial = QtWidgets.QWidget()
    ui = Ui_Serial()
    ui.setupUi(Serial)
    Serial.show()
    sys.exit(app.exec_())
