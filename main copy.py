import funmod
import user
import admin
import listas
import csv
import json
import pathlib
import random
def main():
    """Objetivo: Se introduce un número (1 reservar canchas, 2 cancelar la reservacion de canchas, 3 calcular cobro, 4 mostrar reportes, -1 para finalizar programa)"""
    funmod.dar_bienvenida()
    administrador=0
    comprobacionusuario=pathlib.Path("archivoinicio.json")
    comprobacionadmin=pathlib.Path("admininicio.json")
    usuarios=listas.cargar_usuarios(comprobacionusuario)
    administradorclase=listas.cargar_usuarios(comprobacionadmin)
    class DemasiadosIntentosError(Exception):
        pass
    print("inicio de sesion")
    while True:
        try:
            inicio=int(input("ingrese 0 para iniciar sesion, 1 para registrar una cuenta"))
            while inicio<0 or inicio>1:
                print("error numero ingresado fuera del rango")
                inicio=int(input("ingrese 0 para iniciar sesion, 1 para registrar una cuenta"))
        except ValueError as mensaje8:
            print(mensaje8)
            continue
        if inicio==0:
            usuario=input("ingrese nombre de usuario").strip()
            
            if usuario in usuarios:

            
                """si coincide con un numbre de usuario existente hay que poner que revise y todo lo de la contraseña"""
                conteo10=0
                while True:
                    reinicio=False
                    try:
                        contra=int(input("ingrese su contraseña(6 digitos)"))
                    except ValueError as mensaje9:
                        print(mensaje9)
                        continue
                    if contra==usuarios[usuario]["contraseña"]:#no coincide con el archivo, separar administrador y usuario
                        print("bienvenido usuario")
                        administrador=0
                        reinicio=True
                        break
                        
                    else:
                        conteo10+=1
                        print("contraseña incorrecta, intentos:", conteo10)
                        try:
                            if conteo10>=3:
                                raise DemasiadosIntentosError("Se intento demasiadas veces ingresar con una contraseña incorrecta")    
                        except DemasiadosIntentosError as saje:
                            print(saje)
                            break
                if reinicio:
                    break
            elif usuario in administradorclase:
                """si coincide con un numbre de usuario existente hay que poner que revise y todo lo de la contraseña"""
                conteo10=0
                while True:
                    reinicio=False
                    try:
                        contra=int(input("ingrese su contraseña(6 digitos)"))
                    except ValueError as mensaje9:
                        print(mensaje9)
                        continue
                    if contra==administradorclase[usuario]["contraseña"]:#no coincide con el archivo, separar administrador y usuario
                        administrador=1
                        reinicio=True
                        break
                        
                    else:
                        conteo10+=1
                        print("contraseña incorrecta, intentos:", conteo10)
                        try:
                            if conteo10>=3:
                                raise DemasiadosIntentosError("Se intento demasiadas veces ingresar con una contraseña incorrecta")    
                        except DemasiadosIntentosError as saje:
                            print(saje)
                            break
                if reinicio:
                    break
            else:
                print("no existe ninguna cuenta con ese nombre de usuario")

        elif inicio==1:
            nitro=listas.cargar_usuarios(comprobacionusuario)
            nuevousuario=input("ingrese el nombre de usuario que desea: ").strip()
            while nuevousuario in nitro:
                print("el usuario ya existe")
                nuevousuario=input("ingrese el nombre de usuario que desea: ").strip()
            nuevacontra=input("ingresar su contraseña(solo numeros, 6 digitos)").strip()
            while nuevacontra.isalpha() or len(nuevacontra)!=6:
                print("error, no tiene 6 digitos o no puso solo numeros")
                nuevacontra=input("ingresar su contraseña(solo numeros, 6 digitos)").strip()
            nuevacontra=int(nuevacontra)
            nitro[nuevousuario]={"contraseña":nuevacontra}
            listas.guardar_usuarios(comprobacionusuario,nitro)
            usuarios=listas.cargar_usuarios(comprobacionusuario)
            print("usuario registrado con exito")

    if administrador==1:
        admin.admin()
    else:
        user.user()




    """while True:
        print("OPCIONES: ")
        print("# 1 = reservar canchas")
        print("# 2 = cancelar la reservacion de canchas")
        print("# 3 = calcular cobro")
        print("# 4 = mostrar reportes")
        print("# -1 = finalizar programa")
        try:
            herramienta=int(input("Ingrese el numero segun lo que desee: "))
            while herramienta not in[-1,1,2,3,4,8,9,11]:
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
            print("la recaudacion de la liga fue de: $",sum(recaudacionestorneo))
        
        elif herramienta==5: #incripcion torneos, funciona como el de reservas(podriamos meterlo 
            #en un diccionario que muestre dia del torneo y cuando entras los equipos anotados)
            print("los torneos disponibles son los siguientes")
            for x in range(len(matriztorneos)):
                for y in range(len(matriztorneos[x])):
                    print("%-15s" %(matriztorneos[x][y]),end=" ")
                print()
            print()

        elif herramienta==6:#rellenar el torneo para demostracion, total 
            #16 euipos,fase de grupos,8avos
            print("hola")

        elif herramienta==7:#calcular fase de grupos, se finge el torneo se organizan las llaves para 8avos
            print("dale")


        elif herramienta==8:#inscripcion liga, 
            conteo20=0
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
    




        elif herramienta==9:#rellenar liga, en total 20 equipos, 
            for i in range(len(listaequiposliga)):
                if listaequiposliga[i]==0:
                    agarra de un archivo nombres aleatorios, por ahora agrego una lista
                    listaequiposliga[i]=nombresaleatoriosequipos[random.randint(0,100)]
            print("lista de equipos (20 cupos)")
            for i in range(len(listaequiposliga)):
                print(f"equipo:{i+1}\t{listaequiposliga[i]}")
            listaauxiliarliga=listaequiposliga[::1]


        elif herramienta==10:#calcular los 38 partidos por equipo
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
                        fixtureida.append([equipo1,equipo2])
                        listaequiposliga=listaequiposliga[:1]+listaequiposliga[-1:]+listaequiposliga[1:-1]
                fixturevuelta=[[(b,a) for (a,b) in fecha] for fecha in fixtureida]
                contadorfecha=1
                print("Fixture de ida")
                for ronda in fixtureida:
                    print(f"partido:{contador}")
                    for partidito in ronda:
                        local=partidito[0]
                        visitante=partidito[1]
                        print(f"{local} vs {visitante}")
                    contadorfecha+=1
                contadorfechavuelta=1
                print("Fixture de vuelta")
                for rondavuelta in fixturevuelta:
                    print(f"partido:{contador}")
                    for partiditovuelta in rondavuelta:
                        localvuelta=partiditovuelta[0]
                        visitantevuelta=partiditovuelta[1]
                        print(f"{localvuelta} vs {visitantevuelta}")
                    contadorfechavuelta+=1




        
        elif herramienta==11:#inscripcion sponsors
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
                    break
                                
        elif herramienta==12:#simular partidos resultados, mostrar tabla de liga
            while len(resultadosida)<190:
                resu=[]
                eq1=random.randint(0,15)
                eq2=random.randint(0,15)
                resultadosida.append([eq1,eq2])
            while len(resultadosvuelta)<190:
                resu=[]
                eq12=random.randint(0,15)
                eq22=random.randint(0,15)
                resultadosvuelta.append([eq12,eq22])
            listadopartidos=list(zip(fixtureida,resultadosida,contadorpartidosida))
            print("Resultados partidos de ida")
            for fix,resultaditos,contadorida in listadopartidos:
                print(f"partido: {contadorida}\t{fix[contadorida-1][0]}:{resultaditos[contadorida-1][0]} vs {resultaditos[contadorida-1][1]}:{fix[contadorida-1][1]}")
            print()
            listadopartidosvuelta=list(zip(fixturevuelta,resultadosvuelta,contadorpartidosvuelta))
            print("Resultados partidos de vuelta")
            for fix2,resultaditos2,contadorvuelta in listadopartidosvuelta:
                print(f"partido: {contadorvuelta}\t{fix2[contadorvuelta-1][0]}:{resultaditos2[contadorvuelta-1][0]} vs {resultaditos2[contadorvuelta-1][1]}:{fix2[contadorvuelta-1][1]}")
            #falta hacer mostrar tabla de liga
            

        
        elif herramienta==13:#tengo que hacer el doble creo
            for l in range(len(fixtureida)):
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
            liga=liga.sort(ley=lambda x:x[5],reverse=True)
            print(nombredelaliga.center(180))
            print(f"{"Equipos":-20}{"Partidos jugados":-20}{"Ganados":-20}{"Empatados":-20}{"Perdidos":-20}{"Puntos":-20}{"Goles a favor":-20}{"Goles en contra":-20}{"Diferencia de gol":-20}")
            for leter in liga:
                print(f"{listaauxiliarliga[leter]:-20}{partidosjugados[leter]:-20}{ganados[leter]:-20}{empatados[leter]:-20}{perdidos[leter]:-20}{puntos[leter]:-20}{golesfavor[leter]:-20}{golescontra[leter]:-20}{diferenciagol[leter]:-20}")

            print(f"CAMPEON DE LA SUPER LIGA NACIONAL: \t {liga[0][0]} \t con un premio de $30400000")

            tablaliga=(nombredelaliga.center(180))+"\n"
            tablaliga+=(f"{"Equipos":-20}{"Partidos jugados":-20}{"Ganados":-20}{"Empatados":-20}{"Perdidos":-20}{"Puntos":-20}{"Goles a favor":-20}{"Goles en contra":-20}{"Diferencia de gol":-20}\n")
            for leter in liga:
                tablaliga+=(f"{listaauxiliarliga[leter]:-20}{partidosjugados[leter]:-20}{ganados[leter]:-20}{empatados[leter]:-20}{perdidos[leter]:-20}{puntos[leter]:-20}{golesfavor[leter]:-20}{golescontra[leter]:-20}{diferenciagol[leter]:-20}\n")
            tablaliga+=(f"\nCAMPEON DE LA SUPER LIGA NACIONAL: \t {liga[0][0]} \t con un premio de $30400000\n")
            with open("tabla_liga.txt","a",encoding="utf-8") as guardar:
                guardar.write(tablaliga+"\n\n") 
            with open("tabla_de_liga.csv","a",newline="",encoding="utf-8") as guardarcsv:
                escribir=csv.writer(guardarcsv)
                escribir.writerow(["Equipos","Partidos jugados","Ganados","Empatados","Perdidos","Puntos","Goles a favor","Goles en contra","Diferencia de gol"])
                for fila in liga:
                    escribir.writerow(fila)
                escribir.writerow(f"campeon: {liga[0][0]}")


#hay que subirlo a un archivo que va a contener las ligas tras años, premio = $30400000

#hay que poner if Len(resultados[i])<2:
#.... Todo lo de resultados aleatorios

        elif herramienta==14:
            for r in range(len(fixtureida)):
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
                                print(f"el resultado del partido de ida fue: {jugador5}{jugado5} vs {jugado6}{jugador6}")
                                break
                        else:
                            print("los resultados ya están llenos")
                            break
        elif herramienta==15:
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

        elif herramienta==16:#inscripcion torneo, 
            conteo30=0
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
                        break
    




        elif herramienta==17:#rellenar torneo, en total 16 equipos, 
            for i in range(len(listaequipostorneo)):
                if listaequipostorneo[i]==0:
                    agarra de un archivo nombres aleatorios, por ahora agrego una lista
                    listaequipostorneo[i]=nombresaleatoriosequipos[random.randint(0,100)]
            print("lista de equipos (16 cupos)")
            for i in range(len(listaequipostorneo)):
                print(f"equipo:{i+1}\t{listaequipostorneo[i]}")

        elif herramienta==18:#calcular los partidos por equipo torneo se finge el torneo para ver campeon
            contadortorneo=0
            for i in range(len(listaequipostorneo)):
                if listaequipostorneo[i]==0:
                    contadortorneo+=1
            if contadortorneo>0:
                print("faltan equipos")
            else:
                listaequipostorneoaux=random.shuffle(listaequipostorneo)
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


                for x in range(len(fasegrupos1)-1):
                    fasegrupo1=[]
                    for i in range(len(fasegrupos1)//2):
                        equipo1torneo=fasegrupos1[i]
                        equipo2torneo=fasegrupos1[len(fasegrupos1)-1-i]
                        fasegrupos1.append([equipo1torneo,equipo2torneo])
                        fasegrupos1=fasegrupos1[:1]+fasegrupos1[-1:]+fasegrupos1[1:-1]
                    for x in range(len(fasegrupos2)-1):
                        fasegrupo2=[]
                        for i in range(len(fasegrupos2)//2):
                            equipo3torneo=fasegrupos2[i]
                            equipo4torneo=fasegrupos2[len(fasegrupos2)-1-i]
                            fasegrupos2.append([equipo3torneo,equipo4torneo])
                            fasegrupos2=fasegrupos2[:1]+fasegrupos2[-1:]+fasegrupos2[1:-1]
                    for x in range(len(fasegrupos3)-1):
                        fasegrupo3=[]
                        for i in range(len(fasegrupos3)//2):
                            equipo5torneo=fasegrupos3[i]
                            equipo6torneo=fasegrupos3[len(fasegrupos3)-1-i]
                            fasegrupos3.append([equipo5torneo,equipo6torneo])
                            fasegrupos3=fasegrupos3[:1]+fasegrupos3[-1:]+fasegrupos3[1:-1]

                    for x in range(len(fasegrupos4)-1):
                        fasegrupo4=[]
                        for i in range(len(fasegrupos4)//2):
                            equipo7torneo=fasegrupos4[i]
                            equipo8torneo=fasegrupos4[len(fasegrupos4)-1-i]
                            fasegrupos4.append([equipo7torneo,equipo8torneo])
                            fasegrupos4=fasegrupos4[:1]+fasegrupos4[-1:]+fasegrupos4[1:-1]

        elif herramienta==19:#calcular cuartos de final

            while len(fasegrupos1resultados)<12:
                resu=[]
                fase1eq1=random.randint(0,15)
                fase1eq2=random.randint(0,15)
                fasegrupos1resultados.append([fase1eq1,fase1eq2])
            while len(fasegrupos2resultados)<12:
                resu=[]
                fase2eq12=random.randint(0,15)
                fase2eq22=random.randint(0,15)
                fasegrupos2resultados.append([fase2eq12,fase2eq22])
            while len(fasegrupos3resultados)<12:
                resu=[]
                fase3eq1=random.randint(0,15)
                fase3eq2=random.randint(0,15)
                fasegrupos3resultados.append([fase3eq1,fase3eq2])
            while len(fasegrupos4resultados)<12:
                resu=[]
                fase4eq12=random.randint(0,15)
                fase4eq22=random.randint(0,15)
                fasegrupos4resultados.append([fase4eq12,fase4eq22])
            listadopartidosfase1=list(zip(fasegrupos1,fasegrupos1resultados,contadorpartidosfase1))
            print("Resultados partidos fase 1")
            for fixe,resultadito,contadorfase1 in listadopartidosfase1:
                print(f"partido: {contadortorneo}\t{fixe[contadortorneo-1][0]}:{resultadito[contadortorneo-1][0]} vs {resultadito[contadortorneo-1][1]}:{fixe[contadortorneo-1][1]}")
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

        elif herramienta==20:#tablas fase grupos del torneo
            for l in range(len(fasegrupos1resultados)):
                jugador1fase1=fasegrupos1resultados[l][0]
                jugador2fase1=fasegrupos1resultados[l][1]
                jugado1fase1=fasegrupos1aux.index(jugador1fase1)
                jugado2fase1=fasegrupos1aux.index(jugador2fase1)
                partidosjugadosfase1[jugado1fase1]+=1
                partidosjugadosfase1[jugado2fase1]+=1
                if fasegrupos1resultados[l][0]>fasegrupos1resultados[l][1]:
                    ganadosfase1[jugado1fase1]+=1
                    puntosfase1[jugado1fase1]+=3
                    perdidosfase1[jugado2fase1]+=1
                elif fasegrupos1resultados[l][0]<fasegrupos1resultados[l][1]:
                    ganadosfase1[jugado2fase1]+=1
                    puntosfase1[jugado2fase1]+=3
                    perdidosfase1[jugado1fase1]+=1
                else:
                    empatadosfase1[jugado1fase1]+=1
                    puntosfase1[jugado1fase1]+=1
                    empatadosfase1[jugado2fase1]+=1
                    puntosfase1[jugado2fase1]+=1

                golesfavorfase1[jugado1fase1]+=fasegrupos1resultados[l][0]
                golesfavorfase1[jugado2fase1]+=fasegrupos1resultados[l][1]
                golescontrafase1[jugado1fase1]+=fasegrupos1resultados[l][1]
                golescontrafase1[jugado2fase1]+=fasegrupos1resultados[l][0]
                diferenciagolfase1[jugado1fase1]+=golesfavorfase1[jugado1fase1]-golescontrafase1[jugado1fase1]
                diferenciagolfase1[jugado2fase1]+=golesfavorfase1[jugado2fase1]-golescontrafase1[jugado2fase1]
            #corregir lo siguiente
            fase1=list(zip(fasegrupos1aux,partidosjugadosfase1,ganadosfase1,perdidosfase1,empatadosfase1,puntosfase1,golesfavorfase1,golescontrafase1,diferenciagolfase1))
            fase1=fase1.sort(ley=lambda x:x[5],reverse=True)
            print(nombredeltorneo.center(180))
            print(f"{"Equipos":-20}{"Partidos jugados":-20}{"Ganados":-20}{"Empatados":-20}{"Perdidos":-20}{"Puntos":-20}{"Goles a favor":-20}{"Goles en contra":-20}{"Diferencia de gol":-20}")
            for leter in fase1:
                print(f"{fasegrupos1aux[leter]:-20}{partidosjugados[leter]:-20}{ganados[leter]:-20}{empatados[leter]:-20}{perdidos[leter]:-20}{puntos[leter]:-20}{golesfavor[leter]:-20}{golescontra[leter]:-20}{diferenciagol[leter]:-20}")

            print(f"PASAN A LA SIGUIENTE FASE: \t {fasegrupos1aux[0]} \t y \t  {fasegrupos1aux[1]} ")
            #hacer fase2,fase3,fase4
            for l in range(len(fasegrupos2resultados)):
                jugador1fase2=fasegrupos2resultados[l][0]
                jugador2fase2=fasegrupos2resultados[l][1]
                jugado1fase2=fasegrupos2aux.index(jugador1fase2)
                jugado2fase2=fasegrupos2aux.index(jugador2fase2)
                partidosjugadosfase2[jugado1fase2]+=1
                partidosjugadosfase2[jugado2fase2]+=1
                if fasegrupos2resultados[l][0]>fasegrupos2resultados[l][1]:
                    ganadosfase2[jugado1fase2]+=1
                    puntosfase2[jugado1fase2]+=3
                    perdidosfase2[jugado2fase2]+=1
                elif fasegrupos2resultados[l][0]<fasegrupos2resultados[l][1]:
                    ganadosfase2[jugado2fase2]+=1
                    puntosfase2[jugado2fase2]+=3
                    perdidosfase2[jugado1fase2]+=1
                else:
                    empatadosfase2[jugado1fase2]+=1
                    puntosfase2[jugado1fase2]+=1
                    empatadosfase2[jugado2fase2]+=1
                    puntosfase2[jugado2fase2]+=1

                golesfavorfase2[jugado1fase2]+=fasegrupos2resultados[l][0]
                golesfavorfase2[jugado2fase2]+=fasegrupos2resultados[l][1]
                golescontrafase2[jugado1fase2]+=fasegrupos2resultados[l][1]
                golescontrafase2[jugado2fase2]+=fasegrupos2resultados[l][0]

                diferenciagolfase2[jugado1fase2] = golesfavorfase2[jugado1fase2] - golescontrafase2[jugado1fase2]
                diferenciagolfase2[jugado2fase2] = golesfavorfase2[jugado2fase2] - golescontrafase2[jugado2fase2]
                fase2=list(zip(fasegrupos2aux,partidosjugadosfase2,ganadosfase2,empatadosfase2,perdidosfase2,puntosfase2,golesfavorfase2,golescontrafase2,diferenciagolfase2))
                fase2=fase2.sort(key=lambda x: x[5], reverse=True)
                print(nombredeltorneo.center(180))
                print(f"{'Equipos':-20}{'Partidos jugados':-20}{'Ganados':-20}{'Empatados':-20}{'Perdidos':-20}{'Puntos':-20}{'Goles a favor':-20}{'Goles en contra':-20}{'Diferencia de gol':-20}")
                for element in fase2:
                    print(f"{fasegrupos2aux[element]:-20}{partidosjugadosfase2[element]:-20}{ganadosfase2[element]:-20}{empatadosfase2[element]:-20}{perdidosfase2[element]:-20}{puntosfase2[element]:-20}{golesfavorfase2[element]:-20}{golescontrafase2[element]:-20}{diferenciagolfase2[element]:-20}")
            for l in range(len(fasegrupos3resultados)):
                jugador1fase3=fasegrupos3resultados[l][0]
                jugador2fase3=fasegrupos3resultados[l][1]
                jugado1fase3=fasegrupos3aux.index(jugador1fase3)
                jugado2fase3=fasegrupos3aux.index(jugador2fase3)
                partidosjugadosfase3[jugado1fase3]+=1
                partidosjugadosfase3[jugado2fase3]+=1
                if fasegrupos3resultados[l][0]>fasegrupos3resultados[l][1]:
                    ganadosfase3[jugado1fase3]+=1
                    puntosfase3[jugado1fase3]+=3
                    perdidosfase3[jugado2fase3]+=1
                elif fasegrupos3resultados[l][0]<fasegrupos3resultados[l][1]:
                    ganadosfase3[jugado2fase3]+=1
                    puntosfase3[jugado2fase3]+=3
                    perdidosfase3[jugado1fase3]+=1
                else:
                    empatadosfase3[jugado1fase3]+=1
                    puntosfase3[jugado1fase3]+=1
                    empatadosfase3[jugado2fase3]+=1
                    puntosfase3[jugado2fase3]+=1

                golesfavorfase3[jugado1fase3]+=fasegrupos3resultados[l][0]
                golesfavorfase3[jugado2fase3]+=fasegrupos3resultados[l][1]
                golescontrafase3[jugado1fase3]+=fasegrupos3resultados[l][1]
                golescontrafase3[jugado2fase3]+=fasegrupos3resultados[l][0]
                diferenciagolfase3[jugado1fase3] = golesfavorfase3[jugado1fase3] - golescontrafase3[jugado1fase3]
                diferenciagolfase3[jugado2fase3] = golesfavorfase3[jugado2fase3] - golescontrafase3[jugado2fase3]
                fase3=list(zip(fasegrupos3aux,partidosjugadosfase3,ganadosfase3,empatadosfase3,perdidosfase3,puntosfase3,golesfavorfase3,golescontrafase3,diferenciagolfase3))
                fase3=fase3.sort(key=lambda x: x[5], reverse=True)
                print(nombredeltorneo.center(180))
                print(f"{'Equipos':-20}{'Partidos jugados':-20}{'Ganados':-20}{'Empatados':-20}{'Perdidos':-20}{'Puntos':-20}{'Goles a favor':-20}{'Goles en contra':-20}{'Diferencia de gol':-20}")
                for element in fase2:
                    print(f"{fasegrupos3aux[element]:-20}{partidosjugadosfase3[element]:-20}{ganadosfase3[element]:-20}{empatadosfase3[element]:-20}{perdidosfase3[element]:-20}{puntosfase3[element]:-20}{golesfavorfase3[element]:-20}{golescontrafase3[element]:-20}{diferenciagolfase3[element]:-20}")

            for l in range(len(fasegrupos4resultados)):
                jugador1fase4=fasegrupos4resultados[l][0]
                jugador2fase4=fasegrupos4resultados[l][1]
                jugado1fase4=fasegrupos4aux.index(jugador1fase4)
                jugado2fase4=fasegrupos4aux.index(jugador2fase4)
                partidosjugadosfase4[jugado1fase4]+=1
                partidosjugadosfase4[jugado2fase4]+=1
                if fasegrupos4resultados[l][0]>fasegrupos4resultados[l][1]:
                    ganadosfase4[jugado1fase4]+=1
                    puntosfase4[jugado1fase4]+=3
                    perdidosfase4[jugado2fase4]+=1
                elif fasegrupos4resultados[l][0]<fasegrupos4resultados[l][1]:
                    ganadosfase4[jugado2fase4]+=1
                    puntosfase4[jugado2fase4]+=3
                    perdidosfase4[jugado1fase4]+=1
                else:
                    empatadosfase4[jugado1fase4]+=1
                    puntosfase4[jugado1fase4]+=1
                    empatadosfase4[jugado2fase4]+=1
                    puntosfase4[jugado2fase4]+=1

                golesfavorfase4[jugado1fase4]+=fasegrupos4resultados[l][0]
                golesfavorfase4[jugado2fase4]+=fasegrupos4resultados[l][1]
                golescontrafase4[jugado1fase4]+=fasegrupos4resultados[l][1]
                golescontrafase4[jugado2fase4]+=fasegrupos4resultados[l][0]

                diferenciagolfase4[jugado1fase4] = golesfavorfase4[jugado1fase4] - golescontrafase4[jugado1fase4]
                diferenciagolfase4[jugado2fase4] = golesfavorfase4[jugado2fase4] - golescontrafase4[jugado2fase4]
                fase4=list(zip(fasegrupos4aux,partidosjugadosfase4,ganadosfase4,empatadosfase4,perdidosfase4,puntosfase4,golesfavorfase4,golescontrafase4,diferenciagolfase4))
                fase4=fase4.sort(key=lambda x: x[5], reverse=True)
                print(nombredeltorneo.center(180))
                print(f"{'Equipos':-20}{'Partidos jugados':-20}{'Ganados':-20}{'Empatados':-20}{'Perdidos':-20}{'Puntos':-20}{'Goles a favor':-20}{'Goles en contra':-20}{'Diferencia de gol':-20}")
                for element in fase4:
                    print(f"{fasegrupos4aux[element]:-20}{partidosjugadosfase4[element]:-20}{ganadosfase4[element]:-20}{empatadosfase4[element]:-20}{perdidosfase4[element]:-20}{puntosfase4[element]:-20}{golesfavorfase4[element]:-20}{golescontrafase4[element]:-20}{diferenciagolfase4[element]:-20}")




        elif herramienta==21:#calcular cuartos
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
                    ereq1=fase1[i]
                    doeq2=fase2[i]
                    ereq3=fase3[i]
                    toeq4=fase4[i]
                    cuartos.append([ereq1,ereq3])
                    cuartos.append([doeq2,toeq4])
                    cuartosaux=cuartos[::1]

        elif herramienta==22:#calcular semifinal
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

        elif herramienta==23:#calcular final
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
        elif herramienta==24:#campeon final torneo
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
        elif herramienta==25:   #fase de grupos para poner resultados
            try:
                zona=int(input("Elegí la zona a cargar (1-4): "))
                while zona<1 or zona>4:
                    print("Error, solo números del 1 al 4")
                    zona=int(input("Elegí la zona a cargar (1-4): "))
            except ValueError:
                print("Entrada inválida, debe ser un número entre 1 y 4")
                zona=0

            if zona==1:
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
                            print(f"Resultado: {jugadores11} : {goles1} vs {goles2} : {jugador2} ")
                            break
                    else:
                        completos+=1
                if completos==len(fasegrupos1aux):
                    print("Ya se jugaron todos los partidos de la zona 1")

            elif zona==2:
                completos2=0
                for r in range(len(fasegrupos2aux)):
                    if len(fasegrupos2resultados[r])<2:
                        jugadores21=fasegrupos2aux[r][0]
                        jugadores22=fasegrupos2aux[r][1]
                        while True:
                            try:
                                goles21=int(input(f"Ingrese los goles de {jugadores21}: "))
                                while goles21<0:
                                    print("Error, no puede ser menor a 0")
                                    goles21=int(input(f"Ingrese los goles de {jugadores21}: "))
                                goles22=int(input(f"Ingrese los goles de {jugadores22}: "))
                                while goles22<0:
                                    print("Error, no puede ser menor a 0")
                                    goles22=int(input(f"Ingrese los goles de {jugadores22}: "))
                            except ValueError as mostra2:
                                print(mostra2)
                                continue
                            fasegrupos2resultados[r].append([goles21,goles22])
                            print(f"Resultado: {jugadores21} : {goles21} vs {goles22} : {jugadores22}")
                            break
                    else:
                        completos2+=1
                if completos2==len(fasegrupos2aux):
                    print("Ya se jugaron todos los partidos de la zona 2")

            elif zona==3:
                completos3=0
                for r in range(len(fasegrupos3aux)):
                    if len(fasegrupos3resultados[r])<2:
                        jugadores31=fasegrupos3aux[r][0]
                        jugadores32=fasegrupos3aux[r][1]
                        while True:
                            try:
                                goles31=int(input(f"Ingrese los goles de {jugadores31}: "))
                                while goles31<0:
                                    print("Error, no puede ser menor a 0")
                                    goles31=int(input(f"Ingrese los goles de {jugadores31}: "))
                                goles32=int(input(f"Ingrese los goles de {jugadores32}: "))
                                while goles32<0:
                                    print("Error, no puede ser menor a 0")
                                    goles32=int(input(f"Ingrese los goles de {jugadores32}: "))
                            except ValueError as mostra3:
                                print(mostra3)
                                continue
                            fasegrupos3resultados[r].append([goles31,goles32])
                            print(f"Resultado: {jugadores31} : {goles31} vs {goles32} : {jugadores32}")
                            break
                    else:
                        completos3+=1
                if completos3==len(fasegrupos3aux):
                    print("Ya se jugaron todos los partidos de la zona 3")

            elif zona==4:
                completos4=0
                for r in range(len(fasegrupos4aux)):
                    if len(fasegrupos4resultados[r])<2:
                        jugadores41=fasegrupos4aux[r][0]
                        jugadores42=fasegrupos4aux[r][1]
                        while True:
                            try:
                                goles41=int(input(f"Ingrese los goles de {jugadores41}: "))
                                while goles41<0:
                                    print("Error, no puede ser menor a 0")
                                    goles41=int(input(f"Ingrese los goles de {jugadores41}: "))
                                goles42=int(input(f"Ingrese los goles de {jugadores42}: "))
                                while goles42<0:
                                    print("Error, no puede ser menor a 0")
                                    goles42=int(input(f"Ingrese los goles de {jugadores42}: "))
                            except ValueError as mostra4:
                                print(mostra4)
                                continue
                            fasegrupos4resultados[r].append([goles41,goles42])
                            print(f"Resultado: {jugadores41} : {goles41}) vs {goles42} : {jugadores42}")
                            break
                    else:
                        completos4+=1
                if completos4==len(fasegrupos4aux):
                    print("Ya se jugaron todos los partidos de la zona 4")

            #falta hacer mostrar tabla de liga
#falta sumar listas de resultados
        elif herramienta==26:   #poner cuartos manual
            for r in range(len(cuartosaux)):
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
                        print(f"Resultado: {jugadorescuartos1} : {golescuartos1} vs {golescuartos2} : {jugadorescuartos2}")
                        break
                else:
                    print("Este partido ya tiene resultado")

        elif herramienta==27:   #poner semifinal manual
            for r in range(len(semisaux)):
                if len(semisresultados[r])<2:
                    jugadoressemis1=semisaux[r][0]
                    jugadoressemis2=semisaux[r][1]
                    while True:
                        try:
                            golessemis1=int(input(f"Ingrese los goles de {jugadoressemis1}: "))
                            while golessemis1<0:
                                print("Error, no puede ser menor a 0")
                                golessemis1=int(input(f"Ingrese los goles de {jugadoressemis1}: "))
                            golessemis2=int(input(f"Ingrese los goles de {jugadoressemis2}: "))
                            while golessemis2<0:
                                print("Error, no puede ser menor a 0")
                                golessemis2=int(input(f"Ingrese los goles de {jugadoressemis2}: "))
                        except ValueError as mostra6:
                            print(mostra6)
                            continue
                        semisresultados[r].append([golessemis1,golessemis2])
                        print(f"Resultado: {jugadoressemis1} : {golessemis1} vs {golessemis2} : {jugadoressemis2}")
                        break
                else:
                    print("Este partido ya tiene resultado")

        elif herramienta==28:   #poner final manual
            for r in range(len(finalaux)):
                if len(finalresultados[r])<2:
                    jugadoresfinal1=finalaux[r][0]
                    jugadoresfinal2=finalaux[r][1]
                    while True:
                        try:
                            golesfinal1=int(input(f"Ingrese los goles de {jugadoresfinal1}: "))
                            while golesfinal1<0:
                                print("Error, no puede ser menor a 0")
                                golesfinal1=int(input(f"Ingrese los goles de {jugadoresfinal1}: "))
                            golesfinal2=int(input(f"Ingrese los goles de {jugadoresfinal2}: "))
                            while golesfinal2<0:
                                print("Error, no puede ser menor a 0")
                                golesfinal2=int(input(f"Ingrese los goles de {jugadoresfinal2}: "))
                        except ValueError as mostra7:
                            print(mostra7)
                            continue
                        finalresultados[r].append([golesfinal1,golesfinal2])
                        print(f"Resultado FINAL: {jugadoresfinal1} : {golesfinal1} vs {golesfinal2} : {jugadoresfinal2}")
                        break
                else:
                    print("El resultado de la final ya está cargado")

        elif herramienta==29:   #fases de grupo aleatorias
            for r in range(len(fasegrupos1aux)):
                if len(fasegrupos1resultados[r])<2:
                    golcitos1=random.randint(0,15)
                    golcitos2=random.randint(0,15)
                    fasegrupos1resultados[r].append([golcitos1,golcitos2])
            for r in range(len(fasegrupos2aux)):
                if len(fasegrupos2resultados[r])<2:
                    golcitos21=random.randint(0,15)
                    golcitos22=random.randint(0,15)
                    fasegrupos2resultados[r].append([golcitos21,golcitos22])
            for r in range(len(fasegrupos3aux)):
                if len(fasegrupos3resultados[r])<2:
                    golcitos31=random.randint(0,15)
                    golcitos32=random.randint(0,15)
                    fasegrupos3resultados[r].append([golcitos31,golcitos32])
            for r in range(len(fasegrupos4aux)):
                if len(fasegrupos4resultados[r])<2:
                    golcitos41=random.randint(0,15)
                    golcitos42=random.randint(0,15)
                    fasegrupos4resultados[r].append([golcitos41,golcitos42])

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

        elif herramienta==30:   #cuartos aleatorio
            for r in range(len(cuartosaux)):
                if len(cuartosresultados[r])<2:
                    golcitoscuartos1=random.randint(0,15)
                    golcitoscuartos2=random.randint(0,15)
                    cuartosresultados[r].append([golcitoscuartos1,golcitoscuartos2])

            print("RESULTADOS CUARTOS DE FINAL")
            abiertocuartos=list(zip(cuartosaux,cuartosresultados))
            for fix,res in abiertocuartos:
                print(f"{fix[0]} {res[0][0]} vs {res[0][1]} {fix[1]}")

        elif herramienta==31:   #semis aleatorio
            for r in range(len(semisaux)):
                if len(semisresultados[r])<2:
                    golcitossemis1=random.randint(0,15)
                    golcitossemis2=random.randint(0,15)
                    semisresultados[r].append([golcitossemis1,golcitossemis2])

            print("RESULTADOS SEMIFINALES")
            abiertosemis=list(zip(semisaux,semisresultados))
            for fix,res in abiertosemis:
                print(f"{fix[0]} {res[0][0]} vs {res[0][1]} {fix[1]}")

        elif herramienta==32:   #final aleatorio
            for r in range(len(finalaux)):
                if len(finalresultados[r])<2:
                    golcitosfinal1=random.randint(0,15)
                    golcitosfinal2=random.randint(0,15)
                    finalresultados[r].append([golcitosfinal1,golcitosfinal2])

            print("RESULTADO FINAL")
            abiertofinal=list(zip(finalaux,finalresultados))
            for fix,res in abiertofinal:
                print(f"{fix[0]} {res[0][0]} vs {res[0][1]} {fix[1]}")

        




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
            break"""


if __name__=="__main__":
    main()

#hay que revisar si funciona bien el 8(sacarle la opcion de sponsors torneo, dejar solo sponsors liga),falta revisar el 10 un poco 
    #para ver si funciona del todo. 
    #1,2,3,4,5,6,7,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31 funcionan bien por el momento, para iniciarlo se pone primero 6, despues 7, despues 9 y despues 10
#si no se tienen los archivos, para el torneo primero se rellena los equipos 14,calcular partidos 15,resultados aleatorios 16,tabla fase de grupos 17,
#calcular cuartos 18,cuartos resultados 23,calcular semifinal 19,semifinal resultados 24,calcular final torneo 20,final resultados 25,campeon final torneo 21 
#se puede revisar una vez mas antes de entregar
