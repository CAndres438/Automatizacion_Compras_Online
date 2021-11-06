import time
import Som
import sys
from Inicializar_ui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt



class Inicio(QtWidgets.QWidget):
    
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        Ui_Inicializar.__init__(self)
        self.ui=Ui_Inicializar()
        self.ui.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.show()
        self.ui.pushbigin.clicked.connect(self.paso)

    def paso(self):
        self.ui.ventana =QtWidgets.QMainWindow()
        self.ui.ui = Som.Ventana()  
        self.ui.ui.show()
        self.close()


   

        
  
    



        
        
        
        
        
        