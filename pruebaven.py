import sys

import time
from ventanaemergente_ui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from Usuario import usersom
from pruebaven2 import *
import sqlite3
from Select_id import *


class Prueba_ventanaemer(QtWidgets.QWidget):
    
    Usersom = usersom
    def __init__(self):
        super().__init__()
        QtWidgets.QWidget.__init__(self)
        Ui_popup_1.__init__(self)
        self.ui = Ui_popup_1()
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.ui.setupUi(self)
        self.ui.pushsave_1.clicked.connect(self.registrar)
        self.ui.pushsave_1.clicked.connect(self.on_click2)
        self.ui.pushsave_1.clicked.connect(self.close)

    def registrar(self):
        self.Usersom = usersom(self.ui.Nametxt_1.toPlainText(),
                          self.ui.Lastxt_2.toPlainText(),
                          self.ui.Emailtxt_3.toPlainText(),
                          self.ui.Phonetxt_4.toPlainText(),
                          self.ui.Addresstxt_5.toPlainText(),
                          self.ui.Aparttxt_6.toPlainText(),
                          self.ui.Statetxt_7.toPlainText(),
                          self.ui.Citytxt_8.toPlainText(),
                          self.ui.Postaltxt_9.toPlainText(),
                          self.ui.Cardtxt_10.toPlainText(),
                          self.ui.Monthtxt_11.toPlainText(),
                          self.ui.Yeartxt_12.toPlainText(),
                          self.ui.Csctxt_13.toPlainText())



    def on_click2(self):
        self.ui.ventana = QtWidgets.QMainWindow()
        self.ui.ui = Prueba_ventanaemer2(self.Usersom)
        self.ui.ui.show()
    def asignar_valores(self,id):
        respo= Select_id(id)
        self.ui.Nametxt_1.setText(respo.usuario.name)
        self.ui.Lastxt_2.setText(respo.usuario.last)
        self.ui.Emailtxt_3.setText(respo.usuario.email)
        self.ui.Phonetxt_4.setText(respo.usuario.phone)
        self.ui.Addresstxt_5.setText(respo.usuario.street)
        self.ui.Aparttxt_6.setText(respo.usuario.apartment)
        self.ui.Statetxt_7.setText(respo.usuario.state)
        self.ui.Citytxt_8.setText(respo.usuario.city)
        self.ui.Postaltxt_9.setText(respo.usuario.postal)
        self.ui.Cardtxt_10.setText(respo.usuario.credit)
        self.ui.Monthtxt_11.setText(respo.usuario.month)
        self.ui.Yeartxt_12.setText(respo.usuario.year)
        self.ui.Csctxt_13.setText(respo.usuario.csc)

        
    
