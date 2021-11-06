
from delete import Delete
from mainoneboton_ui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from pruebaven import *
import Boton
from Boton import*
from Select import *
from Proxis import Proxis1
from proximode import Proximode
from license import *




class Ventana(QMainWindow):
    i=0
    botones = [] 
    proxi=Proximode
    proxiwin= Proxis1
    
    def __init__(self) :
        super().__init__()
        QtWidgets.QMainWindow.__init__(self)
        Ui_Somniomwindow.__init__(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.ui=Ui_Somniomwindow()
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.move_center()
        self.ui.setupUi(self)
        self.ui.pushextra_13.clicked.connect(self.intermedia)
        self.ui.pushhelp_16.clicked.connect(self.help)
        self.ui.pushmenos_14.clicked.connect(self.eliminar)
        
        self.ui.pushreload_17.clicked.connect(self.update)
        
        self.ui.pushproxis_6.clicked.connect(self.windowproxi)
        self.ui.pushabout_15.clicked.connect(self.about)
        self.proxi=Proximode(None,False,False)
        self.show()
        
        

        
            

        
        
        
        
        
            
    def move_center(self):
        screen = QDesktopWidget().screenGeometry()
        form   = self.geometry()
        x_move_step = (screen.width() - form.width()) / 10
        y_move_step = (screen.height() - form.height()) / 10
        self.move(x_move_step, y_move_step)
    
    def agregar(self,i):
        b1=Boton(self.ui.centralwidget,i,self.ui)
        b1.Posicionar(60,self.i)
        b1.Mostrar()
        self.botones.append(b1)
        b1.pushbig.clicked.connect(b1.On_click)
        b1.pushacom.clicked.connect(b1.Cambio_color)
        

        self.i=self.i+1
    
           
        
        
    def intermedia(self):   
    
        self.agregar(self.i)
        
    def help(self):
       self.ui.ventana = QtWidgets.QMainWindow()
       self.ui.ui = help()
       self.ui.ui.show()
       
    def eliminar(self):
       
        buttonReply = QMessageBox.warning(self, 'DELETE',"Are you sure to delete these data?", QMessageBox.Ok | QMessageBox.Cancel,QMessageBox.Cancel)
        if buttonReply == QMessageBox.Ok:
            
            for recorrido in reversed(self.botones):
             if (recorrido.bol):
                 recorrido.Eliminar()
                 self.botones.pop(recorrido.i)
                 self.i=self.i-1
                 if(recorrido.id != None):
                     Delete(recorrido.id)
            self.repocicionamiento()
            self.show()

        elif buttonReply == QMessageBox.Cancel:
            pass
        
        
    def  repocicionamiento(self):
        j=0
        
        for recorer in self.botones:
            recorer.i=j
            recorer.Posicionar(60,j)
            recorer.Mostrar()
            j=j+1
    
    def update (self):
        s=Select()
        lista=s.list_dates
        for recorrido in reversed(self.botones):
             
                 recorrido.Eliminar()
                 self.botones.pop(recorrido.i)
                 self.i=self.i-1
        
        self.show()
        for j in lista:
         self.user=j
         b1=Boton(self.ui.centralwidget,self.i,self.ui)
         b1.Posicionar(60,self.i)
         b1.Mostrar()
         b1.Guardar_Label(j.name,j.last,j.phone,j.city,j.credit)
         b1.set_id(j.id)
         self.botones.append(b1)
         b1.pushbig.clicked.connect(b1.On_click)
         b1.pushacom.clicked.connect(b1.Cambio_color)
        

         self.i=self.i+1
    

      
    
    def windowproxi(self):

        self.ui.ventana = QtWidgets.QMainWindow()
        self.ui.ui = Proxis1()
        self.ui.ui.show()  
        self.proxiwin = self.ui.ui

    def about(self):

        self.ui.ventana = QtWidgets.QMainWindow()
        self.ui.ui = license()
        self.ui.ui.show()
        
        