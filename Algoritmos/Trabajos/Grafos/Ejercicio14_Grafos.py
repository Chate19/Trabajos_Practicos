from graph import Graph
from heap import HeapMin

class CasaGraph(Graph):
    def prim(self):
        cant_nodos = 0
        for _ in self: cant_nodos += 1
            
        if cant_nodos == 0: return 0
        
        visitados = [self[0].value]
        heap = HeapMin()
        
        for arista in self[0].edges:
            heap.arrive([self[0].value, arista.value], arista.weight)
            
        peso_total = 0
        
        while len(visitados) < cant_nodos and heap.size() > 0:
            dato = heap.attention() 
            peso = dato[0]
            dst = dato[1][1]
            
            if dst not in visitados:
                visitados.append(dst)
                peso_total += peso
                
                pos = self.search(dst, 'value')
                if pos is not None:
                    nodo = self[pos]
                    for arista in nodo.edges:
                        if arista.value not in visitados:
                            heap.arrive([nodo.value, arista.value], arista.weight)
                            
        return peso_total

def get_metros_dijkstra(stack, destino):
    metros = float('inf')
    while stack.size() > 0:
        dato = stack.pop()
        if dato[0] == destino:
            metros = dato[1]
            break
    return metros

# --- CONFIGURACION ---
casa = CasaGraph(is_directed=False)

ambientes = [
    "Cocina", "Comedor", "Cochera", "Quincho", "Baño 1", "Baño 2", 
    "Habitación 1", "Habitación 2", "Sala de Estar", "Terraza", "Patio"
]
for amb in ambientes: casa.insert_vertex(amb)

# Aristas (Cumpliendo consigna: min 3 por nodo, Sala y Patio tienen 5)
conexiones = [
    ("Sala de Estar", "Comedor", 4), ("Sala de Estar", "Cocina", 5),
    ("Sala de Estar", "Habitación 1", 6), ("Sala de Estar", "Habitación 2", 6),
    ("Sala de Estar", "Baño 1", 3),
    ("Patio", "Comedor", 5), ("Patio", "Cochera", 8),
    ("Patio", "Quincho", 4), ("Patio", "Terraza", 6), ("Patio", "Baño 2", 7),
    ("Cocina", "Comedor", 3), ("Cocina", "Terraza", 5),
    ("Comedor", "Cochera", 6), ("Comedor", "Quincho", 9),
    ("Cochera", "Quincho", 3),
    ("Baño 1", "Habitación 1", 2), ("Baño 1", "Habitación 2", 2),
    ("Baño 2", "Terraza", 4), ("Baño 2", "Quincho", 5),
    ("Habitación 1", "Habitación 2", 4)
]

for u, v, p in conexiones: casa.insert_edge(u, v, p)

# --- RESOLUCION ---

# C. Arbol Expansion Minima
print("--- PUNTO C: Metros de cable (MST) ---")
print(f"Total necesario: {casa.prim()} metros")

# D. Camino mas corto (Router a Smart TV)
print("\n--- PUNTO D: Router (Hab 1) a Smart TV (Sala) ---")
origen = "Habitación 1"
destino = "Sala de Estar"
pila = casa.dijkstra(origen)
metros = get_metros_dijkstra(pila, destino)
print(f"De {origen} a {destino}: {metros} metros de cable de red")