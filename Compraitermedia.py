from Compra import *
from Select_id import Select_id
from PyQt5.QtCore import QThread
class intermedia(QThread):
    def __init__(self,url,cicles,chromedriver, headradio,proxi,unheadradio,size,lista):
        super().__init__()

    def run(self):
        for l in self.lista:
                select=Select_id(l.id)
                c=compra1((self.url),(self.cicles),self.chromedriver,self.headradio,self.proxi,self.unheadradio,self.size,select.usuario)