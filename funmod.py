import random
import listas
def dar_bienvenida():
    """Objetivo: Dar la bienvenida"""
    saludo="-------------------- Bienvenido al sistema administrador --------------------"
    print(saludo)

def hacer_sponsors(disponibilidad,listasponsorszona,listasponsors,listadisponibilidad,listanombresponsor,sponsorcito,estadistica):
            print(f"\tsponsors\t\t\tdisponibilidad")
            disponible=-1
            for p in range(len(disponibilidad)):
                if disponibilidad[p]==0:
                    disponible=0
                else:
                    disponible=1
                print(f"{listasponsorszona[p]}\t{listasponsors[p]}\t{listadisponibilidad[disponible]}")
            while True:
                try:
                    eleccion=int(input("ingrese el numero segun lo muestra en la lista anterior para colocar su sponsor"))
                    while eleccion not in listasponsorszona:
                        print("error fuera de rango")
                        eleccion=int(input("ingrese el numero segun lo muestra en la lista anterior para colocar su sponsor"))
                            
                    
                except ValueError as mensaje14:
                    print(mensaje14)
                    continue
                if disponibilidad[eleccion-1]==0:
                    
                    while True:
                        salir=False
                        salir3=False

                        nombresponsor=input("ingrese el nombre del sponsor")
                        print(nombresponsor)
                        while True:
                            try:
                                confirmar=int(input("ingrese 0 si es correcto el nombre o 1 si no lo es"))
                                while confirmar not in[0,1]:
                                    print("error el numero ingresado no se encuentra en el rango")
                                    confirmar=int(input("ingrese 0 si es correcto el nombre o 1 si no lo es"))
                            except ValueError as mensaje15:
                                print(mensaje15)
                                continue
                            if confirmar==0:
                                disponibilidad[eleccion-1]=1
                                listanombresponsor[eleccion-1]=nombresponsor
                                guardo=sponsorcito["listasponsors"][eleccion-1]
                                estadistica["sponsorsuso"][guardo]+=1
                                listas.guardar_sponsors(sponsorcito)
                                salir=True
                                salir3=True
                                break
                                        
                            else:
                                break
                        if salir:
                            break
                    if salir3:
                        break
                else:
                    print("no se encuentra disponible")
                    break
            while True:
                salir10=False
                try:
                    salida=int(input("ingrese cualquier numero para seguir o -1 para salir"))
                except ValueError as mensaje12:
                    print(mensaje12)
                    continue
                if salida==-1:
                    salir10=True
                    break
                else:
                    break
            
def recomendaciones(estadistica):
    entrada=estadistica["entradasvendidas"]
    max=0
    maxsector=""
    for sector in entrada:
        if entrada[sector]>max:
            max=entrada[sector]
            maxsector=sector
    print(f"debido a la cantidad vendida de entradas de {maxsector} con {max} entradas vendidas, se recomienda ampliar para tener mayores ingresos")
    sponsorfe=estadistica["sponsorsuso"]
    maxuso=0
    maxusosponsor=""
    for ronda in sponsorfe:
        if sponsorfe[ronda]>maxuso:
            maxuso=sponsorfe[ronda]
            maxusosponsor=ronda
    print(f"con el uso del sponsor en: {maxusosponsor} con un uso de {maxuso} se recomienda ampliar el espacio para colocar más sponsors en ese sector")
    cualvende=estadistica["cualvendemas"]
    maxvendidas=0
    maxvendidascopa=""
    for letercita in cualvende:
        if cualvende[letercita]>maxvendidas:
            maxvendidas=cualvende[letercita]
            maxvendidascopa=letercita
    print(f" vende más: {maxvendidascopa} con {maxvendidas} por lo tanto conviene hacer mas de esos")
    reservamas=estadistica["cualreserva"]
    maxreserva=0
    maxreservacancha=""
    for cato in reservamas:
        if reservamas[cato]>maxreserva:
            maxreserva=reservamas[cato]
            maxreservacancha=cato
    print(f"recomendación contruir otra cancha de {maxreservacancha} para generar más ingresos, ya que fue la más reservada con: {maxreserva}")

def cobrar_entradas(sector,cantidad,listaentradas,estadisticas,pagoentradas):
    if sector=="vip":
        sector1=random.randint(8500,10000)
    elif sector=="platea":
        sector1=random.randint(3500,5000)
    else:
        sector1=random.randint(1500,3000)
    total=sector1*cantidad
    print("cantidad a pagar: ",total)
    pagoentradas.append(total)
    estadisticas["entradasvendidas"][sector]+=cantidad


def ingreso_aleatorio_partidos(fasegrupos1aux,fasegrupos1resultados,resultaditosgeneral,fasegrupos):
    while len(fasegrupos1resultados)<(len(fasegrupos1aux)):
        
            golcitos1=random.randint(0,15)
            golcitos2=random.randint(0,15)
            fasegrupos1resultados.append([golcitos1,golcitos2])
            resultaditosgeneral[fasegrupos].append([golcitos1,golcitos2])
            listas.guardar_torneo(resultaditosgeneral)

def ingresar_manual_partidos(cuartosaux,cuartosresultados,resultaditosgeneral,cuartos):
    
                for r in range(len(cuartosaux)):
                
                    jugadorescuartos1=cuartosaux[r][0]
                    jugadorescuartos2=cuartosaux[r][1]
                    if r<len(resultaditosgeneral[cuartos]) and len(resultaditosgeneral[cuartos][r])==2:
                        print(f"El partido {jugadorescuartos1} vs {jugadorescuartos2} ya tiene resultado")
                        continue
                    while True:
                        try:
                            golescuartos1=int(input(f"Ingrese los goles de {jugadorescuartos1}: "))
                            while golescuartos1<0:
                                print("Error, no puede ser menor a 0")
                                golescuartos1=int(input(f"Ingrese los goles de {jugadorescuartos1}: "))
                            golescuartos2=int(input(f"Ingrese los goles de {jugadorescuartos2}: "))
                            while golescuartos2<0:
                                print("Error, no puede ser menor a 0")
                                golescuartos2=int(input(f"Ingrese los goles de {jugadorescuartos2}: "))
                        except ValueError as mostra5:
                            print(mostra5)
                            continue
                        resultaditosgeneral[cuartos].append([golescuartos1,golescuartos2])
                        listas.guardar_torneo(resultaditosgeneral)
                        print(f"Resultado: {jugadorescuartos1} : {golescuartos1} vs {golescuartos2} : {jugadorescuartos2}")
                        break
            
def calcular_partidos(fasegrupos1,fasegrupo1partidos):
    for x in range(len(fasegrupos1)-1):            
        for i in range(len(fasegrupos1)//2):
            equipo1torneo=fasegrupos1[i]
            equipo2torneo=fasegrupos1[len(fasegrupos1)-1-i]
            fasegrupo1partidos.append([equipo1torneo,equipo2torneo])
            fasegrupos1=fasegrupos1[:1]+fasegrupos1[-1:]+fasegrupos1[1:-1]

def resultados_liga(fixtureida,resultadosida,listaauxiliarliga,ligaderesultados,fixturevuelta,resultadosvuelta):
    for r in range(len(fixtureida)):
                if len(resultadosida["resultadosidita"][r])<2:
                    jugador3=fixtureida[r][0]
                    jugador4=fixtureida[r][1]
                    jugado3=listaauxiliarliga.index(jugador3)
                    jugado4=listaauxiliarliga.index(jugador4)

                    while True:
                        try:
                            resta1=int(input("ingrese los goles del primer equipo"))
                            while resta1<0:
                                print("error, no puede ser menor a 0")
                                resta1=int(input("ingrese los goles del primer equipo"))
                            resta2=int(input("ingrese los goles del primer equipo"))
                            while resta2<0:
                                print("error, no puede ser menor a 0")
                                resta2=int(input("ingrese los goles del primer equipo"))
                        except ValueError as mensaje16:
                            print(mensaje16)
                            continue
                        resultadosida[r].append([resta1,resta2])
                        ligaderesultados["liga"].append([resta1,resta2])
                        listas.guardar_liga(ligaderesultados)
                        print(f"el resultado del partido de ida fue: {jugador3}{jugado3} vs {jugado4}{jugador4}")
                        break
                else:
                    for t in range(len(fixturevuelta)):
                        if len(resultadosvuelta["resultadosvueltita"][t])<2:
                            jugador5=fixturevuelta[t][0]
                            jugador6=fixtureida[t][1]
                            jugado5=listaauxiliarliga.index(jugador5)
                            jugado6=listaauxiliarliga.index(jugador6)

                            while True:
                                try:
                                    resta3=int(input("ingrese los goles del primer equipo"))
                                    while resta3<0:
                                        print("error, no puede ser menor a 0")
                                        Resta3=int(input("ingrese los goles del primer equipo"))
                                    resta4=int(input("ingrese los goles del primer equipo"))
                                    while resta4<0:
                                        print("error, no puede ser menor a 0")
                                        resta4=int(input("ingrese los goles del primer equipo"))
                                except ValueError as mensaje17:
                                    print(mensaje17)
                                    continue
                                resultadosvuelta[t].append([resta3,resta4])
                                ligaderesultados["liga"].append([resta3,resta4])
                                listas.guardar_liga(ligaderesultados)
                                print(f"el resultado del partido de ida fue: {jugador5}{jugado5} vs {jugado6}{jugador6}")
                                break
                        else:
                            print("los resultados ya están llenos")
                            break
def alquilar(sector,pedido,ocupadas,entradas):
    if sector in ocupadas:
        print("sector totalmente ocupado")
    if entradas[sector]>=pedido:
        entradas[sector]-=pedido
        if entradas[sector]==0:
            ocupadas.add(sector)
    else:
        print("no hay suficientes entradas")

def mostrar_disponibles(datillo,disponible,ocupadas):
    disponibles=disponible-ocupadas
    print("sectores disponibles: ",disponibles)
    for p in datillo:
        print(f"{p} : {datillo[p]} asientos libres")
def alquilartorneo(sector,pedido,ocupadastorneo,entradastorneo):
    if sector in ocupadastorneo:
        print("sector totalmente ocupado")
    if entradastorneo[sector]>=pedido:
        entradastorneo[sector]-=pedido
        if entradastorneo[sector]==0:
            ocupadastorneo.add(sector)
    else:
        print("no hay suficientes entradas")

def mostrar_disponiblestorneo(datillo,disponibletorneo,ocupadastorneo):
    disponibles=disponibletorneo-ocupadastorneo
    print("sectores disponibles: ",disponibles)
    for p in datillo:
        print(f"{p} : {datillo[p]} asientos libres")


def inscripciones_a_la_liga(listaequiposliga,stringer,stringer2,guardar_listaliga):
    conteo20=0
    print(stringer)
    print(stringer2)
    for i in range(len(listaequiposliga)):
        print(f"equipo:{i+1}\t{listaequiposliga[i]}")
    for c in range(len(listaequiposliga)):
        if listaequiposliga[c]==0:
            conteo20+=1
    if conteo20!=0:
                    
        while True:
            nombreequipo=input("ingrese el nombre del equipo que desea inscribir(que no contenga numeros)")
            while len(nombreequipo.strip())==0 or nombreequipo.isdigit():
                print("error no ingreso nada o ingreso numeros")
                nombreequipo=input("ingrese el nombre del equipo que desea inscribir(que no contenga numeros)")
            print("nombre del equipo:",nombreequipo)
            while True:
                try:
                    confirmacion=int(input("ingrese 0 para confirmar nombre, 1 para cancelar y volver a cargar el nombre, -1 para salir"))
                    while confirmacion not in[-1,0,1]:
                        print("error, numero fuera de rango")
                        confirmacion=int(input("ingrese 0 para confirmar nombre, 1 para cancelar y volver a cargar el nombre, -1 para salir"))
                except ValueError as mensaje11:
                    print(mensaje11)
                    continue
                if confirmacion==1:
                    break
                elif confirmacion==0:
                    for v in range(len(listaequiposliga)):
                        if listaequiposliga[v]==0:
                            listaequiposliga[v]=nombreequipo
                            guardar_listaliga(listaequiposliga)
                            print(f"equipo:{nombreequipo} inscripto correctamente")
                            break
                    break
                            
                else:
                    break
            while True:
                salir2=False
                try:
                    salida=int(input("ingrese cualquier numero para seguir o -1 para salir"))
                except ValueError as mensaje12:
                    print(mensaje12)
                    continue
                if salida==-1:
                    salir2=True
                    break
                            
                else:
                    break
            if salir2:
                break
def fasegrupos_ponerresultados(fasegrupos1aux,fasegrupos1resultados,resultaditosgeneral,nombrefase):
    completos=0
    for r in range(len(fasegrupos1aux)):
        if len(fasegrupos1resultados[r])<2:
            jugadores11=fasegrupos1aux[r][0]
            jugadores12=fasegrupos1aux[r][1]
            while True:
                try:
                    goles1=int(input(f"Ingrese los goles de {jugadores11}: "))
                    while goles1<0:
                        print("Error, no puede ser menor a 0")
                        goles1=int(input(f"Ingrese los goles de {jugadores11}: "))
                    goles2=int(input(f"Ingrese los goles de {jugadores12}: "))
                    while goles2<0:
                        print("Error, no puede ser menor a 0")
                        goles2=int(input(f"Ingrese los goles de {jugadores12}: "))
                except ValueError as mostra:
                    print(mostra)
                    continue
                fasegrupos1resultados[r].append([goles1,goles2])
                resultaditosgeneral[nombrefase].append([goles1,goles2])
                listas.guardar_torneo(resultaditosgeneral)
                print(f"Resultado: {jugadores11} : {goles1} vs {goles2} : {jugadores12} ")
                break
        else:
            completos+=1
    if completos==len(fasegrupos1aux):
        print("Ya se jugaron todos los partidos de la zona 1")
def resultados_aleatorios_fasegrupos(fasegrupos1resultados,fixturetorneo):
    while len(fasegrupos1resultados)<(len(fixturetorneo)):
                resu=[]
                fase1eq1=random.randint(0,15)
                fase1eq2=random.randint(0,15)
                fasegrupos1resultados.append([fase1eq1,fase1eq2])

def resultados_aleatorios_liga(resultadosida,ligaderesultados,biene,guardar_resultadosidita):
    while len(resultadosida[biene])<190:
                resu=[]
                eq1=random.randint(0,15)
                eq2=random.randint(0,15)
                resultadosida[biene].append([eq1,eq2])
                ligaderesultados["liga"].append([eq1,eq2])
                listas.guardar_liga(ligaderesultados)
                guardar_resultadosidita(resultadosida)

def calcular_tabla(fixtureida,listaauxiliarliga,partidosjugados,resultadosida,ganados,puntos,perdidos,empatados,golesfavor,golescontra,diferenciagol):
    """fixtureida=[partido for fecha in fixtureida for partido in fecha]"""
    print(len(fixtureida))
    print(len(resultadosida))
    for l in range(len(resultadosida)):
                jugador1=fixtureida[l][0]
                jugador2=fixtureida[l][1]
                jugado1=listaauxiliarliga.index(jugador1)
                jugado2=listaauxiliarliga.index(jugador2)
                partidosjugados[jugado1]+=1
                partidosjugados[jugado2]+=1
                if resultadosida[l][0]>resultadosida[l][1]:
                    ganados[jugado1]+=1
                    """puntos[jugado1]+=3"""
                    perdidos[jugado2]+=1
                    """puntos[jugado2]+=0"""
                elif resultadosida[l][0]<resultadosida[l][1]:
                    ganados[jugado2]+=1
                    """puntos[jugado2]+=3"""
                    perdidos[jugado1]+=1
                    """puntos[jugado1]+=0"""
                elif resultadosida[l][0]==resultadosida[l][1]:
                    empatados[jugado1]+=1
                    """puntos[jugado1]+=1"""
                    empatados[jugado2]+=1
                    """puntos[jugado2]+=1"""

                golesfavor[jugado1]+=resultadosida[l][0]
                golesfavor[jugado2]+=resultadosida[l][1]
                golescontra[jugado1]+=resultadosida[l][1]
                golescontra[jugado2]+=resultadosida[l][0]
                diferenciagol[jugado1]+=resultadosida[l][0]-resultadosida[l][1]
                diferenciagol[jugado2]+=resultadosida[l][1]-resultadosida[l][0]
    for i in range(len(listaauxiliarliga)):
        puntos[i]=ganados[i]*3+empatados[i]
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
        print("Error el nombre que ingreso no es valido(digitos o vacio)")
        clientela=input("Igrese su nombre y apellido al cual reservara la cancha: ")
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
def reporte_metodo_pago(reportes,formpagodef,recaudacionformpagodef,cantformpagodef,cobrodef,listadediezporciento,preciocuidado):
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
        reportes["listrecaudacionformpago"][ran]+=(cobrodef*110//100)
        reportes["listcantformpago"][ran]+=1
        diezporcientoefe=(cobrodef*110//100)-cobrodef
        listadediezporciento.append(diezporcientoefe)
        preciocuidado=(cobrodef*110//100)
        reportes["listadiezporciento"].append(diezporcientoefe)
        listas.guardar_reportes(reportes)
    else:
        ranaux=formpagodef.index("mp")
        recaudacionformpagodef[ranaux]+=cobrodef
        cantformpagodef[ranaux]+=1
        reportes["listrecaudacionformpago"][ranaux]+=cobrodef
        reportes["listcantformpago"][ranaux]+=1
    listas.guardar_reportes(reportes)
    return preciocuidado
def reporte_canchas(reportes,canchasdef,recaudacioncanchasdef,cantcanchasdef,cobrodef,numerocancha):
    """objetivo: actualiza el reporte de canchas"""
    if numerocancha==5:
        rat=canchasdef.index(5)
        recaudacioncanchasdef[rat]+=cobrodef
        cantcanchasdef[rat]+=1
        reportes["listrecaudacioncanchas"][rat]+=cobrodef
        reportes["listcantcanchas"][rat]+=1
    elif numerocancha==8:
        rataux=canchasdef.index(8)
        recaudacioncanchasdef[rataux]+=cobrodef
        cantcanchasdef[rataux]+=1
        reportes["listrecaudacioncanchas"][rataux]+=cobrodef
        reportes["listcantcanchas"][rataux]+=1
    else:
        rataux2=canchasdef.index(11)
        recaudacioncanchasdef[rataux2]+=cobrodef
        cantcanchasdef[rataux2]+=1
        reportes["listrecaudacioncanchas"][rataux2]+=cobrodef
        reportes["listcantcanchas"][rataux2]+=1
    listas.guardar_reportes(reportes)
def reporte_horarios(reportes,horariosdef,recaudacionhorariosdef,canthorariosdef,cobrodef,filadef):
    """objetivo: actualiza el reporte de horarios"""
    if filadef in horariosdef:
        raton=horariosdef.index(filadef)
        recaudacionhorariosdef[raton]+=cobrodef
        canthorariosdef[raton]+=1
        reportes["listrecaudacionhorarios"][raton]+=cobrodef
        reportes["listcanthorarios"][raton]+=1
        listas.guardar_reportes(reportes)
def reporte_torneo(reportes,recaudaciontorneo):
    recaudetorneo=((1000000*16)//2)
    reportes["recaudacionestorneo"].append(recaudetorneo)
    listas.guardar_reportes(reportes)
def reporte_liga(reportes,recaudacionliga):
    recaudeliga=((80000*20*38)//2)
    reportes["recaudacionesliga"].append(recaudeliga)
    listas.guardar_reportes(reportes)   
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


#por ahora viene bien, hay que probar las que dice en main copy.py
