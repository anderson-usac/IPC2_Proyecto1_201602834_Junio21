import tkinter as Tk
import re
from tkinter.constants import LEFT, NO, OFF
import ListaPiezas

class Aplicacion(Tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master=master
        self.pack()
        
        self.inicializar()

    def Tablero(self):
        self.frame1.destroy()
        filas=int(self.fila.get())
        columnas=int(self.col.get())

        self.filas = filas
        self.columnas = columnas
        self.dim_casilla = 35
        self.color_casillas = "white"
        self.dim_borde=0
        self.el_tablero = Tk.Canvas(
            width=self.filas * self.dim_casilla,
            height=self.columnas * self.dim_casilla
            )

        self.el_tablero.place(relx=0.020,rely=0.020)
        self.el_tablero.bind("<Button-1>")
        for r in range(self.filas):
            for c in range(self.columnas):
                id_casilla = str(r + 1).zfill(2) +  str(c + 1).zfill(2)
                x1, y1 = c * self.dim_casilla, r * self.dim_casilla
                x2, y2 = x1 + self.dim_casilla, y1 + self.dim_casilla 
                self.el_tablero.create_rectangle(
                    x1, y1, x2, y2,
                    fill=self.color_casillas,
                    tags=id_casilla
                    
                    )   
               # print(id_casilla)

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
        self.botonJ1=Tk.Button(self.frame1,text='Jugador1',font='Arial 12')
        self.botonJ1.place(relx=0.60,rely=0.060)
        self.J2=Tk.Label(self.frame1,text='Jugador 2',font='Arial 14')
        self.J2.place(relx=0.25,rely=0.15)
        self.textJ2=Tk.Entry(self.frame1,font='Helvetica 14')
        self.textJ2.place(relx=0.25,rely=0.20)
        self.botonJ2=Tk.Button(self.frame1,text='Jugador2',font='Arial 12')
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


