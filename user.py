import listas
import funmod
import datetime
def user(user):
    cualvendemas,entradasvendidas,fixturevueltita,fixtureidita,resultadosvueltita,resultadosidita,expediente,entradonas2,entradonas,sponsors,fixturetorneo,fixture,liguita,torneito,torneooficial4,torneooficial3,listatorneo,listaliga,torneooficial,torneooficial2,reportes,cualreserva,sponsorsuso,bitacora,archivo,archivo2=listas.cargar_rutas_archivos()
    reportaje=listas.cargar_reportes(reportes)
    pagoentrada=reportaje["pagoentrada"]
    tuplasin=("# 1 = reservar canchas","# 2 = cancelar la reservacion de canchas","# 3 = inscripción liga","# 4 = calcular partidos de liga (mostrarlos)","# 5 = inscripcion sponsors","# 6 = tabla de liga","# 7 = inscripción torneo","# 8 = ver torneo","# 9 = comprar entradas","# -1 = finalizar programa")
    disponible,ocupadas,disponibletorneo,ocupadastorneo=listas.cargar_entradasdelisto()
    vendemas=listas.cargar_cualvendemas(cualvendemas)
    reservamas=listas.cargar_cualreserva(cualreserva)
    usosponsors=listas.cargar_sponsorsuso(sponsorsuso)
    entradasvendi=listas.cargar_entradasvendidas(entradasvendidas)
    stringer="bienvenido a inscripcion en el Torneo Nacional"
    stringer2="lista de equipos (16 cupos)"
    stringer3="bienvenido a inscripcion en la Super Liga Nacional"
    stringer4="lista de equipos (20 cupos)"
    entradastorneo=listas.cargar_entradastorneo(entradonas2)
    entradas=listas.cargar_entradas(entradonas)
    estadistica=listas.cargar_estadisticas(expediente)
    sponsorcito=listas.cargar_sponsors(sponsors)
    matrizper=listas.cargar_matrizpe(archivo)
    matriznombre=listas.cargar_matriznombr(archivo2)
    blinger=listas.cargar_partidosdetorneo(fixturetorneo)
    bling=listas.cargar_torneo(torneito)
    fixtureliga=listas.cargar_partidosdeliga(fixture)
    listaequiposliga=listas.cargar_listaliga(listaliga)
    listaequipostorneo=listas.cargar_listatorneo(listatorneo)

    while True:
        print("OPCIONES: ")
        print("# 1 = reservar canchas")
        print("# 2 = cancelar la reservacion de canchas")
        print("# 3 = inscripción liga")
        print("# 4 = calcular partidos de liga (mostrarlos)")
        print("# 5 = inscripcion sponsors")
        print("# 6 = tabla de liga")
        print("# 7 = inscripción torneo")
        print("# 8 = ver torneo")
        print("# 9 = comprar entradas")
        print("# -1 = finalizar programa")
        try:
            herramienta=int(input("Ingrese el numero segun lo que desee: "))
            while herramienta not in[-1,1,2,3,4,5,6,7,8,9]:
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
                try:
                    print(matrizper[fila],"Los horarios que se muestran ya estan tomados")
                except IndexError as msj:
                    print(msj)
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
                    try:
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
                                if string in estadistica["cualreserva"]:
                                    estadistica["cualreserva"][string]+=1
                            if string in reservamas:
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
                        else:
                            print("Ese horario ya esta ocupado")
                    except IndexError as msj2:
                        print(msj2)
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
                try:  
                    print(matrizper[fila2],"Los horarios que se muestran son los que ya estan tomados")
                except IndexError as msj3:
                    print(msj3)
                while True:
                    try:
                        hora2=int(input("Ingrese en formato militar la hora que desea cancelar el alquilar (1200 a 2400, de 100 en 100): "))
                        while hora2<1200 or hora2>2400 or hora2%100!=0:
                            print("La hora ingresada no se encuentra en el rango (1200 a 2400, de 100 en 100)")
                            hora2=int(input("Ingrese en formato militar la hora que desea alquilar (1200 a 2400, de 100 en 100): "))
                    except ValueError as mensaje4:
                        print(mensaje4)
                        continue
                    try:
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
                                if string2 in estadistica["cualreserva"]:
                                    estadistica["cualreserva"][string2]-=1
                            if string2 in reservamas:
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
                        else:
                            print("Ese horario no se encuentra alquilado")
                    except IndexError as msj4:
                        print(msj4)
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

        
        elif herramienta==3:#inscripcion liga, 
            funmod.inscripciones_a_la_liga(listaequiposliga,stringer3,stringer4,listas.guardar_listaliga,listaliga)
            
    

        elif herramienta==4:#calcular los 38 partidos por equipo
            #doble bombo, es decir, se juega dos veces contra el mismo equipo (ida y vuelta). se finge el torneo para ver campeon
            
            if "fixture" in fixtureliga:
                for partido in fixtureliga["fixture"]:
                    local,visitante=partido
                    print(f"partido: {local:15} vs {visitante:<15}")



        elif herramienta==5:#inscripcion sponsors
            salidita=False
            while True:
                    funmod.hacer_sponsors(usosponsors,sponsorcito["disponibilidad"],sponsorcito["listasponsorszona"],sponsorcito["listasponsors"],sponsorcito["listadisponibilidad"],sponsorcito["nombresponsor"],sponsorcito,estadistica,sponsors)
                    listas.guardar_sponsorsuso(usosponsors,sponsorsuso)
                    listas.guardar_estadisticas(estadistica,expediente)
                    break
                
        elif herramienta==6:#tengo que hacer el doble creo
            try:
                with open("tabla_de_liga.csv","rt") as leercsv:
                    for fila in leercsv:
                        celdas=fila.strip().split(";")
                        for celda in celdas:
                            print(celda,end="\t")
                        print()
            except OSError as men:
                print(men)
            


#hay que subirlo a un archivo que va a contener las ligas tras años, premio = $30400000

#hay que poner if Len(resultados[i])<2:
#.... Todo lo de resultados aleatorios

     

        elif herramienta==7:#inscripcion torneo, 
            funmod.inscripciones_a_la_liga(listaequipostorneo,stringer,stringer2,listas.guardar_listatorneo,listatorneo)
            
    
                        #ver torneo mediante archivos, averiguar que son y como se hace para agregarlo
        elif herramienta==8:#ver torneo
            print("Fase de grupos 1")
            for partido in range(len(bling["fasegrupos1"])):
                print(bling["fasegrupos1"][partido],blinger["fixturefasegrupos1"][partido])
            print("Fase de grupos 2")
            for partido2 in range(len(bling["fasegrupos2"])):
                print(bling["fasegrupos2"][partido2],blinger["fixturefasegrupos2"][partido2])
            print("Fase de grupos 3")
            for partido3 in range(len(bling["fasegrupos3"])):
                print(bling["fasegrupos3"][partido3],blinger["fixturefasegrupos3"][partido3])
            print("Fase de grupos 4")
            for partido4 in range(len(bling["fasegrupos4"])):
                print(bling["fasegrupos4"][partido4],blinger["fixturefasegrupos4"][partido4])
            print("Cuartos de final")
            for partido5 in range(len(bling["cuartos"])):
                print(bling["cuartos"][partido5],blinger["fixturecuartos"][partido5])
            print("Semi final")
            for partido6 in range(len(bling["semis"])):
                print(bling["semis"][partido6],blinger["fixturesemis"][partido6])
            print("Final")
            for partido7 in range(len(bling["final"])):
                print(bling["final"][partido7],blinger["fixturefinal"][partido7])

        elif herramienta==9:#comprar entradas
            while True:
                try:
                    numero=int(input("ingresa 1 para liga, 2 para torneo, -1 para salir: "))
                    while numero not in[1,2,-1]:
                        print("error")
                        numero=int(input("ingresa 1 para liga, 2 para torneo, -1 para salir: "))
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
                        cantidad=int(input("ingrese la cantidad de entradas que desea: "))
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
                    listas.guardar_cualvendemas(vendemas,cualvendemas)
                    listas.guardar_estadisticas(estadistica,expediente)
                    listas.guardar_entradasvendidas(entradasvendi,entradasvendidas)
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
                        elif entraditas==3:
                            decercion="popular"
                        else:
                            break
                        cantidad=int(input("ingrese la cantidad de entradas que desea: "))
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
                    listas.guardar_cualvendemas(vendemas,cualvendemas)
                    listas.guardar_estadisticas(estadistica,expediente)
                    listas.guardar_entradasvendidas(entradasvendi,entradasvendidas)
                    break
                else:
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


#ya revise pero se podria revisar devuelta porque hice cambios en el admin
#funciona todo, podriamos revisarlo de vuelta antes de entregarlo. tambien se podria borrar el exceso
