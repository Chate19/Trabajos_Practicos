# Ejercicio 1: Se tiene los datos de Pokémons de las 9 generaciones cargados de manera aleatoria (1025 en total) de los cuales se conoce su nombre, numero, tipo/tipos, debilidad frente a tipo/tipos, si tiene mega evolucion (bool) y si tiene forma gigamax (bool) para el cual debemos construir tres árboles para acceder de manera eficiente a los datos contemplando lo siguiente:
#los índices de cada uno de los árboles deben ser nombre, numero y tipo;
#mostrar todos los datos de un Pokemon a partir de su numero y nombre –para este último, la búsqueda debe ser por proximidad, es decir si busco “bul” se deben mostrar todos los Pokémons cuyos nombres comiencen o contengan dichos caracteres–;
#mostrar todos los nombres de los Pokémons de un determinado tipo: fantasma, fuego, acero y eléctrico;
#realizar un listado en orden ascendente por numero y nombre de Pokemon, y además un listado por nivel por nombre;
#mostrar todos los Pokémons que son debiles frente a Jolteon, Lycanroc y Tyrantrum;
#mostrar todos los tipos de Pokémons y cuántos hay de cada tipo;
#determinar cuantos Pokémons tienen megaevolucion.
#eterminar cuantos Pokémons tiene forma gigamax.

from tree import BinaryTree

class Pokemon:
    def __init__(self, numero, nombre, tipos, debilidades, mega, gigamax):
        self.numero = numero
        self.nombre = nombre
        self.tipos = tipos
        self.debilidades = debilidades
        self.mega_evolucion = mega
        self.forma_gigamax = gigamax

    def __str__(self):
        return (f"N°{self.numero} {self.nombre} | Tipos: {', '.join(self.tipos)} | "
                f"Debilidades: {', '.join(self.debilidades)} | "
                f"Mega: {'Sí' if self.mega_evolucion else 'No'} | Gigamax: {'Sí' if self.forma_gigamax else 'No'}")

# --- LISTA DE 50 POKÉMONS ALEATORIOS ---

datos_pokemon = [
    Pokemon(1, "Bulbasaur", ["Planta", "Veneno"], ["Fuego", "Hielo", "Volador", "Psiquico"], False, False),
    Pokemon(6, "Charizard", ["Fuego", "Volador"], ["Roca", "Agua", "Electrico"], True, True),
    Pokemon(9, "Blastoise", ["Agua"], ["Planta", "Electrico"], True, True),
    Pokemon(25, "Pikachu", ["Electrico"], ["Tierra"], False, True),
    Pokemon(59, "Arcanine", ["Fuego"], ["Agua", "Tierra", "Roca"], False, False),
    Pokemon(65, "Alakazam", ["Psiquico"], ["Bicho", "Fantasma", "Siniestro"], True, False),
    Pokemon(68, "Machamp", ["Lucha"], ["Volador", "Psiquico", "Hada"], False, True),
    Pokemon(94, "Gengar", ["Fantasma", "Veneno"], ["Tierra", "Psiquico", "Fantasma", "Siniestro"], True, True),
    Pokemon(130, "Gyarados", ["Agua", "Volador"], ["Roca", "Electrico"], True, False),
    Pokemon(143, "Snorlax", ["Normal"], ["Lucha"], False, True),
    Pokemon(149, "Dragonite", ["Dragon", "Volador"], ["Hielo", "Roca", "Dragon", "Hada"], False, False),
    Pokemon(150, "Mewtwo", ["Psiquico"], ["Bicho", "Fantasma", "Siniestro"], True, False),
    Pokemon(151, "Mew", ["Psiquico"], ["Bicho", "Fantasma", "Siniestro"], False, False),
    Pokemon(154, "Meganium", ["Planta"], ["Fuego", "Hielo", "Veneno", "Volador", "Bicho"], False, False),
    Pokemon(157, "Typhlosion", ["Fuego"], ["Agua", "Tierra", "Roca"], False, False),
    Pokemon(160, "Feraligatr", ["Agua"], ["Planta", "Electrico"], False, False),
    Pokemon(181, "Ampharos", ["Electrico"], ["Tierra"], True, False),
    Pokemon(196, "Espeon", ["Psiquico"], ["Bicho", "Fantasma", "Siniestro"], False, False),
    Pokemon(197, "Umbreon", ["Siniestro"], ["Lucha", "Bicho", "Hada"], False, False),
    Pokemon(212, "Scizor", ["Bicho", "Acero"], ["Fuego"], True, False),
    Pokemon(214, "Heracross", ["Bicho", "Lucha"], ["Volador", "Fuego", "Psiquico", "Hada"], True, False),
    Pokemon(248, "Tyranitar", ["Roca", "Siniestro"], ["Lucha", "Tierra", "Bicho", "Acero", "Agua", "Planta", "Hada"], True, False),
    Pokemon(254, "Sceptile", ["Planta"], ["Fuego", "Hielo", "Veneno", "Volador", "Bicho"], True, False),
    Pokemon(257, "Blaziken", ["Fuego", "Lucha"], ["Agua", "Tierra", "Volador", "Psiquico"], True, False),
    Pokemon(260, "Swampert", ["Agua", "Tierra"], ["Planta"], True, False),
    Pokemon(282, "Gardevoir", ["Psiquico", "Hada"], ["Veneno", "Fantasma", "Acero"], True, False),
    Pokemon(302, "Sableye", ["Fantasma", "Siniestro"], ["Hada"], True, False),
    Pokemon(306, "Aggron", ["Acero", "Roca"], ["Lucha", "Tierra", "Fuego"], True, False),
    Pokemon(373, "Salamence", ["Dragon", "Volador"], ["Hielo", "Roca", "Dragon", "Hada"], True, False),
    Pokemon(376, "Metagross", ["Acero", "Psiquico"], ["Fuego", "Tierra", "Fantasma", "Siniestro"], True, False),
    Pokemon(384, "Rayquaza", ["Dragon", "Volador"], ["Hielo", "Roca", "Dragon", "Hada"], True, False),
    Pokemon(392, "Infernape", ["Fuego", "Lucha"], ["Agua", "Tierra", "Volador", "Psiquico"], False, False),
    Pokemon(445, "Garchomp", ["Dragon", "Tierra"], ["Hielo", "Dragon", "Hada"], True, False),
    Pokemon(448, "Lucario", ["Lucha", "Acero"], ["Fuego", "Tierra", "Lucha"], True, False),
    Pokemon(475, "Gallade", ["Psiquico", "Lucha"], ["Volador", "Fantasma", "Hada"], True, False),
    Pokemon(487, "Giratina", ["Fantasma", "Dragon"], ["Hielo", "Fantasma", "Dragon", "Siniestro", "Hada"], False, False),
    Pokemon(571, "Zoroark", ["Siniestro"], ["Lucha", "Bicho", "Hada"], False, False),
    Pokemon(609, "Chandelure", ["Fantasma", "Fuego"], ["Siniestro", "Fantasma", "Roca", "Tierra", "Agua"], False, False),
    Pokemon(635, "Hydreigon", ["Siniestro", "Dragon"], ["Hada", "Lucha", "Bicho", "Dragon", "Hielo"], False, False),
    Pokemon(658, "Greninja", ["Agua", "Siniestro"], ["Planta", "Electrico", "Lucha", "Bicho", "Hada"], False, False),
    Pokemon(700, "Sylveon", ["Hada"], ["Veneno", "Acero"], False, False),
    Pokemon(724, "Decidueye", ["Planta", "Fantasma"], ["Volador", "Fuego", "Hielo", "Fantasma", "Siniestro"], False, False),
    Pokemon(745, "Lycanroc", ["Roca"], ["Agua", "Planta", "Lucha", "Tierra", "Acero"], False, False),
    Pokemon(778, "Mimikyu", ["Fantasma", "Hada"], ["Fantasma", "Acero"], False, False),
    Pokemon(800, "Necrozma", ["Psiquico"], ["Bicho", "Fantasma", "Siniestro"], False, False),
    Pokemon(815, "Cinderace", ["Fuego"], ["Tierra", "Roca", "Agua"], False, True),
    Pokemon(888, "Zacian", ["Hada", "Acero"], ["Fuego", "Tierra"], False, False),
    Pokemon(894, "Regieleki", ["Electrico"], ["Tierra"], False, False),
    Pokemon(901, "Ursaluna", ["Normal", "Tierra"], ["Agua", "Planta", "Hielo", "Lucha"], False, False),
    Pokemon(1008, "Miraidon", ["Electrico", "Dragon"], ["Tierra", "Hielo", "Dragon", "Hada"], False, False)
]

# Creación de los tres árboles
tree_by_name = BinaryTree()
tree_by_number = BinaryTree()
tree_by_type = BinaryTree()

for pokemon in datos_pokemon:
    tree_by_name.insert(pokemon.nombre, pokemon)
    tree_by_number.insert(pokemon.numero, pokemon)
    for tipo in pokemon.tipos:
        type_node = tree_by_type.search(tipo)
        if type_node:
            type_node.other_values.insert(pokemon.nombre, pokemon)
        else:
            new_type_tree = BinaryTree()
            new_type_tree.insert(pokemon.nombre, pokemon)
            tree_by_type.insert(tipo, new_type_tree)

print("Arboles de Pokemon creados exitosamente.")

# b. Mostrar datos de un Pokemon por numero y por proximidad de nombre
print("\n--- b. Busqueda de Pokemon ---")
print("Buscando por numero 25:")
node = tree_by_number.search(25)
if node:
    print(node.other_values)

print("\nBuscando por proximidad de nombre 'Pi':")
tree_by_name.proximity_search('Pi')

# c. Mostrar nombres de Pokemon de tipos específicos
print("\n--- c. Pokemon por tipo ---")
tipos_a_buscar = ["Fantasma", "Fuego", "Acero", "Electrico"]
for tipo in tipos_a_buscar:
    print(f"\nPokemon de tipo '{tipo}':")
    type_node = tree_by_type.search(tipo)
    if type_node:
        type_node.other_values.in_order()
    else:
        print(f"No se encontraron Pokemon de tipo '{tipo}'.")

# d. Listados ordenados
print("\n--- d. Listados ordenados ---")
print("\nListado ascendente por numero:")
tree_by_number.in_order()

print("\nListado ascendente por nombre:")
tree_by_name.in_order()

print("\nListado por nivel por nombre:")
tree_by_name.by_level()

# e. Pokemon debiles frente a Jolteon, Lycanroc y Tyrantrum
print("\n--- e. Pokemon debiles frente a Jolteon, Lycanroc y Tyrantrum ---")
debilidades_a_buscar = set()
for p_name in ["Jolteon", "Lycanroc", "Tyrantrum"]:
    node = tree_by_name.search(p_name)
    if node:
        for tipo in node.other_values.tipos:
            debilidades_a_buscar.add(tipo)

print(f"Tipos a buscar en debilidades: {list(debilidades_a_buscar)}")

def find_weak_pokemon(root):
    if root is not None:
        pokemon = root.other_values
        if any(d in debilidades_a_buscar for d in pokemon.debilidades):
            print(f"- {pokemon.nombre} es debil contra uno de los tipos.")
        find_weak_pokemon(root.left)
        find_weak_pokemon(root.right)

find_weak_pokemon(tree_by_name.root)

# f. Contar Pokemon por tipo
print("\n--- f. Cantidad de Pokemon por tipo ---")
def count_by_type(root):
    if root is not None:
        tipo = root.value
        cantidad = root.other_values.count_nodes()
        print(f"Tipo: {tipo} - Cantidad: {cantidad}")
        count_by_type(root.left)
        count_by_type(root.right)

count_by_type(tree_by_type.root)

# g. Contar Pokemon con megaevolucion
print("\n--- g. Conteo de Pokemon con Megaevolucion ---")
def count_mega_evolutions(root):
    if root is None:
        return 0
    count = 1 if root.other_values.mega_evolucion else 0
    count += count_mega_evolutions(root.left)
    count += count_mega_evolutions(root.right)
    return count

total_mega = count_mega_evolutions(tree_by_name.root)
print(f"Total de Pokemon con megaevolucion: {total_mega}")

# h. Contar Pokemon con forma Gigamax
print("\n--- h. Conteo de Pokemon con forma Gigamax ---")
def count_gigamax(root):
    if root is None:
        return 0
    count = 1 if root.other_values.forma_gigamax else 0
    count += count_gigamax(root.left)
    count += count_gigamax(root.right)
    return count

total_gigamax = count_gigamax(tree_by_name.root)
print(f"Total de Pokemon con forma Gigamax: {total_gigamax}")
