import listas
import random
import pathlib
import datetime
import funmod
def admin(user):
    cualvendemas,entradasvendidas,fixturevueltita,fixtureidita,resultadosvueltita,resultadosidita,expediente,entradonas2,entradonas,sponsors,fixturetorneo,fixture,liguita,torneito,torneooficial4,torneooficial3,listatorneo,listaliga,torneooficial,torneooficial2,reportes,cualreserva,sponsorsuso,bitacora,archivo,archivo2=listas.cargar_rutas_archivos()
    listcanchas,listhorarios,listformpago,listrecaudacioncanchas,listrecaudacionhorarios,listrecaudacionformpago,listcantcanchas,listcanthorarios,listcantformpago,listaclientes,listadiezporciento,recaudacionestorneo,recaudacionesliga,pagoentrada=listas.cargar_reportes()
    comprobacionusuario=pathlib.Path("archivoinicio.txt")
    tuplasin=("# 1 = reservar canchas","# 2 = cancelar la reservacion de canchas","# 3 = calcular cobro","# 4 = mostrar reportes","# 5 = inscripción liga","# 6 = rellenar liga (demostración)","# 7 = calcular partidos de liga","# 8 = inscripcion sponsors","# 9 = simular partidos resultados (demostración)","# 10 = tabla de liga","# 11 = poner resultados partidos liga","# 12 = cobro torneo o liga","# 13 = inscripcion torneo","# 14 = rellenar torneo (demostración)","# 15 = calcular los partidos del torneo","# 16 = resultados aleatorios fase de grupos (demostracion)","# 17 = tablas fase de grupos torneo","# 18 = calcular cuartos de final torneo","# 19 = calcular semifinal torneo","# 20 = calcular final torneo","# 21 = camepon final torneo","# 22 = fase de grupos resultados","# 23 = cuartos de final resultados","# 24 = semifinal resultados","# 25 = final resultados","# 26 = cuartos de final aleatoria resultados (demostración)","# 27 = semifinal aleatoria resultados (demostración)","# 28 = final aleatoria resultados (demostración)","# 29 = comprar entradas","# 30 = proceso de archivos y recomendaciones en base a informes estadisticos","# 31 = dar de baja cuentas","# -1 = finalizar programa")
    vendemas=listas.cargar_cualvendemas(cualvendemas)
    reservamas=listas.cargar_cualreserva(cualreserva)
    usosponsors=listas.cargar_sponsorsuso(sponsorsuso)
    entradasvendi=listas.cargar_entradasvendidas(entradasvendidas)
    reportaje=listas.cargar_reportes(reportes)
    pagoentrada=reportaje["pagoentrada"]
    recaudacionesliga=reportaje["recaudacionesliga"]
    recaudacionestorneo=reportaje["recaudacionestorneo"]
    disponible,ocupadas,disponibletorneo,ocupadastorneo=listas.cargar_entradasdelisto()
    equipostorneo=listas.cargar_listatorneo(listatorneo)
    fixtureida=listas.cargar_fixtureidita(fixtureidita)
    fixturevuelta=listas.cargar_fixturevueltita(fixturevueltita)
    resultadosida=listas.cargar_resultadosidita(resultadosidita)
    resultadosvuelta=listas.cargar_resultadosvueltita(resultadosvueltita)
    stringer="bienvenido a inscripcion en el Torneo Nacional"
    stringer2="lista de equipos (16 cupos)"
    stringer3="bienvenido a inscripcion en la Super Liga Nacional"
    stringer4="lista de equipos (20 cupos)"
    estadistica=listas.cargar_estadisticas(expediente)
    entradastorneo=listas.cargar_entradastorneo(entradonas2)
    entradas=listas.cargar_entradas(entradonas)
    sponsorcito=listas.cargar_sponsors(sponsors)
    fixturecompleto=listas.cargar_partidosdeliga(fixture)
    fixturetorneos=listas.cargar_partidosdetorneo(fixturetorneo)
    listaequiposliga=listas.cargar_listaliga(listaliga)
    listaauxiliarliga=listas.cargar_listaliga(listaliga)
    listaequipostorneo=listas.cargar_listatorneo(listatorneo)
    ligaderesultados=listas.cargar_liga(liguita)
    resultaditosgeneral=listas.cargar_torneo(torneito)
    matrizper=listas.cargar_matrizpe(archivo)
    matriznombre=listas.cargar_matriznombr(archivo2)
    listcanchas,listhorarios,listformpago,listrecaudacioncanchas,listrecaudacionhorarios,listrecaudacionformpago,listcantcanchas,listcanthorarios,listcantformpago,listaclientes,listadiezporciento=reportaje["listcanchas"],reportaje["listhorario"],reportaje["listformpago"],reportaje["listrecaudacioncanchas"],reportaje["listrecaudacionhorarios"],reportaje["listrecaudacionformpago"],reportaje["listcantcanchas"],reportaje["listcanthorarios"],reportaje["listcantformpago"],reportaje["listaclientes"],reportaje["listadiezporciento"]
    nombredelaliga="Super Liga Nacional"
    nombredeltorneo="Torneo Nacional"
    torneoo1=listas.cargar_torneooficial(torneooficial)
    torneoo2=listas.cargar_torneooficial2(torneooficial2)
    torneoo3=listas.cargar_torneooficial3(torneooficial3)
    torneoo4=listas.cargar_torneooficial4(torneooficial4)
    cuartosresultados=resultaditosgeneral["cuartosresultados"]
    ganadorescuartos=[]
    ganadoressemis=[]
    semisresultados=resultaditosgeneral["semisresultados"]
    finalresultados=resultaditosgeneral["finalresultados"]
    ganadorfinal=[]
    campeontorneo=[]
    campeones=[]
    fasegrupos1=torneoo1
    fasegrupos2=torneoo2
    fasegrupos3=torneoo3
    fasegrupos4=torneoo4
    fasegrupos1aux=fasegrupos1[::1]
    fasegrupos2aux=fasegrupos2[::1]
    fasegrupos3aux=fasegrupos3[::1]
    fasegrupos4aux=fasegrupos4[::1]
    fasegrupo1partidos=fixturetorneos["fasegrupo1partidos"]
    fasegrupo2partidos=fixturetorneos["fasegrupo2partidos"]
    fasegrupo3partidos=fixturetorneos["fasegrupo3partidos"]
    fasegrupo4partidos=fixturetorneos["fasegrupo4partidos"]
    cuartos=fixturetorneos["cuartos"]
    semis=fixturetorneos["semis"]
    final=fixturetorneos["final"]
    fasegrupos1resultados=resultaditosgeneral["fasegrupos1resultados"]
    fasegrupos2resultados=resultaditosgeneral["fasegrupos2resultados"]
    fasegrupos3resultados=resultaditosgeneral["fasegrupos3resultados"]
    fasegrupos4resultados=resultaditosgeneral["fasegrupos4resultados"]
    partidosjugados,ganados,empatados,perdidos,puntos,golesfavor,golescontra,diferenciagol=[0 for _ in range(20)],[0 for _ in range(20)],[0 for _ in range(20)],[0 for _ in range(20)],[0 for _ in range(20)],[0 for _ in range(20)],[0 for _ in range(20)],[0 for _ in range(20)]
    partidosjugadosfase1,ganadosfase1,empatadosfase1,perdidosfase1,puntosfase1,golesfavorfase1,golescontrafase1,diferenciagolfase1,partidosjugadosfase2,ganadosfase2,empatadosfase2,perdidosfase2,puntosfase2,golesfavorfase2,golescontrafase2,diferenciagolfase2,partidosjugadosfase3,ganadosfase3,empatadosfase3,perdidosfase3,puntosfase3,golesfavorfase3,golescontrafase3,diferenciagolfase3,partidosjugadosfase4,ganadosfase4,empatadosfase4,perdidosfase4,puntosfase4,golesfavorfase4,golescontrafase4,diferenciagolfase4=[0 for _ in range(20)],[0 for _ in range(20)],[0 for _ in range(20)],[0 for _ in range(20)],[0 for _ in range(20)],[0 for _ in range(20)],[0 for _ in range(20)],[0 for _ in range(20)],[0 for _ in range(20)],[0 for _ in range(20)],[0 for _ in range(20)],[0 for _ in range(20)],[0 for _ in range(20)],[0 for _ in range(20)],[0 for _ in range(20)],[0 for _ in range(20)],[0 for _ in range(20)],[0 for _ in range(20)],[0 for _ in range(20)],[0 for _ in range(20)],[0 for _ in range(20)],[0 for _ in range(20)],[0 for _ in range(20)],[0 for _ in range(20)],[0 for _ in range(20)],[0 for _ in range(20)],[0 for _ in range(20)],[0 for _ in range(20)],[0 for _ in range(20)],[0 for _ in range(20)],[0 for _ in range(20)],[0 for _ in range(20)]
    nombresaleatoriosequipos=["Atletico del Sur", "Club Deportivo Aurora", "Racing Federal", "Juventud Unida","Sportivo Central", "Union del Norte", "Estrella Roja", "Los Dragones FC","San Martin Juniors", "Nueva Esperanza", "Club Social Libertad", "Huracan del Valle","Defensores de la Costa", "Talleres Unidos", "Los Guerreros", "Boca del Oeste","River Plateno", "Cruz Azul del Sur", "Leones Dorados", "Aguilas Negras","Real Horizonte", "Deportivo America", "Universitario Central", "Club Atletico Nacional","Fuerza Joven", "Pumas de la Sierra", "Toros Salvajes", "Estudiantes del Sol","Nueva Generacion", "Atletico Popular", "Club Independiente", "San Lorenzo Unido","Deportivo Patria", "Olimpia del Sur", "Cultural Esperanza", "Ciclon Rojo","Guarani Unido", "Leones del Sur", "Academia del Futbol", "Sport Boys","Los Gladiadores", "Union Deportiva Estrella", "Villa Real FC", "Juventud Federal","Defensa y Justicia Social", "Atletico Horizonte", "Deportivo Norteño", "Tigre Blanco","Halcones Verdes", "Nueva Alianza", "San Carlos Juniors", "Atletico Centenario","Los Piratas FC", "Club Deportivo Cosmos", "Juventud Atletica", "Rayo del Sur","Los Titanes", "Sporting Club Federal", "Atletico Ciudadela", "Universitario Unido","Club Social Victoria", "Deportivo Union", "Santa Fe Atletico", "Real Central","Club Atletico Esperanza", "Independencia FC", "Sportivo Olimpo", "Guerreros del Sol","Aguilas Plateadas", "Los Delfines", "Atletico Mundial", "Nueva Roma FC","San Jose Unido", "Estrella Federal", "Juventud Patriota", "Huracan del Centro","Deportivo Internacional", "Granaderos FC", "Racing Unido", "Union Deportiva Norte","Atletico Azul", "Fuerza Guerrera", "Los Lobos", "Club Estudiantes Unidos","Rivera FC", "Boca Sur", "Atletico Colonial", "Deportivo Horizonte","Club Nacional Popular", "Los Condores", "Sporting Nueva Era", "Juventud del Norte","Atletico Moderno", "Los Pioneros", "Real Metropolitano", "Estrella Joven","Deportivo Victoria", "Union San Pedro", "Club del Sol", "Atletico Bravo"]    
    numeraso=(len(equipostorneo))
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
        print("# 10 = tabla de liga")
        print("# 11 = poner resultados partidos liga")
        print("# 12 = cobro torneo o liga")
        print("# 13 = inscripcion torneo")
        print("# 14 = rellenar torneo (demostración)")
        print("# 15 = calcular los partidos del torneo")
        print("# 16 = resultados aleatorios fase de grupos (demostracion)")
        print("# 17 = tablas fase de grupos torneo")  
        print("# 18 = calcular cuartos de final torneo")
        print("# 19 = calcular semifinal torneo")
        print("# 20 = calcular final torneo")
        print("# 21 = camepon final torneo")
        print("# 22 = fase de grupos resultados")
        print("# 23 = cuartos de final resultados")
        print("# 24 = semifinal resultados")
        print("# 25 = final resultados")
        print("# 26 = cuartos de final aleatoria resultados (demostración)")
        print("# 27 = semifinal aleatoria resultados (demostración)")
        print("# 28 = final aleatoria resultados (demostración)")
        print("# 29 = comprar entradas")
        print("# 30 = proceso de archivos y recomendaciones en base a informes estadisticos")
        print("# 31 = dar de baja una cuenta")
        print("# -1 = finalizar programa")
        try:
            herramienta=int(input("Ingrese el numero segun lo que desee: "))
            while herramienta not in[-1,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]:
                print("Error, el numero ingresado no se encuntra en lo indicado")
                herramienta=int(input("Ingrese el numero segun lo que desee(1 reservar canchas, 2 cancelar la reservacion de canchas, 3 calcular cobro, 4 mostrar reportes, -1 para finalizar programa): "))
        except ValueError as msg:
            print(msg)
            continue
        try:
            herraaux=herramienta
            if herraaux==-1:
                funci=tuplasin[len(tuplasin)-1]
            else:
                funci=tuplasin[herramienta-1]
        except IndexError as msj:
            print(msj)
        tiempo=datetime.datetime.now()
        listas.guardar_bitacora(user,funci,tiempo,bitacora)
        if herramienta==1:
            salir10=False
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
                        listas.guardar_matirzpe(matrizper,archivo)
                        listas.guardar_matirznombr(matriznombre,archivo2)
                        string=f"fut{cancha}"
                        if "cualreserva" in estadistica:
                            if string in estadistica["cualreserva"] and string in reservamas:
                                estadistica["cualreserva"][string]+=1
                                reservamas[string]+=1
                        listas.guardar_cualreserva(reservamas,cualreserva)
                        listas.guardar_estadisticas(estadistica,expediente)
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
                    else:
                        print("Ese horario ya esta ocupado")
                        break
                while True:
                    try:
                        señ=int(input("Ingrese cualquier numero entero si desea continuar o -1 para salir: "))
                    except ValueError as mensaje2:
                        print(mensaje2)
                        continue
                    if señ==-1:
                        salir10=True
                        break
                    else:
                        break
                if salir10:                    
                    break        
                                
        elif herramienta==2:
            salir11=False
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
                        listas.guardar_matirzpe(matrizper,archivo)
                        listas.guardar_matirznombr(matriznombre,archivo2)
                        string2=f"fut{cancha2}"
                        if "cualreserva" in estadistica:
                            if string2 in estadistica["cualreserva"] and string2 in reservamas:
                                estadistica["cualreserva"][string2]-=1
                                reservamas[string2]-=1
                        listas.guardar_cualreserva(reservamas,cualreserva)
                        listas.guardar_estadisticas(estadistica,expediente)
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
                    else:
                        print("Ese horario no se encuentra alquilado")
                        break
                while True:
                    try:
                        señ2=int(input("Ingrese cualquier número entero si desea continuar o -1 para salir: "))
                    except ValueError as mensaje5:
                        print(mensaje5)
                        continue
                    if señ2==-1:
                        salir11=True
                        break
                    else:
                        break
                if salir11:                    
                    break   

        elif herramienta==3:
            while True:
                precios,horas,cancha,ingresohora,clientes=funmod.guardar_precio_cantidad_horas(random.randint(35000,45000),random.randint(65000,75000),random.randint(95000,105000),listhorarios)
                cobro=funmod.calcular_cantidad_a_pagar(precios,horas)
                listaclientes.append(clientes)
                if "listaclientes" in reportaje:
                    reportaje["listaclientes"].append(clientes)
                listas.guardar_reportes(reportaje,reportes)
                print("cantidad a pagar: $",cobro)
                cobrofinal=funmod.reporte_metodo_pago(reportes,reportaje,listformpago,listrecaudacionformpago,listcantformpago,cobro,listadiezporciento,cobro)
                funmod.reporte_canchas(reportes,reportaje,listcanchas,listrecaudacioncanchas,listcantcanchas,cobrofinal,cancha)
                funmod.reporte_horarios(reportes,reportaje,listhorarios,listrecaudacionhorarios,listcanthorarios,cobrofinal,ingresohora)
                
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
            listas.guardar_reportes(reportaje,reportes)
        
        
        elif herramienta==5:#inscripcion liga, 
            funmod.inscripciones_a_la_liga(listaequiposliga,stringer3,stringer4,listas.guardar_listaliga,listaliga)
            
        elif herramienta==6:#rellenar liga, en total 20 equipos, 
            for i in range(len(listaequiposliga)):
                if listaequiposliga[i]==0:
                    while True:
                        """agarra de un archivo nombres aleatorios, por ahora agrego una lista"""
                        randonum=nombresaleatoriosequipos[random.randint(0,len(nombresaleatoriosequipos)-1)]
                        viril=listaequiposliga.count(randonum)
                        if viril==0:
                            listaequiposliga[i]=randonum
                            break
                        else:
                            continue
            listas.guardar_listaliga(listaequiposliga,listaliga)
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
                n=len(listaequiposliga)
                listaauxiliarcito=listaequiposliga[:]
                for x in range(n-1):
                    partidos=[]
                    for i in range(n//2):
                        equipo1=listaauxiliarcito[i]
                        equipo2=listaauxiliarcito[n-1-i]
                        partidos.append([equipo1,equipo2])
                    if "fixtureidita" in fixtureida:
                        fixtureida["fixtureidita"].append(partidos)
                    listaauxiliarcito=[listaauxiliarcito[0]]+[listaauxiliarcito[-1]]+listaauxiliarcito[1:-1]
                if "fixtureidita" in fixtureida:
                    for fecha in fixtureida["fixtureidita"]:
                        partidotes=[[b,a] for [a,b] in fecha]
                        fixturevuelta["fixturevueltita"].append(partidotes)
                    
                contadorfecha=1
                contadorfechaaux=1
                if "fixtureidita" in fixtureida and "fixturevueltita" in fixturevuelta:
                    fixturecompletito=fixtureida["fixtureidita"]+fixturevuelta["fixturevueltita"]
                listas.guardar_fixtureidita(fixtureida,fixtureidita)
                listas.guardar_fixturevueltita(fixturevuelta,fixturevueltita)

                
                
                for ronda in fixturecompletito:
                    for local,bebe in ronda:
                        if "fixture" in fixturecompleto:
                            fixturecompleto["fixture"].append([local,bebe])
                            contadorfechaaux+=1
                listas.guardar_partidosdeliga(fixturecompleto,fixture)
                          

                print("Fixture de ida")
                for ronda in fixtureida["fixtureidita"]:
                    print(f"partido:{contadorfecha}")
                    for partidito in ronda:
                        local=partidito[0]
                        visitante=partidito[1]
                        print(f"{local} vs {visitante}")
                    contadorfecha+=1
                contadorfechavuelta=1
                print("Fixture de vuelta")
                for rondavuelta in fixturevuelta["fixturevueltita"]:
                    print(f"partido:{contadorfechavuelta}")
                    for partiditovuelta in rondavuelta:
                        localvuelta=partiditovuelta[0]
                        visitantevuelta=partiditovuelta[1]
                        print(f"{localvuelta} vs {visitantevuelta}")
                    contadorfechavuelta+=1




        
        elif herramienta==8:#inscripcion sponsors PUEDO HACER UNA FUNCION PORQUE ES EL SPONSORSLIGA Y SPONSORSTORNEO TIENEN LA MISMA MANERA DE INSCRIBIRSE
            salidita=False
            while True:
                    funmod.hacer_sponsors(usosponsors,sponsorcito["disponibilidad"],sponsorcito["listasponsorszona"],sponsorcito["listasponsors"],sponsorcito["listadisponibilidad"],sponsorcito["listanombresponsor"],sponsorcito,estadistica)
                    listas.guardar_sponsorsuso(usosponsors,sponsorsuso)
                    listas.guardar_estadisticas(estadistica,expediente)
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
            funmod.resultados_aleatorios_liga(resultadosida,ligaderesultados,"resultadosidita",listas.guardar_resultadosidita,resultadosidita,liguita)
            funmod.resultados_aleatorios_liga(resultadosvuelta,ligaderesultados,"resultadosvueltita",listas.guardar_resultadosvueltita,resultadosvueltita,liguita)
            fixtureidasss=[p for ronda in fixtureida["fixtureidita"] for p in ronda]
            listadopartidos=list(zip(fixtureidasss,resultadosida["resultadosidita"]))
            print("Resultados partidos de ida")
            for fix,resultaditos in listadopartidos:
                local,visitante=fix
                gollocal,golvisita=resultaditos
                print(f"partido:\t{local}:{gollocal} vs {golvisita}:{visitante}")
            print()
            fixturevueltasss=[p for ronda in fixturevuelta["fixturevueltita"] for p in ronda]
            listadopartidosvuelta=list(zip(fixturevueltasss,resultadosvuelta["resultadosvueltita"]))
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
            funmod.calcular_tabla(fixturecompleto["fixture"],listaauxiliarliga,partidosjugados,ligaderesultados["liga"],ganados,puntos,perdidos,empatados,golesfavor,golescontra,diferenciagol)
            """funmod.calcular_tabla(fixtureida,listaauxiliarliga,partidosjugados,resultadosida,ganados,puntos,perdidos,empatados,golesfavor,golescontra,diferenciagol)
            funmod.calcular_tabla(fixturevuelta,listaauxiliarliga,partidosjugados,resultadosvuelta,ganados,puntos,perdidos,empatados,golesfavor,golescontra,diferenciagol)"""


            liga=list(zip(listaauxiliarliga,partidosjugados,ganados,perdidos,empatados,puntos,golesfavor,golescontra,diferenciagol))
            liga.sort(key=lambda x:x[5],reverse=True)
            print(nombredelaliga.center(180))
            print(f"{'Equipos':<20}{'Partidos jugados':<20}{'Ganados':<20}{'Perdidos':<20}{'Empatados':<20}{'Puntos':<20}{'Goles a favor':<20}{'Goles en contra':<20}{'Diferencia de gol':<20}")
            try:
                for equipo,pj,g,e,p,pts,gf,gc,dg in liga:
                    print(f"{equipo:<20}{pj:<20}{g:<20}{e:<20}{p:<20}{pts:<20}{gf:<20}{gc:<20}{dg:<20}")
                print(f"CAMPEON DE LA SUPER LIGA NACIONAL: \t {liga[0][0]} \t con un premio de $30400000")
            except IndexError as men7:
                print(men7)
            tablaliga=(nombredelaliga.center(180))+"\n"
            tablaliga+=(f"{'Equipos':<20}{'Partidos jugados':<20}{'Ganados':<20}{'Empatados':<20}{'Perdidos':<20}{'Puntos':<20}{'Goles a favor':<20}{'Goles en contra':<20}{'Diferencia de gol':<20}\n")
            
            try:
                for equipo,pj,g,e,p,pts,gf,gc,dg in liga:
                    tablaliga+=(f"{equipo:<20}{pj:<20}{g:<20}{e:<20}{p:<20}{pts:<20}{gf:<20}{gc:<20}{dg:<20}\n")
                tablaliga+=(f"\nCAMPEON DE LA SUPER LIGA NACIONAL: \t {liga[0][0]} \t con un premio de $30400000\n")
            except IndexError as men7:
                print(men7)
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
                    guardarcsv.write("Equipos"+","+"Partidos jugados"+","+"Ganados"+","+"Empatados"+","+"Perdidos"+","+"Puntos"+","+"Goles a favor"+","+"Goles en contra"+","+"Diferencia de gol"+"\n")
                    for fila in liga:
                        for dato in fila:   
                            guardarcsv.write(str(dato)+",")
                        guardarcsv.write("\n")
                    guardarcsv.write(f"campeon: {liga[0][0]}"+"\n")
            except IOError as men4:
                print(men4)
            except PermissionError as men5:
                print(men5)
            except FileNotFoundError as men6:
                print(men6)
            except IndexError as men7:
                print(men7)
#hay que subirlo a un archivo que va a contener las ligas tras años, premio = $30400000

#hay que poner if Len(resultados[i])<2:
#.... Todo lo de resultados aleatorios
        
        elif herramienta==11:#resultados partidos
            funmod.resultados_liga(fixtureida,resultadosida,listaauxiliarliga,ligaderesultados,fixturevuelta,resultadosvuelta,resultadosidita)

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
                    valor=funmod.ingresa_con_rango(0,100,"porcentaje de lo recaudado que va para el premio")
                    print("Ganancia total recaudado por el torneo: $",(1000000*16)*(100-valor)//100)
                    print("Premio del campeón del torneo: $",(1000000*16)*valor//100)
                    funmod.reporte_torneo(reportes,reportaje,recaudacionestorneo,valor)
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
                            valor2=funmod.ingresa_con_rango(0,100,"porcentaje de lo recaudado que va para el premio")
                            print("Ganancia total recaudado por la liga: $",((80000*20*38)*(100-valor2)//100))
                            print("Premio del campeón de liga: $",((80000*20*38)*valor2//100))
                            funmod.reporte_liga(reportes,reportaje,recaudacionesliga,valor2)
                            salida10=True
                            break
                    if salida10:
                        break

            #actualizar reportes de liga y torneo, poner torneo
        
        elif herramienta==13:#inscripcion torneo, 
            funmod.inscripciones_a_la_liga(listaequipostorneo,stringer,stringer2,listas.guardar_listatorneo,listatorneo)
            
                




        elif herramienta==14:#rellenar torneo, en total 16 equipos, 
            for i in range(len(listaequipostorneo)):
                if listaequipostorneo[i]==0:
                    while True:
                        """agarra de un archivo nombres aleatorios, por ahora agrego una lista"""
                        randonum=nombresaleatoriosequipos[random.randint(0,len(nombresaleatoriosequipos)-1)]
                        viril=listaequiposliga.count(randonum)
                        if viril==0:
                            listaequiposliga[i]=randonum
                            break
                        else:
                            continue
            listas.guardar_listatorneo(listaequipostorneo,listatorneo)
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
                
                fasegrupos1=listaequipostorneoaux[0:4]
                fasegrupos2=listaequipostorneoaux[4:8]
                fasegrupos3=listaequipostorneoaux[8:12]
                fasegrupos4=listaequipostorneoaux[12:16]
                listas.guardar_torneooficial(fasegrupos1,torneooficial)
                listas.guardar_torneooficial2(fasegrupos2,torneooficial2)
                listas.guardar_torneooficial3(fasegrupos3,torneooficial3)
                listas.guardar_torneooficial4(fasegrupos4,torneooficial4)
                division1=equipostorneo[0:4]
                division2=equipostorneo[4:8]
                division3=equipostorneo[8:12]
                division4=equipostorneo[12:16]
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
                    fixturetorneos["fixturefasegrupos1"].append([local,visitante])
                for local,visitante in fasegrupo2partidos:
                    fixturetorneos["fixturefasegrupos2"].append([local,visitante])
                for local,visitante in fasegrupo3partidos:
                    fixturetorneos["fixturefasegrupos3"].append([local,visitante])
                for local,visitante in fasegrupo4partidos:
                    fixturetorneos["fixturefasegrupos4"].append([local,visitante])
                listas.guardar_partidosdetorneo(fixturetorneos,fixturetorneo)

        elif herramienta==16:#calcular cuartos de final
            
            funmod.resultados_aleatorios_fasegrupos(fasegrupos1resultados,fixturetorneos["fixturefasegrupos1"])
            funmod.resultados_aleatorios_fasegrupos(fasegrupos2resultados,fixturetorneos["fixturefasegrupos2"])
            funmod.resultados_aleatorios_fasegrupos(fasegrupos3resultados,fixturetorneos["fixturefasegrupos3"])
            funmod.resultados_aleatorios_fasegrupos(fasegrupos4resultados,fixturetorneos["fixturefasegrupos4"])
                         
            for resu1,resu2 in fasegrupos1resultados:
                resultaditosgeneral["fasegrupos1"].append([resu1,resu2])  
            for resu1,resu2 in fasegrupos2resultados:   
                resultaditosgeneral["fasegrupos2"].append([resu1,resu2])
            for resu1,resu2 in fasegrupos3resultados:
                resultaditosgeneral["fasegrupos3"].append([resu1,resu2])
            for resu1,resu2 in fasegrupos4resultados:
                resultaditosgeneral["fasegrupos4"].append([resu1,resu2])
            listas.guardar_torneo(resultaditosgeneral)
            listadopartidosfase1=list(zip(fixturetorneos["fixturefasegrupos1"],fasegrupos1resultados))
            print("Resultados partidos fase 1")
            contador=1
            for fixe,resultadito in listadopartidosfase1:
                eq1,eq2=fixe
                g1,g2=resultadito
                print(f"partido {contador}: {eq1} {g1} vs {g2} {eq2}")
                contador+=1
            print()
            listadopartidosfase2=list(zip(fixturetorneos["fixturefasegrupos2"],fasegrupos2resultados))
            print("Resultados partidos fase 2")
            contador2=1
            for fixe2,resultadito2 in listadopartidosfase2:
                eq1,eq2=fixe2
                g1,g2=resultadito2
                print(f"partido {contador2}: {eq1} {g1} vs {g2} {eq2}")
                contador2+=1
            print()
            listadopartidosfase3=list(zip(fixturetorneos["fixturefasegrupos3"],fasegrupos3resultados))
            print("Resultados partidos fase 3")
            contador3=1
            for fixe3,resultadito3 in listadopartidosfase3:
                eq1,eq2=fixe3
                g1,g2=resultadito3
                print(f"partido {contador3}: {eq1} {g1} vs {g2} {eq2}")
                contador3+=1
            print()
            listadopartidosfase4=list(zip(fixturetorneos["fixturefasegrupos4"],fasegrupos4resultados))
            print("Resultados partidos fase 4")
            contador4=1
            for fixe4,resultadito4 in listadopartidosfase4:
                eq1,eq2=fixe4
                g1,g2=resultadito4
                print(f"partido {contador4}: {eq1} {g1} vs {g2} {eq2}")
                contador4+=1
            print()

        elif herramienta==17:#tablas fase grupos del torneo
            funmod.calcular_tabla(fixturetorneos["fixturefasegrupos1"],equipostorneo,partidosjugadosfase1,resultaditosgeneral["fasegrupos1"],ganadosfase1,puntosfase1,perdidosfase1,empatadosfase1,golesfavorfase1,golescontrafase1,diferenciagolfase1)
            fase1=list(zip(equipostorneo,partidosjugadosfase1,ganadosfase1,perdidosfase1,empatadosfase1,puntosfase1,golesfavorfase1,golescontrafase1,diferenciagolfase1))
            fase1.sort(key=lambda x:x[5],reverse=True)
            print(nombredeltorneo.center(180))
            print(f"{'Equipos':<20}{'Partidos jugados':<20}{'Ganados':<20}{'Perdidos':<20}{'Empatados':<20}{'Puntos':<20}{'Goles a favor':<20}{'Goles en contra':<20}{'Diferencia de gol':<20}")
            for equipo,pj,g,e,p,pts,gf,gc,dg in fase1:
                print(f"{equipo:<20}{pj:<20}{g:<20}{e:<20}{p:<20}{pts:<20}{gf:<20}{gc:<20}{dg:<20}")
            print()
            print(f"PASAN A LA SIGUIENTE FASE: \t {fase1[0][0]} \t y \t  {fase1[1][0]} ")
            
            funmod.calcular_tabla(fixturetorneos["fixturefasegrupos2"],equipostorneo,partidosjugadosfase2,resultaditosgeneral["fasegrupos2"],ganadosfase2,puntosfase2,perdidosfase2,empatadosfase2,golesfavorfase2,golescontrafase2,diferenciagolfase2)
        
            fase2=list(zip(equipostorneo,partidosjugadosfase2,ganadosfase2,empatadosfase2,perdidosfase2,puntosfase2,golesfavorfase2,golescontrafase2,diferenciagolfase2))
            fase2.sort(key=lambda x: x[5], reverse=True)
            print(nombredeltorneo.center(180))
            print(f"{'Equipos':<20}{'Partidos jugados':<20}{'Ganados':<20}{'Empatados':<20}{'Perdidos':<20}{'Puntos':<20}{'Goles a favor':<20}{'Goles en contra':<20}{'Diferencia de gol':<20}")
            for equipo,pj,g,e,p,pts,gf,gc,dg in fase2:
                print(f"{equipo:<20}{pj:<20}{g:<20}{e:<20}{p:<20}{pts:<20}{gf:<20}{gc:<20}{dg:<20}")
            print()
            print(f"PASAN A LA SIGUIENTE FASE: \t {fase2[0][0]} \t y \t  {fase2[1][0]} ")

            funmod.calcular_tabla(fixturetorneos["fixturefasegrupos3"],equipostorneo,partidosjugadosfase3,resultaditosgeneral["fasegrupos3"],ganadosfase3,puntosfase3,perdidosfase3,empatadosfase3,golesfavorfase3,golescontrafase3,diferenciagolfase3)
        
            fase3=list(zip(equipostorneo,partidosjugadosfase3,ganadosfase3,empatadosfase3,perdidosfase3,puntosfase3,golesfavorfase3,golescontrafase3,diferenciagolfase3))
            fase3.sort(key=lambda x: x[5], reverse=True)
            print(nombredeltorneo.center(180))
            print(f"{'Equipos':<20}{'Partidos jugados':<20}{'Ganados':<20}{'Empatados':<20}{'Perdidos':<20}{'Puntos':<20}{'Goles a favor':<20}{'Goles en contra':<20}{'Diferencia de gol':<20}")
            for equipo,pj,g,e,p,pts,gf,gc,dg in fase3:
                print(f"{equipo:<20}{pj:<20}{g:<20}{e:<20}{p:<20}{pts:<20}{gf:<20}{gc:<20}{dg:<20}")
            print()
            print(f"PASAN A LA SIGUIENTE FASE: \t {fase3[0][0]} \t y \t  {fase3[1][0]} ")

            funmod.calcular_tabla(fixturetorneos["fixturefasegrupos4"],equipostorneo,partidosjugadosfase4,resultaditosgeneral["fasegrupos4"],ganadosfase4,puntosfase4,perdidosfase4,empatadosfase4,golesfavorfase4,golescontrafase4,diferenciagolfase4)
        
            
            fase4=list(zip(equipostorneo,partidosjugadosfase4,ganadosfase4,empatadosfase4,perdidosfase4,puntosfase4,golesfavorfase4,golescontrafase4,diferenciagolfase4))
            fase4.sort(key=lambda x: x[5], reverse=True)
            print(nombredeltorneo.center(180))
            print(f"{'Equipos':<20}{'Partidos jugados':<20}{'Ganados':<20}{'Empatados':<20}{'Perdidos':<20}{'Puntos':<20}{'Goles a favor':<20}{'Goles en contra':<20}{'Diferencia de gol':<20}")
            for equipo,pj,g,e,p,pts,gf,gc,dg in fase4:
                print(f"{equipo:<20}{pj:<20}{g:<20}{e:<20}{p:<20}{pts:<20}{gf:<20}{gc:<20}{dg:<20}")
            print()
            print(f"PASAN A LA SIGUIENTE FASE: \t {fase4[0][0]} \t y \t  {fase4[1][0]} ")




        elif herramienta==18:#calcular cuartos
            megacontador=0
            for i in range(len(resultaditosgeneral["fasegrupos1"])):
                if len(resultaditosgeneral["fasegrupos1"][i])<2:
                    megacontador+=1
            for i in range(len(resultaditosgeneral["fasegrupos2"])):
                if len(resultaditosgeneral["fasegrupos2"][i])<2:
                    megacontador+=1
            for i in range(len(resultaditosgeneral["fasegrupos3"])):
                if len(resultaditosgeneral["fasegrupos3"][i])<2:
                    megacontador+=1
            for i in range(len(resultaditosgeneral["fasegrupos4"])):
                if len(resultaditosgeneral["fasegrupos4"][i])<2:
                    megacontador+=1

            if megacontador>0:
                print("faltan partidos por jugar")
            else:
                funmod.calcular_tabla(fixturetorneos["fixturefasegrupos1"],equipostorneo,partidosjugadosfase1,resultaditosgeneral["fasegrupos1"],ganadosfase1,puntosfase1,perdidosfase1,empatadosfase1,golesfavorfase1,golescontrafase1,diferenciagolfase1)
                fase1=list(zip(equipostorneo,partidosjugadosfase1,ganadosfase1,perdidosfase1,empatadosfase1,puntosfase1,golesfavorfase1,golescontrafase1,diferenciagolfase1))
                fase1.sort(key=lambda x:x[5],reverse=True)
                funmod.calcular_tabla(fixturetorneos["fixturefasegrupos2"],equipostorneo,partidosjugadosfase2,resultaditosgeneral["fasegrupos2"],ganadosfase2,puntosfase2,perdidosfase2,empatadosfase2,golesfavorfase2,golescontrafase2,diferenciagolfase2)
                fase2=list(zip(equipostorneo,partidosjugadosfase2,ganadosfase2,empatadosfase2,perdidosfase2,puntosfase2,golesfavorfase2,golescontrafase2,diferenciagolfase2))
                fase2.sort(key=lambda x: x[5], reverse=True)
                funmod.calcular_tabla(fixturetorneos["fixturefasegrupos3"],equipostorneo,partidosjugadosfase3,resultaditosgeneral["fasegrupos3"],ganadosfase3,puntosfase3,perdidosfase3,empatadosfase3,golesfavorfase3,golescontrafase3,diferenciagolfase3)
                fase3=list(zip(equipostorneo,partidosjugadosfase3,ganadosfase3,empatadosfase3,perdidosfase3,puntosfase3,golesfavorfase3,golescontrafase3,diferenciagolfase3))
                fase3.sort(key=lambda x: x[5], reverse=True)
                funmod.calcular_tabla(fixturetorneos["fixturefasegrupos4"],equipostorneo,partidosjugadosfase4,resultaditosgeneral["fasegrupos4"],ganadosfase4,puntosfase4,perdidosfase4,empatadosfase4,golesfavorfase4,golescontrafase4,diferenciagolfase4)
                fase4=list(zip(equipostorneo,partidosjugadosfase4,ganadosfase4,empatadosfase4,perdidosfase4,puntosfase4,golesfavorfase4,golescontrafase4,diferenciagolfase4))
                fase4.sort(key=lambda x: x[5], reverse=True)

                for i in range((numeraso//2//2//2)):
                    ereq1=fase1[i][0]
                    doeq2=fase2[i][0]
                    ereq3=fase3[i][0]
                    toeq4=fase4[i][0]
                    cuartos.append([ereq1,ereq3])
                    cuartos.append([doeq2,toeq4])
                    
                for local,visitante in cuartos:
                    fixturetorneos["fixturecuartos"].append([local,visitante])
                listas.guardar_partidosdetorneo(fixturetorneos,fixturetorneo)

        elif herramienta==19:#calcular semifinal
            megacontador2=0
            for i in range(len(resultaditosgeneral["cuartos"])):
                if len(resultaditosgeneral["cuartos"][i])<2:
                    megacontador2+=1
                if resultaditosgeneral["cuartos"][i][0]>resultaditosgeneral["cuartos"][i][1]:
                    ganador=fixturetorneos["fixturecuartos"][i][0]
                    ganadorescuartos.append(ganador)
                elif resultaditosgeneral["cuartos"][i][0]<resultaditosgeneral["cuartos"][i][1]:
                    ganador=fixturetorneos["fixturecuartos"][i][1]
                    ganadorescuartos.append(ganador)
                else:
                    ganador=fixturetorneos["fixturecuartos"][i][random.randint(0,1)]
                    ganadorescuartos.append(ganador)
            if megacontador2>0:
                print("faltan partidos por jugar")
            else:
                for i in range((numeraso//2//2//2//2)):
                    ereqcuartos1=ganadorescuartos[i]
                    doeqcuartos2=ganadorescuartos[i+1]
                    ereqcuartos3=ganadorescuartos[i+2]
                    toeqcuartos4=ganadorescuartos[i+3]
                    semis.append([ereqcuartos1,ereqcuartos3])
                    semis.append([doeqcuartos2,toeqcuartos4])
                    semisaux=semis[::1]
                for local,visitante in semisaux:
                    fixturetorneos["fixturesemis"].append([local,visitante])
                listas.guardar_partidosdetorneo(fixturetorneos,fixturetorneo)

        elif herramienta==20:#calcular final
            megacontador3=0
            for i in range(len(resultaditosgeneral["semis"])):
                if len(resultaditosgeneral["semis"][i])<2:
                    megacontador3+=1
                if resultaditosgeneral["semis"][i][0]>resultaditosgeneral["semis"][i][1]:
                    ganadorsemis=fixturetorneos["fixturesemis"][i][0]
                    ganadoressemis.append(ganadorsemis)
                    finalaux=final[::1]
                elif resultaditosgeneral["semis"][i][0]<resultaditosgeneral["semis"][i][1]:
                    ganadorsemis=fixturetorneos["fixturesemis"][i][1]
                    ganadoressemis.append(ganadorsemis)
                    finalaux=final[::1]
                else:
                    ganadorsemis=fixturetorneos["fixturesemis"][i][random.randint(0,1)]
                    ganadoressemis.append(ganadorsemis)
                    finalaux=final[::1]
            if megacontador3>0:
                print("faltan partidos por jugar")
            else:
                for i in range((numeraso//2//2//2//2)):
                    ereqfinal1=ganadoressemis[i]
                    doeqfinal2=ganadoressemis[i+1]
                    final.append([ereqfinal1,doeqfinal2])
                    for local,visitante in final:
                        fixturetorneos["fixturefinal"].append([local,visitante])
                    listas.guardar_partidosdetorneo(fixturetorneos,fixturetorneo)
        elif herramienta==21:#campeon final torneo
            megacontador4=0
            for i in range(len(resultaditosgeneral["final"])):
                if len(resultaditosgeneral["final"][i])<2:
                    megacontador4+=1
                if resultaditosgeneral["final"][i][0]>resultaditosgeneral["final"][i][1]:
                    ganadorfinal=fixturetorneos["fixturefinal"][i][0]
                    campeontorneo.append(ganadorfinal)
                elif resultaditosgeneral["final"][i][0]<resultaditosgeneral["final"][i][1]:
                    ganadorfinal=fixturetorneos["fixturefinal"][i][1]
                    campeontorneo.append(ganadorfinal)
                else:
                    ganadorfinal=fixturetorneos["fixturefinal"][i][random.randint(0,1)]
                    campeontorneo.append(ganadorfinal)
            if megacontador4>0:
                print("faltan partidos por jugar")
            else:
                for i in range((numeraso//2//2//2//2)):
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
                    funmod.fasegrupos_ponerresultados(fasegrupos1aux,fasegrupos1resultados,resultaditosgeneral,"fasegrupos1",torneito)
                    
                elif zona==2:
                    funmod.fasegrupos_ponerresultados(fasegrupos2aux,fasegrupos2resultados,resultaditosgeneral,"fasegrupos2",torneito)

                elif zona==3:
                    funmod.fasegrupos_ponerresultados(fasegrupos3aux,fasegrupos3resultados,resultaditosgeneral,"fasegrupos3",torneito)

                elif zona==4:
                    funmod.fasegrupos_ponerresultados(fasegrupos4aux,fasegrupos4resultados,resultaditosgeneral,"fasegrupos4",torneito)
                
                else:
                    break

            #falta hacer mostrar tabla de liga
#falta sumar listas de resultados
#SE PUEDE PONER LOS TRES DE ABAJO EN UNA FUNCION
        elif herramienta==23:   #poner cuartos manual
            cuartos=fixturetorneos["fixturecuartos"]
            funmod.ingresar_manual_partidos(cuartos,cuartosresultados,resultaditosgeneral,"cuartos")
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
            semis=fixturetorneos["fixturesemis"]
            funmod.ingresar_manual_partidos(semis,semisresultados,resultaditosgeneral,"semis")

            
        #EL MISMO QUE EL DE ARRIBA FUNCIONA
        elif herramienta==25:   #poner final manual
            final=fixturetorneos["fixturefinal"]
            funmod.ingresar_manual_partidos(final,finalresultados,resultaditosgeneral,"final")

            
            #PONERLO EN UNA FINCION FUNMOD
            """elif herramienta==26:   #fases de grupo aleatorias
            funmod.ingreso_aleatorio_partidos(fasegrupos1aux,fasegrupos1resultados,resultaditosgeneral,"fasegrupos1")
            funmod.ingreso_aleatorio_partidos(fasegrupos2aux,fasegrupos2resultados,resultaditosgeneral,"fasegrupos2")
            funmod.ingreso_aleatorio_partidos(fasegrupos3aux,fasegrupos3resultados,resultaditosgeneral,"fasegrupos3")
            funmod.ingreso_aleatorio_partidos(fasegrupos4aux,fasegrupos4resultados,resultaditosgeneral,"fasegrupos4")

            for r in range(len(fasegrupos1aux)):
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
                    listas.guardar_torneo(resultaditosgeneral)

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
                print(f"{fix[0]} {res[0][0]} vs {res[0][1]} {fix[1]}")"""

        elif herramienta==26:   #cuartos aleatorio
            cuartos=fixturetorneos["fixturecuartos"]
            funmod.ingreso_aleatorio_partidos(cuartos,cuartosresultados,resultaditosgeneral,"cuartos",torneito)
            cuartosresultados=resultaditosgeneral["cuartos"]
            
            """for r in range(len(cuartosaux)):
                if len(cuartosresultados[r])<2:
                    golcitoscuartos1=random.randint(0,15)
                    golcitoscuartos2=random.randint(0,15)
                    cuartosresultados[r].append([golcitoscuartos1,golcitoscuartos2])
                    resultaditosgeneral["cuartos"].append([golcitoscuartos1,golcitoscuartos2])
                    listas.guardar_torneo(resultaditosgeneral)"""

            print("RESULTADOS CUARTOS DE FINAL")
            abiertocuartos=list(zip(cuartos,cuartosresultados))
            for fix,res in abiertocuartos:
                print(f"{fix[0]} {res[0]} vs {res[1]} {fix[1]}")

        elif herramienta==27:   #semis aleatorio
            semis=fixturetorneos["fixturesemis"]
            funmod.ingreso_aleatorio_partidos(semis,semisresultados,resultaditosgeneral,"semis",torneito)
            semisresultados=resultaditosgeneral["semis"]
            """for r in range(len(semisaux)):
                if len(semisresultados[r])<2:
                    golcitossemis1=random.randint(0,15)
                    golcitossemis2=random.randint(0,15)
                    semisresultados[r].append([golcitossemis1,golcitossemis2])
                    resultaditosgeneral["semis"].append([golcitossemis1,golcitossemis2])
                    listas.guardar_torneo(resultaditosgeneral)"""

            print("RESULTADOS SEMIFINALES")
            abiertosemis=list(zip(semis,semisresultados))
            for fix,res in abiertosemis:
                print(f"{fix[0]} {res[0]} vs {res[1]} {fix[1]}")

        elif herramienta==28:   #final aleatorio
            final=fixturetorneos["fixturefinal"]
            funmod.ingreso_aleatorio_partidos(final,finalresultados,resultaditosgeneral,"final",torneito)
            finalresultados=resultaditosgeneral["final"]
            
            """for r in range(len(finalaux)):
                if len(finalresultados[r])<2:
                    golcitosfinal1=random.randint(0,15)
                    golcitosfinal2=random.randint(0,15)
                    finalresultados[r].append([golcitosfinal1,golcitosfinal2])
                    resultaditosgeneral["final"].append([golcitosfinal1,golcitosfinal2])
                    listas.guardar_torneo(resultaditosgeneral)"""

            print("RESULTADO FINAL")
            abiertofinal=list(zip(final,finalresultados))
            for fix,res in abiertofinal:
                print(f"{fix[0]} {res[0]} vs {res[1]} {fix[1]}")

        



        elif herramienta==29:
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
                        elif entraditas==3:
                            decercion="popular"
                        else:
                            break
                        cantidad=int(input("ingrese la cantidad de entradas que desea"))
                    except ValueError as mensajito:
                        print(mensajito)
                        continue
                    funmod.mostrar_disponibles(entradas,disponible,ocupadas)
                    funmod.alquilar(decercion,cantidad,ocupadas,entradas)
                    listas.guardar_entradas(entradas,entradonas)
                    funmod.cobrar_entradas(entradasvendi,decercion,cantidad,entradas,estadistica,pagoentrada)
                    funmod.mostrar_disponibles(entradas,disponible,ocupadas)
                    if "cualvendemas" in estadistica:
                        if "entradasliga" in estadistica["cualvendemas"]:
                            estadistica["cualvendemas"]["entradasliga"]+=cantidad
                    if "entradasliga" in vendemas:
                        vendemas["entradasliga"]+=cantidad
                    listas.guardar_entradasvendidas(entradasvendi,entradasvendidas)
                    listas.guardar_cualvendemas(vendemas,cualvendemas)
                    listas.guardar_estadisticas(estadistica,expediente)
                    listas.guardar_reportes(reportaje,reportes)
                    break
                elif numero==2:
                    try:
                        print(entradastorneo)
                        entraditas=int(input("ingrese 1 si desea alquilar vip, 2 para platea, 3 para popular o -1 para salir: "))
                        while entraditas not in[-1,1,2,3]:
                            print("error, el valor ingresado se encuentra fuera del rango")
                            entraditas=int(input("ingrese 1 si desea alquilar vip, 2 para platea, 3 para popular o -1 para salir: "))
                        if entraditas==1:
                            decercion="vip"
                        elif entraditas==2:
                            decercion="platea"
                        elif entraditas==3:
                            decercion="popular"
                        else:
                            break
                        cantidad=int(input("ingrese la cantidad de entradas que desea"))
                    except ValueError as mensajito:
                        print(mensajito)
                        continue
                    funmod.mostrar_disponiblestorneo(entradastorneo,disponibletorneo,ocupadastorneo)
                    funmod.alquilartorneo(decercion,cantidad,ocupadastorneo,entradastorneo)
                    listas.guardar_entradastorneo(entradastorneo,entradonas2)
                    funmod.cobrar_entradas(entradasvendi,decercion,cantidad,entradastorneo,estadistica,pagoentrada)
                    funmod.mostrar_disponiblestorneo(entradastorneo,disponibletorneo,ocupadastorneo)
                    if "cualvendemas" in estadistica:
                        if "entradastorneo" in estadistica["cualvendemas"]:
                            estadistica["cualvendemas"]["entradastorneo"]+=cantidad
                    if "entradastorneo" in vendemas:
                        vendemas["entradastorneo"]+=cantidad
                    listas.guardar_entradasvendidas(entradasvendi,entradasvendidas)
                    listas.guardar_cualvendemas(vendemas,cualvendemas)
                    listas.guardar_estadisticas(estadistica,expediente)
                    listas.guardar_reportes(reportaje,reportes)
                    break
                else:
                    break
        elif herramienta==30:
            funmod.recomendaciones(estadistica)

        elif herramienta==31:
            salirdel=False
            while True:
                daraltacuenta=input("ingrese el usuario que desea dar de alta") 
                while True:
                    try:
                        confir=int(input("ingrese 0 para confirmar, 1 para ingresar el nombre devuelta, -1 para salir"))
                        while confir not in[-1,0,1]:
                            print("error, valor ingresado fuera de rango")
                            confir=int(input("ingrese 0 para confirmar, 1 para ingresar el nombre devuelta, -1 para salir"))
                    except ValueError as msj:
                        print(msj)
                        continue
                    if confir==0:
                        nitro=listas.cargar_usuarios(comprobacionusuario)
                        if daraltacuenta in nitro:
                            del nitro[daraltacuenta]
                        listas.guardar_usuarios(comprobacionusuario,nitro)
                        break
                    elif confir==1:
                        break
                    else:
                        salirdel=True
                        break
                if salirdel:
                    break

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

