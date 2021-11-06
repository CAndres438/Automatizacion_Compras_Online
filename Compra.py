from PyQt5.QtWidgets import QMessageBox
from selenium import webdriver
import time
import random
import base64
from selenium.webdriver import ActionChains
import cv2
from selenium.webdriver.common import by
import threading
import os
import zipfile
import sqlite3
import img2pdf
from reportlab.pdfgen import canvas
from PyQt5.QtCore import QThread
class compra1 (QThread):
 url=str
 j=int
 chrome=str
 bolproxy= bool
 direccionproxy=[]
 bolheadlesst=str
 talla=int

 def __init__(self,url,j,chrome,bolproxies,proxy,bolheadlesst,talla,usuario):
     self.url=url
     self.j=int(j)
     self.chrome=chrome
     self.bolproxy=bolproxies
     self.direccionproxy=proxy
     self.bolheadlesst=bolheadlesst
     self.talla=talla
     self.usuario=usuario
     hilos=[]
     i=self.j
     con = sqlite3.connect('payandbillindates.db')
     cur = con.cursor()  
     cur.execute("DROP TABLE COMPRAS ")
     cur.execute("create table COMPRAS (id integer PRIMARY KEY AUTOINCREMENT,link varchar(150),talla varchar(10),nombre varchar(50),apellido varchar(50),CARD VARCHAR(25),ESTADO VARCHAR(10))") 
     con.commit()
     con.close()  

     for x in range(0,i):
      hilos.append(threading.Thread(target=self.compra, args=(url,str(x),chrome,bolproxies,proxy,bolheadlesst,talla,usuario)))
     for x in range(0,i):
       hilos[x].start()
     for x in range(0,i):
      hilos[x].join()


     pass
 def compra(self,url1,n,chrome,bolproxies,direccionproxy,bolheadlesst,talla,usuario):
 
  def esperar_al_boton(xpath,f):
 
     boton = None
     i=0
     
     while not boton and i<f :
         try:
             boton = driver.find_element_by_xpath(xpath)
         except:
             boton = None
             i=i+1
             
 
     return boton
  def esperar_al_boton_css(css,f):
     
 
     i=0
     boton = None
     
     
     while not boton and i<f :
         try:
             boton = driver.find_element_by_css_selector(css)
         except:
             boton = None
             i=i+1
             
 
     return boton      
  def guardar_canvas_to_png(canvas, s):
     
     time.sleep(3)
     canvas_base64 = driver.execute_script("", canvas)
     canvas_png = base64.b64decode(canvas_base64)
     with open(r""+s, 'wb') as f:
      f.write(canvas_png)
  def solve_catcha():
     actionChains = ActionChains(driver)
     
     capcha=esperar_al_boton_css(".geetest_radar_tip_content",100000)
     capcha.click()
     canvas =esperar_al_boton("",10)
     pieza = esperar_al_boton("",10)
     guardar_canvas_to_png(canvas,"canvas"+n+".png")
     guardar_canvas_to_png(pieza,"pieza"+n+".png")
     img_grey = cv2.imread("canvas"+n+".png",0)
     img_grey1 = cv2.imread("pieza"+n+".png",0)
     imacanny=cv2.Canny(img_grey,150,500)
     imacanny1=cv2.Canny(img_grey1,150,500)
     imagenrecor=imacanny1[0:160,0:55]
     res=cv2.matchTemplate(imacanny,imagenrecor,cv2.TM_CCOEFF_NORMED)
     minv,maxv,minlocation,maxlocation=cv2.minMaxLoc(res)
     slit=esperar_al_boton("",10)
     actionChains.drag_and_drop_by_offset(slit,maxlocation[0]-2,8).perform()
     print(maxlocation)
     time.sleep(2)
     cv2.waitKey(0)
  def talla_agregar_carrito(key,talla):
     k=None
     if(key== False):
         time.sleep(2)
         k=cerrar_emergente(key)
     t=encontar_talla(talla)
     if(t!=None):
       t.click()
    
     if (k != None):
      key=k
     if(key== False):
         cerrar_emergente(key)
     add=esperar_al_boton_css("",10) #espera al boton de añadir al carrito lo busca en formato css y lo guarda en una variable
     add.click() # da click en el botton 
     if (k != None):
      key=k
     return(key)
  def cerrar_emergente(key):
     emergente=esperar_al_boton('',10)
     if (emergente != None):
         cerrar=esperar_al_boton('',10)
         key=True
         cerrar.click()
         return key
     return None
  def encontar_talla(talla):
     a=None
     i=1
     while(a!=talla):
      i= str(i)
      t=esperar_al_boton('',10)
      elemet=t
      if (t != None):
       a=t.text
      i=int(i)+1
      if(i>20):
          return None
          break
     return elemet
  def guardarjpg(driver,v):
     driver.get_screenshot_as_file(""+str(v)+".jpg")
     
  def guardarsql():
      con = sqlite3.connect('payandbillindates.db')
      cur = con.cursor()  
      cur.execute('''INSERT INTO COMPRAS (link,talla,nombre,apellido,CARD,ESTADO)  VALUES ('%s','%s','%s','%s','%s','%s')''' % (str(self.url)+str(n),self.talla,self.usuario.name,self.usuario.last,self.usuario.credit,"(1/10)"))
      cur.execute('''INSERT INTO Record (link,talla,nombre,apellido,CARD,ESTADO,fecha)  VALUES ('%s','%s','%s','%s','%s','%s',CURRENT_TIMESTAMP)''' % (str(self.url)+str(n),self.talla,self.usuario.name,self.usuario.last,self.usuario.credit,"(1/10)"))
      cur.execute('SELECT * FROM Record WHERE ID = (SELECT MAX(ID) FROM Record)')
      row= cur.fetchone()
      con.commit()
      con.close()  
      return row[0]
  def retornaridsql():
      con = sqlite3.connect('payandbillindates.db')
      cur = con.cursor()  
      cur.execute('SELECT * FROM COMPRAS c WHERE c.link =? ',((str(self.url)+str(n)),))
      row= cur.fetchone()
      con.commit()
      con.close()
      return row[0]

  def aumentarestado(id1,v):
      con = sqlite3.connect('payandbillindates.db')
      cur = con.cursor()  
      cur.execute('SELECT * FROM COMPRAS c WHERE c.id =? ',(id1,))
      row= cur.fetchone()
      row=row[6]
      if (row =='(1/10)'):
          row='2/10'
      elif (row =='2/10'):
          row='3/10'
      elif (row =='3/10'):
          row='4/10'
      elif (row =='4/10'):
          row='5/10'
      elif (row =='5/10'):
          row='6/10'
      elif (row =='6/10'):
          row='7/10'
      elif (row =='7/10'):
          row='8/10'
      elif (row =='8/10'):
          row='9/10'
      elif (row =='9/10'):
          row='10/10'
      elif (row =='10/10'):
          row='COMPLETE'
      con = sqlite3.connect('payandbillindates.db')
      cur = con.cursor()  
      udate='UPDATE COMPRAS set ESTADO="'+str(row)+'" where id ='+str(id1)
      udate1='UPDATE record set ESTADO="'+str(row)+'" where id ='+str(v)
      cur.execute(udate)
      cur.execute(udate1)
      con.commit()
      con.close()
  def Error(id1):
      con = sqlite3.connect('payandbillindates.db')
      cur = con.cursor()  
      udate='UPDATE COMPRAS set ESTADO="Error" where id ='+str(id1)
      cur.execute(udate)
      con.commit()
      con.close()
  def create_chromedriver(PROXY_HOST, PROXY_PORT, PROXY_USER, PROXY_PASS, USER_AGENT,bolheadlesst,use_proxy,chrome):
    manifest_json = """
    {
    "version": "1.0.0",
    "manifest_version": 2,
    "name": "Chrome Proxy",
    "permissions": [
        "proxy",
        "tabs",
        "unlimitedStorage",
        "storage",
        "<all_urls>",
        "webRequest",
        "webRequestBlocking"
    ],
    "background": {
        "scripts": ["background.js"]
    },
    "minimum_chrome_version":"22.0.0"
    }
    """

    background_js = """
    var config = {
        mode: "fixed_servers",
        rules: {
        singleProxy: {
            scheme: "http",
            host: "%s",
            port: parseInt(%s)
        },
        bypassList: ["localhost"]
        }
    };

    chrome.proxy.settings.set({value: config, scope: "regular"}, function() {});

    function callbackFn(details) {
        return {
            authCredentials: {
            username: "%s",
            password: "%s"
            }
        };
    }

    chrome.webRequest.onAuthRequired.addListener(
            callbackFn,
            {urls: ["<all_urls>"]},
            ['blocking']
    );
    """ % (PROXY_HOST, PROXY_PORT, PROXY_USER, PROXY_PASS)
    def get_chromedriver(use_proxy,bolheadlesst,chrome, user_agent=USER_AGENT):
        path = os.path.dirname(os.path.abspath(__file__))
        chrome_options = webdriver.ChromeOptions()
        chrome_options .add_argument("start-maximized")
        if use_proxy:
            pluginfile = 'proxy_auth_plugin.zip'
            with zipfile.ZipFile(pluginfile, 'w') as zp:
                zp.writestr("manifest.json", manifest_json)
                zp.writestr("background.js", background_js)
            chrome_options.add_extension(pluginfile)
        if user_agent:
            chrome_options.add_argument('--user-agent=%s' % USER_AGENT)

        if(bolheadlesst==True):
         chrome_options.add_argument ("--headless") # oculta el navegador
        driver = webdriver.Chrome(
            os.path.join(path, r''+chrome),
            chrome_options=chrome_options)
        return driver
    driver = get_chromedriver(use_proxy,bolheadlesst,chrome)
    return driver
  
  user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
  try:
    if(bolproxies):
        PROXY = random.choice(direccionproxy)
        PROXY= PROXY.split(':')
        print(PROXY)# imprime el proxy implementado
        driver=create_chromedriver(PROXY[0], PROXY[1], PROXY[2], PROXY[3], user_agent,bolheadlesst,bolproxies,chrome)
    else:
        driver=create_chromedriver(None, None,None, None, user_agent,bolheadlesst,bolproxies,chrome)
    driver.get(url1)
    h=guardarsql() 
    id=retornaridsql()
    print("este es el id"+str(id))
    actionChains = ActionChains(driver)
    key = False
    agrede=esperar_al_boton('',100) # espera al boton de aceptar terminos en formato xml y lo guarda en la variable
    if(agrede != None):
     agrede.click()# da click en el botton 
    aumentarestado(id,h)
    k=talla_agregar_carrito(key,talla)
    aumentarestado(id,h)
    key=k
    time.sleep(3)
    frame=esperar_al_boton('',10)
    
    if (frame != None):
     driver.switch_to_frame(frame)
    solve_catcha()
    aumentarestado(id,h)
    time.sleep(1)
    url=driver.current_url#guarda la direccion actual url
    if( url == ''):
        driver.back()
        key=False
    talla_agregar_carrito(key,talla)
    aumentarestado(id,h)
    carrito=esperar_al_boton_css('.Icon--cart_notEmpty',100000)
    carrito.click()
    time.sleep(1) 
    comprar=esperar_al_boton_css('',10)
    comprar.click()
    aumentarestado(id,h)
    firstName=esperar_al_boton_css('',10)
    firstName.send_keys(usuario.name)
    lastName=esperar_al_boton_css('',10)
    lastName.send_keys(usuario.last)
    email=esperar_al_boton_css('',10)
    email.send_keys(usuario.email)
    telefono=esperar_al_boton_css('',1000)
    telefono.send_keys(usuario.phone)
    continuar=esperar_al_boton_css('',1000)
    continuar.click()
    aumentarestado(id,h)
    address=esperar_al_boton_css('',1000)
    address.send_keys(usuario.street)
    Unit_No_Casille=esperar_al_boton('',1000)	
    Unit_No_Casille.send_keys(usuario.apartment)
    zipcode=esperar_al_boton_css('',1000)
    zipcode.send_keys(usuario.postal)
    time.sleep(10)
    continuar2=esperar_al_boton_css("",1000)
    continuar2.click()
    aumentarestado(id,h)
   
    time.sleep(10)
    frame=esperar_al_boton('',10)
    driver.switch_to_frame(frame)
    card_number=esperar_al_boton('',10)  
    card_number.send_keys(usuario.credit)	
    driver.switch_to.parent_frame()
    frame=esperar_al_boton('',1000)
    driver.switch_to_frame(frame)
    Month=esperar_al_boton('',10)	
    Month.send_keys(usuario.month)
    driver.switch_to.parent_frame()
    frame=esperar_al_boton('',10)
    driver.switch_to_frame(frame)
    Year=esperar_al_boton('',10)		
    Year.send_keys(usuario.year)
    driver.switch_to.parent_frame()
    frame=esperar_al_boton('',10)
    driver.switch_to_frame(frame)
    CsC=esperar_al_boton_css('',10)	
    CsC.send_keys(usuario.csc)
    driver.switch_to.parent_frame()
    aumentarestado(id,h)
    checkelements=esperar_al_boton(']',10)
    checkelements.click()
    country=esperar_al_boton('',10)
    country.click()
    select=esperar_al_boton(''+str(usuario.cod)+']',10)
    select.click()
    address_2=esperar_al_boton_css('',10)
    address_2.send_keys(usuario.streetbill)
    zipcode_2=esperar_al_boton_css('e',10)
    zipcode_2.send_keys(usuario.postabill)
    city=esperar_al_boton('',10)
    city.send_keys(usuario.citybill)
    time.sleep(1)
    continuar3=esperar_al_boton('',10)
    continuar3.click()
    aumentarestado(id,h)
    time.sleep(5)
    Place_Order=esperar_al_boton_css('',10)
    time.sleep(5)
    Place_Order.click()

    
  except:
        Error(id)
    

 
 

