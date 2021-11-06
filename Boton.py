
from PyQt5 import QtCore, QtGui, QtWidgets

from mainoneboton_ui import *
from ventanaemergente_ui import Ui_popup_1
from pruebaven import *


class Boton():
    pushbig = QtWidgets.QPushButton
    pushacom= QtWidgets.QPushButton
    acomlab=QtWidgets.QLabel
    lab_x_1=QtWidgets.QLabel
    lab_x_2=QtWidgets.QLabel
    lab_x_3=QtWidgets.QLabel
    lab_x_4=QtWidgets.QLabel
    lab_x_5= QtWidgets.QLabel
    central = Ui_popup_1
    ui=Ui_Somniomwindow
    bol = bool
    i= int
    id=str
    Usersom = usersom
    def __init__(self,central,i,ui) -> None:
        self.central=central
        self.i=i
        self.ui=ui
        self.bol=False
        self.id=None
        self.pushbig=QtWidgets.QPushButton(self.central)
        self.pushbig.setGeometry(QtCore.QRect(120, 140, 1051, 41))
        self.pushbig.setStyleSheet("border-radius:10px;\n"
"background-image: url(:/imagenes/imagenes/boulas2.png);\n"
"background-attachment: fixed;\n"
"background-position: right righ;\n"
"background-size: cover;\n"
"background-repeat: no-repeat;\n"
"background-color:rgba(50,48,48);\n"
"border-style: solid;\n"
"border-top: none;\n"
"border-bottom:none;\n"
"border-right: solid;\n"
"border-color: rgba(50, 48, 48);\n"
"border-width: 10px;\n"
"padding-right: 3000px;\n"
"\n"
"")
        self.pushbig.setObjectName("pushbig_"+str(i))
        self.pushacom = QtWidgets.QPushButton(self.central)
        self.pushacom.setGeometry(QtCore.QRect(120, 140, 21, 41))
        self.pushacom.setStyleSheet("background-color: rgb(229, 9, 127);\n"
"border-radius: 10px;\n"
"")

        self.pushacom.setObjectName("pushacomacom_"+str(self.i))
        self.acomlab = QtWidgets.QLabel(central)
        self.acomlab.setGeometry(QtCore.QRect(130, 140, 19, 41))
        self.acomlab.setStyleSheet("border-radius:10px;\n"
"background-color:rgba(50,48,48);\n"
"border-style: solid;\n"
"border-top: none;\n"
"border-left:none;\n"
"border-bottom:none;\n"
"border-right: none;\n"
"border-color: rgba(229, 9, 127);\n"
"border-width: 5px;")
        self.lab_x_1=QtWidgets.QLabel('TextLabel',central)
        self.lab_x_1.setGeometry(QtCore.QRect(140, 150, 171, 21))
        self.lab_x_1.setStyleSheet("padding-top:0px;\n"
"padding-bottom:0px;\n"
"padding-left:0px;\n"
"padding-right:0px;\n"
"font: 8 8pt \"MS Shell Dlg 2\";\n"
"color: rgba(187, 181, 181);\n"
"background-color: rgba(50, 48, 48);\n"
"text-align:center;")
        self.lab_x_1.setObjectName("lab_"+str(i)+"_1")
        self.lab_x_2 = QtWidgets.QLabel('TextLabel',central)
        self.lab_x_2.setGeometry(QtCore.QRect(320, 150, 171, 21))
        self.lab_x_2.setStyleSheet("padding-top:0px;\n"
"padding-bottom:0px;\n"
"padding-left:0px;\n"
"padding-right:0px;\n"
"font: 8 8pt \"MS Shell Dlg 2\";\n"
"color: rgba(187, 181, 181);\n"
"background-color: rgba(50, 48, 48);\n"
"text-align:center;")
        self.lab_x_2.setObjectName("lab_"+str(i)+"_2")
        self.lab_x_3=QtWidgets.QLabel('TextLabel',self.central)
        self.lab_x_3.setGeometry(QtCore.QRect(500, 150, 171, 21))
        self.lab_x_3.setStyleSheet("padding-top:0px;\n"
"padding-bottom:0px;\n"
"padding-left:0px;\n"
"padding-right:0px;\n"
"font: 8 8pt \"MS Shell Dlg 2\";\n"
"color: rgba(187, 181, 181);\n"
"background-color: rgba(50, 48, 48);\n"
"text-align:center;")
        self.lab_x_3.setObjectName("lab_"+str(i)+"_3")
        self.lab_x_4= QtWidgets.QLabel('TextLabel',self.central)
        self.lab_x_4.setGeometry(QtCore.QRect(680, 150, 171, 21))
        self.lab_x_4.setStyleSheet("padding-top:0px;\n"
"padding-bottom:0px;\n"
"padding-left:0px;\n"
"padding-right:0px;\n"
"font: 8 8pt \"MS Shell Dlg 2\";\n"
"color: rgba(187, 181, 181);\n"
"background-color: rgba(50, 48, 48);\n"
"text-align:center;")
        self.lab_x_4.setObjectName("lab_"+str(i)+"_4")
        self.lab_x_5 = QtWidgets.QLabel('TextLabel',self.central)
        self.lab_x_5.setGeometry(QtCore.QRect(880, 150, 71, 21))
        self.lab_x_5.setStyleSheet("padding-top:0px;\n"
"padding-bottom:0px;\n"
"padding-left:0px;\n"
"padding-right:0px;\n"
"font: 8 8pt \"MS Shell Dlg 2\";\n"
"color: rgba(229, 9, 127);\n"
"background-color: rgba(50, 48, 48);\n"
"text-align:center;")
        self.lab_x_5.setObjectName("lab_"+str(i)+"_5")
        
    
    def Eliminar(self):
        self.pushbig.deleteLater()
        self.pushacom.deleteLater()
        self.acomlab.deleteLater()
        self.lab_x_1.deleteLater()
        self.lab_x_2.deleteLater()
        self.lab_x_3.deleteLater()
        self.lab_x_4.deleteLater()
        self.lab_x_5.deleteLater()
        
        pass
    def Guardar_Label(self,a,b,c,d,e):
        self.lab_x_1.setText(a)
        self.lab_x_2.setText(b)
        self.lab_x_3.setText(c)
        self.lab_x_4.setText(d)
        self.lab_x_5.setText(e)
        

        pass
    def Mostrar(self):
        self.pushbig.show()
        self.pushacom.show()
        self.acomlab.show()
        self.lab_x_1.show()
        self.lab_x_2.show()
        self.lab_x_3.show()
        self.lab_x_4.show()
        self.lab_x_5.show()
        pass
    def Posicionar(self,separacion,i):
        self.pushbig.move(120,130+(i*separacion))
        self.pushacom.move(120,130+(i*separacion))
        self.acomlab.move(130,130+(i*separacion))
        self.lab_x_1.move(140,140+(i*separacion))
        self.lab_x_2.move(320,140+(i*separacion))
        self.lab_x_3.move(500,140+(i*separacion))
        self.lab_x_4.move(680,140+(i*separacion))
        self.lab_x_5.move(880,140+(i*separacion))


        
    def Cambio_color(self):
        if(self.bol==False):
        
            self.pushacom.setStyleSheet("background-color: rgb(0, 255, 166);\n"
"border-radius: 10px;\n"
"")
            self.pushacom.show()
            self.bol=True
            pass
        else:
             self.pushacom.setStyleSheet("background-color: rgb(229, 9, 127);\n"
"border-radius: 10px;\n"

"")         
             self.pushacom.show()
             self.bol=False
             pass

            

    def On_click (self):
       
        if(self.id==None):
         self.ui=QtWidgets.QMainWindow()
         self.ui.ui=Prueba_ventanaemer()
         self.ui.ui.show()
        
        else:
         self.ui=QtWidgets.QMainWindow()
         self.ui.ui=Prueba_ventanaemer()
         self.ui.ui.asignar_valores(self.id)
         self.ui.ui.show()


        pass 
        
    def set_id(self,id):
            self.id=id
    
    