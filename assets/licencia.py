from tkinter import *
from principal import Principal
import os, sys

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS  # cuando se ejecuta como .exe
    except Exception:
        base_path = os.path.abspath(".")  # cuando estás en VS Code
    return os.path.join(base_path, relative_path)


class Licencia:
    def __init__(self):
        self.ventana= Tk()
        self.ventana.title("TÉRMINOS Y CONDICIONES")
        self.ventana.resizable(False,False)
        self.ventana.geometry("700x400+310+150")
        self.ventana.iconbitmap(resource_path("logo_ico.ico"))
        
        self.fondo= PhotoImage(file=resource_path("imagen_pagina.png"))
        Label(self.ventana,image=self.fondo).place(x=230,y=250)
        
        #labels
        
        self.label1=Label(self.ventana,text="TÉRMINOS Y CONDICIONES")
        self.label1.config(font=("Arial",12,"bold"))
        self.label1.place(x=220,y=10)
        
        
        self.texto_condiciones=Text(self.ventana,width=100,height=12)
        self.texto_condiciones.config(font=("Arial",8,"bold"),bg="white",state=NORMAL)
        self.texto_condiciones.insert(INSERT,'''
    TÉRMINOS Y CONDICIONES

    A.  PROHIBIDA SU VENTA O DISTRIBUCIÓN SIN AUTORIZACIÓN DE JADER FLOREZ LOPEZ.
    B.  PROHIBIDA LA ALTERACIÓN DEL CÓDIGO FUENTE O DISEÑO DE LAS INTERFACES GRÁFICAS.
    C.  JADER FLOREZ NO SE HACE RESPONSABLE DEL MAL USO DE ESTE SOFTWARE.

    LOS ACUERDOS LEGALES EXPUESTOS A CONTINUACION RIGEN EL USO QUE USTED HAGA DE ESTE SOFTWARE
    (JADER FLOREZ), NO SE RESPONSABILIZA DEL USO QUE USTED HAGA CON ESTE SOFTWARE Y SUS SERVICIOS. 
    PARA ACEPTAR ESTOS TERMINOS HAGA CLIC EN (ACEPTO).
    SI USTED NO ACEPTA ESTOS TERMINOS, HAGA CLIC EN (NO ACEPTO) Y NO UTILICE ESTE SOFTWARE.                                                 
        ''')
    
        self.texto_condiciones.place(x=45,y=40)
        self.texto_condiciones.config(state=DISABLED) #para que no puedan escribir en el cuadro de texto
        
        
        #check button
        
        self.acepto=IntVar()
        self.check_acepto=Checkbutton(self.ventana,text="Acepto",font=("Arial",12,"bold"),command=self.aceptar)
        self.check_acepto.place(x=10,y=260)
        
        #botones
        
        self.continuar=Button(self.ventana,text="Acepto",font=("Arial",12,"bold"),width=7,height=2,bd=3,\
            state=DISABLED,command=self.acceso)
        self.continuar.place(x=10,y=290)
        self.cancelar=Button(self.ventana,text="Cancelar",font=("Arial",12,"bold"),width=7,height=2,bd=3,\
            command=self.cancelar)
        self.cancelar.place(x=100,y=290)
    
        self.ventana.mainloop()
        
    def aceptar(self):
        if (self.continuar["state"]==DISABLED):
            self.continuar["state"]=NORMAL
        else:
            self.continuar["state"]=DISABLED
    
    def acceso(self):
        self.ventana.destroy()
        Principal()

    def cancelar(self):
        self.ventana.destroy()
        sys.exit()
