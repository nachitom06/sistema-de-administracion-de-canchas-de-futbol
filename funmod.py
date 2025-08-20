def hola():
    print("hola")

def guardar_precio_cantidad_horas(num1,num2,num3):
    print("los precios de las canchas son: futbol 5=$",num1,", futbol 8=$",num2,", futbol 11=$",num3)
    cobrar=int(input("ingrese numero de cancha(futbol 5, futbol 8, futbol 11)"))
    precio=0
    if cobrar==5:
        precio=num1
    elif cobrar==8:
        precio=num2
    else:
        precio=num3
    canthoras=int(input("ingrese la cantidad de horas alquiladas de la cancha"))
    return (precio,canthoras)

def calcular_cantidad_a_pagar(a,b):
    """objetivo: indicar la cantidad que el cliente debe pagar"""
    plata=lambda a,b: a*b
    return plata(a,b)

def cargar_listas_de_canchas():
    canchas=["5","8","11"]
    horarios=[1200,1300,1400,1500,1600,1700,1800,1900,2000,2100,2200,2300,2400]
    formpago=["e","mp"]
    recaudacioncanchas=[0]*3
    recaudacionhorarios=[0]*13
    recaudacionformpago=[0]*2
    return
def validacion_datos
    


"""agregar lista o matriz, ademas de las dos que ya tenemos, donde acumulamos la recaudacion por canchas y por horarios
    agregar funcion ListadoCanchas de: cantidad de formas de pago(mercado pago 10% mas), cancha de mayor recaudacion y menor 
    recaudacion, incremento por incluir mercado pago.
    cambiar el precio de las canchas por un random.randint
    def validacion de datos"""
