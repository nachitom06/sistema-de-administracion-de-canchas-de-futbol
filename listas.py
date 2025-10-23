import funmod
import json
import pathlib

def cargar_cualvendemas(cualvendemas):
    if not cualvendemas.exists():
        with open(cualvendemas,"wt",encoding="utf-8") as leto:
            leto.write("entradasliga,0\n")
            leto.write("entradastorneo,0\n")
        return {"entradasliga":0,"entradastorneo":0}
    else:
        dat={}
        try:
            with open(cualvendemas,"rt",encoding="utf-8") as forreal:
                for linea in forreal:
                    clave,valor=linea.strip().split(",")
                    dat[clave]=int(valor)
            return dat
        except OSError as msj:
            print(msj)
            return {}
def guardar_cualvendemas(dat,cualvendemas):
    try: 
        with open(cualvendemas,"wt",encoding="utf-8") as forreal:
            for clave,valor in dat.items():
                forreal.write(f"{clave},{valor}\n")
    except OSError as men:
        print(men)
def cargar_entradasvendidas(entradasvendidas):
    if not entradasvendidas.exists():
        with open(entradasvendidas,"wt",encoding="utf-8") as ferreal:
            ferreal.write("vip,0\n")
            ferreal.write("platea,0\n")
            ferreal.write("popular,0\n")
        return {"vip":0,"platea":0,"popular":0}
    else:
        pet={}
        try:
            with open(entradasvendidas,"rt",encoding="utf-8") as forreal:
                for linea in forreal:
                    clave,valor=linea.strip().split(",")
                    pet[clave]=int(valor)
            return pet
        except OSError as msj:
            print(msj)
            return {}
def guardar_entradasvendidas(dat,entradasvendidas):
    try: 
        with open(entradasvendidas,"wt",encoding="utf-8") as forreal:
            for clave,valor in dat.items():
                forreal.write(f"{clave},{valor}\n")
    except OSError as men:
        print(men)
def cargar_cualreserva(cualreserva):
    if not cualreserva.exists():
        with open(cualreserva,"wt",encoding="utf-8") as forlit:
            forlit.write("fut5,0\n")
            forlit.write("fut8,0\n")
            forlit.write("fut11,0\n")
        return {"fut5":0,"fut8":0,"fut11":0}
    else:
        det={}
        try:
            with open(cualreserva,"rt",encoding="utf-8") as ferlit:
                for linea in ferlit:
                    clave,valor=linea.strip().split(",")
                    det[clave]=int(valor)
            return det
        except OSError as msj:
            print(msj)
            return {}
def guardar_cualreserva(dat,cualreserva):
    try: 
        with open(cualreserva,"wt",encoding="utf-8") as forreal:
            for clave,valor in dat.items():
                forreal.write(f"{clave},{valor}\n")
    except OSError as men:
        print(men)
def cargar_sponsorsuso(sponsorsuso):
    if not sponsorsuso.exists():
        with open(sponsorsuso,"wt",encoding="utf-8") as ferlot:
            ferlot.write("entrada,0\n")
            ferlot.write("arco izquiero,0\n")
            ferlot.write("arco derecho,0\n")
            ferlot.write("gradas lado izquierdo,0\n")
            ferlot.write("gradas lado derecho,0\n")
            ferlot.write("fachada de club,0\n")
        return {"entrada":0,"arco izquiero":0,"arco derecho":0,"gradas lado izquierdo":0,"gradas lado derecho":0,"fachada de club":0}
    else:
        lette={}
        try:
            with open(sponsorsuso,"rt",encoding="utf-8") as forreal:
                for linea in forreal:
                    clave,valor=linea.strip().split(",")
                    lette[clave]=int(valor)
            return lette
        except OSError as msj:
            print(msj)
            return {}
def guardar_sponsorsuso(dat,sponsorsuso):
    try: 
        with open(sponsorsuso,"wt",encoding="utf-8") as forreal:
            for clave,valor in dat.items():
                forreal.write(f"{clave},{valor}\n") 
    except OSError as men:
        print(men)
def cargar_bitacora(bitacora):
    if not bitacora.exists():
        bitacora.touch()
def guardar_bitacora(user,nuevo,datadeltiempo,bitacora):
    with open(bitacora,"at",encoding="utf-8") as forreal3:
        forreal3.write(f"{user},{nuevo},{datadeltiempo}")
        forreal3.write("\n")
def guardar_matirzpe(matrizpe,archivo):
    try:
        with open(archivo,"wt",encoding="utf-8") as matrices:
            json.dump(matrizpe,matrices,ensure_ascii=False, indent=2)
    except OSError as men:
        print(men)
def guardar_matirznombr(matriznombr,archivo2):
    try:
        with open(archivo2,"wt",encoding="utf-8") as matrices2:
            json.dump(matriznombr,matrices2,ensure_ascii=False, indent=2)
    except OSError as men:
        print(men)
def cargar_matrizpe(archivo):
    if not archivo.exists():
        matrizcita=[[0 for _ in range(13)] for _ in range(3)]
        guardar_matirzpe(matrizcita)
        return matrizcita
    else:
        try:
            with open(archivo,"rt",encoding="utf-8") as literal:
                return json.load(literal)
        except OSError as men:
            print(men)
            matrizcita=[[0 for _ in range(13)] for _ in range(3)]
            guardar_matirzpe(matrizcita)
            return matrizcita
def cargar_matriznombr(archivo2):
    if not archivo2.exists():
        matrizcita2=[[0 for _ in range(13)] for _ in range(3)]
        guardar_matirznombr(matrizcita2)
        return matrizcita2
    else:
        try:
            with open(archivo2,"rt",encoding="utf-8") as literal2:
                return json.load(literal2)
        except OSError as men:
            print(men)
            matrizcita2=[[0 for _ in range(13)] for _ in range(3)]
            guardar_matirznombr(matrizcita2)
            return matrizcita2
def guardar_reportes(datos,reportes):
    try:
        with open(reportes,"wt",encoding="utf-8") as datal:
            json.dump(datos,datal,ensure_ascii=False, indent=2)
    except OSError as men:
        print(men)
def cargar_reportes(reportes):
    if not reportes.exists():
        datos={"listcanchas":[5,8,11],
        "listhorario":[1200,1300,1400,1500,1600,1700,1800,1900,2000,2100,2200,2300,2400],
        "listformpago":["e","mp"],
        "listrecaudacioncanchas":[0 for x in range(3)],
        "listrecaudacionhorarios":[0 for x in range(13)],
        "listrecaudacionformpago":[0 for x in range(2)],
        "listcantcanchas":[0 for x in range(3)],
        "listcanthorarios":[0 for x in range(13)],
        "listcantformpago":[0 for x in range(2)],
        "listaclientes":[],
        "listadiezporciento":[],
        "recaudacionestorneo":[],
        "recaudacionesliga":[],
        "pagoentrada":[]}
        guardar_reportes(datos)
        return datos
    else:
        try:
            with open(reportes,"rt",encoding="utf-8") as datal2:
                return json.load(datal2)
        except OSError as men:
            print(men)
            datos={"listcanchas":[5,8,11],
            "listhorario":[1200,1300,1400,1500,1600,1700,1800,1900,2000,2100,2200,2300,2400],
            "listformpago":["e","mp"],
            "listrecaudacioncanchas":[0 for x in range(3)],
            "listrecaudacionhorarios":[0 for x in range(13)],
            "listrecaudacionformpago":[0 for x in range(2)],
            "listcantcanchas":[0 for x in range(3)],
            "listcanthorarios":[0 for x in range(13)],
            "listcantformpago":[0 for x in range(2)],
            "listaclientes":[],
            "listadiezporciento":[],
            "recaudacionestorneo":[],
            "recaudacionesliga":[],
            "pagoentrada":[]}
            guardar_reportes(datos)
            return datos
def cargar_listaliga(listaliga):
    if not listaliga.exists():
        lista10=[0 for _ in range(20)]
        guardar_listaliga(lista10)
        return lista10
    else:
        try:
            with open(listaliga,"rt",encoding="utf-8") as bro:
                return json.load(bro)
        except OSError as men:
            print(men)
            lista10=[0 for _ in range(20)]
            guardar_listaliga(lista10)
            return lista10
def guardar_listaliga(lista10,listaliga):
    try:
        with open(listaliga,"wt",encoding="utf-8") as listadelaliga:
            json.dump(lista10,listadelaliga,ensure_ascii=False, indent=2)
    except OSError as men:
        print(men)
def cargar_torneooficial(torneooficial):
    if not torneooficial.exists():
        lista11=[]
        guardar_torneooficial(lista11)
        return lista11
    else:
        try:
            with open(torneooficial,"rt",encoding="utf-8") as bro2:
                return json.load(bro2)
        except OSError as men:
            print(men)
            lista11=[]
            guardar_torneooficial(lista11)
            return lista11
def guardar_torneooficial(lista11,torneooficial):
    try:
        with open(torneooficial,"wt",encoding="utf-8") as listadeltorneo:
            json.dump(lista11,listadeltorneo,ensure_ascii=False, indent=2)
    except OSError as men:
        print(men)
def cargar_torneooficial2(torneooficial2):
    if not torneooficial2.exists():
        lista11=[]
        guardar_torneooficial2(lista11)
        return lista11
    else:
        try:
            with open(torneooficial2,"rt",encoding="utf-8") as bro2:
                return json.load(bro2)
        except OSError as men:
            print(men)
            lista11=[]
            guardar_torneooficial2(lista11)
            return lista11
def guardar_torneooficial2(lista11,torneooficial2):
    try:
        with open(torneooficial2,"wt",encoding="utf-8") as listadeltorneo:
            json.dump(lista11,listadeltorneo,ensure_ascii=False, indent=2)
    except OSError as men:
        print(men)
def cargar_torneooficial3(torneooficial3):
    if not torneooficial3.exists():
        lista11=[]
        guardar_torneooficial3(lista11)
        return lista11
    else:
        try:
            with open(torneooficial3,"rt",encoding="utf-8") as bro2:
                return json.load(bro2)
        except OSError as men:
            print(men)
            lista11=[]
            guardar_torneooficial3(lista11)
            return lista11
def guardar_torneooficial3(lista11,torneooficial3):
    try:
        with open(torneooficial3,"wt",encoding="utf-8") as listadeltorneo:
            json.dump(lista11,listadeltorneo,ensure_ascii=False, indent=2)
    except OSError as men:
        print(men)
def cargar_torneooficial4(torneooficial4):
    if not torneooficial4.exists():
        lista11=[]
        guardar_torneooficial4(lista11)
        return lista11
    else:
        try:
            with open(torneooficial4,"rt",encoding="utf-8") as bro2:
                return json.load(bro2)
        except OSError as men:
            print(men)
            lista11=[]
            guardar_torneooficial3(lista11)
            return lista11
def guardar_torneooficial4(lista11,torneooficial4):
    try:
        with open(torneooficial4,"wt",encoding="utf-8") as listadeltorneo:
            json.dump(lista11,listadeltorneo,ensure_ascii=False, indent=2)
    except OSError as men:
        print(men)
def cargar_listatorneo(listatorneo):
    if not listatorneo.exists():
        lista11=[0 for _ in range(16)]
        guardar_listatorneo(lista11)
        return lista11
    else:
        try:
            with open(listatorneo,"rt",encoding="utf-8") as bro2:
                return json.load(bro2)
        except OSError as men:
            print(men)
            lista11=[0 for _ in range(16)]
            guardar_listatorneo(lista11)
            return lista11
def guardar_listatorneo(lista11,listatorneo):
    try:
        with open(listatorneo,"wt",encoding="utf-8") as listadeltorneo:
            json.dump(lista11,listadeltorneo,ensure_ascii=False, indent=2)
    except OSError as men:
        print(men)
def cargar_usuarios(comprobacion):
    usuarios={}
    administra={"nachom06":140906}
    if not comprobacion.exists():
        if comprobacion==pathlib.Path("admininicio.txt"):
            return administra
        else: 
            return usuarios
    else:
        try:
            with open(comprobacion,"r",encoding="utf-8") as dale0:
                for linea in dale0:
                    usuario,contraseña=linea.strip().split(":")
                    usuarios[usuario]=int(contraseña)
            return usuarios
        except OSError as men:
            print(men)
            return usuarios
def guardar_usuarios(dale20,user):
    try:
        with open(dale20,"w",encoding="utf-8") as lit:
            for usuario,contraseña in user.items():  
                lit.write(f"{usuario}:{contraseña}\n")
    except OSError as men:
        print(men)
def cargar_torneo(torneito):
    if not torneito.exists():
        datazo={"fasegrupos1":[],"fasegrupos2":[],"fasegrupos3":[],"fasegrupos4":[],"cuartos":[],"semis":[],"final":[]}
        guardar_torneo(datazo)
        return datazo
    else:
        try:
            with open(torneito,"rt",encoding="utf-8") as mesengger:
                return json.load(mesengger)
        except OSError as men:
            print(men)
            datazo={"fasegrupos1":[],"fasegrupos2":[],"fasegrupos3":[],"fasegrupos4":[],"cuartos":[],"semis":[],"final":[]}
            guardar_torneo(datazo)
            return datazo
def guardar_torneo(datos,torneito):
    try:
        with open(torneito,"wt",encoding="utf-8") as mesengger2:
            json.dump(datos,mesengger2,ensure_ascii=False,indent=2)
    except OSError as men:
        print(men)
def cargar_liga(liguita):
    if not liguita.exists():
        datazo2={"liga":[]}
        guardar_liga(datazo2)
        return datazo2
    else:
        try:
            with open(liguita,"rt",encoding="utf-8") as mesengger3:
                return json.load(mesengger3)
        except OSError as men:
            print(men)
            datazo2={"liga":[]}
            guardar_liga(datazo2)
            return datazo2
def guardar_liga(datos2,liguita):
    try:
        with open(liguita,"wt",encoding="utf-8") as mesengger4:
            json.dump(datos2,mesengger4,ensure_ascii=False,indent=2)
    except OSError as men:
        print(men)
def cargar_partidosdeliga(fixture):
    if not fixture.exists():
        dirigir={"fixture":[]}
        guardar_partidosdeliga(dirigir)
        return dirigir
    else:
        try:
            with open(fixture,"rt",encoding="utf-8") as berni2:
                return json.load(berni2)
        except OSError as men:
            print(men)
            dirigir={"fixture":[]}
            guardar_partidosdeliga(dirigir)
            return dirigir
def guardar_partidosdeliga(lato,fixture):
    try:
        with open(fixture,"wt",encoding="utf-8") as berni:
            json.dump(lato,berni,ensure_ascii=False,indent=2)
    except OSError as men:
        print(men)
def cargar_partidosdetorneo(fixturetorneo):
    if not fixturetorneo.exists():
        dirigir2={"fixturefasegrupos1":[],"fixturefasegrupos2":[],"fixturefasegrupos3":[],"fixturefasegrupos4":[],"fixturecuartos":[],"fixturesemis":[],"fixturefinal":[]}
        guardar_partidosdetorneo(dirigir2)
        return dirigir2
    else:
        try:
            with open(fixturetorneo,"rt",encoding="utf-8") as berni4:
                return json.load(berni4)
        except OSError as men:
            print(men)
            dirigir2={"fixturefasegrupos1":[],"fixturefasegrupos2":[],"fixturefasegrupos3":[],"fixturefasegrupos4":[],"fixturecuartos":[],"fixturesemis":[],"fixturefinal":[]}
            guardar_partidosdetorneo(dirigir2)
            return dirigir2
def guardar_partidosdetorneo(lato2,fixturetorneo):
    try:
        with open(fixturetorneo,"wt",encoding="utf-8") as berni3:
            json.dump(lato2,berni3,ensure_ascii=False,indent=2)
    except OSError as men:
        print(men)
def cargar_sponsors(sponsors):
    if not sponsors.exists():
        totalsponsors={"listasponsorszona":[1,2,3,4,5,6],"listasponsors":["entrada","arco izquiero","arco derecho","gradas lado izquierdo","gradas lado derecho","fachada de club"],"disponibilidad":[0 for i in range(6)],"listadisponibilidad":["disponible","no disponible"],"nombresponsor":[0 for i in range(6)]}
        guardar_sponsors(totalsponsors)
        return totalsponsors
    else:
        try:
            with open(sponsors,"rt",encoding="utf-8") as spo:
                return json.load(spo)
        except OSError as men:
            print(men)
            totalsponsors={"listasponsorszona":[1,2,3,4,5,6],"listasponsors":["entrada","arco izquiero","arco derecho","gradas lado izquierdo","gradas lado derecho","fachada de club"],"disponibilidad":[0 for i in range(6)],"listadisponibilidad":["disponible","no disponible"],"nombresponsor":[0 for i in range(6)]}
            guardar_sponsors(totalsponsors)
            return totalsponsors
def guardar_sponsors(datos20,sponsors):
    try:
        with open(sponsors,"wt",encoding="utf-8") as spo2:
            json.dump(datos20,spo2,ensure_ascii=False,indent=2)
    except OSError as men:
        print(men)
def cargar_entradas(entradonas):
    if not entradonas.exists():
        dati={"vip":10,"platea":50,"popular":200}
        guardar_entradas(dati)
        return dati
    else:
        try:
            with open(entradonas,"rt",encoding="utf-8") as moned:
                return json.load(moned)
        except OSError as men:
            print(men)
            dati={"vip":10,"platea":50,"popular":200}
            guardar_entradas(dati)
            return dati
def guardar_entradas(datilo,entradonas):
    try:
        with open(entradonas,"wt",encoding="utf-8") as foreigner:
            json.dump(datilo,foreigner,ensure_ascii=False,indent=2)
    except OSError as men:
            print(men)
def cargar_entradastorneo(entradonas2):
    if not entradonas2.exists():
        dati2={"vip":10,"platea":50,"popular":200}
        guardar_entradastorneo(dati2)
        return dati2
    else:
        try:
            with open(entradonas2,"rt",encoding="utf-8") as moned2:
                return json.load(moned2)
        except OSError as men:
            print(men)
            dati2={"vip":10,"platea":50,"popular":200}
            guardar_entradastorneo(dati2)
            return dati2
def guardar_entradastorneo(datilo2,entradonas2):
    try:
        with open(entradonas2,"wt",encoding="utf-8") as foreigner2:
            json.dump(datilo2,foreigner2,ensure_ascii=False,indent=2)
    except OSError as men:
        print(men)
def cargar_estadisticas(expediente):
    if not expediente.exists():
        date={"entradasvendidas":{"vip":0,"platea":0,"popular":0},"sponsorsuso":{"entrada":0,"arco izquiero":0,"arco derecho":0,"gradas lado izquierdo":0,"gradas lado derecho":0,"fachada de club":0},"cualvendemas":{"entradasliga":0,"entradastorneo":0},"cualreserva":{"fut5":0,"fut8":0,"fut11":0}}
        guardar_estadisticas(date)
        return date
    else:
        try:
            with open(expediente,"rt",encoding="utf-8") as fragile:
                return json.load(fragile)
        except OSError as men:
            print(men)
            date={"entradasvendidas":{"vip":0,"platea":0,"popular":0},"sponsorsuso":{"entrada":0,"arco izquiero":0,"arco derecho":0,"gradas lado izquierdo":0,"gradas lado derecho":0,"fachada de club":0},"cualvendemas":{"entradasliga":0,"entradastorneo":0},"cualreserva":{"fut5":0,"fut8":0,"fut11":0}}
            guardar_estadisticas(date)
            return date
def guardar_estadisticas(usito,expediente):
    try:
        with open(expediente,"wt",encoding="utf-8") as fragile2:
            json.dump(usito,fragile2,ensure_ascii=False,indent=2)
    except OSError as men:
        print(men)
def cargar_resultadosidita(resultadosidita):
    if not resultadosidita.exists():
        datazo2={"resultadosidita":[]}
        guardar_resultadosidita(datazo2)
        return datazo2
    else:
        try:
            with open(resultadosidita,"rt",encoding="utf-8") as mesengger3:
                return json.load(mesengger3)
        except OSError as men:
            print(men)
            datazo2={"resultadosidita":[]}
            guardar_liga(datazo2)
            return datazo2
def guardar_resultadosidita(datos2,resultadosidita):
    try:
        with open(resultadosidita,"wt",encoding="utf-8") as mesengger4:
            json.dump(datos2,mesengger4,ensure_ascii=False,indent=2)
    except OSError as men:
        print(men)
def cargar_resultadosvueltita(resultadosvueltita):
    if not resultadosvueltita.exists():
        datazo2={"resultadosvueltita":[]}
        guardar_resultadosvueltita(datazo2)
        return datazo2
    else:
        try:
            with open(resultadosvueltita,"rt",encoding="utf-8") as mesengger3:
                return json.load(mesengger3)
        except OSError as men:
            print(men)
            datazo2={"resultadosvueltita":[]}
            guardar_liga(datazo2)
            return datazo2
def guardar_resultadosvueltita(datos2,resultadosvueltita):
    try:
        with open(resultadosvueltita,"wt",encoding="utf-8") as mesengger4:
            json.dump(datos2,mesengger4,ensure_ascii=False,indent=2)
    except OSError as men:
        print(men)
def cargar_fixtureidita(fixtureidita):
    if not fixtureidita.exists():
        datazo2={"fixtureidita":[]}
        guardar_fixtureidita(datazo2)
        return datazo2
    else:
        try:
            with open(fixtureidita,"rt",encoding="utf-8") as mesengger3:
                return json.load(mesengger3)
        except OSError as men:
            print(men)
            datazo2={"fixtureidita":[]}
            guardar_liga(datazo2)
            return datazo2
def guardar_fixtureidita(datos2,fixtureidita):
    try:
        with open(fixtureidita,"wt",encoding="utf-8") as mesengger4:
            json.dump(datos2,mesengger4,ensure_ascii=False,indent=2)
    except OSError as men:
        print(men)
def cargar_fixturevueltita(fixturevueltita):
    if not fixturevueltita.exists():
        datazo2={"fixturevueltita":[]}
        guardar_fixturevueltita(datazo2)
        return datazo2
    else:
        try:
            with open(fixturevueltita,"rt",encoding="utf-8") as mesengger3:
                return json.load(mesengger3)
        except OSError as men:
            print(men)
            datazo2={"fixturevueltita":[]}
            guardar_liga(datazo2)
            return datazo2
def guardar_fixturevueltita(datos2,fixturevueltita):
    try:
        with open(fixturevueltita,"wt",encoding="utf-8") as mesengger4:
            json.dump(datos2,mesengger4,ensure_ascii=False,indent=2)
    except OSError as men:
        print(men)
def cargar_rutas_archivos():
    cualvendemas=pathlib.Path("cualvendemas.csv")
    entradasvendidas=pathlib.Path("entradasvendidas.csv")
    fixturevueltita=pathlib.Path("fixturevueltita.json")
    fixtureidita=pathlib.Path("fixtureidita.json")
    resultadosvueltita=pathlib.Path("resultadosvueltita.json")
    resultadosidita=pathlib.Path("resultadosidita.json")
    expediente=pathlib.Path("estadisticas.json")
    entradonas2=pathlib.Path("entradastorneo.json")
    entradonas=pathlib.Path("entradas.json")
    sponsors=pathlib.Path("sponsors.json")
    fixturetorneo=pathlib.Path("fixturetorneo.json")
    fixture=pathlib.Path("fixture.json")
    liguita=pathlib.Path("liguita.json")
    torneito=pathlib.Path("torneo.json")
    torneooficial4=pathlib.Path("torneooficial4.json")
    torneooficial3=pathlib.Path("torneooficial3.json")
    listatorneo=pathlib.Path("inscripciones_torneo.json")
    listaliga=pathlib.Path("inscripciones_liga.json")
    torneooficial=pathlib.Path("torneooficial.json")
    torneooficial2=pathlib.Path("torneooficial2.json")
    reportes=pathlib.Path("reportes.json")
    cualreserva=pathlib.Path("cualreserva.csv")
    sponsorsuso=pathlib.Path("sponsorsuso.csv")
    bitacora=pathlib.Path("bitacora.txt")
    archivo=pathlib.Path("reservas.json")
    archivo2=pathlib.Path("nombres.json")
    return cualvendemas,entradasvendidas,fixturevueltita,fixtureidita,resultadosvueltita,resultadosidita,expediente,entradonas2,entradonas,sponsors,fixturetorneo,fixture,liguita,torneito,torneooficial4,torneooficial3,listatorneo,listaliga,torneooficial,torneooficial2,reportes,cualreserva,sponsorsuso,bitacora,archivo,archivo2
def cargar_entradasdelisto():
    disponible={"vip","platea","popular"}
    ocupadas=set()
    disponibletorneo={"vip","platea","popular"}
    ocupadastorneo=set()
    return disponible,ocupadas,disponibletorneo,ocupadastorneo

#esto esta bien, hay que acomodarlo nomas, pero cuando funcione todo
