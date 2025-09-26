import funmod
import random
def main():
    """Objetivo: Se introduce un número (1 reservar canchas, 2 cancelar la reservacion de canchas, 3 calcular cobro, 4 mostrar reportes, -1 para finalizar programa)"""
    funmod.dar_bienvenida()
    matrizper,matriznombre=funmod.iniciar_matriz()
    matriztorneos=[[0 for _ in range(4)] for _ in range(12)]
    listaequiposliga=[0 for _ in range(20)]
    fixtureida=[]
    fixturevuelta=[]
    nombresaleatoriosequipos = ["Atlético del Sur", "Club Deportivo Aurora", "Racing Federal", "Juventud Unida","Sportivo Central", "Unión del Norte", "Estrella Roja", "Los Dragones FC","San Martín Juniors", "Nueva Esperanza", "Club Social Libertad", "Huracán del Valle","Defensores de la Costa", "Talleres Unidos", "Los Guerreros", "Boca del Oeste","River Plateño", "Cruz Azul del Sur", "Leones Dorados", "Águilas Negras","Real Horizonte", "Deportivo América", "Universitario Central", "Club Atlético Nacional","Fuerza Joven", "Pumas de la Sierra", "Toros Salvajes", "Estudiantes del Sol","Nueva Generación", "Atlético Popular", "Club Independiente", "San Lorenzo Unido","Deportivo Patria", "Olimpia del Sur", "Cultural Esperanza", "Ciclón Rojo","Guaraní Unido", "Leones del Sur", "Academia del Fútbol", "Sport Boys","Los Gladiadores", "Unión Deportiva Estrella", "Villa Real FC", "Juventud Federal","Defensa y Justicia Social", "Atlético Horizonte", "Deportivo Norteño", "Tigre Blanco","Halcones Verdes", "Nueva Alianza", "San Carlos Juniors", "Atlético Centenario","Los Piratas FC", "Club Deportivo Cosmos", "Juventud Atlética", "Rayo del Sur","Los Titanes", "Sporting Club Federal", "Atlético Ciudadela", "Universitario Unido","Club Social Victoria", "Deportivo Unión", "Santa Fe Atlético", "Real Central","Club Atlético Esperanza", "Independencia FC", "Sportivo Olimpo", "Guerreros del Sol","Águilas Plateadas", "Los Delfines", "Atlético Mundial", "Nueva Roma FC","San José Unido", "Estrella Federal", "Juventud Patriota", "Huracán del Centro","Deportivo Internacional", "Granaderos FC", "Racing Unido", "Unión Deportiva Norte","Atlético Azul", "Fuerza Guerrera", "Los Lobos", "Club Estudiantes Unidos","Rivera FC", "Boca Sur", "Atlético Colonial", "Deportivo Horizonte","Club Nacional Popular", "Los Cóndores", "Sporting Nueva Era", "Juventud del Norte","Atlético Moderno", "Los Pioneros", "Real Metropolitano", "Estrella Joven","Deportivo Victoria", "Unión San Pedro", "Club del Sol", "Atlético Bravo"]
    listcanchas,listhorarios,listformpago,listrecaudacioncanchas,listrecaudacionhorarios,listrecaudacionformpago,listcantcanchas,listcanthorarios,listcantformpago,listaclientes,listadiezporciento=funmod.cargar_listas_de_canchas()
    listasponsorszona,listasponsors,disponibilidad,listadisponibilidad,listanombresponsor=[1,2,3,4,5,6],["entrada","arco izquiero","arco derecho","gradas lado izquierdo","gradas lado derecho","fachada de club"],[0 for i in range(6)],["disponible","no disponible"],[0 for i in range(6)]
    recaudaciondiezporciento=0
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
            usuario=input("ingrese nombre de usuario")
            """si coincide con un numbre de usuario existente hay que poner que revise y todo lo de la contraseña"""
            conteo10=0
            while True:
                reinicio=False
                try:
                    contra=int(input("ingrese su contraseña(5 digitos)"))
                except ValueError as mensaje9:
                    print(mensaje9)
                    continue
                if contra!=0:#no coincide con el archivo, separar administrador y usuario
                    conteo10+=1
                    print("contraseña incorrecta, intentos:", conteo10)
                    try:
                        if conteo10>=3:
                            raise DemasiadosIntentosError("Se intento demasiadas veces ingresar con una contraseña incorrecta")    
                    except DemasiadosIntentosError as saje:
                        print(saje)
                        break
                else:
                    reinicio=True
                    break
        if reinicio:
            break

    while True:
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
                    """agarra de un archivo nombres aleatorios, por ahora agrego una lista"""
                    listaequiposliga[i]=nombresaleatoriosequipos[random.randint(0,100)]
            print("lista de equipos (20 cupos)")
            for i in range(len(listaequiposliga)):
                print(f"equipo:{i+1}\t{listaequiposliga[i]}")


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
                        fixtureida.append((equipo1,equipo2))
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


if __name__=="__main__":
    main()

