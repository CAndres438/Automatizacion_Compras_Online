import sqlite3


class Select :
    list_dates=[]
    def __init__(self):
        self.list_dates=[]
        con = sqlite3.connect('payandbillindates.db')
        cur = con.cursor()   
        cur.execute("SELECT * FROM PAYBILL")                 
        
        rows = cur.fetchall()

        for row in rows:
          row = list(row)
          
          
        con.commit()
        con.close()
         
          


    
    