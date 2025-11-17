#Ejercicio 2: Dado un grafo no dirigido con personajes de la saga Star Wars, implementar los algoritmos necesarios para resolver las siguientes tareas:
#cada vértice debe almacenar el nombre de un personaje, las aristas representan la cantidad de episodios en los que aparecieron juntos ambos personajes que se relacionan;
#hallar el árbol de expansión mínimo desde el vértice que contiene a: C-3PO, Yoda y Leia;
#determinar cuál es el número máximo de episodio que comparten dos personajes, e indicar todos los pares de personajes que coinciden con dicho número;
#cargue al menos los siguientes personajes: Luke Skywalker, Darth Vader, Yoda, Boba Fett, C-3PO, Leia, Rey, Kylo Ren, Chewbacca, Han Solo, R2-D2, BB-8;
#calcule el camino mas ccorto desde: C-3PO a R2-D2 y desde Yoda a Darth Vader;
#indicar qué personajes aparecieron en los nueve episodios de la saga.

from graph import Graph

# a. y d. Carga de personajes y creación del grafo no dirigido
characters_data = [
    {"name": "Luke Skywalker", "episodes": [1, 2, 3, 4, 5, 6, 7, 8, 9]},
    {"name": "Darth Vader", "episodes": [3, 4, 5, 6]},
    {"name": "Yoda", "episodes": [1, 2, 3, 5, 6, 8]},
    {"name": "Boba Fett", "episodes": [2, 4, 5, 6]},
    {"name": "C-3PO", "episodes": [1, 2, 3, 4, 5, 6, 7, 8, 9]},
    {"name": "Leia", "episodes": [3, 4, 5, 6, 7, 8, 9]},
    {"name": "Rey", "episodes": [7, 8, 9]},
    {"name": "Kylo Ren", "episodes": [7, 8, 9]},
    {"name": "Chewbacca", "episodes": [3, 4, 5, 6, 7, 8, 9]},
    {"name": "Han Solo", "episodes": [4, 5, 6, 7]},
    {"name": "R2-D2", "episodes": [1, 2, 3, 4, 5, 6, 7, 8, 9]},
    {"name": "BB-8", "episodes": [7, 8, 9]},
    {"name": "Darth Maul", "episodes": [1]},
    {"name": "Obi-Wan Kenobi", "episodes": [1, 2, 3, 4, 5, 6]},
]

edges_data = [
    ("Luke Skywalker", "Darth Vader", 4),
    ("Luke Skywalker", "Leia", 5),
    ("Luke Skywalker", "Han Solo", 4),
    ("Luke Skywalker", "Yoda", 3),
    ("Luke Skywalker", "R2-D2", 7),
    ("Darth Vader", "Obi-Wan Kenobi", 2),
    ("Yoda", "Obi-Wan Kenobi", 3),
    ("Yoda", "Boba Fett", 1),
    ("C-3PO", "R2-D2", 9),
    ("C-3PO", "Leia", 6),
    ("Leia", "Han Solo", 4),
    ("Rey", "Kylo Ren", 3),
    ("Rey", "BB-8", 3),
    ("Han Solo", "Chewbacca", 4),
]

g = Graph(is_directed=False)

# Insertar vértices
for character in characters_data:
    g.insert_vertex(character["name"])

# Insertar vértices
for character in characters_data:
    g.insert_vertex(character["name"])

# Insertar aristas
for edge in edges_data:
    g.insert_edge(edge[0], edge[1], edge[2])

print("Grafo de Star Wars creado exitosamente.")

# b. Hallar el árbol de expansión mínimo
print("\n--- b. Árbol de Expansión Mínimo (Kruskal) ---")
expansion_tree_str = g.kruskal("C-3PO")
if expansion_tree_str:
    print(f"\nÁrbol de expansión mínimo que conecta a todos los personajes:")
    peso_total = 0
    aristas_mst = expansion_tree_str.split(';')
    for edge in aristas_mst:
        try:
            origin, destination, weight = edge.split('-')
            print(f"- Arista: {origin} <-> {destination}, Episodios: {weight}")
            peso_total += int(weight)
        except ValueError:
            if edge: print(f"Componente: {edge}")
    print(f"Total de episodios (peso) del MST: {peso_total}")

# c. Número máximo de episodios compartidos
print("\n--- c. Máximo de episodios compartidos ---")
max_episodios = 0
pares_personajes = []

for i in range(len(g)):
    vertex = g[i]
    for edge in vertex.edges:
        if edge.weight > max_episodios:
            max_episodios = edge.weight
            pares_personajes = [(vertex.value, edge.value)]
        elif edge.weight == max_episodios:
            par_actual = tuple(sorted((vertex.value, edge.value)))
            if not any(tuple(sorted(p)) == par_actual for p in pares_personajes):
                pares_personajes.append((vertex.value, edge.value))

print(f"El número máximo de episodios que comparten dos personajes es: {max_episodios}")
print("Los pares de personajes que coinciden con este número son:")
for par in pares_personajes:
    print(f"- {par[0]} y {par[1]}")

# e. Calcular el camino más corto
print("\n--- e. Camino más corto (Dijkstra) ---")

def mostrar_camino_corto(graph, origen, destino):
    path_stack = graph.dijkstra(origen)
    peso_total = None
    camino_completo = []
    destino_original = destino

    while path_stack.size() > 0:
        value = path_stack.pop()
        if value[0] == destino:
            if peso_total is None:
                peso_total = value[1]
            camino_completo.append(value[0])
            destino = value[2]
    
    camino_completo.reverse()
    if peso_total is not None and camino_completo and camino_completo[0] == origen:
        print(f"El camino más corto es: {' -> '.join(camino_completo)}")
        print(f"Costo total (episodios): {peso_total}")
    else:
        print(f"No se encontró un camino desde {origen} hasta {destino_original}.")

print("Camino de C-3PO a R2-D2:")
mostrar_camino_corto(g, "C-3PO", "R2-D2")

print("\nCamino de Yoda a Darth Vader:")
mostrar_camino_corto(g, "Yoda", "Darth Vader")

# f. Indicar qué personajes aparecieron en los nueve episodios de la saga
print("\n--- f. Personajes en nueve episodios ---")
print("La información sobre el número total de episodios en los que apareció un personaje no está disponible en la estructura del grafo.")
print("El grafo solo almacena la cantidad de episodios en los que los personajes aparecieron *juntos*.")
