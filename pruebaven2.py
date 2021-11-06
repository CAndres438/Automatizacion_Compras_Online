import sqlite3
import sys


from ventanaemergente2_ui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from Usuario import usersom
import Usuario
from cod import *




class Prueba_ventanaemer2(QtWidgets.QWidget):
    # switch_window = QtCore.pyqtSignal(str)
    Usersom = usersom
    def __init__(self,Usersom):
        self.Usersom=Usersom
        super().__init__()
        QtWidgets.QWidget.__init__(self)
        Ui_popup_2.__init__(self)
        self.ui = Ui_popup_2()
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.ui.setupUi(self)
        self.ui.pushcod_3.clicked.connect(self.cods)
        self.ui.pushsave_2.clicked.connect(self.registerbill)
        self.ui.pushsave_2.clicked.connect(self.close)
        
        
    def cods(self):
        self.ui.help = QtWidgets.QDialog()
        self.ui.ui = cod()
        self.ui.ui.show()    
        
    def registerbill(self):
        self.Usersom.bill (
                          self.ui.comboBox.currentText(),
                          self.ui.ApartBitxt_2.toPlainText(),
                          self.ui.AddressBitxt_3.toPlainText(),
                          self.ui.PostalBitxt_4.toPlainText(),
                          self.ui.CityBitxt_5.toPlainText())
         
        con = sqlite3.connect('payandbillindates.db')
        cur = con.cursor()

        cur.execute('''INSERT INTO PAYBILL (NAME, LAST, EMAIL, PHONE, STREET, APARTMENT, STATE, CITY, POSTAL, CARD, MONTH, YEAR, CSC,COD, APARTBILL, ADDREESSBILL, POSTALBILL, CITYBILL) 
                       VALUES ('%s', '%s', '%s','%s','%s','%s', '%s', '%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s') ''' % (self.Usersom.name,
                                                                                                          self.Usersom.last,
                                                                                                          self.Usersom.email,
                                                                                                          self.Usersom.phone,
                                                                                                          self.Usersom.street,
                                                                                                          self.Usersom.apartment,
                                                                                                          self.Usersom.state,
                                                                                                          self.Usersom.city,
                                                                                                          self.Usersom.postal,
                                                                                                          self.Usersom.credit,
                                                                                                          self.Usersom.month,
                                                                                                          self.Usersom.year,
                                                                                                          self.Usersom.csc,
                                                                                                          self.Usersom.cod,
                                                                                                          self.Usersom.apartmentbill,
                                                                                                          self.Usersom.streetbill,
                                                                                                          self.Usersom.postabill,
                                                                                                          self.Usersom.citybill)) 
                                                                                               
        con.commit()
        con.close()
                            
    # def on_click3(self):
    #     self.ui.ventana=QtWidgets.QMainWindow()
    #     self.ui.ui=Prueba_ventanaemer()
    #     self.ui.ui.close()    
        
            
            
            
        
               
        
            
            
               
               
               
               
                 
        
    