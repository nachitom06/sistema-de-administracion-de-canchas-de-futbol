import funmod
import random
def main():
    """Objetivo: Se introduce un número (1 reservar canchas, 2 cancelar la reservacion de canchas, 3 calcular cobro, 4 mostrar reportes, -1 para finalizar programa)"""
    funmod.dar_bienvenida()
    matrizper,matriznombre=funmod.iniciar_matriz()
    listcanchas,listhorarios,listformpago,listrecaudacioncanchas,listrecaudacionhorarios,listrecaudacionformpago,listcantcanchas,listcanthorarios,listcantformpago,listaclientes,listadiezporciento=funmod.cargar_listas_de_canchas()
    general,recaudaciondiezporciento=0,0
    while general==0:
        print("OPCIONES: ")
        print("# 1 = reservar canchas")
        print("# 2 = cancelar la reservacion de canchas")
        print("# 3 = calcular cobro")
        print("# 4 = mostrar reportes")
        print("# -1 = finalizar programa")
        herramienta=int(input("Ingrese el numero segun lo que desee: "))
        while herramienta not in[-1,1,2,3,4]:
            print("Error, el numero ingresado no se encuntra en lo indicado")
            herramienta=int(input("Ingrese el numero segun lo que desee(1 reservar canchas, 2 cancelar la reservacion de canchas, 3 calcular cobro, 4 mostrar reportes, -1 para finalizar programa): "))
        if herramienta==1:
            sig=0
            while sig==0:
                fila=0
                cancha=int(input("Ingrese el número de cancha que desea elegir (5, 8, 11) o -1 si no desea reservar: "))
                if cancha!=-1:
                    while cancha not in[5,8,11]:
                        print("Error, el numero de cancha seleccionado no se encuentra")
                        cancha=int(input("Ingrese el número de cancha que desea elegir (5, 8, 11): "))
                    if cancha==5:
                        fila=0
                    elif cancha==8:
                        fila=1
                    else:
                        fila=2
                    print(matrizper[fila],"Los horarios que se muestran ya estan tomados")
                    hora=int(input("ingrese en formato militar la hora que desea alquilar (1200 a 2400, de 100 en 100): "))
                    while hora<1200 or hora>2400 or hora%100!=0:
                        print("La hora ingresada no se encuentra en el rango (1200 a 2400, de 100 en 100)")
                        hora=int(input("Ingrese en formato militar la hora que desea alquilar (1200 a 2400, de 100 en 100): "))
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
                    señ=int(input("Ingrese cualquier numero entero si desea continuar o -1 para salir: "))
                    if señ==-1:
                        sig=-1
                    else:
                        sig=0
                else:
                    sig=-1
        elif herramienta==2:
            signal=0
            while signal==0:
                fila2=0
                cancha2=int(input("Ingrese el número de cancha que desea cancelar la reserva (5, 8, 11) o -1 si no desea cancelar: "))
                if cancha2!=-1:
                    while cancha2 not in[5,8,11]:
                        print("Error, el número de cancha seleccionado no se encuentra")
                        cancha2=int(input("Ingrese el número de cancha que desea cancelar la reserva (5, 8, 11)"))
                    if cancha2==5:
                        fila2=0
                    elif cancha2==8:
                        fila2=1
                    else:
                        fila2=2
                    print(matrizper[fila2],"Los horarios que se muestran son los que ya estan tomados")
                    hora2=int(input("Ingrese en formato militar la hora que desea cancelar el alquilar (1200 a 2400, de 100 en 100): "))
                    while hora2<1200 or hora2>2400 or hora2%100!=0:
                        print("La hora ingresada no se encuentra en el rango (1200 a 2400, de 100 en 100)")
                        hora2=int(input("Ingrese en formato militar la hora que desea alquilar (1200 a 2400, de 100 en 100): "))
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
                    señ2=int(input("Ingrese cualquier número entero si desea continuar o -1 para salir: "))
                    if señ2==-1:
                        signal=-1
                    else:
                        signal=0
                else:
                    signal=-1

        elif herramienta==3:
            sigo=0
            while sigo==0:
                precios,horas,cancha,ingresohora,clientes=funmod.guardar_precio_cantidad_horas(random.randint(35000,45000),random.randint(65000,75000),random.randint(95000,105000),listhorarios)
                cobro=funmod.calcular_cantidad_a_pagar(precios,horas)
                listaclientes.append(clientes)
                print("cantidad a pagar: $",cobro)
                cobrofinal=funmod.reporte_metodo_pago(listformpago,listrecaudacionformpago,listcantformpago,cobro,listadiezporciento,cobro)
                funmod.reporte_canchas(listcanchas,listrecaudacioncanchas,listcantcanchas,cobrofinal,cancha)
                funmod.reporte_horarios(listhorarios,listrecaudacionhorarios,listcanthorarios,cobrofinal,ingresohora)
                sigo2=int(input("Ingrese cualquier numero entero si desea continuar o -1 para salir: "))
                if sigo2==-1:
                    sigo=-1
                else:
                    sigo=0
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
            for listrecaudacionhorarios,listhorarios in listadoarmado:
                print(f"${listrecaudacionhorarios}\t\ta las {listhorarios} horas")
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
            general=-1
if __name__=="__main__":
    main()

