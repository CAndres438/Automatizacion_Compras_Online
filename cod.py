import sys

from cod_ui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

class cod (QtWidgets.QDialog):
    
    def __init__(self):
        super().__init__()
        QtWidgets.QWidget.__init__(self)
        Ui_Dia.__init__(self)
        self.ui = Ui_Dia()
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.ui.setupUi(self)