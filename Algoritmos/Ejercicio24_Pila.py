#24. Dada una pila de personajes de Marvel Cinematic Universe (MCU), de los cuales se dispone de su nombre y la cantidad de películas de la saga en la que participó, implementar las funciones necesarias para resolver las siguientes actividades:
    #a. determinar en qué posición se encuentran Rocket Raccoon y Groot, tomando como posición uno la cima de la pila;
    #b. determinar los personajes que participaron en más de 5 películas de la saga, además indicar la cantidad de películas en la que aparece;
    #c. determinar en cuantas películas participo la Viuda Negra (Black Widow);
    #d. mostrar todos los personajes cuyos nombre empiezan con C, D y G.
    
from stack import Stack 

class Personaje:
    def __init__(self, nombre: str, peliculas: int):
        self.nombre = nombre
        self.peliculas = peliculas

    def __str__(self):
        return f"{self.nombre} ({self.peliculas} películas)"


personajes_datos = [
    {"nombre": "Iron Man", "peliculas": 10},
    {"nombre": "Rocket Raccoon", "peliculas": 4},
    {"nombre": "Black Widow", "peliculas": 7},
    {"nombre": "Groot", "peliculas": 5},
    {"nombre": "Doctor Strange", "peliculas": 4},
    {"nombre": "Captain America", "peliculas": 9},
    {"nombre": "Gamora", "peliculas": 6},
    {"nombre": "Drax", "peliculas": 6},
    {"nombre": "Hawkeye", "peliculas": 5},
]

pila_personajes = Stack()

for p in personajes_datos:
    pila_personajes.push(Personaje(p["nombre"], p["peliculas"]))

    
def resolver_ejercicio(pila:Stack):
    aux_stack = Stack()
    posicion = 1
    posiciones = {}
    personajes_mas_de_5 = []
    viuda_negra_peliculas = 0
    personajes_iniciales = []

    while pila.size() > 0:
        personaje = pila.pop()
        
        # a.
        if personaje.nombre == "Rocket Raccoon":
            posiciones["Rocket Raccoon"] = posicion
        if personaje.nombre == "Groot":
            posiciones["Groot"] = posicion

        # b.
        if personaje.peliculas > 5:
            personajes_mas_de_5.append((personaje.nombre, personaje.peliculas))

        # c.
        if personaje.nombre == "Black Widow":
            viuda_negra_peliculas = personaje.peliculas

        # d.
        if personaje.nombre[0] in ['C', 'D', 'G']:
            personajes_iniciales.append(personaje.nombre)

        aux_stack.push(personaje)
        posicion += 1

    while aux_stack.size() > 0:
        pila.push(aux_stack.pop())

    print("a. Posiciones:")
    for nombre in ["Rocket Raccoon", "Groot"]:
        pos = posiciones.get(nombre, "No encontrado")
        print(f"   {nombre}: posición {pos}")

    print("\nb. Personajes con más de 5 películas:")
    for nombre, cant in personajes_mas_de_5:
        print(f"   {nombre}: {cant} películas")

    print(f"\nc. Viuda Negra participó en {viuda_negra_peliculas} películas")

    print("\nd. Personajes cuyos nombres empiezan con C, D y G:")
    for nombre in personajes_iniciales:
        print(f"   {nombre}")

resolver_ejercicio(pila_personajes)