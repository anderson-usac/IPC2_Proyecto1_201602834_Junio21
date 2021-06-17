import tkinter as Tk
import re
from tkinter.constants import LEFT, NO, OFF
import ListaPiezas
import MatrizTablero 


class Aplicacion(Tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master=master
        self.pack()
        self.inicializar()

    def colocarPiezas(self):
        self.cx1=self.x1.get()  #Coordenadas en x
        self.cy1=self.y1.get()  #coordenada en y
        self.coordenadaJ1=self.cx1+self.cy1
        for i in range(int(self.id_casilla)):
            if i==int(self.coordenadaJ1):
                self.el_tablero['fill']='red'
                print(i)
        
        
                

        
        MatrizTablero.Matriz.insertar()

    def Tablero(self):
        self.frame1.destroy()
        self.frame2=Tk.Frame(self.master)
        self.frame2.pack(expand='true',fill='both')
        self.filas=int(self.fila.get())
        self.columnas=int(self.col.get())
        self.J1L=Tk.Label(self.frame2,text="Jugador 1",font='Arial 12')
        self.J1L.place(relx=0.015,rely=0.7)
        self.J1x=Tk.Label(self.frame2,text="Pos X:",font="Arial 12")
        self.J1x.place(relx=0.015,rely=0.75)
        self.x1=Tk.StringVar()
        self.textJ1x=Tk.Entry(self.frame2,textvariable=self.x1)
        self.textJ1x.place(relx=0.1,rely=0.75,width=50)
        self.J1y=Tk.Label(self.frame2,text="Pos Y:",font="Arial 12")
        self.J1y.place(relx=0.015,rely=0.83)
        self.y1=Tk.StringVar()
        self.textJ1y=Tk.Entry(self.frame2,textvariable=self.y1)
        self.textJ1y.place(relx=0.1,rely=0.83,width=50)
        self.J2L=Tk.Label(self.frame2,text="Jugador 2",font="Arial 12")
        self.J2L.place(relx=0.25,rely=0.7)
        self.J2x=Tk.Label(self.frame2,text="Pos X:",font="Arial 12")
        self.J2x.place(relx=0.25,rely=0.75)
        self.x2=Tk.StringVar()
        self.textJ2x=Tk.Entry(self.frame2,textvariable=self.x2)
        self.textJ2x.place(relx=0.35,rely=0.75,width=50)
        self.J2y=Tk.Label(self.frame2,text="Pos Y:",font="Arial 12")
        self.J2y.place(relx=0.25,rely=0.83)
        self.y2=Tk.StringVar()
        self.textJ2y=Tk.Entry(self.frame2,textvariable=self.y2)
        self.textJ2y.place(relx=0.35,rely=0.83,width=50)
        self.BtnJ1=Tk.Button(self.frame2,text='Jugador 1',command=self.colocarPiezas)
        self.BtnJ1.place(relx=0.02,rely=0.9)
        #Tablero----------
        self.filas = self.filas
        self.columnas = self.columnas
        self.dim_casilla = 35
        self.color_casillas = "white"
        self.dim_borde=0
        self.el_tablero = Tk.Canvas(self.frame2,
            width=self.filas * self.dim_casilla,
            height=self.columnas * self.dim_casilla
            )

        self.el_tablero.place(relx=0.030,rely=0.030)
        self.el_tablero.bind("<Button-1>")
        for r in range(self.filas):
            for c in range(self.columnas):
                self.id_casilla = str(r + 1).zfill(2) +  str(c + 1).zfill(2)
                x1, y1 = c * self.dim_casilla, r * self.dim_casilla
                x2, y2 = x1 + self.dim_casilla, y1 + self.dim_casilla 
                self.el_tablero.create_rectangle(
                    x1, y1, x2, y2,
                    fill=self.color_casillas,
                    tags=self.id_casilla
                    
                    )   
                #print(self.id_casilla)
        self.J1L.config(fg=self.colorJ1)
        self.J2L.config(fg=self.colorJ2)

    def asignarcolorJ1(self):
        self.color=self.v.get()
        if self.color==1:
            self.colorJ1='red'
            
        elif self.color==2:
            self.colorJ1='blue'
        elif self.color==3:
            self.colorJ1='yellow'
        elif self.color==4:
            self.colorJ1='green'

    def asignarcolorJ2(self):
        self.color=self.v.get()
        if self.color==1:
            self.colorJ2='red'
            
        elif self.color==2:
            self.colorJ2='blue'
        elif self.color==3:
            self.colorJ2='yellow'
        elif self.color==4:
            self.colorJ2='green'
        

    def InicioJuego(self):
        self.v=Tk.IntVar()
        self.frame1=Tk.Frame(self.master)
        self.frame1.pack(expand='true',fill='both')
        self.color=Tk.Label(self.frame1,text='Colores',font='Arial 14')
        self.color.place(relx=0.010,rely=0.010)
        self.radiored=Tk.Radiobutton(self.frame1,text='Rojo',fg='red',variable=self.v,value=1)
        self.radiored.place(relx=0.010,rely=0.070)
        self.radioblue=Tk.Radiobutton(self.frame1,text='Azul',fg='Blue',variable=self.v,value=2)
        self.radioblue.place(relx=0.010,rely=0.15) 
        self.radioyellow=Tk.Radiobutton(self.frame1,text='Amarillo',fg='yellow',variable=self.v,value=3)
        self.radioyellow.place(relx=0.010,rely=0.25)
        self.radiogreen=Tk.Radiobutton(self.frame1,text='Verde',fg='green',variable=self.v,value=4)
        self.radiogreen.place(relx=0.010,rely=0.35)
        self.J1=Tk.Label(self.frame1,text='Jugador 1',font='Arial 14')
        self.J1.place(relx=0.25,rely=0.010)
        self.textJ1=Tk.Entry(self.frame1,font='Helvetica 14')
        self.textJ1.place(relx=0.25,rely=0.065)
        self.botonJ1=Tk.Button(self.frame1,text='Jugador1',font='Arial 12',command=self.asignarcolorJ1)
        self.botonJ1.place(relx=0.60,rely=0.060)
        self.J2=Tk.Label(self.frame1,text='Jugador 2',font='Arial 14')
        self.J2.place(relx=0.25,rely=0.15)
        self.textJ2=Tk.Entry(self.frame1,font='Helvetica 14')
        self.textJ2.place(relx=0.25,rely=0.20)
        self.botonJ2=Tk.Button(self.frame1,text='Jugador2',font='Arial 12',command=self.asignarcolorJ2)
        self.botonJ2.place(relx=0.60,rely=0.20)
        self.columas=Tk.Label(self.frame1,text='Columnas',font='Arial 14')
        self.columas.place(relx=0.010,rely=0.4)
        self.col=Tk.StringVar()
        self.textcol=Tk.Entry(self.frame1,textvariable=self.col)
        self.textcol.place(relx=0.15,rely=0.41,width=50)
        self.filas=Tk.Label(self.frame1,text='Filas',font='Arial 14')
        self.filas.place(relx=0.010,rely=0.5)
        self.fila=Tk.StringVar()
        self.textfil=Tk.Entry(self.frame1,textvariable=self.fila)
        self.textfil.place(relx=0.15,rely=0.51,width=50)
        self.botoncrear=Tk.Button(self.frame1,text='Crear Tablero',font='Arial 12',command=self.Tablero)
        self.botoncrear.place(relx=0.3,rely=0.45)


    
    def inicializar(self):
        menubar=Tk.Menu(self.master)
        m_barra1=Tk.Menu(menubar)
        m_panel=Tk.Menu(menubar)
        menubar.add_cascade(label='Barra de menu',menu=m_barra1) #Crea la opcion sobre la barra
        m_barra1.add_command(label='Abrir Partida') #Sub opciones del menu
        m_barra1.add_command(label='Guardar Partida')
        m_barra1.add_command(label='Ayuda')
        menubar.add_cascade(label='Inicio de juego',command=self.InicioJuego)
        menubar.add_cascade(label='Reportes')
        self.master.configure(menu=menubar)

def main():
    ventana_principal=Tk.Tk()
    ventana_principal.title('Ventana Principal')
    ventana_principal.geometry('860x700')
    app=Aplicacion(ventana_principal)
    app.mainloop()

if __name__ == "__main__":
    main()


