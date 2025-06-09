#Ejercicio 2: Dada una lista de personajes de marvel (la desarrollada en clases) debe tener 100 o mas, resolver:
#a-Listado ordenado de manera ascendente por nombre de los personajes.
#b-Determinar en que posicion esta The Thing y Rocket Raccoon.
#c-Listar todos los villanos de la lista.
#d-Poner todos los villanos en una cola para determinar luego cuales aparecieron antes de 1980.
#e-Listar los superheores que comienzan con  Bl, G, My, y W.
#f-Listado de personajes ordenado por nombre real de manera ascendente de los personajes.
#g-Listado de superheroes ordenados por fecha de aparación.
#h-Modificar el nombre real de Ant Man a Scott Lang.
#i-Mostrar los personajes que en su biografia incluyan la palabra time-traveling o suit.
#j-Eliminar a Electro y Baron Zemo de la lista y mostrar su información si estaba en la lista.

from super_heroes_data import superheroes
from list_ import Lista
from queue_ import Queue

def order_by_name(item):
    return item.name or ""

def order_by_year(item):
    return item.year

def order_by_real_name(item):
    return item.real_name or ""

def order_by_first_appearance(item):
    return item.first_appearance


class Superhero:
    
    def __init__(self, name, alias, real_name, short_bio, first_appearance, is_villain):
        self.name = name
        self.alias = alias
        self.real_name = real_name
        self.short_bio = short_bio
        self.first_appearance = first_appearance
        self.is_villain = is_villain
        self.movies = Lista()
        self.movies.add_criterion('name', order_by_name)
        self.movies.add_criterion('year', order_by_year)
        
    def __str__(self):
        return f"{self.name,}, {self.real_name}, {self.first_appearance}"

superheroes_list = Lista()
for hero in superheroes:
    superheroes_list.append(Superhero(
        name=hero['name'],
        alias=hero['alias'],
        real_name=hero['real_name'],
        short_bio=hero['short_bio'],
        first_appearance=hero['first_appearance'],
        is_villain=hero['is_villain']
    ))

superheroes_list.add_criterion('name', order_by_name)
superheroes_list.add_criterion('real_name', order_by_real_name)
superheroes_list.add_criterion('first_appearance', order_by_first_appearance)


#a- Listado ordenado de manera ascendente por nombre de los personajes.
def punto_a():
    print("Listado ordenado de manera ascendente por nombre de los personajes:")
    superheroes_list.sort_by_criterion('name')
    for hero in superheroes_list:
        print(hero)
        


#b- Determinar en que posicion esta The Thing y Rocket Raccoon.
def punto_b():
    print("Posicion de The Thing y Rocket Raccoon:")
    posicion_the_thing = superheroes_list.search('The Thing', 'name')
    posicion_rocket_raccoon = superheroes_list.search('Rocket Raccoon', 'name')
    
    print(f"The Thing esta en la posicion: {posicion_the_thing}")
    print(f"Rocket Raccoon esta en la posicion: {posicion_rocket_raccoon}")
    

#c- Listar todos los villanos de la lista.
def punto_c():
    print("Listado de villanos:")
    villanos = [hero for hero in superheroes_list if hero.is_villain]
    for villano in villanos:
        print(villano)
        

#d- Poner todos los villanos en una cola para determinar luego cuales aparecieron antes de 1980.
def punto_d():
    print("Villanos que aparecieron antes de 1980:")
    villanos_queue = Queue()
    for hero in superheroes_list:
        if hero.is_villain and hero.first_appearance < 1980:
            villanos_queue.arrive(hero)
    
    while villanos_queue.size() > 0:
        print(villanos_queue.attention())
        

#e- Listar los superheroes que comienzan con Bl, G, My, y W.
def punto_e():
    print("Listado de superheroes que comienzan con Bl, G, My, y W:")
    prefixes = ['Bl', 'G', 'My', 'W']
    for hero in superheroes_list:
        if any(hero.name.startswith(prefix) for prefix in prefixes):
            print(hero)
        
            
#f- Listado de personajes ordenado por nombre real de manera ascendente de los personajes.
def punto_f():
    print("Listado de superheroes ordenado por nombre real:")
    superheroes_list.sort_by_criterion("real_name")
    superheroes_list.show()
    

#g- Listado de superheroes ordenados por fecha de aparicion.
def punto_g():
    print("Listado de superheroes ordenados por fecha de aparicion:")
    superheroes_list.sort_by_criterion("first_appearance")
    superheroes_list.show()
    
    
#h- Modificar el nombre real de Ant Man
def punto_h():
    print("Modificando el nombre real de Ant Man a Scott Lang:")
    indice = superheroes_list.search("Ant Man", "name")
    if indice is not None:
        superheroes_list[indice].real_name = "Scott Lang"
        print(f"Nombre real de Ant Man actualizado a: {superheroes_list[indice].real_name}")
    else:
        print("Ant Man no encontrado en la lista.")
        
        
#i- Mostrar los personajes que en su biografia incluyan la palabra time-traveling o suit.
def punto_i():
    print("Personajes con 'time-traveling' o 'suit' en su biografia:")
    for hero in superheroes_list:
        if 'time-traveling' in hero.short_bio or 'suit' in hero.short_bio:
            print(hero)
            
            
#j- Eliminar a Electro y Baron Zemo de la lista y mostrar su informacion si estaba en la lista.
def punto_j():
    print("Eliminando a Electro y Baron Zemo:")
    for name in ['Electro', 'Baron Zemo']:
        index = superheroes_list.search(name, 'name')
        if index is not None:
            removed_hero = superheroes_list.delete_value(name, 'name')
            print(f"Eliminado: {removed_hero}")
        else:
            print(f"{name} no encontrado en la lista.")
            
print("Ejercicio 2: Parcial Algoritmos - Chatelain Agustin")
print("-" * 75)
print("a- Listado ordenado de manera ascendente por nombre de los personajes.") 
punto_a()
print("-"*75)
print("b- Determinar en que posicion esta The Thing y Rocket Raccoon.")
punto_b()
print("-"*75)
print("c- Listar todos los villanos de la lista.")
punto_c()
print("-"*75)
print("d- Poner todos los villanos en una cola para determinar luego cuales aparecieron antes de 1980.")
punto_d()
print("-"*75)
print("e- Listar los superheroes que comienzan con Bl, G, My, y W.")
punto_e()
print("-"*75)
print("f- Listado de personajes ordenado por nombre real de manera ascendente de los personajes.")
punto_f()
print("-"*75)
print("g- Listado de superheroes ordenados por fecha de aparicion.")
punto_g()
print("-"*75)
print("h- Modificar el nombre real de Ant Man a Scott Lang.")
punto_h()
print("-"*75)
print("i- Mostrar los personajes que en su biografia incluyan la palabra time-traveling o suit.")
punto_i()
print("-"*75)
print("j- Eliminar a Electro y Baron Zemo de la lista y mostrar su informacion si estaba en la lista.")
punto_j()