#22. Se tienen una cola con personajes de Marvel Cinematic Universe (MCU), de los cuales se conoce el nombre del personaje, el nombre del superhéroe y su género (Masculino M y Femenino F) –por ejemplo {Tony Stark, Iron Man, M}, {Steve Rogers, Capitán América, M}, {Natasha Romanoff, Black Widow, F}, etc., desarrollar un algoritmo que resuelva las siguientes actividades:
    #a. determinar el nombre del personaje de la superhéroe Capitana Marvel;
    #b. mostrar los nombre de los superhéroes femeninos;
    #c. mostrar los nombres de los personajes masculinos;
    #d. determinar el nombre del superhéroe del personaje Scott Lang;
    #e. mostrar todos datos de los superhéroes o personaje cuyos nombres comienzan con la letra S;
    #f. determinar si el personaje Carol Danvers se encuentra en la cola e indicar su nombre de superhéroes.

from queue_ import Queue

def crear_personaje(nombre_real, superheroe, genero):
    return {"nombre_real": nombre_real, "superheroe": superheroe, "genero": genero.upper()}

# a. Determinar el nombre del personaje de la superhéroe Capitana Marvel
def obtener_personaje_de_superheroe(cola, nombre_superheroe):
    resultado = None
    # Usamos el tamaño para rotar la cola sin perder datos
    for _ in range(cola.size()):
        p = cola.attention() # Desencolamos
        if p["superheroe"].lower() == nombre_superheroe.lower():
            resultado = p["nombre_real"]
        cola.arrive(p) # Re-encolamos al final
    return resultado

# b. Mostrar los nombres de los superhéroes femeninos
def mostrar_superheroes_femeninos(cola):
    print("\n[b] Superhéroes femeninos:")
    for _ in range(cola.size()):
        p = cola.attention()
        if p["genero"] == "F":
            print(f" - {p['superheroe']}")
        cola.arrive(p)

# c. Mostrar los nombres de los personajes masculinos
def mostrar_personajes_masculinos(cola):
    print("\n[c] Personajes masculinos:")
    for _ in range(cola.size()):
        p = cola.attention()
        if p["genero"] == "M":
            print(f" - {p['nombre_real']}")
        cola.arrive(p)

# d. Determinar el nombre del superheroe del personaje Scott Lang
def obtener_superheroe_de_personaje(cola, nombre_personaje):
    resultado = None
    for _ in range(cola.size()):
        p = cola.attention()
        if p["nombre_real"].lower() == nombre_personaje.lower():
            resultado = p["superheroe"]
        cola.arrive(p)
    return resultado

# e. Mostrar todos los datos de los que comienzan con 'S'
def mostrar_datos_con_s(cola):
    print("\n[e] Personajes o superhéroes que comienzan con 'S':")
    for _ in range(cola.size()):
        p = cola.attention()
        if p["nombre_real"].lower().startswith("s") or p["superheroe"].lower().startswith("s"):
            print(f" - {p}")
        cola.arrive(p)

# f. Determinar si Carol Danvers está e indicar su superhéroe
def buscar_personaje_y_heroe(cola, nombre_personaje):
    superheroe = None
    for _ in range(cola.size()):
        p = cola.attention()
        if p["nombre_real"].lower() == nombre_personaje.lower():
            superheroe = p["superheroe"]
        cola.arrive(p)
    return superheroe

# --- BLOQUE PRINCIPAL ---
if __name__ == "__main__":
    cola_mcu = Queue()
    
    personajes = [
        crear_personaje("Tony Stark", "Iron Man", "M"),
        crear_personaje("Steve Rogers", "Capitán América", "M"),
        crear_personaje("Natasha Romanoff", "Black Widow", "F"),
        crear_personaje("Carol Danvers", "Capitana Marvel", "F"),
        crear_personaje("Scott Lang", "Ant-Man", "M"),
        crear_personaje("Stephen Strange", "Doctor Strange", "M")
    ]

    for p in personajes:
        cola_mcu.arrive(p) # Cargamos la cola

    # Ejecución de actividades
    nom_real = obtener_personaje_de_superheroe(cola_mcu, "Capitana Marvel")
    print(f"[a] Personaje de Capitana Marvel: {nom_real}")
    
    mostrar_superheroes_femeninos(cola_mcu)
    mostrar_personajes_masculinos(cola_mcu)
    
    heroe_scott = obtener_superheroe_de_personaje(cola_mcu, "Scott Lang")
    print(f"\n[d] Superhéroe de Scott Lang: {heroe_scott}")
    
    mostrar_datos_con_s(cola_mcu)
    
    heroe_carol = buscar_personaje_y_heroe(cola_mcu, "Carol Danvers")
    if heroe_carol:
        print(f"\n[f] Carol Danvers está y es {heroe_carol}")