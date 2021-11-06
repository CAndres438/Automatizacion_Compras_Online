import sqlite3
import time
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtCore import QThread
import Inicio
import sys
import json 
from werkzeug.security import check_password_hash



if __name__ == "__main__":
  mi_aplicacion= QApplication(sys.argv)
  with open('work.json') as file:
     data = json.load(file)
     con = sqlite3.connect('payandbillindates.db')
     cur = con.cursor()   
     cur.execute('SELECT seria from SERIA')  
     registro= cur.fetchone()
     while (registro != None ):
         x=registro
         str=' '.join(x)
         registro = cur.fetchone()
     for client in data['clients']:
        if (check_password_hash(client['first_name'],str)):
         Ini=Inicio.Inicio()
         sys.exit(mi_aplicacion.exec())
        if not (check_password_hash(client['first_name'],str)):
         
         sys.exit(mi_aplicacion.exec())
     con.commit()
     con.close() 
        
    
    
    