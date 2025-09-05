def dar_bienvenida():
    """Objetivo: Dar la bienvenida"""
    saludo="-------------------- Bienvenido al sistema administrador --------------------"
    print(saludo)
def iniciar_matriz():
    """objetivo: inicia las matrices"""
    matrizper=[[0 for _ in range(13)] for _ in range(3)]
    matriznombre=[[0 for _ in range(13)] for _ in range(3)]
    return matrizper,matriznombre
def listado(recaudo,numerocanch):
    """objetivo: arma listado de los horarios de mayor a menor recaudacion"""
    lista=list(zip(recaudo,numerocanch))
    lista.sort(key=lambda x:x[0])
    lista=lista[::-1]
    return lista
def guardar_precio_cantidad_horas(num1,num2,num3,horarioscomp):
    """objetivo: guarda numero de cancha,cantidad de horas, horario y cliente"""
    print("los precios de las canchas son: futbol 5=$",num1,", futbol 8=$",num2,", futbol 11=$",num3)
    cobrar=int(input("ingrese numero de cancha(futbol 5, futbol 8, futbol 11): "))
    while cobrar not in[5,8,11]:
        print("error no se encuentra en el rango")
        cobrar=int(input("ingrese numero de cancha(futbol 5, futbol 8, futbol 11): "))
    precio=0
    if cobrar==5:
        precio=num1
    elif cobrar==8:
        precio=num2
    else:
        precio=num3
    canthoras=int(input("Ingrese la cantidad de horas alquiladas de la cancha: "))
    while canthoras>13:
        print("Error: no se puede alquilar más de 13 horas seguidas")
        canthoras=int(input("Ingrese la cantidad de horas alquiladas de la cancha: "))
    horarioingreso=int(input("Ingrese el horario de ingreso a la cancha, 1200 a 2400(de 100 en 100): "))
    while horarioingreso not in horarioscomp:
        print("Error, debe ingresar el horario de ingreso a la cancha, 1200 a 2400(de 100 en 100)")
        horarioingreso=int(input("Ingrese el horario de ingreso a la cancha, 1200 a 2400(de 100 en 100): "))
    clientela=input("Ingrese el nombre y apellido de la persona: ")
    while len(clientela.strip())==0 or clientela.isdigit():
        print("Error el nombre que inngreso no es valido(digitos o vacio)")
        cliedntela=input("Igrese su nombre y apellido al cual reservara la cancha: ")
    return (precio,canthoras,cobrar,horarioingreso,clientela)
def calcular_cantidad_a_pagar(a,b):
    """objetivo: indicar la cantidad que el cliente debe pagar"""
    plata=lambda a,b: a*b
    return plata(a,b)
def cargar_listas_de_canchas():
    """objetivo: cargar listas"""
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
def reporte_metodo_pago(formpagodef,recaudacionformpagodef,cantformpagodef,cobrodef,listadediezporciento,preciocuidado):
    """Objetivo: Actualiza el reporte de metodo de pago"""
    fp=input("Ingrese (e) para efectivo, 10% mas, y (mp) para mercado pago: ")
    diezporcientoefe=0
    while fp not in formpagodef:
        fp=input("Ingrese (e) para efectivo, 10% mas, y (mp) para mercado pago: ")
    if fp=="e":
        ran=formpagodef.index("e")
        recaudacionformpagodef[ran]+=(cobrodef*110//100)
        print(cobrodef*110//100,"es el importe a pagar con efectivo(10% mas)")
        cantformpagodef[ran]+=1
        diezporcientoefe=(cobrodef*110//100)-cobrodef
        listadediezporciento.append(diezporcientoefe)
        preciocuidado=(cobrodef*110//100)
    else:
        ranaux=formpagodef.index("mp")
        recaudacionformpagodef[ranaux]+=cobrodef
        cantformpagodef[ranaux]+=1
    return preciocuidado
def reporte_canchas(canchasdef,recaudacioncanchasdef,cantcanchasdef,cobrodef,numerocancha):
    """objetivo: actualiza el reporte de canchas"""
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
    """objetivo: actualiza el reporte de horarios"""
    if filadef in horariosdef:
        raton=horariosdef.index(filadef)
        recaudacionhorariosdef[raton]+=cobrodef
        canthorariosdef[raton]+=1
def cancha_mayor_recuaudo_con_porcentaje(listita,listadecanchas,cant):
    """objetivo: calcula la cancha con mayor recaudo y el porcentaje de usos que tuvo"""
    maxi=max(listita)
    cont=listita.index(maxi)
    conteo=listadecanchas[cont]
    diviso=sum(cant)
    if diviso==0:
        porcen=0
    else:
        porcen=(cant[cont])*100/diviso
    return maxi,conteo,porcen
def cancha_menor_recuaudo_con_porcentaje(listita,listadecanchas,cant):
    """objetivo: calcula la cancha con menor recaudo y el porcentaje de usos que tuvo"""
    mini=min(listita)
    cont=listita.index(mini)
    conteo=listadecanchas[cont]
    diviso=sum(cant)
    if diviso==0:
        porcen=0
    else:
        porcen=(cant[cont])*100/diviso
    return mini,conteo,porcen
def calcular_total(listaformapago):
    """objetivo: calcular la recaudacion total"""
    total=sum(listaformapago)
    return total
def mayor_cliente(listacanthorarios,listahorarios):
    """objetivo: calcula el mayor cliente de los horarios con el promedio tambien"""
    mayorclient=max(listacanthorarios)
    cancha=listacanthorarios.index(mayorclient)
    numcancha=listahorarios[cancha]
    conteo2=listacanthorarios.count(mayorclient)
    promedio=sum(listacanthorarios)/(len(listacanthorarios))
    hay2=0
    if conteo2>1:
        hay2=1
    return mayorclient,hay2,promedio,numcancha
