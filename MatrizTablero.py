class Nodo1():
    def __init__(self,fila,columna,pieza):
        self.pieza=pieza
        self.fila=fila
        self.columna=columna
        self.derecha=None
        self.izquierda=None
        self.abajo=None
        self.arriba=None
class nodoencabezado:
    def __init__(self,id):
        self.id=id
        self.siguiente=None
        self.anterior=None
        self.acceso=None
    
class listaencabezado:
    def __init__(self,primero=None):
        self.primero=primero
    
                
    def crearencabezado(self,nuevo):
        if (self.primero==None):
            self.primero=nuevo
        elif(nuevo.id < self.primero.id):
            nuevo.siguiente=self.primero
            self.primero.anterior=nuevo
            self.primero=nuevo
        else:
            actual=self.primero
            while actual.siguiente !=None:
                if(nuevo.id<actual.siguiente.id):
                    nuevo.siguiente=actual.siguiente
                    actual.siguiente.anterior=nuevo
                    nuevo.anterior=actual
                    actual.siguiente=nuevo
                    break
                actual=actual.siguiente
            if(actual.siguiente==None):
                actual.siguiente=nuevo
                nuevo.anterior=actual
    def obtenerencabezado(self,id):
        actual = self.primero
        while actual != None:
            if actual.id == id:
                return actual
            actual = actual.siguiente
        return None

class Matriz:
    def __init__(self):
        self.encabezadof=listaencabezado()
        self.encabezadoc=listaencabezado()

    def insertar(self,fila,columna,pieza):
        nuevo=Nodo1(fila,columna,pieza) 
        encabezadof=self.encabezadof.obtenerencabezado(fila)
        if( encabezadof == None):                           
            encabezadof = nodoencabezado(fila)            
            encabezadof.acceso = nuevo
            self.encabezadof.crearencabezado(encabezadof)        
        else:                                      
            if nuevo.columna < encabezadof.acceso.columna: 
                nuevo.derecha = encabezadof.acceso     
                encabezadof.acceso.izquierda = nuevo
                encabezadof.acceso = nuevo
            else:
                actual = encabezadof.acceso
                while actual.derecha != None:
                    if nuevo.columna < actual.derecha.columna:
                        nuevo.derecha = actual.derecha  
                        actual.derecha.izquierda = nuevo
                        nuevo.izquierda = actual
                        actual.derecha = nuevo
                        break
                    actual = actual.derecha
                
                if actual.derecha == None:
                    actual.derecha = nuevo           
                    nuevo.izquierda = actual
        encabezadoc = self.encabezadoc.obtenerencabezado(columna)
        if encabezadoc == None:                           
            encabezadoc = nodoencabezado(columna)            
            encabezadoc.acceso = nuevo
            self.encabezadoc.crearencabezado(encabezadoc)        
        else:                                       
            if nuevo.fila < encabezadoc.acceso.fila: 
                nuevo.abajo = encabezadoc.acceso      
                encabezadoc.acceso.arriba = nuevo
                encabezadoc.acceso = nuevo
            else:
                actual = encabezadoc.acceso
                while actual.abajo != None:
                    if nuevo.fila < actual.abajo.fila:
                        nuevo.abajo = actual.abajo  
                        actual.abajo.arriba = nuevo
                        nuevo.arriba = actual
                        actual.abajo = nuevo
                        break
                    actual = actual.abajo
                
                if actual.abajo == None:
                    actual.abajo = nuevo            
                    nuevo.arriba = actual

    
    
   

   