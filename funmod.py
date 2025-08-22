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
        print("error, debe ingresar el horario de ingreso a la cancha, 1200 a 2400(de 100 en 100)")
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
    formpago=["e","mp"]
    recaudacioncanchas=[0]*3
    recaudacionhorarios=[0]*13
    recaudacionformpago=[0]*2
    cantcanchas=[0]*3
    canthorarios=[0]*13
    cantformpago=[0]*2
    listaclientela=[]
    listadiezporciento=[]
    return canchas,horarios,formpago,recaudacioncanchas,recaudacionhorarios,recaudacionformpago,cantcanchas,canthorarios,cantformpago,listaclientela,listadiezporciento
    
def reporte_metodo_pago(formpagodef,recaudacionformpagodef,cantformpagodef,cobrodef,listadediezporciento):
    fp=input("ingrese (e) para efectivo, 10% mas, y (mp) para mercado pago")
    diezporcientoefe=0
    while fp not in formpagodef:
        fp=input("ingrese (e) para efectivo, 10% mas, y (mp) para mercado pago")
    if fp=="e":
        ran=formpagodef.index("e")
        recaudacionformpagodef[ran]+=(cobrodef*110//100)
        print(cobrodef*110//100,"es el importe a pagar con efectivo(10% mas)")
        cantformpagodef[ran]+=1
        diezporcientoefe=(cobrodef*110//100)-cobrodef
        listadediezporciento.append(diezporcientoefe)
    else:
        ranaux=formpagodef.index("mp")
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
    if filadef in horariosdef:
        raton=horariosdef.index(filadef)
        recaudacionhorariosdef[raton]+=cobrodef
        canthorariosdef[raton]+=1

def cancha_mayor_recuaudo(listita,listadecanchas):
    maxi=max(listita)
    cont=listita.index(maxi)
    conteo=listadecanchas[cont]
    return maxi,conteo

def cancha_menor_recuaudo(listita,listadecanchas):
    mini=min(listita)
    cont=listita.index(mini)
    conteo=listadecanchas[cont]      
    return mini,conteo

def calcular_total(listaformapago):
    total=sum(listaformapago)
    return total

def mayor_cliente(listacanthorarios):
    mayorclient=max(listacanthorarios)
    conteo2=listacanthorarios.count(mayorclient)
    hay2=0
    if conteo2>1:
        hay2=1
    return mayorclient,hay2
    
"""agregar lista o matriz, ademas de las dos que ya tenemos, donde acumulamos la recaudacion por canchas y por horarios
    agregar funcion ListadoCanchas de: cantidad de formas de pago(mercado pago 10% mas), cancha de mayor recaudacion y menor 
    recaudacion, incremento por incluir mercado pago.
    cambiar el precio de las canchas por un random.randint
    def validacion de datos"""
