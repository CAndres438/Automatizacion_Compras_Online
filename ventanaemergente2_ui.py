# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventanaemergente2.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_popup_2(object):
    def setupUi(self, popup_2):
        popup_2.setObjectName("popup_2")
        popup_2.setWindowModality(QtCore.Qt.NonModal)
        popup_2.resize(411, 280)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(popup_2.sizePolicy().hasHeightForWidth())
        popup_2.setSizePolicy(sizePolicy)
        popup_2.setMinimumSize(QtCore.QSize(411, 280))
        popup_2.setMaximumSize(QtCore.QSize(411, 280))
        popup_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        popup_2.setFocusPolicy(QtCore.Qt.NoFocus)
        popup_2.setAcceptDrops(True)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/imagenes/imagenes/shul.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap(":/imagenes/imagenes/shul.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        icon.addPixmap(QtGui.QPixmap(":/imagenes/imagenes/shul.png"), QtGui.QIcon.Disabled, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap(":/imagenes/imagenes/shul.png"), QtGui.QIcon.Disabled, QtGui.QIcon.On)
        icon.addPixmap(QtGui.QPixmap(":/imagenes/imagenes/shul.png"), QtGui.QIcon.Active, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap(":/imagenes/imagenes/shul.png"), QtGui.QIcon.Active, QtGui.QIcon.On)
        icon.addPixmap(QtGui.QPixmap(":/imagenes/imagenes/shul.png"), QtGui.QIcon.Selected, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap(":/imagenes/imagenes/shul.png"), QtGui.QIcon.Selected, QtGui.QIcon.On)
        popup_2.setWindowIcon(icon)
        popup_2.setWindowOpacity(1.0)
        popup_2.setToolTipDuration(6)
        popup_2.setAutoFillBackground(False)
        popup_2.setStyleSheet("background-color:  rgba(39,37,37);\n"
"color: rgb(229, 9, 127);\n"
"font: 75 8pt \"MS Shell Dlg 2\";\n"
"")
        self.AddressBitxt_3 = QtWidgets.QTextEdit(popup_2)
        self.AddressBitxt_3.setGeometry(QtCore.QRect(10, 140, 391, 31))
        self.AddressBitxt_3.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.AddressBitxt_3.setMouseTracking(True)
        self.AddressBitxt_3.setStyleSheet("border-style: solid;\n"
"font: 75 8pt \"MS Shell Dlg 2\";\n"
"border-width: 0px;\n"
"border-color: rgba(50,48,48);\n"
"background-color: rgba(50,48,48); \n"
"color: rgb(229, 9, 127);\n"
"border-radius: 5px;\n"
"padding-top:3px;\n"
"padding-left:30px;\n"
"")
        self.AddressBitxt_3.setObjectName("AddressBitxt_3")
        self.ApartBitxt_2 = QtWidgets.QTextEdit(popup_2)
        self.ApartBitxt_2.setGeometry(QtCore.QRect(210, 70, 191, 31))
        self.ApartBitxt_2.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ApartBitxt_2.setMouseTracking(True)
        self.ApartBitxt_2.setStyleSheet("border-style: solid;\n"
"font: 75 8pt \"MS Shell Dlg 2\";\n"
"border-width: 0px;\n"
"border-color: rgba(50,48,48);\n"
"background-color: rgba(50,48,48); \n"
"color: rgb(229, 9, 127);\n"
"border-radius: 5px;\n"
"padding-top:3px;\n"
"padding-left:30px;\n"
"")
        self.ApartBitxt_2.setObjectName("ApartBitxt_2")
        self.label = QtWidgets.QLabel(popup_2)
        self.label.setGeometry(QtCore.QRect(10, 10, 131, 21))
        self.label.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";\n"
"color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:1 rgba(229,9,127));\n"
"")
        self.label.setObjectName("label")
        self.label_6 = QtWidgets.QLabel(popup_2)
        self.label_6.setGeometry(QtCore.QRect(10, 120, 81, 16))
        self.label_6.setStyleSheet("font: 8pt \"MS Shell Dlg 2\";\n"
"background-color: rgba(39,37,37);\n"
"color: rgb(187,181,181);\n"
"padding-bottom: 0px\n"
"")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(popup_2)
        self.label_7.setGeometry(QtCore.QRect(210, 50, 61, 16))
        self.label_7.setStyleSheet("font: 8pt \"MS Shell Dlg 2\";\n"
"background-color: rgba(39,37,37);\n"
"color: rgb(187,181,181);\n"
"padding-bottom: 0px")
        self.label_7.setObjectName("label_7")
        self.label_9 = QtWidgets.QLabel(popup_2)
        self.label_9.setGeometry(QtCore.QRect(210, 190, 31, 16))
        self.label_9.setStyleSheet("font: 8pt \"MS Shell Dlg 2\";\n"
"background-color: rgba(39,37,37);\n"
"color: rgb(187,181,181);\n"
"padding-bottom: 0px")
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(popup_2)
        self.label_10.setGeometry(QtCore.QRect(10, 190, 61, 16))
        self.label_10.setStyleSheet("font: 8pt \"MS Shell Dlg 2\";\n"
"background-color: rgba(39,37,37);\n"
"color: rgb(187,181,181);\n"
"padding-bottom: 0px\n"
"")
        self.label_10.setObjectName("label_10")
        self.CityBitxt_5 = QtWidgets.QTextEdit(popup_2)
        self.CityBitxt_5.setGeometry(QtCore.QRect(210, 210, 191, 31))
        self.CityBitxt_5.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.CityBitxt_5.setMouseTracking(True)
        self.CityBitxt_5.setStyleSheet("border-style: solid;\n"
"font: 75 8pt \"MS Shell Dlg 2\";\n"
"border-width: 0px;\n"
"border-color: rgba(50,48,48);\n"
"background-color: rgba(50,48,48); \n"
"color: rgb(229, 9, 127);\n"
"border-radius: 5px;\n"
"padding-top:3px;\n"
"padding-left:30px;\n"
"")
        self.CityBitxt_5.setObjectName("CityBitxt_5")
        self.PostalBitxt_4 = QtWidgets.QTextEdit(popup_2)
        self.PostalBitxt_4.setGeometry(QtCore.QRect(10, 210, 191, 31))
        self.PostalBitxt_4.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.PostalBitxt_4.setMouseTracking(True)
        self.PostalBitxt_4.setStyleSheet("border-style: solid;\n"
"font: 75 8pt \"MS Shell Dlg 2\";\n"
"border-width: 0px;\n"
"border-color: rgba(50,48,48);\n"
"background-color: rgba(50,48,48); \n"
"color: rgb(229, 9, 127);\n"
"border-radius: 5px;\n"
"padding-top:3px;\n"
"padding-left:30px;\n"
"")
        self.PostalBitxt_4.setObjectName("PostalBitxt_4")
        self.graphicsView_5 = QtWidgets.QGraphicsView(popup_2)
        self.graphicsView_5.setGeometry(QtCore.QRect(10, 140, 31, 31))
        self.graphicsView_5.setStyleSheet("border-style: solid;\n"
"border-width: 0px;\n"
"border-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:1 rgba(50,48,48));\n"
"background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:1 rgba(50,48,48)); \n"
"border-radius: 5px;\n"
"background-image: url(:/imagenes/imagenes/dir.png);\n"
"background-repeat:no-repeat;\n"
"margin:10px;\n"
"")
        self.graphicsView_5.setObjectName("graphicsView_5")
        self.graphicsView_6 = QtWidgets.QGraphicsView(popup_2)
        self.graphicsView_6.setGeometry(QtCore.QRect(210, 70, 31, 31))
        self.graphicsView_6.setStyleSheet("border-style: solid;\n"
"border-width: 0px;\n"
"border-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:1 rgba(50,48,48));\n"
"background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:1 rgba(50,48,48)); \n"
"border-radius: 5px;\n"
"background-image: url(:/imagenes/imagenes/num.png);\n"
"background-repeat:no-repeat;\n"
"margin:10px;\n"
"")
        self.graphicsView_6.setObjectName("graphicsView_6")
        self.graphicsView_8 = QtWidgets.QGraphicsView(popup_2)
        self.graphicsView_8.setGeometry(QtCore.QRect(210, 210, 31, 31))
        self.graphicsView_8.setStyleSheet("border-style: solid;\n"
"border-width: 0px;\n"
"border-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:1 rgba(50,48,48));\n"
"background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:1 rgba(50,48,48)); \n"
"border-radius: 5px;\n"
"background-image: url(:/imagenes/imagenes/state.png);\n"
"background-repeat:no-repeat;\n"
"margin:10px;\n"
"")
        self.graphicsView_8.setObjectName("graphicsView_8")
        self.graphicsView_9 = QtWidgets.QGraphicsView(popup_2)
        self.graphicsView_9.setGeometry(QtCore.QRect(10, 210, 31, 31))
        self.graphicsView_9.setStyleSheet("border-style: solid;\n"
"border-width: 0px;\n"
"border-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:1 rgba(50,48,48));\n"
"background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:1 rgba(50,48,48)); \n"
"border-radius: 5px;\n"
"background-image: url(:/imagenes/imagenes/state.png);\n"
"background-repeat:no-repeat;\n"
"margin:10px;\n"
"")
        self.graphicsView_9.setObjectName("graphicsView_9")
        self.label_8 = QtWidgets.QLabel(popup_2)
        self.label_8.setGeometry(QtCore.QRect(10, 50, 61, 16))
        self.label_8.setStyleSheet("font: 8pt \"MS Shell Dlg 2\";\n"
"background-color: rgba(39,37,37);\n"
"color: rgb(187,181,181);\n"
"padding-bottom: 0px")
        self.label_8.setObjectName("label_8")
        self.pushclose_2 = QtWidgets.QPushButton(popup_2)
        self.pushclose_2.setGeometry(QtCore.QRect(380, 10, 21, 23))
        self.pushclose_2.setStyleSheet("background-color:  rgba(39,37,37);\n"
"background-image: url(:/imagenes/imagenes/equisgris.png);\n"
"background-attachment: fixed;\n"
"background-position: center center;\n"
"background-size: cover;\n"
"background-repeat: no-repeat;\n"
"border-style: solid;\n"
"border-top: none;\n"
"border-bottom:none;\n"
"border-right: solid;")
        self.pushclose_2.setText("")
        self.pushclose_2.setObjectName("pushclose_2")
        self.pushsave_2 = QtWidgets.QPushButton(popup_2)
        self.pushsave_2.setGeometry(QtCore.QRect(360, 10, 21, 23))
        self.pushsave_2.setStyleSheet("background-color:  rgba(39,37,37);\n"
"background-image: url(:/imagenes/imagenes/guardar6.png);\n"
"background-attachment: fixed;\n"
"background-position: center center;\n"
"background-size: cover;\n"
"background-repeat: no-repeat;\n"
"border-style: solid;\n"
"border-top: none;\n"
"border-bottom:none;\n"
"border-right: solid;")
        self.pushsave_2.setText("")
        self.pushsave_2.setObjectName("pushsave_2")
        self.graphicsView_10 = QtWidgets.QGraphicsView(popup_2)
        self.graphicsView_10.setGeometry(QtCore.QRect(10, 70, 31, 31))
        self.graphicsView_10.setStyleSheet("border-style: solid;\n"
"border-width: 0px;\n"
"border-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:1 rgba(50,48,48));\n"
"background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:1 rgba(50,48,48)); \n"
"border-radius: 5px;\n"
"background-image: url(:/imagenes/imagenes/url.png);\n"
"background-repeat:no-repeat;\n"
"margin:10px;\n"
"")
        self.graphicsView_10.setObjectName("graphicsView_10")
        self.comboBox = QtWidgets.QComboBox(popup_2)
        self.comboBox.setGeometry(QtCore.QRect(10, 70, 191, 31))
        self.comboBox.setStyleSheet("border-style: solid;\n"
"font: 75 8pt \"MS Shell Dlg 2\";\n"
"border-width: 0px;\n"
"border-color: rgba(50,48,48);\n"
"background-color: rgba(50,48,48); \n"
"color: rgb(229, 9, 127);\n"
"border-radius: 5px;\n"
"padding-top:3px;\n"
"padding-left:30px;")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.setItemText(0, "")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.pushcod_3 = QtWidgets.QPushButton(popup_2)
        self.pushcod_3.setGeometry(QtCore.QRect(340, 10, 21, 23))
        self.pushcod_3.setStyleSheet("background-color:  rgba(39,37,37);\n"
"background-image: url(:/imagenes/imagenes/url.png);\n"
"background-attachment: fixed;\n"
"background-position: center center;\n"
"background-size: cover;\n"
"background-repeat: no-repeat;\n"
"border-style: solid;\n"
"border-top: none;\n"
"border-bottom:none;\n"
"border-right: solid;")
        self.pushcod_3.setText("")
        self.pushcod_3.setObjectName("pushcod_3")
        self.comboBox.raise_()
        self.AddressBitxt_3.raise_()
        self.ApartBitxt_2.raise_()
        self.label.raise_()
        self.label_6.raise_()
        self.label_7.raise_()
        self.label_9.raise_()
        self.label_10.raise_()
        self.CityBitxt_5.raise_()
        self.PostalBitxt_4.raise_()
        self.graphicsView_5.raise_()
        self.graphicsView_6.raise_()
        self.graphicsView_8.raise_()
        self.graphicsView_9.raise_()
        self.label_8.raise_()
        self.pushclose_2.raise_()
        self.pushsave_2.raise_()
        self.graphicsView_10.raise_()
        self.pushcod_3.raise_()

        self.retranslateUi(popup_2)
        self.pushclose_2.clicked.connect(popup_2.close)
        QtCore.QMetaObject.connectSlotsByName(popup_2)

    def retranslateUi(self, popup_2):
        _translate = QtCore.QCoreApplication.translate
        popup_2.setWindowTitle(_translate("popup_2", "                                    Somnium-Billing Details"))
        self.AddressBitxt_3.setHtml(_translate("popup_2", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:72; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8.25pt; font-weight:400;\"><br /></p></body></html>"))
        self.ApartBitxt_2.setHtml(_translate("popup_2", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:72; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8.25pt; font-weight:400;\"><br /></p></body></html>"))
        self.label.setText(_translate("popup_2", "Billing Details"))
        self.label_6.setText(_translate("popup_2", "Street Address"))
        self.label_7.setText(_translate("popup_2", "Apartment"))
        self.label_9.setText(_translate("popup_2", "City"))
        self.label_10.setText(_translate("popup_2", "Postal Code"))
        self.CityBitxt_5.setHtml(_translate("popup_2", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:72; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8.25pt; font-weight:400;\"><br /></p></body></html>"))
        self.PostalBitxt_4.setHtml(_translate("popup_2", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:72; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8.25pt; font-weight:400;\"><br /></p></body></html>"))
        self.label_8.setText(_translate("popup_2", "Country Cod"))
        self.comboBox.setItemText(1, _translate("popup_2", "1"))
        self.comboBox.setItemText(2, _translate("popup_2", "2"))
        self.comboBox.setItemText(3, _translate("popup_2", "3"))
        self.comboBox.setItemText(4, _translate("popup_2", "4"))
        self.comboBox.setItemText(5, _translate("popup_2", "5"))
        self.comboBox.setItemText(6, _translate("popup_2", "6"))
        self.comboBox.setItemText(7, _translate("popup_2", "7"))
        self.comboBox.setItemText(8, _translate("popup_2", "8"))
        self.comboBox.setItemText(9, _translate("popup_2", "9"))
        self.comboBox.setItemText(10, _translate("popup_2", "10"))
        self.comboBox.setItemText(11, _translate("popup_2", "11"))
        self.comboBox.setItemText(12, _translate("popup_2", "12"))
        self.comboBox.setItemText(13, _translate("popup_2", "13"))
        self.comboBox.setItemText(14, _translate("popup_2", "14"))
        self.comboBox.setItemText(15, _translate("popup_2", "15"))
        self.comboBox.setItemText(16, _translate("popup_2", "16"))
        self.comboBox.setItemText(17, _translate("popup_2", "17"))
        self.comboBox.setItemText(18, _translate("popup_2", "18"))
        self.comboBox.setItemText(19, _translate("popup_2", "19"))
        self.comboBox.setItemText(20, _translate("popup_2", "20"))
        self.comboBox.setItemText(21, _translate("popup_2", "21"))
        self.comboBox.setItemText(22, _translate("popup_2", "22"))
        self.comboBox.setItemText(23, _translate("popup_2", "23"))
        self.comboBox.setItemText(24, _translate("popup_2", "24"))
        self.comboBox.setItemText(25, _translate("popup_2", "25"))
        self.comboBox.setItemText(26, _translate("popup_2", "26"))
        self.comboBox.setItemText(27, _translate("popup_2", "27"))
        self.comboBox.setItemText(28, _translate("popup_2", "28"))
        self.comboBox.setItemText(29, _translate("popup_2", "29"))
        self.comboBox.setItemText(30, _translate("popup_2", "30"))
        self.comboBox.setItemText(31, _translate("popup_2", "31"))
        self.comboBox.setItemText(32, _translate("popup_2", "32"))
        self.comboBox.setItemText(33, _translate("popup_2", "33"))
        self.comboBox.setItemText(34, _translate("popup_2", "34"))
        self.comboBox.setItemText(35, _translate("popup_2", "35"))
        self.comboBox.setItemText(36, _translate("popup_2", "36"))
        self.comboBox.setItemText(37, _translate("popup_2", "37"))
        self.comboBox.setItemText(38, _translate("popup_2", "38"))
        self.comboBox.setItemText(39, _translate("popup_2", "39"))
        self.comboBox.setItemText(40, _translate("popup_2", "40"))
        self.comboBox.setItemText(41, _translate("popup_2", "41"))
        self.comboBox.setItemText(42, _translate("popup_2", "42"))
        self.comboBox.setItemText(43, _translate("popup_2", "43"))
        self.comboBox.setItemText(44, _translate("popup_2", "44"))
        self.comboBox.setItemText(45, _translate("popup_2", "45"))
        self.comboBox.setItemText(46, _translate("popup_2", "46"))
        self.comboBox.setItemText(47, _translate("popup_2", "47"))
        self.comboBox.setItemText(48, _translate("popup_2", "48"))
        self.comboBox.setItemText(49, _translate("popup_2", "49"))
        self.comboBox.setItemText(50, _translate("popup_2", "50"))
        self.comboBox.setItemText(51, _translate("popup_2", "51"))
        self.comboBox.setItemText(52, _translate("popup_2", "52"))
        self.comboBox.setItemText(53, _translate("popup_2", "53"))
        self.comboBox.setItemText(54, _translate("popup_2", "54"))
        self.comboBox.setItemText(55, _translate("popup_2", "55"))
        self.comboBox.setItemText(56, _translate("popup_2", "56"))
        self.comboBox.setItemText(57, _translate("popup_2", "57"))
        self.comboBox.setItemText(58, _translate("popup_2", "58"))
        self.comboBox.setItemText(59, _translate("popup_2", "59"))
        self.comboBox.setItemText(60, _translate("popup_2", "60"))
        self.comboBox.setItemText(61, _translate("popup_2", "61"))
        self.comboBox.setItemText(62, _translate("popup_2", "62"))
        self.comboBox.setItemText(63, _translate("popup_2", "63"))
        self.comboBox.setItemText(64, _translate("popup_2", "64"))
        self.comboBox.setItemText(65, _translate("popup_2", "65"))
        self.comboBox.setItemText(66, _translate("popup_2", "66"))
        self.comboBox.setItemText(67, _translate("popup_2", "67"))
        self.comboBox.setItemText(68, _translate("popup_2", "68"))
        self.comboBox.setItemText(69, _translate("popup_2", "69"))
        self.comboBox.setItemText(70, _translate("popup_2", "70"))
        self.comboBox.setItemText(71, _translate("popup_2", "71"))
        self.comboBox.setItemText(72, _translate("popup_2", "72"))
        self.comboBox.setItemText(73, _translate("popup_2", "73"))
        self.comboBox.setItemText(74, _translate("popup_2", "74"))
        self.comboBox.setItemText(75, _translate("popup_2", "75"))
        self.comboBox.setItemText(76, _translate("popup_2", "76"))
        self.comboBox.setItemText(77, _translate("popup_2", "77"))
        self.comboBox.setItemText(78, _translate("popup_2", "78"))
        self.comboBox.setItemText(79, _translate("popup_2", "79"))
        self.comboBox.setItemText(80, _translate("popup_2", "80"))
        self.comboBox.setItemText(81, _translate("popup_2", "81"))
        self.comboBox.setItemText(82, _translate("popup_2", "82"))
        self.comboBox.setItemText(83, _translate("popup_2", "83"))
        self.comboBox.setItemText(84, _translate("popup_2", "84"))
        self.comboBox.setItemText(85, _translate("popup_2", "85"))
        self.comboBox.setItemText(86, _translate("popup_2", "86"))
        self.comboBox.setItemText(87, _translate("popup_2", "87"))
        self.comboBox.setItemText(88, _translate("popup_2", "88"))
        self.comboBox.setItemText(89, _translate("popup_2", "89"))
        self.comboBox.setItemText(90, _translate("popup_2", "90"))
        self.comboBox.setItemText(91, _translate("popup_2", "91"))
        self.comboBox.setItemText(92, _translate("popup_2", "92"))
        self.comboBox.setItemText(93, _translate("popup_2", "93"))
        self.comboBox.setItemText(94, _translate("popup_2", "94"))
        self.comboBox.setItemText(95, _translate("popup_2", "95"))
        self.comboBox.setItemText(96, _translate("popup_2", "96"))
        self.comboBox.setItemText(97, _translate("popup_2", "97"))
        self.comboBox.setItemText(98, _translate("popup_2", "98"))
        self.comboBox.setItemText(99, _translate("popup_2", "99"))
        self.comboBox.setItemText(100, _translate("popup_2", "100"))
        self.comboBox.setItemText(101, _translate("popup_2", "101"))
        self.comboBox.setItemText(102, _translate("popup_2", "102"))
        self.comboBox.setItemText(103, _translate("popup_2", "103"))
        self.comboBox.setItemText(104, _translate("popup_2", "104"))
        self.comboBox.setItemText(105, _translate("popup_2", "105"))
        self.comboBox.setItemText(106, _translate("popup_2", "106"))
        self.comboBox.setItemText(107, _translate("popup_2", "107"))
        self.comboBox.setItemText(108, _translate("popup_2", "108"))
        self.comboBox.setItemText(109, _translate("popup_2", "109"))
        self.comboBox.setItemText(110, _translate("popup_2", "110"))
        self.comboBox.setItemText(111, _translate("popup_2", "111"))
        self.comboBox.setItemText(112, _translate("popup_2", "112"))
        self.comboBox.setItemText(113, _translate("popup_2", "113"))
        self.comboBox.setItemText(114, _translate("popup_2", "114"))
        self.comboBox.setItemText(115, _translate("popup_2", "115"))
        self.comboBox.setItemText(116, _translate("popup_2", "116"))
        self.comboBox.setItemText(117, _translate("popup_2", "117"))
        self.comboBox.setItemText(118, _translate("popup_2", "118"))
        self.comboBox.setItemText(119, _translate("popup_2", "119"))
        self.comboBox.setItemText(120, _translate("popup_2", "120"))
        self.comboBox.setItemText(121, _translate("popup_2", "121"))
        self.comboBox.setItemText(122, _translate("popup_2", "122"))
        self.comboBox.setItemText(123, _translate("popup_2", "123"))
        self.comboBox.setItemText(124, _translate("popup_2", "124"))
        self.comboBox.setItemText(125, _translate("popup_2", "125"))
        self.comboBox.setItemText(126, _translate("popup_2", "126"))
        self.comboBox.setItemText(127, _translate("popup_2", "127"))
        self.comboBox.setItemText(128, _translate("popup_2", "128"))
        self.comboBox.setItemText(129, _translate("popup_2", "129"))
        self.comboBox.setItemText(130, _translate("popup_2", "130"))
        self.comboBox.setItemText(131, _translate("popup_2", "131"))
        self.comboBox.setItemText(132, _translate("popup_2", "132"))
        self.comboBox.setItemText(133, _translate("popup_2", "133"))
        self.comboBox.setItemText(134, _translate("popup_2", "134"))
        self.comboBox.setItemText(135, _translate("popup_2", "135"))
        self.comboBox.setItemText(136, _translate("popup_2", "136"))
        self.comboBox.setItemText(137, _translate("popup_2", "137"))
        self.comboBox.setItemText(138, _translate("popup_2", "138"))
        self.comboBox.setItemText(139, _translate("popup_2", "139"))
        self.comboBox.setItemText(140, _translate("popup_2", "140"))
        self.comboBox.setItemText(141, _translate("popup_2", "141"))
        self.comboBox.setItemText(142, _translate("popup_2", "142"))
        self.comboBox.setItemText(143, _translate("popup_2", "143"))
        self.comboBox.setItemText(144, _translate("popup_2", "144"))
        self.comboBox.setItemText(145, _translate("popup_2", "145"))
        self.comboBox.setItemText(146, _translate("popup_2", "146"))
        self.comboBox.setItemText(147, _translate("popup_2", "147"))
        self.comboBox.setItemText(148, _translate("popup_2", "148"))
        self.comboBox.setItemText(149, _translate("popup_2", "149"))
        self.comboBox.setItemText(150, _translate("popup_2", "150"))
        self.comboBox.setItemText(151, _translate("popup_2", "151"))
        self.comboBox.setItemText(152, _translate("popup_2", "152"))
        self.comboBox.setItemText(153, _translate("popup_2", "153"))
        self.comboBox.setItemText(154, _translate("popup_2", "154"))
        self.comboBox.setItemText(155, _translate("popup_2", "155"))
        self.comboBox.setItemText(156, _translate("popup_2", "156"))
        self.comboBox.setItemText(157, _translate("popup_2", "157"))
        self.comboBox.setItemText(158, _translate("popup_2", "158"))
        self.comboBox.setItemText(159, _translate("popup_2", "159"))
        self.comboBox.setItemText(160, _translate("popup_2", "160"))
        self.comboBox.setItemText(161, _translate("popup_2", "161"))
        self.comboBox.setItemText(162, _translate("popup_2", "162"))
        self.comboBox.setItemText(163, _translate("popup_2", "163"))
        self.comboBox.setItemText(164, _translate("popup_2", "164"))
        self.comboBox.setItemText(165, _translate("popup_2", "165"))
        self.comboBox.setItemText(166, _translate("popup_2", "166"))
        self.comboBox.setItemText(167, _translate("popup_2", "167"))
        self.comboBox.setItemText(168, _translate("popup_2", "168"))
        self.comboBox.setItemText(169, _translate("popup_2", "169"))
        self.comboBox.setItemText(170, _translate("popup_2", "170"))
        self.comboBox.setItemText(171, _translate("popup_2", "171"))
        self.comboBox.setItemText(172, _translate("popup_2", "172"))
import an_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    popup_2 = QtWidgets.QWidget()
    ui = Ui_popup_2()
    ui.setupUi(popup_2)
    popup_2.show()
    sys.exit(app.exec_())
