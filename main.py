
def main(matriz):
    """Objetivo: Se introduce tipo de cancha (F5, F8, F11) Y una hora de en el formato hora militar, como por ejemplo 15:00 PM = 1500, para reservar la cancha. abierto de 12:00Hs a 24:00Hs"""
    sig=0
    while sig==0:
        fila=0
        cancha=int(input("Ingrese el número de cancha que desea elegir (5, 8, 11)"))
        while cancha not in[5,8,11]:
            print("Error, el numero de cancha seleccionado no se encuentra")
            cancha=int(input("Ingrese el número de cancha que desea elegir (5, 8, 11)"))
        if cancha==5:
            fila=0
        elif cancha==8:
            fila=1
        else:
            fila=2
         """print(matriz[fila])
        dia=int(input("ingrese el día en el cual desea reservar"))
        while dia<1 or dia>31:
            print("error, numero ingresado fuera del rango")
            dia=int(input("ingrese el día en el cual desea reservar"))
        print(matriz[fila][dia-1],"los horarios que se muestran ya estan tomados")""" #2da etapa
        print(matriz[fila],"los horarios que se muestran ya estan tomados")
        hora=int(input("ingrese en formato militar la hora que desea alquilar (1200 a 2400, de 100 en 100)"))
        while hora<1200 or hora>2400 or hora%100!=0:
            print("La hora ingresada no se encuentra en el rango (1200 a 2400, de 100 en 100)")
            hora=int(input("ingrese en formato militar la hora que desea alquilar (1200 a 2400, de 100 en 100)"))
        if hora not in matriz[fila]:
            columna=(hora-1200)//100
            matriz[fila][columna]=hora
            print("reserva realizada con exito: cancha de futbol",cancha,"a las",hora,"horas")
        else:
            print("ese horario ya esta ocupado")
        señ=int(input("ingrese cualquier numero entero si desea continuar o -1 para salir"))
        if señ==-1:
            sig=-1
        else:
            sig=0
    cargar_precios_canchas()
    cobro=calcular_cantidad_a_pagar(precio,canthoras)
    print("cantidad a pagar: $",cobro)
    
matrizper=[[0 for _ in range(13)] for _ in range(3)]
main(matrizper)




