# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainoneboton.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Somniomwindow(object):
    def setupUi(self, Somniomwindow):
        Somniomwindow.setObjectName("Somniomwindow")
        Somniomwindow.setWindowModality(QtCore.Qt.NonModal)
        Somniomwindow.resize(1200, 690)
        Somniomwindow.setMinimumSize(QtCore.QSize(999, 690))
        Somniomwindow.setMaximumSize(QtCore.QSize(1200, 698))
        Somniomwindow.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        Somniomwindow.setMouseTracking(True)
        Somniomwindow.setFocusPolicy(QtCore.Qt.WheelFocus)
        Somniomwindow.setAcceptDrops(True)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/imagenes/imagenes/shul.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Somniomwindow.setWindowIcon(icon)
        Somniomwindow.setStyleSheet("border-style: solid;\n"
"border-left: none;\n"
"border-right: none;\n"
"border-top: none;\n"
"font: 75 8pt \"MS Shell Dlg 2\";\n"
"border-width: 0px;\n"
"border-color: rgba(9, 9, 9);\n"
"background-color: rgba(30, 29, 29); \n"
"color: rgb(229, 9, 127);\n"
"/*border-radius: 5px;*/\n"
"padding-top:3px;\n"
"padding-left:30px;\n"
"")
        self.centralwidget = QtWidgets.QWidget(Somniomwindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushmain_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushmain_5.setGeometry(QtCore.QRect(0, 30, 90, 70))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.pushmain_5.setFont(font)
        self.pushmain_5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushmain_5.setStyleSheet("border-style: solid;\n"
"border-left: none;\n"
"border-right: none;\n"
"border-top: none;\n"
"font: 75 8pt \"MS Shell Dlg 2\";\n"
"border-width: 3px;\n"
"border-color: rgba(9, 9, 9);\n"
"background-color: rgba(18,17,17); \n"
"color: rgb(229, 9, 127);\n"
"/*border-radius: 5px;*/\n"
"background-image:url(:/imagenes/imagenes/cont.png);\n"
"background-attachment: fixed;\n"
"background-position: center center;\n"
"background-size: cover;\n"
"background-repeat: no-repeat;\n"
"padding-top:3px;\n"
"padding-left:30px;\n"
"\n"
"\n"
"\n"
"")
        self.pushmain_5.setText("")
        self.pushmain_5.setObjectName("pushmain_5")
        self.pushproxis_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushproxis_6.setGeometry(QtCore.QRect(0, 100, 90, 70))
        self.pushproxis_6.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushproxis_6.setStyleSheet("border-style: solid;\n"
"border-left: none;\n"
"border-right: none;\n"
"border-top: none;\n"
"font: 75 8pt \"MS Shell Dlg 2\";\n"
"border-width: 3px;\n"
"border-color: rgba(9, 9, 9);\n"
"background-color: rgba(18,17,17); \n"
"color: rgb(229, 9, 127);\n"
"/*border-radius: 5px;*/\n"
"\n"
"background-image: url(:/imagenes/imagenes/barras.png);\n"
"background-attachment: fixed;\n"
"background-position: center center;\n"
"background-size: cover;\n"
"background-repeat: no-repeat;\n"
"padding-top:3px;\n"
"padding-left:30px;\n"
"")
        self.pushproxis_6.setText("")
        self.pushproxis_6.setObjectName("pushproxis_6")
        self.pushbuy_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushbuy_7.setGeometry(QtCore.QRect(0, 170, 90, 70))
        self.pushbuy_7.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushbuy_7.setStyleSheet("border-style: solid;\n"
"border-left: none;\n"
"border-right: none;\n"
"border-top: none;\n"
"font: 75 8pt \"MS Shell Dlg 2\";\n"
"border-width: 3px;\n"
"border-color: rgba(9, 9, 9);\n"
"background-color: rgba(18,17,17); \n"
"color: rgb(229, 9, 127);\n"
"/*border-radius: 5px;*/\n"
"background-image: url(:/imagenes/imagenes/cedula.png);\n"
"background-attachment: fixed;\n"
"background-position: center center;\n"
"background-size: cover;\n"
"background-repeat: no-repeat;\n"
"padding-top:3px;\n"
"padding-left:30px;\n"
"")
        self.pushbuy_7.setText("")
        self.pushbuy_7.setObjectName("pushbuy_7")
        self.pushrelease_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushrelease_8.setGeometry(QtCore.QRect(0, 240, 90, 70))
        self.pushrelease_8.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushrelease_8.setStyleSheet("border-style: solid;\n"
"border-left: none;\n"
"border-right: none;\n"
"border-top: none;\n"
"font: 75 8pt \"MS Shell Dlg 2\";\n"
"border-width: 3px;\n"
"border-color: rgba(9, 9, 9);\n"
"background-color: rgba(18,17,17); \n"
"color: rgb(229, 9, 127);\n"
"/*border-radius: 5px;*/\n"
"\n"
"background-image: url(:/imagenes/imagenes/estatics.png);\n"
"background-attachment: fixed;\n"
"background-position: center center;\n"
"background-size: cover;\n"
"background-repeat: no-repeat;\n"
"padding-top:3px;\n"
"padding-left:30px;\n"
"")
        self.pushrelease_8.setText("")
        self.pushrelease_8.setObjectName("pushrelease_8")
        self.pushconfig_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushconfig_9.setGeometry(QtCore.QRect(0, 310, 90, 70))
        self.pushconfig_9.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushconfig_9.setStyleSheet("border-style: solid;\n"
"border-left: none;\n"
"border-right: none;\n"
"border-top: none;\n"
"border-bottom:none;\n"
"font: 75 8pt \"MS Shell Dlg 2\";\n"
"border-width: 3px;\n"
"border-color: rgba(9, 9, 9);\n"
"background-image: url(:/imagenes/imagenes/deliz.png);\n"
"background-attachment: fixed;\n"
"background-position: center center;\n"
"background-size: cover;\n"
"background-repeat: no-repeat;\n"
"background-color: rgba(18,17,17); \n"
"color: rgb(229, 9, 127);\n"
"/*border-radius: 5px;*/\n"
"padding-top:3px;\n"
"padding-left:30px;")
        self.pushconfig_9.setText("")
        self.pushconfig_9.setObjectName("pushconfig_9")
        self.barblack_10 = QtWidgets.QGraphicsView(self.centralwidget)
        self.barblack_10.setGeometry(QtCore.QRect(-10, 20, 111, 971))
        self.barblack_10.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.barblack_10.setStyleSheet("border-style: solid;\n"
"border-width: 0px;\n"
"border-color: rgba(18, 17, 17);\n"
"background-color: rgba(18, 17, 17); \n"
"/*border-radius: 5px;*/\n"
"background-image: url(:/imagenes/imagenes/lol.png);\n"
"background-repeat:no-repeat;\n"
"margin:10px;")
        self.barblack_10.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.barblack_10.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.barblack_10.setObjectName("barblack_10")
        self.barblack_2 = QtWidgets.QGraphicsView(self.centralwidget)
        self.barblack_2.setGeometry(QtCore.QRect(-30, -10, 1341, 41))
        self.barblack_2.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.barblack_2.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.barblack_2.setStyleSheet("border-style: solid;\n"
"\n"
"border-left: none;\n"
"border-right: none;\n"
"border-top: none;\n"
"border-bottom: solid;\n"
"font: 75 8pt \"MS Shell Dlg 2\";\n"
"border-width: 3px;\n"
"border-color: rgba(9, 9, 9);\n"
"background-color: rgba(9, 9, 9); \n"
"color: rgb(229, 9, 127);\n"
"/*border-radius: 5px;*/\n"
"padding-top:3px;\n"
"padding-left:50px;")
        self.barblack_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.barblack_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.barblack_2.setObjectName("barblack_2")
        self.nombrelab_11 = QtWidgets.QLabel(self.centralwidget)
        self.nombrelab_11.setGeometry(QtCore.QRect(110, 50, 141, 21))
        self.nombrelab_11.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.nombrelab_11.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";\n"
"color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:1 rgba(187, 181, 181));\n"
"padding-top: 0px;\n"
"padding-bottom: 0px;\n"
"padding-right: 0px;\n"
"padding-left: 0px;\n"
"")
        self.nombrelab_11.setObjectName("nombrelab_11")
        self.pushextra_13 = QtWidgets.QPushButton(self.centralwidget)
        self.pushextra_13.setGeometry(QtCore.QRect(250, 50, 31, 31))
        self.pushextra_13.setStyleSheet("background-image: url(:/imagenes/imagenes/carga2.png);\n"
"background-attachment: fixed;\n"
"background-position: center center;\n"
"background-size: cover;\n"
"background-repeat: no-repeat;\n"
"padding-left:0px;\n"
"padding-right:0px;\n"
"")
        self.pushextra_13.setText("")
        self.pushextra_13.setObjectName("pushextra_13")
        self.pushmenos_14 = QtWidgets.QPushButton(self.centralwidget)
        self.pushmenos_14.setGeometry(QtCore.QRect(280, 46, 31, 31))
        self.pushmenos_14.setStyleSheet("background-image: url(:/imagenes/imagenes/carga1.png);\n"
"background-attachment: fixed;\n"
"background-position: center center;\n"
"background-size: cover;\n"
"background-repeat: no-repeat;")
        self.pushmenos_14.setText("")
        self.pushmenos_14.setObjectName("pushmenos_14")
        self.pushabout_15 = QtWidgets.QPushButton(self.centralwidget)
        self.pushabout_15.setGeometry(QtCore.QRect(320, 50, 71, 31))
        self.pushabout_15.setStyleSheet("font:9 9pt \"MS Shell Dlg 2\";\n"
"color: white;\n"
"\n"
"background-color: rgb(229, 9, 127);\n"
"border: 0px outset #E5097F ;  /* Grosor del Borde */  /* Color del Borde */\n"
"text-align: center;  /* Alineación del texto */\n"
"text-shadow: 2px 2px rgba(0,0,0,.1);\n"
"padding-left:0px;\n"
"padding-top:0px;\n"
"padding-bottom:2px;\n"
"border-radius: 8px;\n"
"")
        self.pushabout_15.setObjectName("pushabout_15")
        self.nombrelab_12 = QtWidgets.QLabel(self.centralwidget)
        self.nombrelab_12.setGeometry(QtCore.QRect(110, 70, 61, 21))
        self.nombrelab_12.setStyleSheet("font: 7pt \"MS Shell Dlg 2\";\n"
"color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:1 rgba(187, 181, 181));\n"
"padding-top: 0px;\n"
"padding-bottom: 0px;\n"
"padding-right: 0px;\n"
"padding-left: 0px;\n"
"")
        self.nombrelab_12.setObjectName("nombrelab_12")
        self.Lastlab_18 = QtWidgets.QLabel(self.centralwidget)
        self.Lastlab_18.setGeometry(QtCore.QRect(320, 100, 171, 21))
        self.Lastlab_18.setStyleSheet("padding-top:0px;\n"
"padding-bottom:0px;\n"
"padding-left:0px;\n"
"padding-right:0px;\n"
"font: 8 8pt \"MS Shell Dlg 2\";\n"
"color: rgba(187, 181, 181);\n"
"background-color: rgba(30, 29, 29);\n"
"text-align:center;")
        self.Lastlab_18.setObjectName("Lastlab_18")
        self.cardlab_21 = QtWidgets.QLabel(self.centralwidget)
        self.cardlab_21.setGeometry(QtCore.QRect(880, 100, 71, 21))
        self.cardlab_21.setStyleSheet("padding-top:0px;\n"
"padding-bottom:0px;\n"
"padding-left:0px;\n"
"padding-right:0px;\n"
"font: 8 8pt \"MS Shell Dlg 2\";\n"
"color: rgba(229, 9, 127);\n"
"background-color: rgba(30, 29, 29);\n"
"text-align:center;")
        self.cardlab_21.setObjectName("cardlab_21")
        self.Namelab_17 = QtWidgets.QLabel(self.centralwidget)
        self.Namelab_17.setGeometry(QtCore.QRect(140, 100, 171, 21))
        self.Namelab_17.setStyleSheet("padding-top:0px;\n"
"padding-bottom:0px;\n"
"padding-left:0px;\n"
"padding-right:0px;\n"
"font: 8 8pt \"MS Shell Dlg 2\";\n"
"color: rgba(187, 181, 181);\n"
"background-color: rgba(30, 29, 29);\n"
"text-align:center;")
        self.Namelab_17.setObjectName("Namelab_17")
        self.citylab_20 = QtWidgets.QLabel(self.centralwidget)
        self.citylab_20.setGeometry(QtCore.QRect(680, 100, 171, 21))
        self.citylab_20.setStyleSheet("padding-top:0px;\n"
"padding-bottom:0px;\n"
"padding-left:0px;\n"
"padding-right:0px;\n"
"font: 8 8pt \"MS Shell Dlg 2\";\n"
"color: rgba(187, 181, 181);\n"
"background-color: rgba(30, 29, 29);\n"
"text-align:center;")
        self.citylab_20.setObjectName("citylab_20")
        self.Phonenumlab_19 = QtWidgets.QLabel(self.centralwidget)
        self.Phonenumlab_19.setGeometry(QtCore.QRect(500, 100, 171, 21))
        self.Phonenumlab_19.setStyleSheet("padding-top:0px;\n"
"padding-bottom:0px;\n"
"padding-left:0px;\n"
"padding-right:0px;\n"
"font: 8 8pt \"MS Shell Dlg 2\";\n"
"color: rgba(187, 181, 181);\n"
"background-color: rgba(30, 29, 29);\n"
"text-align:center;")
        self.Phonenumlab_19.setObjectName("Phonenumlab_19")
        self.editlab_22 = QtWidgets.QLabel(self.centralwidget)
        self.editlab_22.setGeometry(QtCore.QRect(1100, 100, 71, 21))
        self.editlab_22.setStyleSheet("padding-top:0px;\n"
"padding-bottom:0px;\n"
"padding-left:0px;\n"
"padding-right:0px;\n"
"font: 8 8pt \"MS Shell Dlg 2\";\n"
"color: rgba(229, 9, 127);\n"
"background-color: rgba(30, 29, 29);\n"
"text-align:center;")
        self.editlab_22.setObjectName("editlab_22")
        self.icon_1 = QtWidgets.QPushButton(self.centralwidget)
        self.icon_1.setGeometry(QtCore.QRect(30, 0, 31, 31))
        self.icon_1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.icon_1.setStyleSheet("background-image: url(:/imagenes/imagenes/shul.png);\n"
"background-color: rgba(9,9,9);\n"
"background-attachment: fixed;\n"
"background-position: center center;\n"
"background-size: cover;\n"
"background-repeat: no-repeat;\n"
"padding-left:0px;\n"
"padding-right:0px;\n"
"")
        self.icon_1.setText("")
        self.icon_1.setObjectName("icon_1")
        self.pushhelp_16 = QtWidgets.QPushButton(self.centralwidget)
        self.pushhelp_16.setGeometry(QtCore.QRect(1100, 50, 71, 31))
        self.pushhelp_16.setStyleSheet("font:9 9pt \"MS Shell Dlg 2\";\n"
"color: white;\n"
"\n"
"background-color: rgb(229, 9, 127);\n"
"border: 0px outset #E5097F ;  /* Grosor del Borde */  /* Color del Borde */\n"
"text-align: center;  /* Alineación del texto */\n"
"text-shadow: 2px 2px rgba(0,0,0,.1);\n"
"padding-left:0px;\n"
"padding-top:0px;\n"
"padding-bottom:2px;\n"
"border-radius: 8px;\n"
"")
        self.pushhelp_16.setObjectName("pushhelp_16")
        self.somlab_3 = QtWidgets.QLabel(self.centralwidget)
        self.somlab_3.setGeometry(QtCore.QRect(600, 0, 41, 31))
        self.somlab_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.somlab_3.setStyleSheet("font: 8pt \"MS Shell Dlg 2\";\n"
"color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:1 rgba(187, 181, 181));\n"
"padding-top: 0px;\n"
"padding-bottom: 0px;\n"
"padding-right: 0px;\n"
"padding-left: 0px;\n"
"background-color: rgb(9,9,9);\n"
"")
        self.somlab_3.setObjectName("somlab_3")
        self.somlab_4 = QtWidgets.QLabel(self.centralwidget)
        self.somlab_4.setGeometry(QtCore.QRect(640, 10, 21, 16))
        self.somlab_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.somlab_4.setStyleSheet("font: 4pt \"MS Shell Dlg 2\";\n"
"color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:1 rgba(187, 181, 181));\n"
"padding-top: 0px;\n"
"padding-bottom: 0px;\n"
"padding-right: 0px;\n"
"padding-left: 0px;\n"
"background-color: rgb(9,9,9);\n"
"")
        self.somlab_4.setObjectName("somlab_4")
        self.pushclose_1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushclose_1.setGeometry(QtCore.QRect(1160, 0, 31, 31))
        self.pushclose_1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushclose_1.setStyleSheet("background-image:url(:/imagenes/imagenes/ex.png);\n"
"background-attachment: fixed;\n"
"background-position: center center;\n"
"background-size: cover;\n"
"background-repeat: no-repeat;\n"
"background-color: rgba(9,9,9);")
        self.pushclose_1.setText("")
        self.pushclose_1.setObjectName("pushclose_1")
        self.pushmin_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushmin_2.setGeometry(QtCore.QRect(1130, 0, 31, 31))
        self.pushmin_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushmin_2.setStyleSheet("background-image: url(:/imagenes/imagenes/min.png);\n"
"background-attachment: fixed;\n"
"background-position: center center;\n"
"background-size: cover;\n"
"background-repeat: no-repeat;\n"
"background-color: rgba(9,9,9);")
        self.pushmin_2.setText("")
        self.pushmin_2.setObjectName("pushmin_2")
        self.pushreload_17 = QtWidgets.QPushButton(self.centralwidget)
        self.pushreload_17.setGeometry(QtCore.QRect(1020, 50, 71, 31))
        self.pushreload_17.setStyleSheet("font:9 9pt \"MS Shell Dlg 2\";\n"
"color: white;\n"
"\n"
"background-color: rgb(229, 9, 127);\n"
"border: 0px outset #E5097F ;  /* Grosor del Borde */  /* Color del Borde */\n"
"text-align: center;  /* Alineación del texto */\n"
"text-shadow: 2px 2px rgba(0,0,0,.1);\n"
"padding-left:0px;\n"
"padding-top:0px;\n"
"padding-bottom:2px;\n"
"border-radius: 8px;\n"
"")
        self.pushreload_17.setObjectName("pushreload_17")
        self.barblack_10.raise_()
        self.pushmain_5.raise_()
        self.pushproxis_6.raise_()
        self.pushbuy_7.raise_()
        self.pushrelease_8.raise_()
        self.pushconfig_9.raise_()
        self.barblack_2.raise_()
        self.nombrelab_11.raise_()
        self.pushextra_13.raise_()
        self.pushmenos_14.raise_()
        self.pushabout_15.raise_()
        self.nombrelab_12.raise_()
        self.Lastlab_18.raise_()
        self.cardlab_21.raise_()
        self.Namelab_17.raise_()
        self.citylab_20.raise_()
        self.Phonenumlab_19.raise_()
        self.editlab_22.raise_()
        self.icon_1.raise_()
        self.pushhelp_16.raise_()
        self.somlab_3.raise_()
        self.somlab_4.raise_()
        self.pushclose_1.raise_()
        self.pushmin_2.raise_()
        self.pushreload_17.raise_()
        Somniomwindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(Somniomwindow)
        self.pushclose_1.clicked.connect(Somniomwindow.close)
        self.pushmin_2.clicked.connect(Somniomwindow.showMinimized)
        QtCore.QMetaObject.connectSlotsByName(Somniomwindow)

    def retranslateUi(self, Somniomwindow):
        _translate = QtCore.QCoreApplication.translate
        Somniomwindow.setWindowTitle(_translate("Somniomwindow", "                                                                                                                                                                     Somnium"))
        self.nombrelab_11.setText(_translate("Somniomwindow", "Somnium Data"))
        self.pushabout_15.setText(_translate("Somniomwindow", "About us"))
        self.nombrelab_12.setText(_translate("Somniomwindow", "Automatic buy"))
        self.Lastlab_18.setText(_translate("Somniomwindow", "Last Name"))
        self.cardlab_21.setText(_translate("Somniomwindow", "Card Number"))
        self.Namelab_17.setText(_translate("Somniomwindow", "First Name"))
        self.citylab_20.setText(_translate("Somniomwindow", "City"))
        self.Phonenumlab_19.setText(_translate("Somniomwindow", "Phone Number"))
        self.editlab_22.setText(_translate("Somniomwindow", "Push Edit"))
        self.pushhelp_16.setText(_translate("Somniomwindow", "Help"))
        self.somlab_3.setText(_translate("Somniomwindow", "Somnium"))
        self.somlab_4.setText(_translate("Somniomwindow", "1.0"))
        self.pushreload_17.setText(_translate("Somniomwindow", "Update"))
import an_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Somniomwindow = QtWidgets.QMainWindow()
    ui = Ui_Somniomwindow()
    ui.setupUi(Somniomwindow)
    Somniomwindow.show()
    sys.exit(app.exec_())
