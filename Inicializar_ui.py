# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Inicializar.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Inicializar(object):
    def setupUi(self, Inicializar):
        Inicializar.setObjectName("Inicializar")
        Inicializar.resize(491, 256)
        Inicializar.setStyleSheet("\n"
"color: rgb(30,29,29);\n"
"font: 75 8pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(30,29,29);")
        self.label = QtWidgets.QLabel(Inicializar)
        self.label.setGeometry(QtCore.QRect(10, 220, 471, 21))
        self.label.setStyleSheet("background-image: url(:/imagenes/imagenes/vita.png);\n"
"font: 8pt \"MS Shell Dlg 2\";\n"
"color: rgb(187, 181, 181);\n"
"text align:  center;")
        self.label.setObjectName("label")
        self.pushbigin = QtWidgets.QPushButton(Inicializar)
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

        self.retranslateUi(Inicializar)
        QtCore.QMetaObject.connectSlotsByName(Inicializar)

    def retranslateUi(self, Inicializar):
        _translate = QtCore.QCoreApplication.translate
        Inicializar.setWindowTitle(_translate("Inicializar", "Form"))
        self.label.setText(_translate("Inicializar", "           Somnium 1.0, Windows Version/21 - automation technologies by Daalu with Selenium "))
        self.pushbigin.setText(_translate("Inicializar", "PushButton"))
import an_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Inicializar = QtWidgets.QWidget()
    ui = Ui_Inicializar()
    ui.setupUi(Inicializar)
    Inicializar.show()
    sys.exit(app.exec_())