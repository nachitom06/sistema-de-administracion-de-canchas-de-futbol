import funmod
import json
import pathlib
todo={"matriztorneos":[[0 for _ in range(4)] for _ in range(12)],"nombredelaliga":"Super Liga Nacional","nombredeltorneo":"Torneo Nacional","cuartosresultados":[],"ganadorescuartos":[],"ganadoressemis":[],"semisresultados":[],"finalresultados":[],"ganadorfinal":[],"campeontorneo":[],"campeones":[],"fasegrupos1":[0 for _ in range(4)],"fasegrupos2":[0 for _ in range(4)],"fasegrupos3":[0 for _ in range(4)],"fasegrupos4":[0 for _ in range(4)],"fasegrupo1partidos":[],"fasegrupo2partidos":[],"fasegrupo3partidos":[],"fasegrupo4partidos":[],"cuartos":[],"semis":[],"final":[],"fasegrupos1resultados":[],"fasegrupos2resultados":[],"fasegrupos3resultados":[],"fasegrupos4resultados":[],"contadorpartidosfase1":[],"contadorpartidosfase2":[],"contadorpartidosfase3":[],"contadorpartidosfase4":[],"fixtureida":[],"recaudacionesliga":[],"recaudacionestorne":[],"fasegrupos1aux":[],"fasegrupos2aux":[],"fasegrupos3aux":[],"fasegrupos4aux":[],"cuartosaux":[],"semisaux":[],"finalaux":[],"fixturevuelta":[],"puntosequipos":[],"partidosjugados":[0 for _ in range(20)],"ganados":[0 for _ in range(20)],"empatados":[0 for _ in range(20)],"perdidos":[0 for _ in range(20)],"puntos":[0 for _ in range(20)],"golesfavor":[0 for _ in range(20)],"golescontra":[0 for _ in range(20)],"diferenciagol":[0 for _ in range(20)],"resultadosida":[],"partidosjugadosfase1":[0 for _ in range(20)],"ganadosfase1":[0 for _ in range(20)],"empatadosfase1":[0 for _ in range(20)],"perdidosfase1":[0 for _ in range(20)],"puntosfase1":[0 for _ in range(20)],"golesfavorfase1":[0 for _ in range(20)],"golescontrafase1":[0 for _ in range(20)],"diferenciagolfase1":[0 for _ in range(20)],"partidosjugadosfase2":[0 for _ in range(20)],"ganadosfase2":[0 for _ in range(20)],"empatadosfase2":[0 for _ in range(20)],"perdidosfase2":[0 for _ in range(20)],"puntosfase2":[0 for _ in range(20)],"golesfavorfase2":[0 for _ in range(20)],"golescontrafase2":[0 for _ in range(20)],"diferenciagolfase2":[0 for _ in range(20)],"partidosjugadosfase3":[0 for _ in range(20)],"ganadosfase3":[0 for _ in range(20)],"empatadosfase3":[0 for _ in range(20)],"perdidosfase3":[0 for _ in range(20)],"puntosfase3":[0 for _ in range(20)],"golesfavorfase3":[0 for _ in range(20)],"golescontrafase3":[0 for _ in range(20)],"diferenciagolfase3":[0 for _ in range(20)],"partidosjugadosfase4":[0 for _ in range(20)],"ganadosfase4":[0 for _ in range(20)],"empatadosfase4":[0 for _ in range(20)],"perdidosfase4":[0 for _ in range(20)],"puntosfase4":[0 for _ in range(20)],"golesfavorfase4":[0 for _ in range(20)],"golescontrafase4":[0 for _ in range(20)],"diferenciagolfase4":[0 for _ in range(20)],"contadorpartidosida":[i for i in range(1,191)],"resultadosvuelta":[],"contadorpartidosvuelta":[x for x in range(1,191)],"nombresaleatoriosequipos":["Atlético del Sur", "Club Deportivo Aurora", "Racing Federal", "Juventud Unida","Sportivo Central", "Unión del Norte", "Estrella Roja", "Los Dragones FC","San Martín Juniors", "Nueva Esperanza", "Club Social Libertad", "Huracán del Valle","Defensores de la Costa", "Talleres Unidos", "Los Guerreros", "Boca del Oeste","River Plateño", "Cruz Azul del Sur", "Leones Dorados", "Águilas Negras","Real Horizonte", "Deportivo América", "Universitario Central", "Club Atlético Nacional","Fuerza Joven", "Pumas de la Sierra", "Toros Salvajes", "Estudiantes del Sol","Nueva Generación", "Atlético Popular", "Club Independiente", "San Lorenzo Unido","Deportivo Patria", "Olimpia del Sur", "Cultural Esperanza", "Ciclón Rojo","Guaraní Unido", "Leones del Sur", "Academia del Fútbol", "Sport Boys","Los Gladiadores", "Unión Deportiva Estrella", "Villa Real FC", "Juventud Federal","Defensa y Justicia Social", "Atlético Horizonte", "Deportivo Norteño", "Tigre Blanco","Halcones Verdes", "Nueva Alianza", "San Carlos Juniors", "Atlético Centenario","Los Piratas FC", "Club Deportivo Cosmos", "Juventud Atlética", "Rayo del Sur","Los Titanes", "Sporting Club Federal", "Atlético Ciudadela", "Universitario Unido","Club Social Victoria", "Deportivo Unión", "Santa Fe Atlético", "Real Central","Club Atlético Esperanza", "Independencia FC", "Sportivo Olimpo", "Guerreros del Sol","Águilas Plateadas", "Los Delfines", "Atlético Mundial", "Nueva Roma FC","San José Unido", "Estrella Federal", "Juventud Patriota", "Huracán del Centro","Deportivo Internacional", "Granaderos FC", "Racing Unido", "Unión Deportiva Norte","Atlético Azul", "Fuerza Guerrera", "Los Lobos", "Club Estudiantes Unidos","Rivera FC", "Boca Sur", "Atlético Colonial", "Deportivo Horizonte","Club Nacional Popular", "Los Cóndores", "Sporting Nueva Era", "Juventud del Norte","Atlético Moderno", "Los Pioneros", "Real Metropolitano", "Estrella Joven","Deportivo Victoria", "Unión San Pedro", "Club del Sol", "Atlético Bravo"],"listasponsorszona":[1,2,3,4,5,6],"listasponsors":["entrada","arco izquiero","arco derecho","gradas lado izquierdo","gradas lado derecho","fachada de club"],"disponibilidad":[0 for i in range(6)],"listadisponibilidad":["disponible","no disponible"],"listanombresponsor":[0 for i in range(6)],"recaudaciondiezporciento":0,"disponibilidadtorneo":[0 for i in range(6)],"listanombresponsortorneo":[0 for i in range(6)]
    }
ganados,puntos,perdidos,empatados,golesfavor,golescontra,diferenciagol=[0 for _ in range(20)],[0 for _ in range(20)],[0 for _ in range(20)],[0 for _ in range(20)],[0 for _ in range(20)],[0 for _ in range(20)],[0 for _ in range(20)]

archivo=pathlib.Path("reservas.json")
def guardar_matirzpe(matrizpe):
    try:
        with open(archivo,"w",encoding="utf-8") as matrices:
            json.dump(matrizpe,matrices,ensure_ascii=False, indent=2)
    except IOError as men:
        print(men)
    except PermissionError as men2:
        print(men2)
    except FileNotFoundError as men3:
        print(men3)

archivo2=pathlib.Path("nombres.json")
def guardar_matirznombr(matriznombr):
    try:
        with open(archivo2,"w",encoding="utf-8") as matrices2:
            json.dump(matriznombr,matrices2,ensure_ascii=False, indent=2)
    except IOError as men:
        print(men)
    except PermissionError as men2:
        print(men2)
    except FileNotFoundError as men3:
        print(men3)

def cargar_matrizpe():
    if not archivo.exists():
        matrizcita=[[0 for _ in range(13)] for _ in range(3)]
        guardar_matirzpe(matrizcita)
        return matrizcita
    else:
        try:
            with open(archivo,"r",encoding="utf-8") as literal:
                return json.load(literal)
        except IOError as men:
            print(men)
            matrizcita=[[0 for _ in range(13)] for _ in range(3)]
            guardar_matirzpe(matrizcita)
            return matrizcita
        except PermissionError as men2:
            print(men2)
            matrizcita=[[0 for _ in range(13)] for _ in range(3)]
            guardar_matirzpe(matrizcita)
            return matrizcita
        except FileNotFoundError as men3:
            print(men3)
            matrizcita=[[0 for _ in range(13)] for _ in range(3)]
            guardar_matirzpe(matrizcita)
            return matrizcita
def cargar_matriznombr():
    if not archivo2.exists():
        matrizcita2=[[0 for _ in range(13)] for _ in range(3)]
        guardar_matirznombr(matrizcita2)
        return matrizcita2
    else:
        try:
            with open(archivo2,"r",encoding="utf-8") as literal2:
                return json.load(literal2)
        except IOError as men:
            print(men)
            matrizcita2=[[0 for _ in range(13)] for _ in range(3)]
            guardar_matirznombr(matrizcita2)
            return matrizcita2
        except PermissionError as men2:
            print(men2)
            matrizcita2=[[0 for _ in range(13)] for _ in range(3)]
            guardar_matirznombr(matrizcita2)
            return matrizcita2
        except FileNotFoundError as men3:
            print(men3)
            matrizcita2=[[0 for _ in range(13)] for _ in range(3)]
            guardar_matirznombr(matrizcita2)
            return matrizcita2
        
entradas={"vip":10,"platea":50,"popular":200}
disponible={"vip","platea","popular"}
ocupadas=set()
entradastorneo={"vip":10,"platea":50,"popular":200}
disponibletorneo={"vip","platea","popular"}
ocupadastorneo=set()
matrizper=cargar_matrizpe()
matriznombre=cargar_matriznombr()
reportes=pathlib.Path("reportes.json")
def guardar_reportes(datos):
    try:
        with open(reportes,"w",encoding="utf-8") as datal:
            json.dump(datos,datal,ensure_ascii=False, indent=2)
    except IOError as men:
        print(men)
    except PermissionError as men2:
        print(men2)
    except FileNotFoundError as men3:
        print(men3)
def cargar_reportes():
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
        "recaudacionesliga":[]}
        guardar_reportes(datos)
        return datos
    else:
        try:
            with open(reportes,"r",encoding="utf-8") as datal2:
                return json.load(datal2)
        except IOError as men:
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
            "recaudacionesliga":[]}
            guardar_reportes(datos)
            return datos
        except PermissionError as men2:
            print(men2)
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
            "recaudacionesliga":[]}
            guardar_reportes(datos)
            return datos
        except FileNotFoundError as men3:
            print(men3)
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
            "recaudacionesliga":[]}
            guardar_reportes(datos)
            return datos
   
listcanchas,listhorarios,listformpago,listrecaudacioncanchas,listrecaudacionhorarios,listrecaudacionformpago,listcantcanchas,listcanthorarios,listcantformpago,listaclientes,listadiezporciento,recaudacionestorneo,recaudacionesliga=cargar_reportes()

listaliga=pathlib.Path("inscripciones_liga.json")
def cargar_listaliga():
    if not listaliga.exists():
        lista10=[0 for _ in range(20)]
        guardar_listaliga(lista10)
        return lista10
    else:
        try:
            with open(listaliga,"r",encoding="utf-8") as bro:
                return json.load(bro)
        except IOError as men:
            print(men)
            lista10=[0 for _ in range(20)]
            guardar_listaliga(lista10)
            return lista10
        except PermissionError as men2:
            print(men2)
            lista10=[0 for _ in range(20)]
            guardar_listaliga(lista10)
            return lista10
        except FileNotFoundError as men3:
            print(men3)
            lista10=[0 for _ in range(20)]
            guardar_listaliga(lista10)
            return lista10

def guardar_listaliga(lista10):
    try:
        with open(listaliga,"w",encoding="utf-8") as listadelaliga:
            json.dump(lista10,listadelaliga,ensure_ascii=False, indent=2)
    except IOError as men:
        print(men)
    except PermissionError as men2:
        print(men2)
    except FileNotFoundError as men3:
        print(men3)
listaequiposliga=cargar_listaliga()
torneooficial=pathlib.Path("torneooficial.json")
def cargar_torneooficial():
    if not torneooficial.exists():
        lista11=[]
        guardar_torneooficial(lista11)
        return lista11
    else:
        try:
            with open(torneooficial,"r",encoding="utf-8") as bro2:
                return json.load(bro2)
        except IOError as men:
            print(men)
            lista11=[]
            guardar_torneooficial(lista11)
            return lista11
        except PermissionError as men2:
            print(men2)
            lista11=[]
            guardar_torneooficial(lista11)
            return lista11
        except FileNotFoundError as men3:
            print(men3)
            lista11=[]
            guardar_torneooficial(lista11)
            return lista11

def guardar_torneooficial(lista11):
    try:
        with open(torneooficial,"w",encoding="utf-8") as listadeltorneo:
            json.dump(lista11,listadeltorneo,ensure_ascii=False, indent=2)
    except IOError as men:
        print(men)
    except PermissionError as men2:
        print(men2)
    except FileNotFoundError as men3:
        print(men3)
torneooficial2=pathlib.Path("torneooficial2.json")
def cargar_torneooficial2():
    if not torneooficial2.exists():
        lista11=[]
        guardar_torneooficial2(lista11)
        return lista11
    else:
        try:
            with open(torneooficial2,"r",encoding="utf-8") as bro2:
                return json.load(bro2)
        except IOError as men:
            print(men)
            lista11=[]
            guardar_torneooficial2(lista11)
            return lista11
        except PermissionError as men2:
            print(men2)
            lista11=[]
            guardar_torneooficial2(lista11)
            return lista11
        except FileNotFoundError as men3:
            print(men3)
            lista11=[]
            guardar_torneooficial2(lista11)
            return lista11

def guardar_torneooficial2(lista11):
    try:
        with open(torneooficial2,"w",encoding="utf-8") as listadeltorneo:
            json.dump(lista11,listadeltorneo,ensure_ascii=False, indent=2)
    except IOError as men:
        print(men)
    except PermissionError as men2:
        print(men2)
    except FileNotFoundError as men3:
        print(men3)
torneooficial3=pathlib.Path("torneooficial3.json")
def cargar_torneooficial3():
    if not torneooficial3.exists():
        lista11=[]
        guardar_torneooficial3(lista11)
        return lista11
    else:
        try:
            with open(torneooficial3,"r",encoding="utf-8") as bro2:
                return json.load(bro2)
        except IOError as men:
            print(men)
            lista11=[]
            guardar_torneooficial3(lista11)
            return lista11
        except PermissionError as men2:
            print(men2)
            lista11=[]
            guardar_torneooficial3(lista11)
            return lista11
        except FileNotFoundError as men3:
            print(men3)
            lista11=[]
            guardar_torneooficial3(lista11)
            return lista11

def guardar_torneooficial3(lista11):
    try:
        with open(torneooficial3,"w",encoding="utf-8") as listadeltorneo:
            json.dump(lista11,listadeltorneo,ensure_ascii=False, indent=2)
    except IOError as men:
        print(men)
    except PermissionError as men2:
        print(men2)
    except FileNotFoundError as men3:
        print(men3)
torneooficial4=pathlib.Path("torneooficial4.json")
def cargar_torneooficial4():
    if not torneooficial4.exists():
        lista11=[]
        guardar_torneooficial4(lista11)
        return lista11
    else:
        try:
            with open(torneooficial4,"r",encoding="utf-8") as bro2:
                return json.load(bro2)
        except IOError as men:
            print(men)
            lista11=[]
            guardar_torneooficial3(lista11)
            return lista11
        except PermissionError as men2:
            print(men2)
            lista11=[]
            guardar_torneooficial4(lista11)
            return lista11
        except FileNotFoundError as men3:
            print(men3)
            lista11=[]
            guardar_torneooficial4(lista11)
            return lista11

def guardar_torneooficial4(lista11):
    try:
        with open(torneooficial4,"w",encoding="utf-8") as listadeltorneo:
            json.dump(lista11,listadeltorneo,ensure_ascii=False, indent=2)
    except IOError as men:
        print(men)
    except PermissionError as men2:
        print(men2)
    except FileNotFoundError as men3:
        print(men3)
listatorneo=pathlib.Path("inscripciones_torneo.json")
def cargar_listatorneo():
    if not listatorneo.exists():
        lista11=[0 for _ in range(16)]
        guardar_listatorneo(lista11)
        return lista11
    else:
        try:
            with open(listatorneo,"r",encoding="utf-8") as bro2:
                return json.load(bro2)
        except IOError as men:
            print(men)
            lista11=[0 for _ in range(16)]
            guardar_listatorneo(lista11)
            return lista11
        except PermissionError as men2:
            print(men2)
            lista11=[0 for _ in range(16)]
            guardar_listatorneo(lista11)
            return lista11
        except FileNotFoundError as men3:
            print(men3)
            lista11=[0 for _ in range(16)]
            guardar_listatorneo(lista11)
            return lista11

def guardar_listatorneo(lista11):
    try:
        with open(listatorneo,"w",encoding="utf-8") as listadeltorneo:
            json.dump(lista11,listadeltorneo,ensure_ascii=False, indent=2)
    except IOError as men:
        print(men)
    except PermissionError as men2:
        print(men2)
    except FileNotFoundError as men3:
        print(men3)
listaequipostorneo=cargar_listatorneo()

comprobacionusuario=pathlib.Path("archivoinicio.json")
comprobacionadmin=pathlib.Path("admininicio.json")
def cargar_usuarios(comprobacion):
    if not comprobacion.exists():
        return {}
    try:
        with open(comprobacion,"r",encoding="utf-8") as dale0:
            return json.load(dale0)
    except IOError as men:
        print(men)
        return {}
    except PermissionError as men2:
        print(men2)
        return {}
    except FileNotFoundError as men3:
        print(men3)
        return {}
def guardar_usuarios(dale20,user):
    try:
        with open(dale20,"w",encoding="utf-8") as lit:
            json.dump(user,lit,ensure_ascii=False, indent=2)
    except IOError as men:
        print(men)
    except PermissionError as men2:
        print(men2)
    except FileNotFoundError as men3:
        print(men3)

torneito=pathlib.Path("torneo.json")
def cargar_torneo():
    if not torneito.exists():
        datazo={"fasegrupos1":[],"fasegrupos2":[],"fasegrupos3":[],"fasegrupos4":[],"cuartos":[],"semis":[],"final":[]}
        guardar_torneo(datazo)
        return datazo
    else:
        try:
            with open(torneito,"r",encoding="utf-8") as mesengger:
                return json.load(mesengger)
        except IOError as men:
            print(men)
            datazo={"fasegrupos1":[],"fasegrupos2":[],"fasegrupos3":[],"fasegrupos4":[],"cuartos":[],"semis":[],"final":[]}
            guardar_torneo(datazo)
            return datazo
        except PermissionError as men2:
            print(men2)
            datazo={"fasegrupos1":[],"fasegrupos2":[],"fasegrupos3":[],"fasegrupos4":[],"cuartos":[],"semis":[],"final":[]}
            guardar_torneo(datazo)
            return datazo
        except FileNotFoundError as men3:
            print(men3)
            datazo={"fasegrupos1":[],"fasegrupos2":[],"fasegrupos3":[],"fasegrupos4":[],"cuartos":[],"semis":[],"final":[]}
            guardar_torneo(datazo)
            return datazo
def guardar_torneo(datos):
    try:
        with open(torneito,"w",encoding="utf-8") as mesengger2:
            json.dump(datos,mesengger2,ensure_ascii=False,indent=2)
    except IOError as men:
        print(men)
    except PermissionError as men2:
        print(men2)
    except FileNotFoundError as men3:
        print(men3)

liguita=pathlib.Path("liguita.json")
def cargar_liga():
    if not liguita.exists():
        datazo2={"liga":[]}
        guardar_liga(datazo2)
        return datazo2
    else:
        try:
            with open(liguita,"r",encoding="utf-8") as mesengger3:
                return json.load(mesengger3)
        except IOError as men:
            print(men)
            datazo2={"liga":[]}
            guardar_liga(datazo2)
            return datazo2
        except PermissionError as men2:
            print(men2)
            datazo2={"liga":[]}
            guardar_liga(datazo2)
            return datazo2
        except FileNotFoundError as men3:
            print(men3)
            datazo2={"liga":[]}
            guardar_liga(datazo2)
            return datazo2
def guardar_liga(datos2):
    try:
        with open(liguita,"w",encoding="utf-8") as mesengger4:
            json.dump(datos2,mesengger4,ensure_ascii=False,indent=2)
    except IOError as men:
        print(men)
    except PermissionError as men2:
        print(men2)
    except FileNotFoundError as men3:
        print(men3)


fixture=pathlib.Path("fixture.json")
def cargar_partidosdeliga():
    if not fixture.exists():
        dirigir={"fixture":[]}
        guardar_partidosdeliga(dirigir)
        return dirigir
    else:
        try:
            with open(fixture,"r",encoding="utf-8") as berni2:
                return json.load(berni2)
        except IOError as men:
            print(men)
            dirigir={"fixture":[]}
            guardar_partidosdeliga(dirigir)
            return dirigir
        except PermissionError as men2:
            print(men2)
            dirigir={"fixture":[]}
            guardar_partidosdeliga(dirigir)
            return dirigir
        except FileNotFoundError as men3:
            print(men3)
            dirigir={"fixture":[]}
            guardar_partidosdeliga(dirigir)
            return dirigir
def guardar_partidosdeliga(lato):
    try:
        with open(fixture,"w",encoding="utf-8") as berni:
            json.dump(lato,berni,ensure_ascii=False,indent=2)
    except IOError as men:
        print(men)
    except PermissionError as men2:
        print(men2)
    except FileNotFoundError as men3:
        print(men3)

fixturetorneo=pathlib.Path("fixturetorneo.json")
def cargar_partidosdetorneo():
    if not fixturetorneo.exists():
        dirigir2={"fixturefasegrupos1":[],"fixturefasegrupos2":[],"fixturefasegrupos3":[],"fixturefasegrupos4":[],"fixturecuartos":[],"fixturesemis":[],"fixturefinal":[]}
        guardar_partidosdetorneo(dirigir2)
        return dirigir2
    else:
        try:
            with open(fixturetorneo,"r",encoding="utf-8") as berni4:
                return json.load(berni4)
        except IOError as men:
            print(men)
            dirigir2={"fixturefasegrupos1":[],"fixturefasegrupos2":[],"fixturefasegrupos3":[],"fixturefasegrupos4":[],"fixturecuartos":[],"fixturesemis":[],"fixturefinal":[]}
            guardar_partidosdetorneo(dirigir2)
            return dirigir2
        except PermissionError as men2:
            print(men2)
            dirigir2={"fixturefasegrupos1":[],"fixturefasegrupos2":[],"fixturefasegrupos3":[],"fixturefasegrupos4":[],"fixturecuartos":[],"fixturesemis":[],"fixturefinal":[]}
            guardar_partidosdetorneo(dirigir2)
            return dirigir2
        except FileNotFoundError as men3:
            print(men3)
            dirigir2={"fixturefasegrupos1":[],"fixturefasegrupos2":[],"fixturefasegrupos3":[],"fixturefasegrupos4":[],"fixturecuartos":[],"fixturesemis":[],"fixturefinal":[]}
            guardar_partidosdetorneo(dirigir2)
            return dirigir2
def guardar_partidosdetorneo(lato2):
    try:
        with open(fixturetorneo,"w",encoding="utf-8") as berni3:
            json.dump(lato2,berni3,ensure_ascii=False,indent=2)
    except IOError as men:
        print(men)
    except PermissionError as men2:
        print(men2)
    except FileNotFoundError as men3:
        print(men3)

sponsors=pathlib.Path("sponsors.json")
def cargar_sponsors():
    if not sponsors.exists():
        totalsponsors={"listasponsors":["entrada","arco izquiero","arco derecho","gradas lado izquierdo","gradas lado derecho","fachada de club"],"disponibilidad":[0 for i in range(6)],"listadisponibilidad":["disponible","no disponible"],"nombresponsor":[0 for i in range(6)]}
        guardar_sponsors(totalsponsors)
        return totalsponsors
    else:
        try:
            with open(sponsors,"r",encoding="utf-8") as spo:
                return json.load(spo)
        except IOError as men:
            print(men)
            totalsponsors={"listasponsors":["entrada","arco izquiero","arco derecho","gradas lado izquierdo","gradas lado derecho","fachada de club"],"disponibilidad":[0 for i in range(6)],"listadisponibilidad":["disponible","no disponible"],"nombresponsor":[0 for i in range(6)]}
            guardar_sponsors(totalsponsors)
            return totalsponsors
        except PermissionError as men2:
            print(men2)
            totalsponsors={"listasponsors":["entrada","arco izquiero","arco derecho","gradas lado izquierdo","gradas lado derecho","fachada de club"],"disponibilidad":[0 for i in range(6)],"listadisponibilidad":["disponible","no disponible"],"nombresponsor":[0 for i in range(6)]}
            guardar_sponsors(totalsponsors)
            return totalsponsors
        except FileNotFoundError as men3:
            print(men3)
            totalsponsors={"listasponsors":["entrada","arco izquiero","arco derecho","gradas lado izquierdo","gradas lado derecho","fachada de club"],"disponibilidad":[0 for i in range(6)],"listadisponibilidad":["disponible","no disponible"],"nombresponsor":[0 for i in range(6)]}
            guardar_sponsors(totalsponsors)
            return totalsponsors
def guardar_sponsors(datos20):
    try:
        with open(sponsors,"w",encoding="utf-8") as spo2:
            json.dump(datos20,spo2,ensure_ascii=False,indent=2)
    except IOError as men:
        print(men)
    except PermissionError as men2:
        print(men2)
    except FileNotFoundError as men3:
        print(men3)

entradonas=pathlib.Path("entradas.json")
def cargar_entradas():
    if not entradonas.exists():
        dati={"vip":10,"platea":50,"popular":200}
        guardar_entradas(dati)
        return dati
    else:
        try:
            with open(entradonas,"r",encoding="utf-8") as moned:
                return json.load(moned)
        except IOError as men:
            print(men)
            dati={"vip":10,"platea":50,"popular":200}
            guardar_entradas(dati)
            return dati
        except PermissionError as men2:
            print(men2)
            dati={"vip":10,"platea":50,"popular":200}
            guardar_entradas(dati)
            return dati
        except FileNotFoundError as men3:
            print(men3)
            dati={"vip":10,"platea":50,"popular":200}
            guardar_entradas(dati)
            return dati
def guardar_entradas(datilo):
    try:
        with open(entradonas,"w",encoding="utf-8") as foreigner:
            json.dump(datilo,foreigner,ensure_ascii=False,indent=2)
    except IOError as men:
            print(men)
    except PermissionError as men2:
        print(men2)
    except FileNotFoundError as men3:
        print(men3)

entradonas2=pathlib.Path("entradastorneo.json")
def cargar_entradastorneo():
    if not entradonas2.exists():
        dati2={"vip":10,"platea":50,"popular":200}
        guardar_entradastorneo(dati2)
        return dati2
    else:
        try:
            with open(entradonas2,"r",encoding="utf-8") as moned2:
                return json.load(moned2)
        except IOError as men:
            print(men)
            dati2={"vip":10,"platea":50,"popular":200}
            guardar_entradastorneo(dati2)
            return dati2
        except PermissionError as men2:
            print(men2)
            dati2={"vip":10,"platea":50,"popular":200}
            guardar_entradastorneo(dati2)
            return dati2
        except FileNotFoundError as men3:
            print(men3)
            dati2={"vip":10,"platea":50,"popular":200}
            guardar_entradastorneo(dati2)
            return dati2
def guardar_entradastorneo(datilo2):
    try:
        with open(entradonas2,"w",encoding="utf-8") as foreigner2:
            json.dump(datilo2,foreigner2,ensure_ascii=False,indent=2)
    except IOError as men:
        print(men)
    except PermissionError as men2:
        print(men2)
    except FileNotFoundError as men3:
        print(men3)

expediente=pathlib.Path("estadisticas.json")
def cargar_estadisticas():
    if not expediente.exists():
        date={"entradasvendidas":{"vip":0,"platea":0,"popular":0},"sponsorsuso":{"entrada":0,"arco izquiero":0,"arco derecho":0,"gradas lado izquierdo":0,"gradas lado derecho":0,"fachada de club":0},"cualvendemas":{"entradasliga":0,"entradastorneo":0},"cualreserva":{"fut5":0,"fut8":0,"fut11":0}}
        guardar_estadisticas(date)
        return date
    else:
        try:
            with open(expediente,"r",encoding="utf-8") as fragile:
                return json.load(fragile)
        except IOError as men:
            print(men)
            date={"entradasvendidas":{"vip":0,"platea":0,"popular":0},"sponsorsuso":{"entrada":0,"arco izquiero":0,"arco derecho":0,"gradas lado izquierdo":0,"gradas lado derecho":0,"fachada de club":0},"cualvendemas":{"entradasliga":0,"entradastorneo":0},"cualreserva":{"fut5":0,"fut8":0,"fut11":0}}
            guardar_estadisticas(date)
            return date
        except PermissionError as men2:
            print(men2)
            date={"entradasvendidas":{"vip":0,"platea":0,"popular":0},"sponsorsuso":{"entrada":0,"arco izquiero":0,"arco derecho":0,"gradas lado izquierdo":0,"gradas lado derecho":0,"fachada de club":0},"cualvendemas":{"entradasliga":0,"entradastorneo":0},"cualreserva":{"fut5":0,"fut8":0,"fut11":0}}
            guardar_estadisticas(date)
            return date
        except FileNotFoundError as men3:
            print(men3)
            date={"entradasvendidas":{"vip":0,"platea":0,"popular":0},"sponsorsuso":{"entrada":0,"arco izquiero":0,"arco derecho":0,"gradas lado izquierdo":0,"gradas lado derecho":0,"fachada de club":0},"cualvendemas":{"entradasliga":0,"entradastorneo":0},"cualreserva":{"fut5":0,"fut8":0,"fut11":0}}
            guardar_estadisticas(date)
            return date
def guardar_estadisticas(usito):
    try:
        with open(expediente,"w",encoding="utf-8") as fragile2:
            json.dump(usito,fragile2,ensure_ascii=False,indent=2)
    except IOError as men:
        print(men)
    except PermissionError as men2:
        print(men2)
    except FileNotFoundError as men3:
        print(men3)
resultadosidita=pathlib.Path("resultadosidita.json")
def cargar_resultadosidita():
    if not resultadosidita.exists():
        datazo2={"resultadosidita":[]}
        guardar_resultadosidita(datazo2)
        return datazo2
    else:
        try:
            with open(resultadosidita,"r",encoding="utf-8") as mesengger3:
                return json.load(mesengger3)
        except IOError as men:
            print(men)
            datazo2={"resultadosidita":[]}
            guardar_liga(datazo2)
            return datazo2
        except PermissionError as men2:
            print(men2)
            datazo2={"resultadosidita":[]}
            guardar_liga(datazo2)
            return datazo2
        except FileNotFoundError as men3:
            print(men3)
            datazo2={"resultadosidita":[]}
            guardar_liga(datazo2)
            return datazo2
def guardar_resultadosidita(datos2):
    try:
        with open(resultadosidita,"w",encoding="utf-8") as mesengger4:
            json.dump(datos2,mesengger4,ensure_ascii=False,indent=2)
    except IOError as men:
        print(men)
    except PermissionError as men2:
        print(men2)
    except FileNotFoundError as men3:
        print(men3)
resultadosvueltita=pathlib.Path("resultadosvueltita.json")
def cargar_resultadosvueltita():
    if not resultadosvueltita.exists():
        datazo2={"resultadosvueltita":[]}
        guardar_resultadosvueltita(datazo2)
        return datazo2
    else:
        try:
            with open(resultadosvueltita,"r",encoding="utf-8") as mesengger3:
                return json.load(mesengger3)
        except IOError as men:
            print(men)
            datazo2={"resultadosvueltita":[]}
            guardar_liga(datazo2)
            return datazo2
        except PermissionError as men2:
            print(men2)
            datazo2={"resultadosvueltita":[]}
            guardar_liga(datazo2)
            return datazo2
        except FileNotFoundError as men3:
            print(men3)
            datazo2={"resultadosvueltita":[]}
            guardar_liga(datazo2)
            return datazo2
def guardar_resultadosvueltita(datos2):
    try:
        with open(resultadosvueltita,"w",encoding="utf-8") as mesengger4:
            json.dump(datos2,mesengger4,ensure_ascii=False,indent=2)
    except IOError as men:
        print(men)
    except PermissionError as men2:
        print(men2)
    except FileNotFoundError as men3:
        print(men3)
fixtureidita=pathlib.Path("fixtureidita.json")
def cargar_fixtureidita():
    if not fixtureidita.exists():
        datazo2={"fixtureidita":[]}
        guardar_fixtureidita(datazo2)
        return datazo2
    else:
        try:
            with open(fixtureidita,"r",encoding="utf-8") as mesengger3:
                return json.load(mesengger3)
        except IOError as men:
            print(men)
            datazo2={"fixtureidita":[]}
            guardar_liga(datazo2)
            return datazo2
        except PermissionError as men2:
            print(men2)
            datazo2={"fixtureidita":[]}
            guardar_liga(datazo2)
            return datazo2
        except FileNotFoundError as men3:
            print(men3)
            datazo2={"fixtureidita":[]}
            guardar_liga(datazo2)
            return datazo2
def guardar_fixtureidita(datos2):
    try:
        with open(fixtureidita,"w",encoding="utf-8") as mesengger4:
            json.dump(datos2,mesengger4,ensure_ascii=False,indent=2)
    except IOError as men:
        print(men)
    except PermissionError as men2:
        print(men2)
    except FileNotFoundError as men3:
        print(men3)
fixturevueltita=pathlib.Path("fixturevueltita.json")
def cargar_fixturevueltita():
    if not fixturevueltita.exists():
        datazo2={"fixturevueltita":[]}
        guardar_fixturevueltita(datazo2)
        return datazo2
    else:
        try:
            with open(fixturevueltita,"r",encoding="utf-8") as mesengger3:
                return json.load(mesengger3)
        except IOError as men:
            print(men)
            datazo2={"fixturevueltita":[]}
            guardar_liga(datazo2)
            return datazo2
        except PermissionError as men2:
            print(men2)
            datazo2={"fixturevueltita":[]}
            guardar_liga(datazo2)
            return datazo2
        except FileNotFoundError as men3:
            print(men3)
            datazo2={"fixturevueltita":[]}
            guardar_liga(datazo2)
            return datazo2
def guardar_fixturevueltita(datos2):
    try:
        with open(fixturevueltita,"w",encoding="utf-8") as mesengger4:
            json.dump(datos2,mesengger4,ensure_ascii=False,indent=2)
    except IOError as men:
        print(men)
    except PermissionError as men2:
        print(men2)
    except FileNotFoundError as men3:
        print(men3)
        
#esto esta bien, hay que acomodarlo nomas, pero cuando funcione todo
