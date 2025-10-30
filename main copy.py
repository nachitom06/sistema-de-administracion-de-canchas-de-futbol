import funmod
import user
import admin
import listas
import pathlib
def main():
    """Objetivo: Se introduce un número (1 reservar canchas, 2 cancelar la reservacion de canchas, 3 calcular cobro, 4 mostrar reportes, -1 para finalizar programa)"""
    funmod.dar_bienvenida()
    administrador=0
    letek234,cantidadcaracteres,cantidadcontra=1,10,6
    comprobacionusuario=pathlib.Path("archivoinicio.txt")
    comprobacionadmin=pathlib.Path("admininicio.txt")
    usuarios=listas.cargar_usuarios(comprobacionusuario)
    administradorclase=listas.cargar_usuarios(comprobacionadmin)
    class DemasiadosIntentosError(Exception):
        pass
    print("inicio de sesion")
    while True:
        try:
            inicio=int(input("ingrese 0 para iniciar sesion, 1 para registrar una cuenta: "))
            while inicio<0 or inicio>1:
                print("error numero ingresado fuera del rango")
                inicio=int(input("ingrese 0 para iniciar sesion, 1 para registrar una cuenta: "))
        except ValueError as mensaje8:
            print(mensaje8)
            continue
        if inicio==0:
            usuario=input("ingrese nombre de usuario: ").strip()
            if usuario in usuarios:
                """si coincide con un numbre de usuario existente hay que poner que revise y todo lo de la contraseña"""
                conteo10=0
                while True:
                    reinicio=False
                    try:
                        contra=int(input("ingrese su contraseña(6 digitos): "))
                    except ValueError as mensaje9:
                        print(mensaje9)
                        continue
                    if contra==usuarios[usuario]:#no coincide con el archivo, separar administrador y usuario
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
                        contra=int(input("ingrese su contraseña(6 digitos): "))
                    except ValueError as mensaje9:
                        print(mensaje9)
                        continue
                    if contra==administradorclase[usuario]:#no coincide con el archivo, separar administrador y usuario
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
            letek=funmod.calcular_cantidad_posiblesdecontraseñas(letek234,cantidadcaracteres,cantidadcontra)
            print(f"cantidad posibles de contraseñas de 6 digitos: {letek}")
            nuevacontra=input("ingresar su contraseña(solo numeros, 6 digitos): ").strip()
            while nuevacontra.isalpha() or len(nuevacontra)!=6:
                print("error, no tiene 6 digitos o no puso solo numeros")
                nuevacontra=input("ingresar su contraseña(solo numeros, 6 digitos): ").strip()
            nuevacontra=int(nuevacontra)
            nitro[nuevousuario]=nuevacontra
            listas.guardar_usuarios(comprobacionusuario,nitro)
            usuarios=listas.cargar_usuarios(comprobacionusuario)
            print("usuario registrado con exito")

    if administrador==1:
        admin.admin(usuario)
    else:
        user.user(usuario)

if __name__=="__main__":
    main()



#hay que revisar si funciona bien el 8(sacarle la opcion de sponsors torneo, dejar solo sponsors liga),falta revisar el 10 un poco 
    #para ver si funciona del todo. 
    #1,2,3,4,5,6,7,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31 funcionan bien por el momento, para iniciarlo se pone primero 6, despues 7, despues 9 y despues 10
#si no se tienen los archivos, para el torneo primero se rellena los equipos 14,calcular partidos 15,resultados aleatorios 16,tabla fase de grupos 17,
#calcular cuartos 18,cuartos resultados 23,calcular semifinal 19,semifinal resultados 24,calcular final torneo 20,final resultados 25,campeon final torneo 21 
#se puede revisar una vez mas antes de entregar
