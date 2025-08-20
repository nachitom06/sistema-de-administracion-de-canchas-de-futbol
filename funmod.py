def hola():
    print("hola")

def cargar_precios_canchas():
    print(los precios de las canchas son: futbol 5=$40000, futbol 8=$70000, futbol 11=$100000")
    cobrar=int(input("ingrese numero de cancha(futbol 5, futbol 8, futbol 11)"))
    precio=0
    if cobrar==5:
        precio=40000
    elif cobrar==8:
        precio=70000
    else:
        precio=100000
    canthoras=int(input("ingrese la cantidad de horas alquiladas de la cancha"))
    return precio,canthoras

def calcular_cantidad_a_pagar(a,b):
    """objetivo: indicar la cantidad que el cliente debe pagar"""
    plata=lambda a,b: a*b
    return plata
