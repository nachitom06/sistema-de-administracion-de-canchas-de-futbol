import listas
import random
import funmod
import csv
def user():
    disponible=listas.disponible
    disponibletorneo=listas.disponibletorneo
    ocupadas=listas.ocupadas
    ocupadastorneo=listas.ocupadastorneo

    fixtureida=listas.cargar_fixturevueltita()
    fixturevuelta=listas.cargar_fixturevueltita()
    resultadosida=listas.cargar_resultadosidita()
    resultadosvuelta=listas.cargar_resultadosvueltita()
    stringer="bienvenido a inscripcion en el Torneo Nacional"
    stringer2="lista de equipos (16 cupos)"
    stringer3="bienvenido a inscripcion en la Super Liga Nacional"
    stringer4="lista de equipos (20 cupos)"
    entradastorneo=listas.cargar_entradastorneo()
    entradas=listas.cargar_entradas()
    estadistica=listas.cargar_estadisticas()
    sponsorcito=listas.cargar_sponsors()
    matrizper,matriznombre=listas.matrizper,listas.matriznombre
    blinger=listas.cargar_partidosdetorneo()
    bling=listas.cargar_torneo()
    fixtureliga=listas.cargar_partidosdeliga()
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
    
    recaudacionesliga=listas.todo["recaudacionesliga"]
    recaudacionestorneo=listas.todo["recaudacionestorne"]
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
    
    contadorpartidosvuelta=listas.todo["contadorpartidosvuelta"]
    nombresaleatoriosequipos=listas.todo["nombresaleatoriosequipos"]
    listasponsorszona=listas.todo["listasponsorszona"]
    listasponsors=listas.todo["listasponsors"]
    disponibilidad=listas.todo["disponibilidad"]
    disponibilidadtorneo=listas.todo["disponibilidadtorneo"]
    listadisponibilidad=listas.todo["listadisponibilidad"]
    listanombresponsor=listas.todo["listanombresponsor"]
    listanombresponsortorneo=listas.todo["listanombresponsortorneo"]
    recaudaciondiezporciento=listas.todo["recaudaciondiezporciento"]
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

        
        elif herramienta==3:#inscripcion liga, 
            funmod.inscripciones_a_la_liga(listaequiposliga,stringer3,stringer4)
            """conteo20=0
            print("bienvenido a inscripcion en la Super Liga Nacional")
            print("lista de equipos (20 cupos)")
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
                                    listas.guardar_listaliga(listaequiposliga)
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
                        break"""
    

        elif herramienta==4:#calcular los 38 partidos por equipo
            #doble bombo, es decir, se juega dos veces contra el mismo equipo (ida y vuelta). se finge el torneo para ver campeon
            """contadorfecha=1
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
                contadorfechavuelta+=1"""
            for partido in fixtureliga["fixture"]:
                numero,local,visitante=partido
                print(f"partido: {numero:<6}{local:15} vs {visitante:<15}")



        
        elif herramienta==5:#inscripcion sponsors
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
                                
       
            

        
        elif herramienta==6:#tengo que hacer el doble creo
            """for l in range(len(fixtureida)):
                jugador1=fixtureida[l][0]
                jugador2=fixtureida[l][1]
                jugado1=listaauxiliarliga.index(jugador1)
                jugado2=listaauxiliarliga.index(jugador2)
                partidosjugados[jugado1]+=1
                partidosjugados[jugado2]+=1
                if resultadosida[l][0]>resultadosida[l][1]:
                    ganados[jugado1]+=1
                    puntos[jugado1]+=3
                    perdidos[jugado2]+=1
                elif resultadosida[l][0]<resultadosida[l][1]:
                    ganados[jugado2]+=1
                    puntos[jugado2]+=3
                    perdidos[jugado1]+=1
                else:
                    empatados[jugado1]+=1
                    puntos[jugado1]+=1
                    empatados[jugado2]+=1
                    puntos[jugado2]+=1

                golesfavor[jugado1]+=resultadosida[l][0]
                golesfavor[jugado2]+=resultadosida[l][1]
                golescontra[jugado1]+=resultadosida[l][1]
                golescontra[jugado2]+=resultadosida[l][0]
                diferenciagol[jugado1]+=golesfavor[jugado1]-golescontra[jugado1]
                diferenciagol[jugado2]+=golesfavor[jugado2]-golescontra[jugado2]
            for l in range(len(fixturevuelta)):
                jugador1vuelta=fixturevuelta[l][0]
                jugador2vuelta=fixturevuelta[l][1]
                jugado1vuelta=listaauxiliarliga.index(jugador1vuelta)
                jugado2vuelta=listaauxiliarliga.index(jugador2vuelta)
                partidosjugados[jugado1vuelta]+=1
                partidosjugados[jugado2vuelta]+=1
                if resultadosvuelta[l][0]>resultadosvuelta[l][1]:
                    ganados[jugado1vuelta]+=1
                    puntos[jugado1vuelta]+=3
                    perdidos[jugado2vuelta]+=1
                elif resultadosvuelta[l][0]<resultadosvuelta[l][1]:
                    ganados[jugado2vuelta]+=1
                    puntos[jugado2vuelta]+=3
                    perdidos[jugado1vuelta]+=1
                else:
                    empatados[jugado1vuelta]+=1
                    puntos[jugado1vuelta]+=1
                    empatados[jugado2vuelta]+=1
                    puntos[jugado2vuelta]+=1

                golesfavor[jugado1vuelta]+=resultadosvuelta[l][0]
                golesfavor[jugado2vuelta]+=resultadosvuelta[l][1]
                golescontra[jugado1vuelta]+=resultadosvuelta[l][1]
                golescontra[jugado2vuelta]+=resultadosvuelta[l][0]
                diferenciagol[jugado1vuelta]+=golesfavor[jugado1vuelta]-golescontra[jugado1vuelta]
                diferenciagol[jugado2vuelta]+=golesfavor[jugado2vuelta]-golescontra[jugado2vuelta]
            liga=list(zip(listaauxiliarliga,partidosjugados,ganados,perdidos,empatados,puntos,golesfavor,golescontra,diferenciagol))
            liga.sort(ley=lambda x:x[5],reverse=True)
            print(nombredelaliga.center(180))
            print(f"{"Equipos":-20}{"Partidos jugados":-20}{"Ganados":-20}{"Empatados":-20}{"Perdidos":-20}{"Puntos":-20}{"Goles a favor":-20}{"Goles en contra":-20}{"Diferencia de gol":-20}")
            for leter in liga:
                print(f"{listaauxiliarliga[leter]:-20}{partidosjugados[leter]:-20}{ganados[leter]:-20}{empatados[leter]:-20}{perdidos[leter]:-20}{puntos[leter]:-20}{golesfavor[leter]:-20}{golescontra[leter]:-20}{diferenciagol[leter]:-20}")

            print(f"CAMPEON DE LA SUPER LIGA NACIONAL: \t {liga[0][0]} \t con un premio de $30400000")"""
            try:
                with open("tabla_de_liga.csv","r",newline="",encoding="utf-8") as leercsv:
                    leer=csv.reader(leercsv)
                    for fila in leer:
                        for celda in fila:
                            print(celda,end="\t")
                        print()
            except IOError as men:
                print(men)
            except PermissionError as men2:
                print(men2)
            except FileNotFoundError as men3:
                print(men3)


#hay que subirlo a un archivo que va a contener las ligas tras años, premio = $30400000

#hay que poner if Len(resultados[i])<2:
#.... Todo lo de resultados aleatorios

     

        elif herramienta==7:#inscripcion torneo, 
            funmod.inscripciones_a_la_liga(listaequipostorneo,stringer,stringer2)
            """conteo30=0
            print("bienvenido a inscripcion en el Torneo Nacional")
            print("lista de equipos (16 cupos)")
            for i in range(len(listaequipostorneo)):
                print(f"equipo:{i+1}\t{listaequipostorneo[i]}")
            for c in range(len(listaequipostorneo)):
                if listaequipostorneo[c]==0:
                    conteo30+=1
            if conteo30!=0:
                    
                while True:
                    nombreequipotorneo=input("ingrese el nombre del equipo que desea inscribir(que no contenga numeros)")
                    while len(nombreequipotorneo.strip())==0 or nombreequipotorneo.isdigit():
                        print("error no ingreso nada o ingreso numeros")
                        nombreequipotorneo=input("ingrese el nombre del equipo que desea inscribir(que no contenga numeros)")
                    print("nombre del equipo:",nombreequipotorneo)
                    while True:
                        try:
                            confirmaciontorneo=int(input("ingrese 0 para confirmar nombre, 1 para cancelar y volver a cargar el nombre, -1 para salir"))
                            while confirmaciontorneo not in[-1,0,1]:
                                print("error, numero fuera de rango")
                                confirmaciontorneo=int(input("ingrese 0 para confirmar nombre, 1 para cancelar y volver a cargar el nombre, -1 para salir"))
                        except ValueError as mensaje17:
                            print(mensaje17)
                            continue
                        if confirmaciontorneo==1:
                            break
                        elif confirmaciontorneo==0:
                            for v in range(len(listaequipostorneo)):
                                if listaequipostorneo[v]==0:
                                    listaequipostorneo[v]=nombreequipotorneo
                                    listas.guardar_listatorneo(listaequipostorneo)
                                    print(f"equipo:{nombreequipotorneo} inscripto correctamente")
                                    break
                            break
                            
                        else:
                            break
                    while True:
                        salir2torneo=False
                        try:
                            salidatorneo=int(input("ingrese cualquier numero para seguir o -1 para salir"))
                        except ValueError as mensaje18:
                            print(mensaje18)
                            continue
                        if salidatorneo==-1:
                            salir2torneo=True
                            break
                            
                        else:
                            break
                    if salir2torneo:
                        break"""
    
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
                    listas.guardar_entradas(entradas)
                    funmod.mostrar_disponibles(entradas,disponible,ocupadas)
                    estadistica["cualvendemas"]["entradasliga"]+=cantidad
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
                    listas.guardar_entradastorneo(entradastorneo)
                    funmod.mostrar_disponiblestorneo(entradastorneo,disponibletorneo,ocupadastorneo)
                    estadistica["cualvendemas"]["entradastorneo"]+=cantidad
                    listas.guardar_estadisticas(estadistica)
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

#funciona todo, podriamos revisarlo de vuelta antes de entregarlo. tambien se podria borrar el exceso
