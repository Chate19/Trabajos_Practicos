#22. Se tienen una cola con personajes de Marvel Cinematic Universe (MCU), de los cuales se conoce el nombre del personaje, el nombre del superhéroe y su género (Masculino M y Femenino F) –por ejemplo {Tony Stark, Iron Man, M}, {Steve Rogers, Capitán América, M}, {Natasha Romanoff, Black Widow, F}, etc., desarrollar un algoritmo que resuelva las siguientes actividades:
	#a. determinar el nombre del personaje de la superhéroe Capitana Marvel;
	#b. mostrar los nombre de los superhéroes femeninos;
	#c. mostrar los nombres de los personajes masculinos;
	#d. determinar el nombre del superhéroe del personaje Scott Lang;
	#e. mostrar todos datos de los superhéroes o personaje cuyos nombres comienzan con la letra S;
	#f. determinar si el personaje Carol Danvers se encuentra en la cola e indicar su nombre de superhéroes.
 
from queue import Queue

def crear_personaje(nombre_real, superheroe, genero):
    """
    Crea un diccionario que representa un personaje del MCU.

    Parámetros:
    - nombre_real (str): nombre del personaje
    - superheroe (str): nombre del superhéroe
    - genero (str): 'M' para masculino, 'F' para femenino

    Retorna:
    - dict: personaje
    """
    return {"nombre_real": nombre_real, "superheroe": superheroe, "genero": genero.upper()}

def obtener_personaje_de_superheroe(cola, nombre_superheroe):
    """
    Busca el nombre del personaje real dado el nombre del superhéroe.

    Parámetros:
    - cola (Queue): cola de personajes
    - nombre_superheroe (str): superhéroe buscado

    Retorna:
    - Queue: cola restaurada
    - str|None: nombre del personaje si se encuentra, None en caso contrario
    """
    cola_aux = Queue()
    resultado = None

    while not cola.empty():
        p = cola.get()
        if p["superheroe"].lower() == nombre_superheroe.lower():
            resultado = p["nombre_real"]
        cola_aux.put(p)

    return cola_aux, resultado

def mostrar_superheroes_femeninos(cola):
    """
    Muestra los nombres de superhéroes femeninos.

    Parámetros:
    - cola (Queue): cola de personajes

    Retorna:
    - Queue: cola restaurada
    """
    cola_aux = Queue()
    print("\n Superhéroes femeninos:")
    while not cola.empty():
        p = cola.get()
        if p["genero"] == "F":
            print(p["superheroe"])
        cola_aux.put(p)
    return cola_aux

def mostrar_personajes_masculinos(cola):
    """
    Muestra los nombres de personajes masculinos (nombre real).

    Parámetros:
    - cola (Queue): cola de personajes

    Retorna:
    - Queue: cola restaurada
    """
    cola_aux = Queue()
    print("\n Personajes masculinos:")
    while not cola.empty():
        p = cola.get()
        if p["genero"] == "M":
            print(p["nombre_real"])
        cola_aux.put(p)
    return cola_aux

def obtener_superheroe_de_personaje(cola, nombre_personaje):
    """
    Busca el nombre del superhéroe dado el nombre del personaje.

    Parámetros:
    - cola (Queue): cola de personajes
    - nombre_personaje (str): nombre del personaje

    Retorna:
    - Queue: cola restaurada
    - str|None: nombre del superhéroe si se encuentra, None si no está
    """
    cola_aux = Queue()
    resultado = None

    while not cola.empty():
        p = cola.get()
        if p["nombre_real"].lower() == nombre_personaje.lower():
            resultado = p["superheroe"]
        cola_aux.put(p)

    return cola_aux, resultado

def mostrar_datos_con_s(cola):
    """
    Muestra todos los datos de los personajes o superhéroes que comienzan con la letra 'S'.

    Parámetros:
    - cola (Queue): cola de personajes

    Retorna:
    - Queue: cola restaurada
    """
    cola_aux = Queue()
    print("\n Personajes o superhéroes que comienzan con 'S':")
    while not cola.empty():
        p = cola.get()
        if p["nombre_real"].lower().startswith("s") or p["superheroe"].lower().startswith("s"):
            print(f"Nombre real: {p['nombre_real']} | Superhéroe: {p['superheroe']} | Género: {p['genero']}")
        cola_aux.put(p)
    return cola_aux

def buscar_personaje(cola, nombre_personaje):
    """
    Verifica si un personaje está en la cola e imprime su nombre de superhéroe.

    Parámetros:
    - cola (Queue): cola de personajes
    - nombre_personaje (str): nombre del personaje a buscar

    Retorna:
    - Queue: cola restaurada
    - bool: True si se encuentra, False si no
    """
    cola_aux = Queue()
    encontrado = False
    superheroe = None

    while not cola.empty():
        p = cola.get()
        if p["nombre_real"].lower() == nombre_personaje.lower():
            encontrado = True
            superheroe = p["superheroe"]
        cola_aux.put(p)

    if encontrado:
        print(f"\n El personaje {nombre_personaje} se encuentra en la cola y su superhéroe es: {superheroe}")
    else:
        print(f"\n El personaje {nombre_personaje} no se encuentra en la cola.")
    return cola_aux, encontrado


#              BLOQUE PRINCIPAL DE PRUEBA

if __name__ == "__main__":
    cola_personajes = Queue()
    personajes = [
        crear_personaje("Tony Stark", "Iron Man", "M"),
        crear_personaje("Steve Rogers", "Capitán América", "M"),
        crear_personaje("Natasha Romanoff", "Black Widow", "F"),
        crear_personaje("Carol Danvers", "Capitana Marvel", "F"),
        crear_personaje("Scott Lang", "Ant-Man", "M"),
        crear_personaje("Stephen Strange", "Doctor Strange", "M"),
        crear_personaje("Shuri", "Shuri", "F")
    ]

    for p in personajes:
        cola_personajes.put(p)

    # a. Nombre del personaje de Capitana Marvel
    cola_personajes, personaje_cm = obtener_personaje_de_superheroe(cola_personajes, "Capitana Marvel")
    print(f"\n El personaje que interpreta a Capitana Marvel es: {personaje_cm}")

    # b. Superhéroes femeninos
    cola_personajes = mostrar_superheroes_femeninos(cola_personajes)

    # c. Personajes masculinos
    cola_personajes = mostrar_personajes_masculinos(cola_personajes)

    # d. Superhéroe de Scott Lang
    cola_personajes, sh_scott = obtener_superheroe_de_personaje(cola_personajes, "Scott Lang")
    print(f"\n El superhéroe de Scott Lang es: {sh_scott}")

    # e. Mostrar datos de nombres que comienzan con S
    cola_personajes = mostrar_datos_con_s(cola_personajes)

    # f. Verificar si Carol Danvers está y mostrar su superhéroe
    cola_personajes, _ = buscar_personaje(cola_personajes, "Carol Danvers")
