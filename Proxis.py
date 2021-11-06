import sys
import sqlite3

from proxis_ui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from proximode import Proximode

class Proxis1(QtWidgets.QWidget):
    # switch_window = QtCore.pyqtSignal(str)
    proximode = Proximode
    proxi = [] 
    def __init__(self):
        super().__init__()
        QtWidgets.QWidget.__init__(self)
        Ui_Proxis.__init__(self)
        self.ui = Ui_Proxis()
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.ui.setupUi(self)
        self.ui.pushsave_3.clicked.connect(self.guardado)
        self.ui.pushupdate_1.clicked.connect(self.update)
        self.ui.pushdelate_2.clicked.connect(self.delate)
        
        
        
    def guardado(self):
       
                            
       
        daalu2 = QMessageBox.warning(self, 'SAVE',"Are you sure ?", QMessageBox.Ok | QMessageBox.Cancel,QMessageBox.Cancel)
        if daalu2 == QMessageBox.Ok:
            
            self.proximode = Proximode (self.ui.proxitxt_1.toPlainText().splitlines(),
                               self.ui.headbutradio.isChecked(),
                               self.ui.unheadbutradio_2.isChecked()
                                )
            self.proxi=(self.ui.proxitxt_1.toPlainText().splitlines())
            con = sqlite3.connect('payandbillindates.db')
            cur = con.cursor()   
            cur.execute("DROP TABLE PROXI ")
            cur.execute("CREATE TABLE PROXI (id INTEGER PRIMARY KEY autoincrement, proxi varchar(150))")     
            for x in self.proxi:
             cur.execute('''INSERT INTO PROXI (proxi)  VALUES ('%s')''' % (x))
            con.commit()
            con.close()
            self.show()

        elif daalu2 == QMessageBox.Cancel:
            self.close()
        
    def update(self):
        con = sqlite3.connect('payandbillindates.db')
        cur = con.cursor()   
        cur.execute("SELECT proxi FROM PROXI")                 
        
        rows = cur.fetchall()

        for row in rows:
          row = list(row)
          row=row[0]
          self.proxi.append(row)
          
        con.commit()
        con.close()
        st='\n'.join(self.proxi)
        self.ui.proxitxt_1.setText(st)
        

    def delate(self):
        buttonReply = QMessageBox.warning(self, 'DELETE',"Are you sure to delete these data?", QMessageBox.Ok | QMessageBox.Cancel,QMessageBox.Cancel)
        if buttonReply == QMessageBox.Ok:
            
           self.proxi=[]
           self.ui.proxitxt_1.setText('')
           con = sqlite3.connect('payandbillindates.db')
           cur = con.cursor()   
           cur.execute("DELETE FROM PROXI ")
                          
           con.commit()
           con.close()



        elif buttonReply == QMessageBox.Cancel:
            pass
           
    def get_proximode(self):
        return self.proximode