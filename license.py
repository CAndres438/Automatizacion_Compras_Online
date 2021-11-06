import sys

from pruebadialog_ui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

class license (QtWidgets.QDialog):
    
    def __init__(self):
        super().__init__()
        QtWidgets.QWidget.__init__(self)
        Ui_Dialog.__init__(self)
        self.ui = Ui_Dialog()
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.ui.setupUi(self)