import sqlite3
class Delete:
 def __init__(self,id_valor):
        
        con = sqlite3.connect('payandbillindates.db')
        cur = con.cursor()   
        sql="DELETE FROM PAYBILL where ID=? "
        cur.execute(sql,(id_valor,))                 
        con.commit()
        con.close()
         