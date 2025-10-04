import listas
import random
import csv
import funmod

def admin():


    fixtureida=listas.cargar_fixturevueltita()
    fixturevuelta=listas.cargar_fixturevueltita()
    resultadosida=listas.cargar_resultadosidita()
    resultadosvuelta=listas.cargar_resultadosvueltita()
    stringer="bienvenido a inscripcion en el Torneo Nacional"
    stringer2="lista de equipos (16 cupos)"
    stringer3="bienvenido a inscripcion en la Super Liga Nacional"
    stringer4="lista de equipos (20 cupos)"
    estadistica=listas.cargar_estadisticas()
    entradastorneo=listas.cargar_entradastorneo()
    entradas=listas.cargar_entradas()
    sponsorcito=listas.cargar_sponsors()
    fixturecompleto=listas.cargar_partidosdeliga()
    fixturetorneo=listas.cargar_partidosdetorneo()
    ligaderesultados=listas.cargar_liga()
    resultaditosgeneral=listas.cargar_torneo()
    matrizper,matriznombre=listas.matrizper,listas.matriznombre
    matriztorneos=listas.todo["matriztorneos"]
    listcanchas,listhorarios,listformpago,listrecaudacioncanchas,listrecaudacionhorarios,listrecaudacionformpago,listcantcanchas,listcanthorarios,listcantformpago,listaclientes,listadiezporciento=listas.listcanchas,listas.listhorarios,listas.listformpago,listas.listrecaudacioncanchas,listas.listrecaudacionhorarios,listas.listrecaudacionformpago,listas.listcantcanchas,listas.listcanthorarios,listas.listcantformpago,listas.listaclientes,listas.listadiezporciento
    nombredelaliga=listas.todo["nombredelaliga"]
    nombredeltorneo=listas.todo["nombredeltorneo"]
    listaequiposliga=listas.listaequiposliga
    listaauxiliarliga=listas.listaequiposliga
    listaequipostorneo=listas.listaequipostorneo
    cuartosresultados=listas.todo["cuartosresultados"]
    ganadorescuartos=listas.todo["ganadorescuartos"]
    ganadoressemis=listas.todo["ganadoressemis"]
    semisresultados=listas.todo["semisresultados"]
    finalresultados=listas.todo["finalresultados"]
    ganadorfinal=listas.todo["ganadorfinal"]
    campeontorneo=listas.todo["campeontorneo"]
    campeones=listas.todo["campeones"]
    fasegrupos1=listas.todo["fasegrupos1"]
    fasegrupos2=listas.todo["fasegrupos2"]
    fasegrupos3=listas.todo["fasegrupos3"]
    fasegrupos4=listas.todo["fasegrupos4"]
    fasegrupo1partidos=listas.todo["fasegrupo1partidos"]
    fasegrupo2partidos=listas.todo["fasegrupo2partidos"]
    fasegrupo3partidos=listas.todo["fasegrupo3partidos"]
    fasegrupo4partidos=listas.todo["fasegrupo4partidos"]
    cuartos=listas.todo["cuartos"]
    semis=listas.todo["semis"]
    final=listas.todo["final"]
    fasegrupos1resultados=listas.todo["fasegrupos1resultados"]
    fasegrupos2resultados=listas.todo["fasegrupos2resultados"]
    fasegrupos3resultados=listas.todo["fasegrupos3resultados"]
    fasegrupos4resultados=listas.todo["fasegrupos4resultados"]
    contadorpartidosfase1=listas.todo["contadorpartidosfase1"]
    contadorpartidosfase2=listas.todo["contadorpartidosfase2"]
    contadorpartidosfase3=listas.todo["contadorpartidosfase3"]
    contadorpartidosfase4=listas.todo["contadorpartidosfase4"]
    fixtureida=listas.todo["fixtureida"]
    fixturevuelta=listas.todo["fixturevuelta"]
    recaudacionesliga=listas.todo["recaudacionesliga"]
    recaudacionestorneo=listas.recaudacionestorneo
    puntosequipos=listas.todo["puntosequipos"]
    partidosjugados=listas.todo["partidosjugados"]
    ganados=listas.todo["ganados"]
    empatados=listas.todo["empatados"]
    perdidos=listas.todo["perdidos"]
    puntos=listas.todo["puntos"]
    golesfavor=listas.todo["golesfavor"]
    golescontra=listas.todo["golescontra"]
    diferenciagol=listas.todo["diferenciagol"]
    partidosjugadosfase1=listas.todo["partidosjugadosfase1"]
    ganadosfase1=listas.todo["ganadosfase1"]
    empatadosfase1=listas.todo["empatadosfase1"]
    perdidosfase1=listas.todo["perdidosfase1"]
    puntosfase1=listas.todo["puntosfase1"]
    golesfavorfase1=listas.todo["golesfavorfase1"]
    golescontrafase1=listas.todo["golescontrafase1"]
    diferenciagolfase1=listas.todo["diferenciagolfase1"]
    partidosjugadosfase2=listas.todo["partidosjugadosfase2"]
    ganadosfase2=listas.todo["ganadosfase2"]
    empatadosfase2=listas.todo["empatadosfase2"]
    perdidosfase2=listas.todo["perdidosfase2"]
    puntosfase2=listas.todo["puntosfase2"]
    golesfavorfase2=listas.todo["golesfavorfase2"]
    golescontrafase2=listas.todo["golescontrafase2"]
    diferenciagolfase2=listas.todo["diferenciagolfase2"]
    partidosjugadosfase3=listas.todo["partidosjugadosfase3"]
    ganadosfase3=listas.todo["ganadosfase3"]
    empatadosfase3=listas.todo["empatadosfase3"]
    perdidosfase3=listas.todo["perdidosfase3"]
    puntosfase3=listas.todo["puntosfase3"]
    golesfavorfase3=listas.todo["golesfavorfase3"]
    golescontrafase3=listas.todo["golescontrafase3"]
    diferenciagolfase3=listas.todo["diferenciagolfase3"]
    partidosjugadosfase4=listas.todo["partidosjugadosfase4"]
    ganadosfase4=listas.todo["ganadosfase4"]
    empatadosfase4=listas.todo["empatadosfase4"]
    perdidosfase4=listas.todo["perdidosfase4"]
    puntosfase4=listas.todo["puntosfase4"]
    golesfavorfase4=listas.todo["golesfavorfase4"]
    golescontrafase4=listas.todo["golescontrafase4"]
    diferenciagolfase4=listas.todo["diferenciagolfase4"]
    contadorpartidosida=listas.todo["contadorpartidosida"]
    resultadosida=listas.todo["resultadosida"]
    resultadosvuelta=listas.todo["resultadosvuelta"]
    contadorpartidosvuelta=listas.todo["contadorpartidosvuelta"]
    nombresaleatoriosequipos=listas.todo["nombresaleatoriosequipos"]
    listasponsorszona=listas.todo["listasponsorszona"]
    listasponsors=listas.todo["listasponsors"]
    disponibilidad=sponsorcito["disponibilidad"]
    listadisponibilidad=listas.todo["listadisponibilidad"]
    listanombresponsor=sponsorcito["nombresponsor"]
    disponibilidadtorneo=listas.todo["disponibilidadtorneo"]
    listanombresponsortorneo=listas.todo["listanombresponsortorneo"]
    recaudaciondiezporciento=listas.todo["recaudaciondiezporciento"]
    while True:
        print("OPCIONES: ")
        print("# 1 = reservar canchas")
        print("# 2 = cancelar la reservacion de canchas")
        print("# 3 = calcular cobro")
        print("# 4 = mostrar reportes")
        print("# 5 = inscripción liga")
        print("# 6 = rellenar liga (demostración)")
        print("# 7 = calcular partidos de liga")
        print("# 8 = inscripcion sponsors")
        print("# 9 = simular partidos resultados (demostración)")
        print("# 11 = tabla de liga")
        print("# 12 = poner resultados partidos liga")
        print("# 13 = cobro torneo o liga")
        print("# 14 = inscripcion torneo")
        print("# 15 = rellenar torneo (demostración)")
        print("# 16 = calcular los partidos del torneo")
        print("# 17 = tablas fase de grupos torneo")  
        print("# 18 = calcular cuartos de final torneo")
        print("# 19 = calcular semifinal torneo")
        print("# 20 = calcular final torneo")
        print("# 21 = camepon final torneo")
        print("# 22 = fase de grupos resultados")
        print("# 23 = cuartos de final resultados")
        print("# 24 = semifinal resultados")
        print("# 25 = final resultados")
        print("# 26 = fase de grupos aleatoria resultados (demostración)")
        print("# 27 = cuartos de final aleatoria resultados (demostración)")
        print("# 28 = semifinal aleatoria resultados (demostración)")
        print("# 29 = final aleatoria resultados (demostración)")
        print("# 30 = comprar entradas")
        print("# 31 = proceso de archivos y recomendaciones en base a informes estadisticos")
        print("# -1 = finalizar programa")
        try:
            herramienta=int(input("Ingrese el numero segun lo que desee: "))
            while herramienta not in[-1,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29]:
                print("Error, el numero ingresado no se encuntra en lo indicado")
                herramienta=int(input("Ingrese el numero segun lo que desee(1 reservar canchas, 2 cancelar la reservacion de canchas, 3 calcular cobro, 4 mostrar reportes, -1 para finalizar programa): "))
        except ValueError as msg:
            print(msg)
            continue
                
        if herramienta==1:
            while True:
                try:
                    fila=0
                    cancha=int(input("Ingrese el número de cancha que desea elegir (5, 8, 11) o -1 si no desea reservar: "))
                    if cancha!=-1:
                        while cancha not in[5,8,11]:
                            print("Error, el numero de cancha seleccionado no se encuentra")
                            cancha=int(input("Ingrese el número de cancha que desea elegir (5, 8, 11): "))
                except ValueError as mensaje:
                    print(mensaje)
                    continue
                if cancha==5:
                    fila=0
                elif cancha==8:
                    fila=1
                else:
                    fila=2
                print(matrizper[fila],"Los horarios que se muestran ya estan tomados")
                while True:
                    try:
                        hora=int(input("ingrese en formato militar la hora que desea alquilar (1200 a 2400, de 100 en 100): "))
                        while hora<1200 or hora>2400 or hora%100!=0:
                            print("La hora ingresada no se encuentra en el rango (1200 a 2400, de 100 en 100)")
                            hora=int(input("Ingrese en formato militar la hora que desea alquilar (1200 a 2400, de 100 en 100): "))
                    except ValueError as mensa:
                        print(mensa)
                        continue
                    columna=(hora-1200)//100
                    if matrizper[fila][columna]==0:
                        matrizper[fila][columna]=hora
                        nombre=input("Igrese su nombre y apellido al cual reservara la cancha: ")
                        while len(nombre.strip())==0 or nombre.isdigit():
                            print("Error el nombre que inngreso no es valido(digitos o vacio)")
                            nombre=input("Igrese su nombre y apellido al cual reservara la cancha: ")
                        matriznombre[fila][columna]=nombre
                        print("Reserva realizada con exito: Cancha de futbol",cancha,"a las",hora,"horas a nombre de:",nombre)
                        listas.guardar_matirzpe(matrizper)
                        listas.guardar_matirznombr(matriznombre)
                        string=f"fut{cancha}"
                        estadistica["cualreserva"][string]+=1
                        listas.guardar_estadisticas(estadistica)
                        print("Matriz que en su interior tiene horarios en formato militar si esta alquilada y en 0 si no esta alquilada")
                        for i in range(len(matrizper)):
                            for j in range(len(matrizper[i])):
                                print("%6d" %(matrizper[i][j]),end=" ")
                            print()
                        print()
                        print("Matriz que en su interior tiene nombre a quien esta la reserva de las canchas si esta alquilada y en 0 si no esta alquilada")
                        for i in range(len(matriznombre)):
                            for j in range(len(matriznombre[i])):
                                print("%-15s" %(matriznombre[i][j]),end=" ")
                            print()
                        print()
                    else:
                        print("Ese horario ya esta ocupado")
                    while True:
                        try:
                            señ=int(input("Ingrese cualquier numero entero si desea continuar o -1 para salir: "))
                        except ValueError as mensaje2:
                            print(mensaje2)
                            continue
                        if señ==-1:
                            break
                    break
                break        
                                
        elif herramienta==2:
            while True:
                try:
                    fila2=0
                    cancha2=int(input("Ingrese el número de cancha que desea elegir (5, 8, 11) o -1 si no desea reservar: "))
                    if cancha2!=-1:
                        while cancha2 not in[5,8,11]:
                            print("Error, el numero de cancha seleccionado no se encuentra")
                            cancha2=int(input("Ingrese el número de cancha que desea elegir (5, 8, 11): "))
                except ValueError as mensaje3:
                    print(mensaje3)
                    continue

                if cancha2==5:
                    fila2=0
                elif cancha2==8:
                    fila2=1
                else:
                    fila2=2
                print(matrizper[fila2],"Los horarios que se muestran son los que ya estan tomados")
                while True:
                    try:
                        hora2=int(input("Ingrese en formato militar la hora que desea cancelar el alquilar (1200 a 2400, de 100 en 100): "))
                        while hora2<1200 or hora2>2400 or hora2%100!=0:
                            print("La hora ingresada no se encuentra en el rango (1200 a 2400, de 100 en 100)")
                            hora2=int(input("Ingrese en formato militar la hora que desea alquilar (1200 a 2400, de 100 en 100): "))
                    except ValueError as mensaje4:
                        print(mensaje4)
                        continue
                    if hora2 in matrizper[fila2]:
                        columna2=(hora2-1200)//100
                        nombrecancelado=matriznombre[fila2][columna2]
                        matrizper[fila2][columna2]=0
                        matriznombre[fila2][columna2]=0
                        print("Cancelación realizada con exito: cancha de futbol",cancha2,"de las",hora2,"horas a nombre de: ",nombrecancelado)
                        listas.guardar_matirzpe(matrizper)
                        listas.guardar_matirznombr(matriznombre)
                        string2=f"fut{cancha2}"
                        estadistica["cualreserva"][string2]-=1
                        listas.guardar_estadisticas(estadistica)
                        print("Matriz que en su interior tiene horarios en formato militar si esta alquilada y en 0 si no esta alquilada")
                        for i in range(len(matrizper)):
                            for j in range(len(matrizper[i])):
                                print("%6d" %(matrizper[i][j]),end=" ")
                            print()
                        print()
                        print("Matriz que en su interior tiene nombre a quien esta la reserva de las canchas si esta alquilada y en 0 si no esta alquilada")
                        for i in range(len(matriznombre)):
                            for j in range(len(matriznombre[i])):
                                print("%-15s" %(matriznombre[i][j]),end=" ")
                            print()
                        print()
                    else:
                        print("Ese horario no se encuentra alquilado")
                    while True:
                        try:
                            señ2=int(input("Ingrese cualquier número entero si desea continuar o -1 para salir: "))
                        except ValueError as mensaje5:
                            print(mensaje5)
                            continue
                        if señ2==-1:
                            break
                    break
                break

        elif herramienta==3:
            while True:
                precios,horas,cancha,ingresohora,clientes=funmod.guardar_precio_cantidad_horas(random.randint(35000,45000),random.randint(65000,75000),random.randint(95000,105000),listhorarios)
                cobro=funmod.calcular_cantidad_a_pagar(precios,horas)
                listaclientes.append(clientes)
                print("cantidad a pagar: $",cobro)
                cobrofinal=funmod.reporte_metodo_pago(listformpago,listrecaudacionformpago,listcantformpago,cobro,listadiezporciento,cobro)
                funmod.reporte_canchas(listcanchas,listrecaudacioncanchas,listcantcanchas,cobrofinal,cancha)
                funmod.reporte_horarios(listhorarios,listrecaudacionhorarios,listcanthorarios,cobrofinal,ingresohora)
                while True:
                    try:
                        sigo2=int(input("Ingrese cualquier numero entero si desea continuar o -1 para salir: "))
                    except ValueError as mensaje6:
                        print(mensaje6)
                        continue
                    if sigo2==-1:
                        break
                break



        elif herramienta==4:
            print(listcanchas,"Lista de canchas disponibles")
            print(listrecaudacioncanchas,"Lista de recaudación de canchas")
            print(listcantcanchas,"Lista de cantidad de usos de cada cancha")
            print(listhorarios,"Lista de horarios disponibles")
            print(listrecaudacionhorarios,"Lista de recaudación de horarios")
            print(listcanthorarios,"Lista de cantidad de usos de cada horario")
            print(listformpago,"Lista de formas de pago disponibles")
            print(listrecaudacionformpago,"Lista de recaudación de formas de pago")
            print(listcantformpago,"Lista de cantidad de usos de cada forma de pago")
            maximo,numcancha,porcentaje=funmod.cancha_mayor_recuaudo_con_porcentaje(listrecaudacioncanchas,listcanchas,listcantcanchas)
            minimo,numcancha10,porcentaje10=funmod.cancha_menor_recuaudo_con_porcentaje(listrecaudacioncanchas,listcanchas,listcantcanchas)
            print("La cancha numero",numcancha,"es la que mas recaudo con: $",maximo,"con un porcentaje de:",porcentaje,"% de usos")
            print("La cancha numero",numcancha10,"es la que menos recaudo con: $",minimo,"con un porcentaje de:",porcentaje10,"% de usos")
            print("La recaudacion del 10% mas por efectivo fue de: $",sum(listadiezporciento))
            totaltodo=funmod.calcular_total(listrecaudacionformpago)
            print("$",totaltodo,"recaudacion total")
            mayorcliente,hay2,prom,horarios7=funmod.mayor_cliente(listcanthorarios,listhorarios)
            if hay2==0:
                print("El horario con la mayor cantidad de clientes es",horarios7,"con",mayorcliente,"clientes y un promedio de",prom,"clientes")
            else:
                print("Hay varios horarios con la misma cantidad de clientes",listcanthorarios)
            listadoarmado=funmod.listado(listrecaudacionhorarios,listhorarios)
            print("Listado de la recaudacion de horarios\nRecaudacion\tHorarios")
            for recaudacionhorarios,horarios in listadoarmado:
                print(f"${recaudacionhorarios}\t\ta las {horarios} horas")
            print("la recaudacion de los torneos fue de: $",sum(recaudacionestorneo))
            print("la recaudacion de la liga fue de: $",sum(recaudacionesliga))
            listas.guardar_reportes()
        
        
        elif herramienta==5:#inscripcion liga, 
            funmod.inscripciones_a_la_liga(listaequiposliga,stringer3,stringer4)
            
        elif herramienta==6:#rellenar liga, en total 20 equipos, 
            for i in range(len(listaequiposliga)):
                if listaequiposliga[i]==0:
                    while True:
                        """agarra de un archivo nombres aleatorios, por ahora agrego una lista"""
                        randonum=nombresaleatoriosequipos[random.randint(0,99)]
                        viril=listaequiposliga.count(randonum)
                        if viril==0:
                            listaequiposliga[i]=randonum
                            break
                        else:
                            continue
            listas.guardar_listaliga(listaequiposliga)
            print("lista de equipos (20 cupos)")
            for i in range(len(listaequiposliga)):
                print(f"equipo:{i+1}\t{listaequiposliga[i]}")
            listaauxiliarliga=listaequiposliga[::1]


        elif herramienta==7:#calcular los 38 partidos por equipo
            #doble bombo, es decir, se juega dos veces contra el mismo equipo (ida y vuelta). se finge el torneo para ver campeon
            contador=0
            for i in range(len(listaequiposliga)):
                if listaequiposliga[i]==0:
                    contador+=1
            if contador>0:
                print("faltan equipos")
            else:
                for x in range(len(listaequiposliga)-1):
                    partidos=[]
                    for i in range(len(listaequiposliga)//2):
                        equipo1=listaequiposliga[i]
                        equipo2=listaequiposliga[len(listaequiposliga)-1-i]
                        partidos.append([equipo1,equipo2])
                    fixtureida.append(partidos)
                    listaequiposliga=listaequiposliga[:1]+listaequiposliga[-1:]+listaequiposliga[1:-1]
                fixturevuelta=[[[b,a] for [a,b] in fecha] for fecha in fixtureida]
                contadorfecha=1
                contadorfechaaux=1
                fixturecompletito=fixtureida+fixturevuelta
                listas.guardar_fixtureidita(fixtureida)
                listas.guardar_fixturevueltita(fixturevuelta)

                
                for ronda in fixturecompletito:
                    for local,bebe in ronda:
                        fixturecompleto["fixture"].append([contadorfechaaux,local,bebe])
                        contadorfechaaux+=1
                listas.guardar_partidosdeliga(fixturecompleto)
                        

                print("Fixture de ida")
                for ronda in fixtureida:
                    print(f"partido:{contadorfecha}")
                    for partidito in ronda:
                        local=partidito[0]
                        visitante=partidito[1]
                        print(f"{local} vs {visitante}")
                    contadorfecha+=1
                contadorfechavuelta=1
                print("Fixture de vuelta")
                for rondavuelta in fixturevuelta:
                    print(f"partido:{contadorfechavuelta}")
                    for partiditovuelta in rondavuelta:
                        localvuelta=partiditovuelta[0]
                        visitantevuelta=partiditovuelta[1]
                        print(f"{localvuelta} vs {visitantevuelta}")
                    contadorfechavuelta+=1




        
        elif herramienta==8:#inscripcion sponsors PUEDO HACER UNA FUNCION PORQUE ES EL SPONSORSLIGA Y SPONSORSTORNEO TIENEN LA MISMA MANERA DE INSCRIBIRSE
            salidita=False
            while True:
                try:
                    sponsors=int(input("ingrese 0 si desea tener su sponsor en la Super Liga Nacional, o 1 si desea tener sponsor en el torneo nacional"))
                    while sponsors not in[0,1]:
                        print("error el numero ingresado no se encuentra en el rango")
                        sponsors=int(input("ingrese 0 si desea tener su sponsor en la Super Liga Nacional, o 1 si desea tener sponsor en el torneo nacional"))
                except ValueError as mensaje13:
                    print(mensaje13)
                    continue
                if sponsors==0:
                    eleccion=funmod.hacer_sponsors(disponibilidad,listasponsorszona,listasponsors,listadisponibilidad,listanombresponsor,sponsorcito,estadistica)
                    listas.guardar_estadisticas(estadistica)
                    break
                elif sponsors==1:
                    eleccion=funmod.hacer_sponsors(disponibilidadtorneo,listasponsorszona,listasponsors,listadisponibilidad,listanombresponsortorneo,sponsorcito,estadistica)
                    listas.guardar_estadisticas(estadistica)
                    break
                

            """salidita=False
            while True:
                try:
                    sponsors=int(input("ingrese 0 si desea tener su sponsor en la Super Liga Nacional, o 1 si desea tener sponsor en el torneo nacional"))
                    while sponsors not in[0,1]:
                        print("error el numero ingresado no se encuentra en el rango")
                        sponsors=int(input("ingrese 0 si desea tener su sponsor en la Super Liga Nacional, o 1 si desea tener sponsor en el torneo nacional"))
                except ValueError as mensaje13:
                    print(mensaje13)
                    continue
                if sponsors==0:
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
                                    salir=True
                                    salir3=True
                                    break
                                    
                                else:
                                    break
                            if salir:
                                break
                        if salir3:
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
                if salir10:
                    break

                elif sponsors==1:
                    print(f"\tsponsors\t\t\tdisponibilidad")
                    disponible2=-1
                    for pe in range(len(disponibilidad)):
                        if disponibilidad[pe]==0:
                            disponible2=0
                        else:
                            disponible2=1
                        print(f"{listasponsorszona[pe]}\t{listasponsors[pe]}\t{listadisponibilidad[disponible2]}")
                    while True:
                        try:
                            eleccion=int(input("ingrese el numero segun lo muestra en la lista anterior para colocar su sponsor"))
                            while eleccion not in listasponsorszona:
                                print("error fuera de rango")
                                eleccion=int(input("ingrese el numero segun lo muestra en la lista anterior para colocar su sponsor"))
                            
                        except ValueError as mensaje14:
                            print(mensaje14)
                            continue
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
                                    salir=True
                                    salir3=True
                                    break
                                    
                                else:
                                    break
                            if salir:
                                break
                        if salir3:
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
                if salir10:
                    break"""
        
        elif herramienta==9:#simular partidos resultados, mostrar tabla de liga
            funmod.resultados_aleatorios_liga(resultadosida,ligaderesultados)
            funmod.resultados_aleatorios_liga(resultadosvuelta,ligaderesultados)
            fixtureidasss=[p for ronda in fixtureida for p in ronda]
            listadopartidos=list(zip(fixtureidasss,resultadosida))
            print("Resultados partidos de ida")
            for fix,resultaditos in listadopartidos:
                local,visitante=fix
                gollocal,golvisita=resultaditos
                print(f"partido:\t{local}:{gollocal} vs {golvisita}:{visitante}")
            print()
            fixturevueltasss=[p for ronda in fixturevuelta for p in ronda]
            listadopartidosvuelta=list(zip(fixturevueltasss,resultadosvuelta))
            print("Resultados partidos de vuelta")
            for fix2,resultaditos2 in listadopartidosvuelta:
                local,visitante=fix2
                gollocal,golvisita=resultaditos2
                print(f"partido:\t{local}:{gollocal} vs {golvisita}:{visitante}")
            #falta hacer mostrar tabla de liga
            
        
        elif herramienta==10:#tengo que hacer el doble creo
            print(listaauxiliarliga)
            print(fixtureida)
            print(fixturevuelta)
            print(resultadosida)
            print(resultadosvuelta)
            funmod.calcular_tabla(fixtureida,listaauxiliarliga,partidosjugados,resultadosida,ganados,puntos,perdidos,empatados,golesfavor,golescontra,diferenciagol)
            funmod.calcular_tabla(fixturevuelta,listaauxiliarliga,partidosjugados,resultadosvuelta,ganados,puntos,perdidos,empatados,golesfavor,golescontra,diferenciagol)
            

            liga=list(zip(listaauxiliarliga,partidosjugados,ganados,perdidos,empatados,puntos,golesfavor,golescontra,diferenciagol))
            liga.sort(key=lambda x:x[5],reverse=True)
            print(nombredelaliga.center(180))
            print(f"{'Equipos':<20}{'Partidos jugados':<20}{'Ganados':<20}{'Empatados':<20}{'Perdidos':<20}{'Puntos':<20}{'Goles a favor':<20}{'Goles en contra':<20}{'Diferencia de gol':<20}")
            for equipo,pj,g,e,p,pts,gf,gc,dg in liga:
                print(f"{equipo:<20}{pj:<20}{g:<20}{e:<20}{p:<20}{pts:<20}{gf:<20}{gc:<20}{dg:<20}")
            print(f"CAMPEON DE LA SUPER LIGA NACIONAL: \t {liga[0][0]} \t con un premio de $30400000")

            tablaliga=(nombredelaliga.center(180))+"\n"
            tablaliga+=(f"{'Equipos':<20}{'Partidos jugados':<20}{'Ganados':<20}{'Empatados':<20}{'Perdidos':<20}{'Puntos':<20}{'Goles a favor':<20}{'Goles en contra':<20}{'Diferencia de gol':<20}\n")
            
            
            for equipo,pj,g,e,p,pts,gf,gc,dg in liga:
                tablaliga+=(f"{equipo:<20}{pj:<20}{g:<20}{e:<20}{p:<20}{pts:<20}{gf:<20}{gc:<20}{dg:<20}\n")
            tablaliga+=(f"\nCAMPEON DE LA SUPER LIGA NACIONAL: \t {liga[0][0]} \t con un premio de $30400000\n")
            try:
                with open("tabla_liga.txt","a",encoding="utf-8") as guardar:
                    guardar.write(tablaliga+"\n\n") 
            except IOError as men:
                print(men)
            except PermissionError as men2:
                print(men2)
            except FileNotFoundError as men3:
                print(men3)
            try:
                with open("tabla_de_liga.csv","a",newline="",encoding="utf-8") as guardarcsv:
                    escribir=csv.writer(guardarcsv)
                    escribir.writerow(["Equipos","Partidos jugados","Ganados","Empatados","Perdidos","Puntos","Goles a favor","Goles en contra","Diferencia de gol"])
                    for fila in liga:
                        escribir.writerow(fila)
                    escribir.writerow([f"campeon: {liga[0][0]}"])
            except IOError as men4:
                print(men4)
            except PermissionError as men5:
                print(men5)
            except FileNotFoundError as men6:
                print(men6)
#hay que subirlo a un archivo que va a contener las ligas tras años, premio = $30400000

#hay que poner if Len(resultados[i])<2:
#.... Todo lo de resultados aleatorios
        
        elif herramienta==11:#resultados partidos
            funmod.resultados_liga(fixtureida,resultadosida,listaauxiliarliga,ligaderesultados,fixturevuelta,resultadosvuelta)

            """for r in range(len(fixtureida)):
                if len(resultadosida[r])<2:
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
                        if len(resultadosvuelta[t])<2:
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
                            break"""
        
        elif herramienta==12:#cobro torneo o liga
            salida10=False
            while True:
                try:
                    cobrito=int(input("ingrese 1 para torneo, 2 para liga"))
                    while cobrito not in[1,2]:
                        print("error, valor ingresado fuera de rango")
                        cobrito=int(input("ingrese 1 para torneo, 2 para liga"))
                except ValueError as mostra10:
                    print(mostra10)
                    continue
                if cobrito==1:
                    print("Cada equipo debe pagar $1000000 para la inscripcion al torneo")
                    print("Total recaudado por el torneo: $",1000000*16)
                    print("Ganancia total recaudado por el torneo: $",((1000000*16)//2))
                    print("Premio del campeón del torneo: $",((1000000*16)//2))
                    funmod.reporte_torneo(recaudacionestorneo)
                    break

                else:
                    while True:
                        try:
                            finalizacion=int(input("ingrese 0 si la liga no termino, ingrese 1 si se encuentra finalizada"))
                            while finalizacion not in[0,1]:
                                print("error, el valor ingresado se encuentra fuera del rango")
                                finalizacion=int(input("ingrese 0 si la liga no termino, ingrese 1 si se encuentra finalizada"))
                        except ValueError as mostra11:
                            print(mostra11)
                            continue
                        if finalizacion==0:
                            print("Cada equipo debe pagar $80000 por fecha")
                            #ACA TENGO QUE BORRAR EL DOC CON LAS ENTRADAS
                            salida10=True
                            break

                        else:
                            print("Total recaudado por la liga: $",80000*20*38)
                            print("Ganancia total recaudado por la liga: $",((80000*20*38)//2))
                            print("Premio del campeón de liga: $",((80000*20*38)//2))
                            funmod.reporte_liga(recaudacionesliga)
                            salida10=True
                            break
                    if salida10:
                        break

            #actualizar reportes de liga y torneo, poner torneo
        
        elif herramienta==13:#inscripcion torneo, 
            funmod.inscripciones_a_la_liga(listaequipostorneo,stringer,stringer2)
            
                




        elif herramienta==14:#rellenar torneo, en total 16 equipos, 
            for i in range(len(listaequipostorneo)):
                if listaequipostorneo[i]==0:
                    """agarra de un archivo nombres aleatorios, por ahora agrego una lista"""
                    listaequipostorneo[i]=nombresaleatoriosequipos[random.randint(0,100)]
                    listas.guardar_listatorneo(listaequipostorneo)
            print("lista de equipos (16 cupos)")
            for i in range(len(listaequipostorneo)):
                print(f"equipo:{i+1}\t{listaequipostorneo[i]}")

        elif herramienta==15:#calcular los partidos por equipo torneo se finge el torneo para ver campeon
            contadortorneo=0
            for i in range(len(listaequipostorneo)):
                if listaequipostorneo[i]==0:
                    contadortorneo+=1
            if contadortorneo>0:
                print("faltan equipos")
            else:
                random.shuffle(listaequipostorneo)
                listaequipostorneoaux=listaequipostorneo[:]
                for l in range(len(fasegrupos1)):
                    fasegrupos1.append(listaequipostorneoaux[l])
                for z in range(len(fasegrupos2)):
                    fasegrupos2.append(listaequipostorneoaux[z+(len(fasegrupos1))])
                for b in range(len(fasegrupos3)):
                    fasegrupos3.append(listaequipostorneoaux[b+(len(fasegrupos1))+(len(fasegrupos2))])
                for n in range(len(fasegrupos4)):
                    fasegrupos4.append(listaequipostorneoaux[n+(len(fasegrupos1))+(len(fasegrupos2))+(len(fasegrupos3))])
                fasegrupos1aux=fasegrupos1[::1]
                fasegrupos2aux=fasegrupos2[::1]
                fasegrupos3aux=fasegrupos3[::1]
                fasegrupos4aux=fasegrupos4[::1]

                #SE PUEDE HACER UNA FUNCION
                funmod.calcular_partidos(fasegrupos1,fasegrupo1partidos)
                funmod.calcular_partidos(fasegrupos2,fasegrupo2partidos)
                funmod.calcular_partidos(fasegrupos3,fasegrupo3partidos)
                funmod.calcular_partidos(fasegrupos4,fasegrupo4partidos)
                """for x in range(len(fasegrupos1)-1):
                    
                    for i in range(len(fasegrupos1)//2):
                        equipo1torneo=fasegrupos1[i]
                        equipo2torneo=fasegrupos1[len(fasegrupos1)-1-i]
                        fasegrupo1partidos.append([equipo1torneo,equipo2torneo])
                        fasegrupos1=fasegrupos1[:1]+fasegrupos1[-1:]+fasegrupos1[1:-1]
                for x in range(len(fasegrupos2)-1):
                    
                    for i in range(len(fasegrupos2)//2):
                        equipo3torneo=fasegrupos2[i]
                        equipo4torneo=fasegrupos2[len(fasegrupos2)-1-i]
                        fasegrupo2partidos.append([equipo3torneo,equipo4torneo])
                        fasegrupos2=fasegrupos2[:1]+fasegrupos2[-1:]+fasegrupos2[1:-1]
                for x in range(len(fasegrupos3)-1):
                    
                    for i in range(len(fasegrupos3)//2):
                        equipo5torneo=fasegrupos3[i]
                        equipo6torneo=fasegrupos3[len(fasegrupos3)-1-i]
                        fasegrupo3partidos.append([equipo5torneo,equipo6torneo])
                        fasegrupos3=fasegrupos3[:1]+fasegrupos3[-1:]+fasegrupos3[1:-1]

                for x in range(len(fasegrupos4)-1):
                    
                    for i in range(len(fasegrupos4)//2):
                        equipo7torneo=fasegrupos4[i]
                        equipo8torneo=fasegrupos4[len(fasegrupos4)-1-i]
                        fasegrupo4partidos.append([equipo7torneo,equipo8torneo])
                        fasegrupos4=fasegrupos4[:1]+fasegrupos4[-1:]+fasegrupos4[1:-1]"""
                   
                
                for local,visitante in fasegrupo1partidos:
                    fixturetorneo["fixturefasegrupos1"].append([local,visitante])
                for local,visitante in fasegrupo2partidos:
                    fixturetorneo["fixturefasegrupos2"].append([local,visitante])
                for local,visitante in fasegrupo3partidos:
                    fixturetorneo["fixturefasegrupos3"].append([local,visitante])
                for local,visitante in fasegrupo4partidos:
                    fixturetorneo["fixturefasegrupos4"].append([local,visitante])
                listas.guardar_partidosdetorneo(fixturetorneo)

        elif herramienta==16:#calcular cuartos de final
            
            funmod.resultados_aleatorios_fasegrupos(fasegrupos1resultados)
            funmod.resultados_aleatorios_fasegrupos(fasegrupos2resultados)
            funmod.resultados_aleatorios_fasegrupos(fasegrupos3resultados)
            funmod.resultados_aleatorios_fasegrupos(fasegrupos4resultados)
                         
            for resu1,resu2 in fasegrupos1resultados:
                resultaditosgeneral["fasegrupos1"].append([resu1,resu2])  
            for resu1,resu2 in fasegrupos2resultados:   
                resultaditosgeneral["fasegrupos2"].append([resu1,resu2])
            for resu1,resu2 in fasegrupos3resultados:
                resultaditosgeneral["fasegrupos3"].append([resu1,resu2])
            for resu1,resu2 in fasegrupos4resultados:
                resultaditosgeneral["fasegrupos4"].append([resu1,resu2])
            listas.guardar_torneo(resultaditosgeneral)
            listadopartidosfase1=list(zip(fasegrupos1,fasegrupos1resultados,contadorpartidosfase1))
            print("Resultados partidos fase 1")
            for fixe,resultadito,contadorfase1 in listadopartidosfase1:
                print(f"partido: {contadorfase1}\t{fixe[contadorfase1-1][0]}:{resultadito[contadorfase1-1][0]} vs {resultadito[contadorfase1-1][1]}:{fixe[contadorfase1-1][1]}")
            print()
            listadopartidosfase2=list(zip(fasegrupos2,fasegrupos2resultados,contadorpartidosfase2))
            print("Resultados partidos fase 2")
            for fixe2,resultadito2,contadorfase2 in listadopartidosfase2:
                print(f"partido: {contadorfase2}\t{fixe2[contadorfase2-1][0]}:{resultadito2[contadorfase2-1][0]} vs {resultadito2[contadorfase2-1][1]}:{fixe2[contadorfase2-1][1]}")
            print()
            listadopartidosfase3=list(zip(fasegrupos3,fasegrupos3resultados,contadorpartidosfase3))
            print("Resultados partidos fase 3")
            for fixe3,resultadito3,contadorfase3 in listadopartidosfase3:
                print(f"partido: {contadorfase3}\t{fixe3[contadorfase3-1][0]}:{resultadito3[contadorfase3-1][0]} vs {resultadito3[contadorfase3-1][1]}:{fixe3[contadorfase3-1][1]}")
            print()
            listadopartidosfase4=list(zip(fasegrupos4,fasegrupos4resultados,contadorpartidosfase4))
            print("Resultados partidos fase 4")
            for fixe4,resultadito4,contadorfase4 in listadopartidosfase4:
                print(f"partido: {contadorfase4}\t{fixe4[contadorfase4-1][0]}:{resultadito4[contadorfase4-1][0]} vs {resultadito4[contadorfase4-1][1]}:{fixe4[contadorfase4-1][1]}")
            print()

        elif herramienta==17:#tablas fase grupos del torneo
            funmod.calcular_tabla(fasegrupos1resultados,fasegrupos1aux,partidosjugadosfase1,fasegrupos1resultados,ganadosfase1,puntosfase1,perdidosfase1,empatadosfase1,golesfavorfase1,golescontrafase1,diferenciagolfase1)
        
            fase1=list(zip(fasegrupos1aux,partidosjugadosfase1,ganadosfase1,perdidosfase1,empatadosfase1,puntosfase1,golesfavorfase1,golescontrafase1,diferenciagolfase1))
            fase1.sort(ley=lambda x:x[5],reverse=True)
            print(nombredeltorneo.center(180))
            print(f"{'Equipos':-20}{'Partidos jugados':-20}{'Ganados':-20}{'Empatados':-20}{'Perdidos':-20}{'Puntos':-20}{'Goles a favor':-20}{'Goles en contra':-20}{'Diferencia de gol':-20}")
            for leter in fase1:
                print(f"{fasegrupos1aux[leter]:-20}{partidosjugados[leter]:-20}{ganados[leter]:-20}{empatados[leter]:-20}{perdidos[leter]:-20}{puntos[leter]:-20}{golesfavor[leter]:-20}{golescontra[leter]:-20}{diferenciagol[leter]:-20}")
            print()
            print(f"PASAN A LA SIGUIENTE FASE: \t {fase1[0][0]} \t y \t  {fase1[0][1]} ")
            
            funmod.calcular_tabla(fasegrupos2resultados,fasegrupos2aux,partidosjugadosfase2,fasegrupos2resultados,ganadosfase2,puntosfase2,perdidosfase2,empatadosfase2,golesfavorfase2,golescontrafase2,diferenciagolfase2)
        
            fase2=list(zip(fasegrupos2aux,partidosjugadosfase2,ganadosfase2,empatadosfase2,perdidosfase2,puntosfase2,golesfavorfase2,golescontrafase2,diferenciagolfase2))
            fase2.sort(key=lambda x: x[5], reverse=True)
            print(nombredeltorneo.center(180))
            print(f"{'Equipos':-20}{'Partidos jugados':-20}{'Ganados':-20}{'Empatados':-20}{'Perdidos':-20}{'Puntos':-20}{'Goles a favor':-20}{'Goles en contra':-20}{'Diferencia de gol':-20}")
            for element in fase2:
                print(f"{fasegrupos2aux[element]:-20}{partidosjugadosfase2[element]:-20}{ganadosfase2[element]:-20}{empatadosfase2[element]:-20}{perdidosfase2[element]:-20}{puntosfase2[element]:-20}{golesfavorfase2[element]:-20}{golescontrafase2[element]:-20}{diferenciagolfase2[element]:-20}")
            print()
            print(f"PASAN A LA SIGUIENTE FASE: \t {fase2[0][0]} \t y \t  {fase2[0][1]} ")

            funmod.calcular_tabla(fasegrupos3resultados,fasegrupos3aux,partidosjugadosfase3,fasegrupos3resultados,ganadosfase3,puntosfase3,perdidosfase3,empatadosfase3,golesfavorfase3,golescontrafase3,diferenciagolfase3)
        
            fase3=list(zip(fasegrupos3aux,partidosjugadosfase3,ganadosfase3,empatadosfase3,perdidosfase3,puntosfase3,golesfavorfase3,golescontrafase3,diferenciagolfase3))
            fase3.sort(key=lambda x: x[5], reverse=True)
            print(nombredeltorneo.center(180))
            print(f"{'Equipos':-20}{'Partidos jugados':-20}{'Ganados':-20}{'Empatados':-20}{'Perdidos':-20}{'Puntos':-20}{'Goles a favor':-20}{'Goles en contra':-20}{'Diferencia de gol':-20}")
            for element in fase2:
                print(f"{fasegrupos3aux[element]:-20}{partidosjugadosfase3[element]:-20}{ganadosfase3[element]:-20}{empatadosfase3[element]:-20}{perdidosfase3[element]:-20}{puntosfase3[element]:-20}{golesfavorfase3[element]:-20}{golescontrafase3[element]:-20}{diferenciagolfase3[element]:-20}")
            print()
            print(f"PASAN A LA SIGUIENTE FASE: \t {fase3[0][0]} \t y \t  {fase3[0][1]} ")

            funmod.calcular_tabla(fasegrupos4resultados,fasegrupos4aux,partidosjugadosfase4,fasegrupos4resultados,ganadosfase4,puntosfase4,perdidosfase4,empatadosfase4,golesfavorfase4,golescontrafase4,diferenciagolfase4)
        
            
            fase4=list(zip(fasegrupos4aux,partidosjugadosfase4,ganadosfase4,empatadosfase4,perdidosfase4,puntosfase4,golesfavorfase4,golescontrafase4,diferenciagolfase4))
            fase4.sort(key=lambda x: x[5], reverse=True)
            print(nombredeltorneo.center(180))
            print(f"{'Equipos':-20}{'Partidos jugados':-20}{'Ganados':-20}{'Empatados':-20}{'Perdidos':-20}{'Puntos':-20}{'Goles a favor':-20}{'Goles en contra':-20}{'Diferencia de gol':-20}")
            for element in fase4:
                print(f"{fasegrupos4aux[element]:-20}{partidosjugadosfase4[element]:-20}{ganadosfase4[element]:-20}{empatadosfase4[element]:-20}{perdidosfase4[element]:-20}{puntosfase4[element]:-20}{golesfavorfase4[element]:-20}{golescontrafase4[element]:-20}{diferenciagolfase4[element]:-20}")
            print()
            print(f"PASAN A LA SIGUIENTE FASE: \t {fase4[0][0]} \t y \t  {fase4[0][1]} ")




        elif herramienta==18:#calcular cuartos
            megacontador=0
            for i in range(len(fasegrupos1resultados)):
                if len(fasegrupos1resultados[i])<2:
                    megacontador+=1
            for i in range(len(fasegrupos2resultados)):
                if len(fasegrupos2resultados[i])<2:
                    megacontador+=1
            for i in range(len(fasegrupos3resultados)):
                if len(fasegrupos3resultados[i])<2:
                    megacontador+=1
            for i in range(len(fasegrupos4resultados)):
                if len(fasegrupos4resultados[i])<2:
                    megacontador+=1

            if megacontador>0:
                print("faltan partidos por jugar")
            else:
                for i in range((len(listaequipostorneoaux)//2//2//2)):
                    ereq1=fase1[0][i]
                    doeq2=fase2[0][i]
                    ereq3=fase3[0][i]
                    toeq4=fase4[0][i]
                    cuartos.append([ereq1,ereq3])
                    cuartos.append([doeq2,toeq4])
                    cuartosaux=cuartos[::1]
                    for local,visitante in cuartosaux:
                        fixturetorneo["fixturecuartos"].append([local,visitante])
                    listas.guardar_partidosdetorneo(fixturetorneo)

        elif herramienta==19:#calcular semifinal
            megacontador2=0
            for i in range(len(cuartosresultados)):
                if len(cuartosresultados[i])<2:
                    megacontador2+=1
                if cuartosresultados[i][0]>cuartosresultados[i][1]:
                    ganador=cuartosresultados[i][0]
                    ganadorescuartos.append(ganador)
                else:
                    ganador=cuartosresultados[i][1]
                    ganadorescuartos.append(ganador)
            if megacontador2>0:
                print("faltan partidos por jugar")
            else:
                for i in range((len(listaequipostorneoaux)//2//2//2//2)):
                    ereqcuartos1=ganadorescuartos[i]
                    doeqcuartos2=ganadorescuartos[i+1]
                    ereqcuartos3=ganadorescuartos[i+2]
                    toeqcuartos4=ganadorescuartos[i+3]
                    semis.append([ereqcuartos1,ereqcuartos3])
                    semis.append([doeqcuartos2,toeqcuartos4])
                    semisaux=semis[::1]
                    for local,visitante in semisaux:
                        fixturetorneo["fixturesemis"].append([local,visitante])
                    listas.guardar_partidosdetorneo(fixturetorneo)

        elif herramienta==20:#calcular final
            megacontador3=0
            for i in range(len(semisresultados)):
                if len(semisresultados[i])<2:
                    megacontador3+=1
                if semisresultados[i][0]>semisresultados[i][1]:
                    ganadorsemis=cuartosresultados[i][0]
                    ganadoressemis.append(ganadorsemis)
                    finalaux=final[::1]
                else:
                    ganadorsemis=cuartosresultados[i][1]
                    ganadoressemis.append(ganadorsemis)
                    finalaux=final[::1]
            if megacontador3>0:
                print("faltan partidos por jugar")
            else:
                for i in range((len(listaequipostorneoaux)//2//2//2//2)):
                    ereqfinal1=ganadoressemis[i]
                    doeqfinal2=ganadoressemis[i+1]
                    final.append([ereqfinal1,doeqfinal2])
                    for local,visitante in final:
                        fixturetorneo["fixturefinal"].append([local,visitante])
                    listas.guardar_partidosdetorneo(fixturetorneo)
        elif herramienta==21:#campeon final torneo
            megacontador4=0
            for i in range(len(finalresultados)):
                if len(finalresultados[i])<2:
                    megacontador4+=1
                if finalresultados[i][0]>finalresultados[i][1]:
                    ganadorfinal=finalresultados[i][0]
                    campeontorneo.append(ganadorfinal)
                else:
                    ganadorfinal=finalresultados[i][1]
                    campeontorneo.append(ganadorfinal)
            if megacontador4>0:
                print("faltan partidos por jugar")
            else:
                for i in range((len(listaequipostorneoaux)//2//2//2//2)):
                    megacampeon=campeontorneo[i]
                    campeones.append(megacampeon)
            print(f"CAMPEON DEL TORNEO NACIONAL: {megacampeon}")
        elif herramienta==22:   #fase de grupos para poner resultados
            while True:    
                try:
                    zona=int(input("Elegí la zona a cargar (1-4), o -1 para salir: "))
                    while zona<1 or zona>4:
                        print("Error, solo números del 1 al 4 y -1")
                        zona=int(input("Elegí la zona a cargar (1-4), o -1 para salir: "))
                except ValueError:
                    print("Entrada inválida, debe ser un número entre 1 y 4 y -1")
                    continue

                if zona==1:
                    funmod.fasegrupos_ponerresultados(fasegrupos1aux,fasegrupos1resultados,resultaditosgeneral,"fasegrupos1")
                    
                elif zona==2:
                    funmod.fasegrupos_ponerresultados(fasegrupos2aux,fasegrupos2resultados,resultaditosgeneral,"fasegrupos2")

                elif zona==3:
                    funmod.fasegrupos_ponerresultados(fasegrupos3aux,fasegrupos3resultados,resultaditosgeneral,"fasegrupos3")

                elif zona==4:
                    funmod.fasegrupos_ponerresultados(fasegrupos4aux,fasegrupos4resultados,resultaditosgeneral,"fasegrupos4")
                
                else:
                    break

            #falta hacer mostrar tabla de liga
#falta sumar listas de resultados
#SE PUEDE PONER LOS TRES DE ABAJO EN UNA FUNCION
        elif herramienta==23:   #poner cuartos manual
            funmod.ingresar_manual_partidos(cuartosaux,cuartosresultados,resultaditosgeneral,"cuartos")
            """for r in range(len(cuartosaux)):
                if len(cuartosresultados[r])<2:
                    jugadorescuartos1=cuartosaux[r][0]
                    jugadorescuartos2=cuartosaux[r][1]
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
                        cuartosresultados[r].append([golescuartos1,golescuartos2])
                        resultaditosgeneral["cuartos"].append([golescuartos1,golescuartos2])
                        listas.guardar_torneo(resultaditosgeneral)
                        print(f"Resultado: {jugadorescuartos1} : {golescuartos1} vs {golescuartos2} : {jugadorescuartos2}")
                        break
                else:
                    print("Este partido ya tiene resultado")"""
        #PONERLO EN UNA FINCION FUNMOD
        elif herramienta==24:   #poner semifinal manual
            funmod.ingresar_manual_partidos(semisaux,semisresultados,resultaditosgeneral,"semis")

            
        #EL MISMO QUE EL DE ARRIBA FUNCIONA
        elif herramienta==25:   #poner final manual
            funmod.ingresar_manual_partidos(finalaux,finalresultados,resultaditosgeneral,"final")

            
        #PONERLO EN UNA FINCION FUNMOD
        elif herramienta==26:   #fases de grupo aleatorias
            funmod.ingreso_aleatorio_partidos(fasegrupos1aux,fasegrupos1resultados,resultaditosgeneral,"fasegrupos1")
            funmod.ingreso_aleatorio_partidos(fasegrupos2aux,fasegrupos2resultados,resultaditosgeneral,"fasegrupos2")
            funmod.ingreso_aleatorio_partidos(fasegrupos3aux,fasegrupos3resultados,resultaditosgeneral,"fasegrupos3")
            funmod.ingreso_aleatorio_partidos(fasegrupos4aux,fasegrupos4resultados,resultaditosgeneral,"fasegrupos4")

            """for r in range(len(fasegrupos1aux)):
                if len(fasegrupos1resultados[r])<2:
                    golcitos1=random.randint(0,15)
                    golcitos2=random.randint(0,15)
                    fasegrupos1resultados[r].append([golcitos1,golcitos2])
                    resultaditosgeneral["fasegrupos1"].append([golcitos1,golcitos2])
                    listas.guardar_torneo(resultaditosgeneral)
            for r in range(len(fasegrupos2aux)):
                if len(fasegrupos2resultados[r])<2:
                    golcitos21=random.randint(0,15)
                    golcitos22=random.randint(0,15)
                    fasegrupos2resultados[r].append([golcitos21,golcitos22])
                    resultaditosgeneral["fasegrupos2"].append([golcitos21,golcitos22])
                    listas.guardar_torneo(resultaditosgeneral)
            for r in range(len(fasegrupos3aux)):
                if len(fasegrupos3resultados[r])<2:
                    golcitos31=random.randint(0,15)
                    golcitos32=random.randint(0,15)
                    fasegrupos3resultados[r].append([golcitos31,golcitos32])
                    resultaditosgeneral["fasegrupos3"].append([golcitos31,golcitos32])
                    listas.guardar_torneo(resultaditosgeneral)
            for r in range(len(fasegrupos4aux)):
                if len(fasegrupos4resultados[r])<2:
                    golcitos41=random.randint(0,15)
                    golcitos42=random.randint(0,15)
                    fasegrupos4resultados[r].append([golcitos41,golcitos42])
                    resultaditosgeneral["fasegrupos4"].append([golcitos41,golcitos42])
                    listas.guardar_torneo(resultaditosgeneral)"""

            print("RESULTADOS FASE DE GRUPOS")
            print("Zona 1:")
            abierto1=list(zip(fasegrupos1aux,fasegrupos1resultados))
            for fix,res in abierto1:
                print(f"{fix[0]} {res[0][0]} vs {res[0][1]} {fix[1]}")
            print("Zona 2:")
            abierto2=list(zip(fasegrupos2aux,fasegrupos2resultados))
            for fix,res in abierto2:
                print(f"{fix[0]} {res[0][0]} vs {res[0][1]} {fix[1]}")
            print("Zona 3:")
            abierto3=list(zip(fasegrupos3aux,fasegrupos3resultados))
            for fix,res in abierto3:
                print(f"{fix[0]} {res[0][0]} vs {res[0][1]} {fix[1]}")
            print("Zona 4:")
            abierto4=list(zip(fasegrupos4aux,fasegrupos4resultados))
            for fix,res in abierto4:
                print(f"{fix[0]} {res[0][0]} vs {res[0][1]} {fix[1]}")

        elif herramienta==27:   #cuartos aleatorio
            funmod.ingreso_aleatorio_partidos(cuartosaux,cuartosresultados,resultaditosgeneral,"cuartos")

            """for r in range(len(cuartosaux)):
                if len(cuartosresultados[r])<2:
                    golcitoscuartos1=random.randint(0,15)
                    golcitoscuartos2=random.randint(0,15)
                    cuartosresultados[r].append([golcitoscuartos1,golcitoscuartos2])
                    resultaditosgeneral["cuartos"].append([golcitoscuartos1,golcitoscuartos2])
                    listas.guardar_torneo(resultaditosgeneral)"""

            print("RESULTADOS CUARTOS DE FINAL")
            abiertocuartos=list(zip(cuartosaux,cuartosresultados))
            for fix,res in abiertocuartos:
                print(f"{fix[0]} {res[0][0]} vs {res[0][1]} {fix[1]}")

        elif herramienta==28:   #semis aleatorio
            funmod.ingreso_aleatorio_partidos(semisaux,semisresultados,resultaditosgeneral,"semis")

            """for r in range(len(semisaux)):
                if len(semisresultados[r])<2:
                    golcitossemis1=random.randint(0,15)
                    golcitossemis2=random.randint(0,15)
                    semisresultados[r].append([golcitossemis1,golcitossemis2])
                    resultaditosgeneral["semis"].append([golcitossemis1,golcitossemis2])
                    listas.guardar_torneo(resultaditosgeneral)"""

            print("RESULTADOS SEMIFINALES")
            abiertosemis=list(zip(semisaux,semisresultados))
            for fix,res in abiertosemis:
                print(f"{fix[0]} {res[0][0]} vs {res[0][1]} {fix[1]}")

        elif herramienta==29:   #final aleatorio
            funmod.ingreso_aleatorio_partidos(finalaux,finalresultados,resultaditosgeneral,"final")

            """for r in range(len(finalaux)):
                if len(finalresultados[r])<2:
                    golcitosfinal1=random.randint(0,15)
                    golcitosfinal2=random.randint(0,15)
                    finalresultados[r].append([golcitosfinal1,golcitosfinal2])
                    resultaditosgeneral["final"].append([golcitosfinal1,golcitosfinal2])
                    listas.guardar_torneo(resultaditosgeneral)"""

            print("RESULTADO FINAL")
            abiertofinal=list(zip(finalaux,finalresultados))
            for fix,res in abiertofinal:
                print(f"{fix[0]} {res[0][0]} vs {res[0][1]} {fix[1]}")

        



        elif herramienta==30:
            while True:
                try:
                    numero=int(input("ingresa 1 para liga, 2 para torneo, -1 para salir"))
                    while numero not in[1,2,-1]:
                        print("error")
                        numero=int(input("ingresa 1 para liga, 2 para torneo, -1 para salir"))
                except ValueError as mensajote:
                    print(mensajote)
                    continue
                if numero==1:
                    try:
                        print(entradas)
                        entraditas=int(input("ingrese 1 si desea alquilar vip, 2 para platea, 3 para popular o -1 para salir: "))
                        while entraditas not in[-1,1,2,3]:
                            print("error, el valor ingresado se encuentra fuera del rango")
                            entraditas=int(input("ingrese 1 si desea alquilar vip, 2 para platea, 3 para popular o -1 para salir: "))
                        if entraditas==1:
                            decercion="vip"
                        elif entraditas==2:
                            decercion="platea"
                        elif entraditas==2:
                            decercion="popular"
                        else:
                            break
                        cantidad=int(input("ingrese la cantidad de entradas que desea"))
                    except ValueError as mensajito:
                        print(mensajito)
                        continue
                    funmod.mostrar_disponibles(entradas)
                    funmod.alquilar(decercion,cantidad)
                    listas.guardar_entradas(entradas)
                    estadistica["cualvendemas"]["entradasliga"]+=1
                    listas.guardar_estadisticas(estadistica)
                    break
                elif numero==2:
                    try:
                        print(entradas)
                        entraditas=int(input("ingrese 1 si desea alquilar vip, 2 para platea, 3 para popular o -1 para salir: "))
                        while entraditas not in[-1,1,2,3]:
                            print("error, el valor ingresado se encuentra fuera del rango")
                            entraditas=int(input("ingrese 1 si desea alquilar vip, 2 para platea, 3 para popular o -1 para salir: "))
                        if entraditas==1:
                            decercion="vip"
                        elif entraditas==2:
                            decercion="platea"
                        elif entraditas==2:
                            decercion="popular"
                        else:
                            break
                        cantidad=int(input("ingrese la cantidad de entradas que desea"))
                    except ValueError as mensajito:
                        print(mensajito)
                        continue
                    funmod.mostrar_disponiblestorneo(entradastorneo)
                    funmod.alquilartorneo(decercion,cantidad,estadistica)
                    listas.guardar_entradastorneo(entradastorneo)
                    estadistica["cualvendemas"]["entradastorneo"]+=1
                    listas.guardar_estadisticas(estadistica)
                    break
                else:
                    break
        elif herramienta==31:
            funmod.recomendaciones(estadistica)

        else:
            print("-------------------- Finalización del Programa --------------------")
            print("Matriz que en su interior tiene horarios en formato militar si esta alquilada y en 0 si no esta alquilada")
            for i in range(len(matrizper)):
                for j in range(len(matrizper[i])):
                    print("%6d" %(matrizper[i][j]),end=" ")
                print()
            print()
            print("Matriz que en su interior tiene nombre a quien esta la reserva de las canchas si esta alquilada y en 0 si no esta alquilada")
            for i in range(len(matriznombre)):
                for j in range(len(matriznombre[i])):
                    print("%-15s" %(matriznombre[i][j]),end=" ")
                print()
            print()
            break
#este por el momento viene bien, hay que probar lo que dice el main copy.py

