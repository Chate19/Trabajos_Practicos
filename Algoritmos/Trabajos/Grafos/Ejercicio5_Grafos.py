from graph import Graph
from heap import HeapMin

class RedGraph(Graph):
    def insert_vertex(self, value, tipo=None):
        super().insert_vertex(value)
        if tipo:
            pos = self.search(value, 'value')
            if pos is not None:
                self[pos].other_values = tipo

    # --- CORRECCIÓN AQUÍ ---
    def prim(self):
        # Contamos vértices manualmente
        cantidad_vertices = 0
        for _ in self:
            cantidad_vertices += 1
            
        if cantidad_vertices == 0: return 0
        
        visitados = [self[0].value]
        heap = HeapMin()
        
        # Carga inicial
        for arista in self[0].edges:
            # Guardamos: [origen, destino], peso
            heap.arrive([self[0].value, arista.value], arista.weight)
            
        peso_total = 0
        
        while len(visitados) < cantidad_vertices and heap.size() > 0:
            dato = heap.attention() 
            # ESTRUCTURA DE DATO: (peso, [origen, destino])
            
            peso = dato[0]
            origen = dato[1][0]
            destino = dato[1][1]
            
            if destino not in visitados:
                visitados.append(destino)
                peso_total += peso
                
                # Buscar vecino para añadir sus aristas
                pos_dest = self.search(destino, 'value')
                if pos_dest is not None:
                    nodo_dest = self[pos_dest]
                    for arista in nodo_dest.edges:
                        if arista.value not in visitados:
                            heap.arrive([nodo_dest.value, arista.value], arista.weight)
                            
        return peso_total

def get_costo_dijkstra(stack, destino):
    costo = float('inf')
    temp = []
    # Buscamos en la pila sin vaciarla permanentemente (si quisieras reusarla)
    # Pero como Dijkstra devuelve una pila nueva cada vez, podemos consumirla.
    while stack.size() > 0:
        dato = stack.pop()
        temp.append(dato)
        if dato[0] == destino:
            costo = dato[1]
            break
    return costo

# --- CONFIGURACION ---
red = RedGraph(is_directed=False) 

dispositivos = [
    ("Debian", "notebook"), ("Red Hat", "notebook"), ("Arch", "notebook"),
    ("Ubuntu", "pc"), ("Mint", "pc"), ("Manjaro", "pc"), 
    ("Fedora", "pc"), ("Parrot", "pc"),
    ("Switch 1", "switch"), ("Switch 2", "switch"),
    ("Router 1", "router"), ("Router 2", "router"), ("Router 3", "router"),
    ("Impresora", "impresora"), ("Guaraní", "servidor"), ("MongoDB", "servidor")
]

for nombre, tipo in dispositivos:
    red.insert_vertex(nombre, tipo)

conexiones = [
    ("Switch 1", "Debian", 17), ("Switch 1", "Ubuntu", 18), ("Switch 1", "Mint", 80),
    ("Switch 1", "Impresora", 22), ("Switch 1", "Router 1", 29),
    ("Router 1", "Router 2", 37), ("Router 1", "Router 3", 43),
    ("Router 2", "Red Hat", 25), ("Router 2", "Guaraní", 9), ("Router 2", "Router 3", 50),
    ("Router 3", "Switch 2", 61),
    ("Switch 2", "Manjaro", 40), ("Switch 2", "Fedora", 3), 
    ("Switch 2", "Arch", 56), ("Switch 2", "Parrot", 12), ("Switch 2", "MongoDB", 5)
]

for u, v, p in conexiones:
    red.insert_edge(u, v, p)


# --- RESOLUCION ---

print("--- PUNTO B: Barridos ---")
for nb in ["Red Hat", "Debian", "Arch"]:
    print(f"DFS desde {nb}:")
    red.deep_sweep(nb)
    print(f"BFS desde {nb}:")
    red.amplitude_sweep(nb)

print("\n--- PUNTO C: Camino corto a Impresora ---")
for pc in ["Manjaro", "Red Hat", "Fedora"]:
    pila = red.dijkstra(pc)
    print(f"{pc} -> Costo: {get_costo_dijkstra(pila, 'Impresora')}")

print("\n--- PUNTO D: Arbol Expansion Minima ---")
print(f"Peso total: {red.prim()}")

print("\n--- PUNTO E: PC mas cercana a Guarani ---")
min_dist = float('inf')
mejor_pc = None
for nodo in red:
    if nodo.other_values == "pc":
        pila = red.dijkstra(nodo.value)
        c = get_costo_dijkstra(pila, "Guaraní")
        if c < min_dist:
            min_dist = c
            mejor_pc = nodo.value
print(f"PC: {mejor_pc}, Costo: {min_dist}")

print("\n--- PUNTO F: Equipo Switch 1 a MongoDB ---")
pos_sw1 = red.search("Switch 1", "value")
sw1 = red[pos_sw1]
min_dist_f = float('inf')
mejor_eq = None
for arista in sw1.edges:
    pos_vecino = red.search(arista.value, "value")
    vecino = red[pos_vecino]
    if vecino.other_values in ["pc", "notebook"]:
        pila = red.dijkstra(vecino.value)
        c = get_costo_dijkstra(pila, "MongoDB")
        if c < min_dist_f:
            min_dist_f = c
            mejor_eq = vecino.value
print(f"Equipo: {mejor_eq}, Costo: {min_dist_f}")

print("\n--- PUNTO G: Cambio conexion Impresora ---")
red.delete_edge("Switch 1", "Impresora")
red.insert_edge("Router 2", "Impresora", 22)

for nb in ["Red Hat", "Debian", "Arch"]:
    print(f"BFS actualizado desde {nb}:")
    red.amplitude_sweep(nb)