import funmod
import random
def main(matriz,matrizn):
    """Objetivo: Se introduce tipo de cancha (F5, F8, F11) Y una hora de en el formato hora militar, como por ejemplo 15:00 PM = 1500, para reservar la cancha. abierto de 12:00Hs a 24:00Hs"""
    general=0
    while general==0:
        herramienta=int(input("ingrese el numero segun lo que desee(1 reservar canchas, 2cancelar la reservacion de canchas, 3 calcular cobro, -1 para finalizar programa)"))
        while herramienta not in[-1,1,2,3]:
            print("error, el numero ingresado no se encuntra en lo indicado")
            herramienta=int(input("ingrese el numero segun lo que desee(1 reservar canchas, 2cancelar la reservacion de canchas, 3 calcular cobro, -1 para finalizar programa)"))
        if herramienta==1:
            sig=0
            while sig==0:
                fila=0
                cancha=int(input("Ingrese el número de cancha que desea elegir (5, 8, 11) o -1 si no desea reservar"))
                if cancha!=-1:
                    while cancha not in[5,8,11]:
                        print("Error, el numero de cancha seleccionado no se encuentra")
                        cancha=int(input("Ingrese el número de cancha que desea elegir (5, 8, 11)"))
                    if cancha==5:
                        fila=0
                    elif cancha==8:
                        fila=1
                    else:
                        fila=2
                    print(matriz[fila],"los horarios que se muestran ya estan tomados")
                    hora=int(input("ingrese en formato militar la hora que desea alquilar (1200 a 2400, de 100 en 100)"))
                    while hora<1200 or hora>2400 or hora%100!=0:
                        print("La hora ingresada no se encuentra en el rango (1200 a 2400, de 100 en 100)")
                        hora=int(input("ingrese en formato militar la hora que desea alquilar (1200 a 2400, de 100 en 100)"))
                    if hora not in matriz[fila]:
                        columna=(hora-1200)//100
                        matriz[fila][columna]=hora
                        nombre=input("igrese su nombre y apellido al cual reservara la cancha")
                        matrizn[fila][columna]=nombre
                        print("reserva realizada con exito: cancha de futbol",cancha,"a las",hora,"horas a nombre de:",nombre)
                        print("canchas",matriz)
                        print()
                        print("nombres de reservas",matrizn)
                    else:
                        print("ese horario ya esta ocupado")
                    señ=int(input("ingrese cualquier numero entero si desea continuar o -1 para salir"))
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
                cancha2=int(input("Ingrese el número de cancha que desea cancelar la reserva (5, 8, 11) o -1 si no desea cancelar"))
                if cancha2!=-1:
                    while cancha2 not in[5,8,11]:
                        print("Error, el numero de cancha seleccionado no se encuentra")
                        cancha2=int(input("Ingrese el número de cancha que desea cancelar la reserva (5, 8, 11)"))
                    if cancha2==5:
                        fila2=0
                    elif cancha2==8:
                        fila2=1
                    else:
                        fila2=2
                    print(matriz[fila2],"los horarios que se muestran son los que ya estan tomados")
                    hora2=int(input("ingrese en formato militar la hora que desea cancelar el alquilar (1200 a 2400, de 100 en 100)"))
                    while hora2<1200 or hora2>2400 or hora2%100!=0:
                        print("La hora ingresada no se encuentra en el rango (1200 a 2400, de 100 en 100)")
                        hora2=int(input("ingrese en formato militar la hora que desea alquilar (1200 a 2400, de 100 en 100)"))
                    if hora2 in matriz[fila2]:
                        columna2=(hora2-1200)//100
                        matriz[fila2][columna2]=0
                        matrizn[fila2][columna2]=0
                        print("cancelación realizada con exito: cancha de futbol",cancha,"de las",hora,"horas a nombre de:",nombre)
                        print("canchas",matriz)
                        print()
                        print("nombres de reservas",matrizn)
                    else:
                        print("ese horario no se encuentra alquilado")
                    señ2=int(input("ingrese cualquier numero entero si desea continuar o -1 para salir"))
                    if señ2==-1:
                        signal=-1
                    else:
                        signal=0
                else:
                    signal=-1

        elif herramienta==3:
            sigo=0
            while sigo==0:
                precios,horas=funmod.cargar_precios_canchas()
                cobro=funmod.calcular_cantidad_a_pagar(precios,horas)
                print("cantidad a pagar: $",cobro)
                sigo2=int(input("ingrese cualquier numero entero si desea continuar o -1 para salir"))
                if sigo2==-1:
                    sigo=-1
                else:
                    sigo=0
        else:
            general=-1
        
    
matrizper=[[0 for _ in range(13)] for _ in range(3)]
matriznombre=[[0 for _ in range(13)] for _ in range(3)]
if __name__="__main__":
    main(matrizper,matriznombre)

"""agregar lista o matriz, ademas de las dos que ya tenemos, donde acumulamos la recaudacion por canchas y por horarios
    agregar funcion ListadoCanchas de: cantidad de formas de pago(tarjeta 10% mas), cancha de mayor recaudacion y menor 
    recaudacion, incremento por incluir la tarjeta.
    cambiar el precio de las canchas por un random.randint"""














