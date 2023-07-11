import numpy as np
arreglo=np.zeros((10,10),int)

lista_ruts=[]
lista_nombres=[]
platino=120000
gold=80000
silver=50000
def precios():
    print(""""precios de las entradas:
          Platinum, $120.000. (Asientos del 1 al 20).
          Gold, $80.000. (Asientos del 21 al 50).
          Silver, $50.000. (Asientos del 51 al 100.).""")
    
def validar_menu():
    while True:
        opciones=int(input("ingrese la opcion a escojer:"))
        try:
            if opciones in range(1,2,3,4,5):
                return opciones
            else:
                print("ERROR!, debe ingresar un valor dentro de los parametros")
        except:
            print("ERROR!, debe ingresar un numero entero positivo")


def validar_rut():
    while True:
        rut=int(input("ingrese rut:"))
        try:
            if rut >= 1111111 and rut<=99999999: 
                return rut
            else:
                print("ERROR!, debe ingresar el rut sin dijito verficador, guion y puntos")
        except:
            print("ERROR!, debe ingresar un numero entero positivo")    

def mostrar_ecenario():
    contador=0
    print("ecenario")
    for x in range(10):
        print(f"", end="")
        for y in range (10):
            print(f"{arreglo[x][y]+contador+1}","   ", end="")
            contador +=1
        print("")    

def validar_nombre():
    while True:
        nombre=input(("ingrese nombre:"))
        if len(nombre.strip())>=3 and nombre.isalpha():
            return nombre
        else:
            print("ERROR!, debe ingresar el nombre con mas de 3 letras")

def validar_fila():
    while True:
        fila=int(input("ingrese fila a escojer:"))
        try:
            if fila >=1 and fila<=10:
                fila=fila-1
                return fila
            else:
                print("ERROR!, debe ingresar un valor entre 1 y 10")
        except:
            print("ERROR!, debe ingresar un numero entero positivo")    

def validar_colu():
    while True:
        colu=int(input("ingrese columna a escojer:"))
        try:
            if colu >=1 and colu<=10:
                colu=colu-1
                return colu
            else:
                print("ERROR!, debe ingresar un valor entre 1 y 10")
        except:
            print("ERROR!, debe ingresar un numero entero positivo")                
def comprar_entrada():

    mostrar_ecenario()
    precios()
    rut=validar_rut()
    nombre=validar_nombre()
    while True:
        fila =validar_fila()
        colu=validar_colu()
        if arreglo[fila][colu] == 0:
            arreglo[fila][colu]=arreglo[fila][colu]+1
            print("su ingreso fue valido")
            contador=0
            for x in range(10):
                print(f"", end="")
                for y in range (10):
                    print(f"{arreglo[x][y]}","   ", end="")
                    contador +=1
                print("")    
            lista_nombres.append(nombre)
            lista_ruts.append(rut)
            break

        elif arreglo[fila][colu] == 1:
            print("intente en otro lugar")
            for x in range(10):
                print(f"", end="")
                for y in range (10):
                    print(f"{arreglo[x][y]}","   ", end="")

                print("")    
            
    
def ubicaciones_disponibles():

    mostrar_ecenario()

    for x in range(10):
        print(f"", end="")
        for y in range (10):
            print(f"{arreglo[x][y]}","   ", end="")

def menu():
    print("""MENU DE INGRESO
        1.mostrar ubicaciones disponibles
        2.ver listado de asistentes
        3.mostrar ganncias totales
        4.compar entrada
        5.salir""")
    
def personas_asistentes():
    print(lista_ruts)
    print(lista_nombres)

