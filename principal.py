from tkinter import *
from tkinter import ttk,messagebox
import os, sys

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS  # cuando se ejecuta como .exe
    except Exception:
        base_path = os.path.abspath(".")  # cuando estás en VS Code
    return os.path.join(base_path, relative_path)

class Principal:
    def __init__(self):
        self.ventana=Tk()
        self.ventana.title("Pantalla principal")
        self.ventana.resizable(False,False)
        self.ventana.geometry("640x535+350+100")
        self.ventana.config(bg="blue")
        self.ventana.iconbitmap(resource_path("logo_ico.ico"))
        
        #menú de opciones
        
        self.menubar1=Menu(self.ventana)
        self.ventana.config(menu=self.menubar1)
        self.opciones1=Menu(self.menubar1,tearoff=0)
        self.opciones2=Menu(self.menubar1,tearoff=0)
        self.menubar1.add_cascade(label="opciones",menu=self.opciones1)
        self.opciones1.add_command(label="salir",command=self.salir,font=("Arial",10,"bold"))
        
        self.menubar1.add_cascade(label="Acerca de...",menu=self.opciones2)
        self.opciones2.add_command(label="Info",command=self.acerca,font=("Arial",10,"bold"))
        
        #label bienvenida
        self.l_bienvenida=Label(self.ventana,text="Bienvenid@!")
        self.l_bienvenida.config(fg="white",bg="blue",font=("Andale Mono Regular",20,"bold"))
        self.l_bienvenida.place(x=320,y=30)
        
        #label detalle
        self.l_detalle=Label(self.ventana,text="Cálculo de nómina")
        self.l_detalle.config(fg="white",bg="blue",font=("Andale Mono Regular",18,"bold"))
        self.l_detalle.place(x=290,y=80)

        #label resultado
        
        self.l_resultado=Label(self.ventana,text="Resultado del cálculo")
        self.l_resultado.config(fg="white",bg="blue",font=("Andale Mono Regular",11,"bold"))
        self.l_resultado.place(x=260,y=150)
        
        self.area_resultado=Text(self.ventana,width=45,height=15) #que se insertará un cuadro de texto
        self.area_resultado.config(font=("Andale Mono Regular",11,"bold"),bg="#eee8e8",fg="blue",state=DISABLED)
        #state=DISABLED para que no puedan escribir en el texto
        self.area_resultado.place(x=260,y=180)
        
        #label pie de interfaz
        
        self.l_flooter=Label(self.ventana,text="2025 Jader Flórez.")
        self.l_flooter.config(fg="white",bg="blue",font=("Andale Mono Regular",10,"bold"))
        self.l_flooter.place(x=225,y=480)
        
        #label salario
        
        self.l_salario=Label(self.ventana,text="Ingrese monto del salario")
        self.l_salario.config(fg="white",bg="blue",font=("Andale Mono Regular",11,"bold"))
        self.l_salario.place(x=30,y=25)
        
        self.dato_salario=IntVar() #porque vamos a manejar entero
        self.e_salario=Entry(self.ventana,bd=2,bg="#eee8e8",fg="blue",textvariable=self.dato_salario)
        self.e_salario.config(font=("Andale Mono Regular",12,"bold"),width=22)
        self.e_salario.place(x=30,y=50)
        
        #label dias trabajados
        
        self.l_dias=Label(self.ventana,text="Ingrese días trabajados")
        self.l_dias.config(fg="white",bg="blue",font=("Andale Mono Regular",11,"bold"))
        self.l_dias.place(x=30,y=90)
        
        self.dato_dias=IntVar() 
        self.e_dias=Entry(self.ventana,bd=2,bg="#eee8e8",fg="blue",textvariable=self.dato_dias)
        self.e_dias.config(font=("Andale Mono Regular",12,"bold"),width=22)
        self.e_dias.place(x=30,y=110)
        
        #label horas extras diurnas
        
        self.l_hed=Label(self.ventana,text="Ingrese horas extras diurnas")
        self.l_hed.config(fg="white",bg="blue",font=("Andale Mono Regular",11,"bold"))
        self.l_hed.place(x=30,y=150)
        
        self.dato_hed=IntVar() #porque vamos a manejar entero
        self.e_hed=Entry(self.ventana,bd=2,bg="#eee8e8",fg="blue",textvariable=self.dato_hed)
        self.e_hed.config(font=("Andale Mono Regular",12,"bold"),width=22)
        self.e_hed.place(x=30,y=170)
        
        #label horas extras nocturnas
        
        self.l_hen=Label(self.ventana,text="Ingrese horas extras\nnocturnas")
        self.l_hen.config(fg="white",bg="blue",font=("Andale Mono Regular",11,"bold"))
        self.l_hen.place(x=30,y=200)
        
        self.dato_hen=IntVar() 
        self.e_hen=Entry(self.ventana,bd=2,bg="#eee8e8",fg="blue",textvariable=self.dato_hen)
        self.e_hen.config(font=("Andale Mono Regular",12,"bold"),width=22)
        self.e_hen.place(x=30,y=240)
        
        #label horas extras diurnas dominicales
        
        self.l_hedd=Label(self.ventana,text="Ingrese horas extras\ndiurnas dominicales")
        self.l_hedd.config(fg="white",bg="blue",font=("Andale Mono Regular",11,"bold"))
        self.l_hedd.place(x=30,y=270)
        
        self.dato_hedd=IntVar() #porque vamos a manejar entero
        self.e_hedd=Entry(self.ventana,bd=2,bg="#eee8e8",fg="blue",textvariable=self.dato_hedd)
        self.e_hedd.config(font=("Andale Mono Regular",12,"bold"),width=22)
        self.e_hedd.place(x=30,y=310)
        
        #label horas extras nocturnas dominicales o festivos
        
        self.l_hendf=Label(self.ventana,text="Ingrese horas extras\ndominicales o festivos")
        self.l_hendf.config(fg="white",bg="blue",font=("Andale Mono Regular",11,"bold"))
        self.l_hendf.place(x=30,y=340)
        
        self.dato_hendf=IntVar() 
        self.e_hendf=Entry(self.ventana,bd=2,bg="#eee8e8",fg="blue",textvariable=self.dato_hendf)
        self.e_hendf.config(font=("Andale Mono Regular",12,"bold"),width=22)
        self.e_hendf.place(x=30,y=380)
        
        #botones calcular y limpiar
        self.b_calcular=Button(self.ventana,text="Calcular",width=8,height=2,command=self.calcular_nomina)
        self.b_calcular.config(font=("Andale Mono Regular",12,"bold"),fg="blue",bg="white",bd=5)
        self.b_calcular.place(x=130,y=420)
        
        self.b_limpiar=Button(self.ventana,text="Limpiar",width=8,height=2,command=self.limpia_datos)
        self.b_limpiar.config(font=("Andale Mono Regular",12,"bold"),fg="blue",bg="white",bd=5)
        self.b_limpiar.place(x=30,y=420)

        
        self.ventana.mainloop()

    def calcular_nomina(self):
        # Validar datos obligatorios
        if not self.dato_salario.get() or not self.dato_dias.get():
            messagebox.showerror("AVISO", "LOS CAMPOS DEL SALARIO Y DÍAS TRABAJADOS NO DEBEN QUEDAR VACÍOS")
        else: 
            self.area_resultado.config(state=NORMAL) #es para habilitar el cuadro que lo teniamos desabilitado
            self.area_resultado.delete("1.0","end")
            salario_base= self.dato_salario.get()
            dias_trabajados = self.dato_dias.get()
            hed = self.dato_hed.get()
            hen = self.dato_hen.get()
            hedd = self.dato_hedd.get()
            hendf = self.dato_hendf.get()
            
            # Cálculos
            horas_mensuales = 230
            valor_dia = salario_base / 30
            valor_hora = salario_base / horas_mensuales

            # Horas extra
            if self.dato_hed.get() or self.dato_hen.get() or self.dato_hedd.get() or self.dato_hendf.get():
                valor_hed = (valor_hora*hed) * 1.25
                valor_hen = (valor_hora*hen) * 1.75
                valor_hedd = (valor_hora*hedd) * 2.0
                valor_hendf = (valor_hora*hendf) * 2.5
                total_extras = (hed * valor_hed) + (hen * valor_hen) + (hedd * valor_hedd) + (hendf * valor_hendf)
            else:
                valor_hed = 0
                valor_hen = 0
                valor_hedd = 0
                valor_hendf = 0
                total_extras= 0

            # Aportes
            aporte_salud = salario_base * 0.04
            aporte_pension = salario_base * 0.04
            
            # Auxilio de transporte
            auxilio_transporte = 0
            if salario_base <= 2846000:
                auxilio_transporte = 200000
                salario_con_auxilio = salario_base + auxilio_transporte
                salario_neto = salario_con_auxilio + total_extras - (aporte_salud + aporte_pension)
            else:
                salario_neto= salario_base + total_extras- (aporte_salud + aporte_pension)
                salario_con_auxilio=0

            # Vacaciones
            dias_vacaciones = (dias_trabajados / 360) * 15
            valor_vacaciones = (salario_base * dias_vacaciones) / 30

            # Preparar resultado
            resultado = f"""
    Salario base: {salario_base:,}
    Auxilio de transporte: {auxilio_transporte:,}
    Salario total (con auxilio si aplica): {salario_con_auxilio:,}

    Valor día: {valor_dia:.0f}
    Valor hora ordinaria: {valor_hora:.0f}

    Valor hora extra diurna (25%): {valor_hed:.0f}
    Valor hora extra nocturna (75%): {valor_hen:.0f}
    Valor hora extra diurna dominical (100%): {valor_hedd:.0f}
    Hora extra nocturna dominical(150%): {valor_hendf:.0f}

    Total horas extras: {total_extras:.0f}

    Aporte salud (4%): {aporte_salud:.0f}
    Aporte pensión (4%): {aporte_pension:.0f}
    
    SALARIO NETO: {salario_neto:.0f}

    Días de vacaciones: {dias_vacaciones:.0f}
    Valor de vacaciones: {valor_vacaciones:.0f}
            """
            self.area_resultado.insert(END, resultado)
            self.area_resultado.config(state=DISABLED)
    
    def acerca(self):
        messagebox.showinfo("Info",'''        SISTEMA DE CONTROL DE VACACIONES
        Desarrollado por: Jader Andrés Flórez López
        Derechos reservados 2025''')
    
    def salir(self):
        self.ventana.destroy()
        sys.exit()
    
    def limpia_datos(self): #esta es la función para el botón limpiar
        self.area_resultado.config(state=NORMAL) #aqui habilito el area 
        self.area_resultado.delete("1.0","end") #con delete borro o limpio el area
        self.area_resultado.config(state=DISABLED) #vuelvo a dejar el area inhabilitada para que no escriban en ella
        self.e_salario.delete(0, END)  # <-- aquí sí borro el contenido del Entry
        self.e_dias.delete(0, END)
        self.e_hed.delete(0, END)
        self.e_hen.delete(0, END)
        self.e_hedd.delete(0, END)
        self.e_hendf.delete(0, END)
        
        # Poner variables a cero
        self.dato_salario.set(0)
        self.dato_dias.set(0)
        self.dato_hed.set(0)
        self.dato_hen.set(0)
        self.dato_hedd.set(0)
        self.dato_hendf.set(0)
            
        