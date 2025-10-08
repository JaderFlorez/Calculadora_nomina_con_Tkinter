from tkinter import *
from tkinter import ttk,messagebox
from licencia import Licencia 
import os, sys

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS  # cuando se ejecuta como .exe
    except Exception:
        base_path = os.path.abspath(".")  # cuando estás en VS Code
    return os.path.join(base_path, relative_path)

class Bienvenida:
    def __init__(self):
        #caracteristicas de pantalla
        self.ventana=Tk()
        self.ventana.title("Bienvenida")
        self.ventana.geometry("350x450+500+150")
        self.ventana.config(bg="blue")
        self.ventana.iconbitmap(resource_path("logo_ico.ico"))
        #imagen de fondo
        self.fondo= PhotoImage(file=resource_path("imagen_pagina.png"))
        Label(self.ventana,image=self.fondo,bg="blue").pack()
    
        #labels
        
        self.label1=Label(self.ventana,text="Sistema de consulta de nómina")
        self.label1.config(fg="white",bg="blue",font=("Andale Mono Regular",18,"italic"))
        self.label1.place(x=8,y=200)
        
        self.label2=Label(self.ventana,text="Ingrese su nombre")
        self.label2.config(fg="white",bg="blue",font=("Andale Mono Regular",12,"bold"))
        self.label2.place(x=100,y=270)
        
        self.label3=Label(self.ventana,text="2025 Jader Flórez Company")
        self.label3.config(fg="white",bg="blue",font=("Andale Mono Regular",9,"bold"))
        self.label3.place(x=89,y=410)
        
        #entry
        self.dato1=StringVar()
        self.entry1=Entry(self.ventana,bd=2,bg="#eee8e8",fg="blue",textvariable=self.dato1)
        self.entry1.config(font=("Andale Mono Regular",12,"bold"),width=27) #width ancho del entry
        self.entry1.place(x=50,y=295)
        
        #botton
        self.boton1= Button(self.ventana,text="Ingresar",bd=2,bg="white",fg="blue") #bd borde, bg
        self.boton1.config(font=("Andale Mono Regular",14),width=12,command=self.acceso)
        self.boton1.place(x=100,y=330)
        
        self.ventana.mainloop()

    def acceso(self):
        self.largo=self.dato1.get()
        if not self.dato1.get():
            messagebox.showerror("ATENCION","DEBE COLOCAR NOMBRE DE USUARIO!")
        elif len(self.largo)>0 and len(self.largo)<8:
            messagebox.showerror("Atención","El nombre de usuario debe tener más de 8 caracteres")
        else:
            self.ventana.destroy() #esto significa que si no se cumple lo anterior ejecuta lo siguiente
            Licencia()


if __name__=="__main__":
    ejecutar=Bienvenida()

