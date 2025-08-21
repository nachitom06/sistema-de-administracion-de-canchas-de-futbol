def hola():
    print("hola")

def guardar_precio_cantidad_horas(num1,num2,num3,horarioscomp):
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
    horarioingreso=int(input("ingrese el horario de ingreso a la cancha, 1200 a 2400(de 100 en 100)"))
    while horarioingreso not in horarioscomp:
        horarioingreso=int(input("ingrese el horario de ingreso a la cancha, 1200 a 2400(de 100 en 100)"))
    clientela=input("ingrese el nombre y apellido de la persona")
    return (precio,canthoras,cobrar,horarioingreso,clientela)

def calcular_cantidad_a_pagar(a,b):
    """objetivo: indicar la cantidad que el cliente debe pagar"""
    plata=lambda a,b: a*b
    return plata(a,b)

def cargar_listas_de_canchas():
    canchas=[5,8,11]
    horarios=[1200,1300,1400,1500,1600,1700,1800,1900,2000,2100,2200,2300,2400]
    formpago=[e,mp]
    recaudacioncanchas=[0]*3
    recaudacionhorarios=[0]*13
    recaudacionformpago=[0]*2
    cantcanchas=[0]*3
    canthorarios=[0]*13
    cantformpago=[0]*2
    listaclientela=[]
    return canchas,horarios,formpago,recaudacioncanchas,recaudacionhorarios,recaudacionformpago,cantcanchas,canthorarios,cantformpago,listaclientela
    
def reporte_metodo_pago(formpagodef,recaudacionformpagodef,cantformpagodef,cobrodef):
    fp=input("ingrese (e) para efectivo y (mp) para mercado pago")
    while fp not in formpagodef:
        fp=input("ingrese (e) para efectivo y (mp) para mercado pago")
    if fp==e:
        ran=formpagodef.index(e)
        recaudacionformpagodef[ran]+=cobrodef
        cantformpagodef[ran]+=1
    else:
        ranaux=formpagodef.index(mp)
        recaudacionformpagodef[ranaux]+=cobrodef
        cantformpagodef[ranaux]+=1

def reporte_canchas(canchasdef,recaudacioncanchasdef,cantcanchasdef,cobrodef,numerocancha):
    if numerocancha==5:
        rat=canchasdef.index(5)
        recaudacioncanchasdef[rat]+=cobrodef
        cantcanchasdef[rat]+=1
    elif numerocancha==8:
        rataux=canchasdef.index(8)
        recaudacioncanchasdef[rataux]+=cobrodef
        cantcanchasdef[rataux]+=1
    else:
        rataux2=canchasdef.index(11)
        recaudacioncanchasdef[rataux2]+=cobrodef
        cantcanchasdef[rataux2]+=1

def reporte_horarios(horariosdef,recaudacionhorariosdef,canthorariosdef,cobrodef,filadef):
    if filadef==1200:
        raton=horariosdef.index(1200)
        recaudacionhorariosdef[raton]+=cobrodef
        canthorariosdef[raton]+=1
    elif filadef==1300:
        ratonaux=horariosdef.index(1300)
        recaudacionhorariosdef[ratonaux]+=cobrodef
        canthorariosdef[ratonaux]+=1
    elif filadef==1400:
        ratonaux2=horariosdef.index(1400)
        recaudacionhorariosdef[ratonaux2]+=cobrodef
        canthorariosdef[ratonaux2]+=1
    elif filadef==1500:
        ratonaux3=horariosdef.index(1500)
        recaudacionhorariosdef[ratonaux3]+=cobrodef
        canthorariosdef[ratonaux3]+=1
    elif filadef==1600:
        ratonaux4=horariosdef.index(1600)
        recaudacionhorariosdef[ratonaux4]+=cobrodef
        canthorariosdef[ratonaux4]+=1
    elif filadef==1700:
        ratonaux5=horariosdef.index(1700)
        recaudacionhorariosdef[ratonaux5]+=cobrodef
        canthorariosdef[ratonaux5]+=1
    elif filadef==1800:
        ratonaux6=horariosdef.index(1800)
        recaudacionhorariosdef[ratonaux6]+=cobrodef
        canthorariosdef[ratonaux6]+=1
    elif filadef==1900:
        ratonaux7=horariosdef.index(1900)
        recaudacionhorariosdef[ratonaux7]+=cobrodef
        canthorariosdef[ratonaux7]+=1
    elif filadef==2000:
        ratonaux8=horariosdef.index(2000)
        recaudacionhorariosdef[ratonaux8]+=cobrodef
        canthorariosdef[ratonaux8]+=1
    elif filadef==2100:
        ratonaux9=horariosdef.index(2100)
        recaudacionhorariosdef[ratonaux9]+=cobrodef
        canthorariosdef[ratonaux9]+=1
    elif filadef==2200:
        ratonaux10=horariosdef.index(2200)
        recaudacionhorariosdef[ratonaux10]+=cobrodef
        canthorariosdef[ratonaux10]+=1
    elif filadef==2300:
        ratonaux11=horariosdef.index(2300)
        recaudacionhorariosdef[ratonaux11]+=cobrodef
        canthorariosdef[ratonaux11]+=1
    else:
        ratonaux12=horariosdef.index(2400)
        recaudacionhorariosdef[ratonaux12]+=cobrodef
        canthorariosdef[ratonaux12]+=1

"""agregar lista o matriz, ademas de las dos que ya tenemos, donde acumulamos la recaudacion por canchas y por horarios
    agregar funcion ListadoCanchas de: cantidad de formas de pago(mercado pago 10% mas), cancha de mayor recaudacion y menor 
    recaudacion, incremento por incluir mercado pago.
    cambiar el precio de las canchas por un random.randint
    def validacion de datos"""
