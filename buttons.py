import sys

from buttons_ui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt


class buttons (QtWidgets.QDialog):
    
    def __init__(self):
        super().__init__()
        QtWidgets.QWidget.__init__(self)
        Ui_DiaBu.__init__(self)
        self.ui = Ui_DiaBu()
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.ui.setupUi(self)
        
        
        
   