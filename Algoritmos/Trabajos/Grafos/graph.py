from typing import Any, Optional

# Importamos las estructuras auxiliares necesarias para los algoritmos del grafo
from heap import HeapMin    # Fundamental para Dijkstra y Kruskal (prioridad)
from list_ import Lista     # Estructura base para vértices y aristas
from queue_ import Queue    # Necesaria para el barrido en amplitud (BFS)
from stack import Stack    # Usada para reconstruir caminos en Dijkstra

class Graph(Lista):
    """
    Representa un Grafo utilizando Listas de Adyacencia.
    Hereda de Lista para gestionar los vértices como una colección dinámica.
    """

    class __nodeVertex:
        """
        Clase privada para representar cada Vértice (nodo).
        Contiene el valor, una lista de aristas hacia otros nodos y 
        un booleano para controlar si fue visitado en los recorridos.
        """
        def __init__(self, value: Any, other_values: Optional[Any] = None):
            self.value = value
            self.edges = Lista() # Lista de adyacencia (aristas que salen de este nodo)
            self.edges.add_criterion('value', Graph._order_by_value)
            self.edges.add_criterion('weight', Graph._order_by_weight)
            self.other_values = other_values
            self.visited = False
        
        def __str__(self):
            return str(self.value)
        
        def __lt__(self, other):
            return self.value < other.value
    
    class __nodeEdge:
        """
        Clase privada para representar una Arista (conexión).
        Guarda el destino y el peso (costo) de la conexión.
        
        """
        def __init__(self, value: Any, weight: Any, other_values: Optional[Any] = None):
            self.value = value
            self.weight = weight
            self.other_values = other_values
        
        def __str__(self):
            return f'Destino: {self.value} | Peso: {self.weight}'
    
    def __init__(self, is_directed=False):
        """
        Inicializa el grafo. 
        is_directed: True si las flechas tienen un solo sentido.
        
        """
        self.add_criterion('value', self._order_by_value)
        self.is_directed = is_directed

    @staticmethod
    def _order_by_value(item):
        return item.value

    @staticmethod
    def _order_by_weight(item):
        return item.weight
    
    def show(self) -> None:
        """Muestra la estructura completa del grafo: vértices y sus conexiones."""
        for vertex in self:
            print(f"Vértice: {vertex}")
            vertex.edges.show() 

    def insert_vertex(self, value: Any) -> None:
        """Añade un nuevo nodo al grafo."""
        node_vertex = Graph.__nodeVertex(value)
        self.append(node_vertex)

    def insert_edge(self, origin_vertex: Any, destination_vertex: Any, weight: int) -> None:
        """Crea una conexión entre dos vértices existentes."""
        origin = self.search(origin_vertex, 'value')
        destination = self.search(destination_vertex, 'value')
        if origin is not None and destination is not None:
            # Insertar en el sentido origen -> destino
            node_edge = Graph.__nodeEdge(destination_vertex, weight)
            self[origin].edges.append(node_edge)
            # Si es NO dirigido, se inserta la vuelta destino -> origen
            if not self.is_directed and origin != destination:
                node_edge = Graph.__nodeEdge(origin_vertex, weight)
                self[destination].edges.append(node_edge)
        else:
            print('Error: Uno de los vértices no existe.')

    def delete_edge(self, origin, destination, key_value: str = None) -> Optional[Any]:
        """Elimina la arista entre dos nodos."""
        pos_origin = self.search(origin, key_value)
        if pos_origin is not None:
            edge = self[pos_origin].edges.delete_value(destination, key_value)
            if not self.is_directed: # Si es no dirigido, borra la arista inversa
                pos_destination = self.search(destination, key_value)
                if pos_destination is not None:
                    self[pos_destination].edges.delete_value(origin, key_value)
            return edge

    def delete_vertex(self, value, key_value_vertex: str = None) -> Optional[Any]:
        """Elimina un vértice y todas las aristas que apunten a él desde otros nodos."""
        delete_value = self.delete_value(value, key_value_vertex)
        if delete_value is not None:
            for vertex in self:
                self.delete_edge(vertex.value, value, 'value')
        return delete_value

    def mark_as_unvisited(self) -> None:
        """Reinicia el estado de 'visited' en todos los nodos (necesario antes de barridos)."""
        for vertex in self:
            vertex.visited = False

    def exist_path(self, origin, destination) -> bool:
        """Verifica si hay camino entre dos nodos usando DFS (Profundidad)."""
        def __exist_path(graph, origin, destination):
            result = False
            vertex_pos = graph.search(origin, 'value')
            if vertex_pos is not None:
                if not graph[vertex_pos].visited:
                    graph[vertex_pos].visited = True
                    if graph[vertex_pos].value == destination:
                        return True
                    else:
                        for edge in graph[vertex_pos].edges:
                            result = __exist_path(graph, edge.value, destination)
                            if result: break
            return result
        
        self.mark_as_unvisited()
        return __exist_path(self, origin, destination)
    
    def deep_sweep(self, value) -> None:
        """Barrido en Profundidad (DFS): Explora lo más profundo posible de una rama."""
        def __deep_sweep(graph, value):
            vertex_pos = graph.search(value, 'value')
            if vertex_pos is not None:
                if not graph[vertex_pos].visited:
                    graph[vertex_pos].visited = True
                    print(graph[vertex_pos])
                    for edge in graph[vertex_pos].edges:
                        __deep_sweep(graph, edge.value)

        self.mark_as_unvisited()
        __deep_sweep(self, value)
        
    def amplitude_sweep(self, value) -> None:
        """Barrido en Amplitud (BFS): Visita los nodos por 'niveles' usando una Cola."""
        queue_vertex = Queue()
        self.mark_as_unvisited()
        vertex_pos = self.search(value, 'value')
        if vertex_pos is not None:
            self[vertex_pos].visited = True
            queue_vertex.arrive(self[vertex_pos])
            while queue_vertex.size() > 0:
                vertex = queue_vertex.attention()
                print(vertex.value)
                for edge in vertex.edges:
                    pos = self.search(edge.value, 'value')
                    if pos is not None and not self[pos].visited:
                        self[pos].visited = True
                        queue_vertex.arrive(self[pos])

    def dijkstra(self, origin):
        """Camino más corto desde un origen (pesos no negativos). Usa HeapMin para eficiencia."""
        from math import inf
        no_visited = HeapMin()
        path = Stack()
        
        for vertex in self:
            distance = 0 if vertex.value == origin else inf
            # Guardamos [valor, referencia al nodo, predecesor]
            no_visited.arrive([vertex.value, vertex, None], distance)

        while no_visited.size() > 0:
            # Obtenemos el nodo con la distancia mínima actual
            dist_min, (value_name, vertex_obj, father) = no_visited.attention()
            path.push([value_name, dist_min, father])
            
            for edge in vertex_obj.edges:
                pos = no_visited.search(edge.value)
                if pos is not None:
                    # Relajación de la arista
                    new_dist = dist_min + edge.weight
                    if new_dist < no_visited.elements[pos][0]:
                        no_visited.elements[pos][1][2] = value_name # Actualizar padre
                        no_visited.change_priority(pos, new_dist)
        return path

    def kruskal(self, origin_vertex):
        """Árbol de Expansión Mínima (MST): Conecta todos los nodos con el menor peso total."""
        def search_in_forest(forest, value):
            for index, tree in enumerate(forest):
                if value in tree: return index
                
        forest = []
        edges = HeapMin()
        for vertex in self:
            forest.append(vertex.value) # Cada nodo empieza como un árbol separado
            for edge in vertex.edges:
                edges.arrive([vertex.value, edge.value], edge.weight)
        
        while len(forest) > 1 and edges.size() > 0:
            weight, (u, v) = edges.attention()
            origin = search_in_forest(forest, u)
            destination = search_in_forest(forest, v)
            
            # Si están en árboles distintos, no forman ciclo
            if origin is not None and destination is not None and origin != destination:
                # Combinar árboles en el bosque
                t1 = forest.pop(max(origin, destination))
                t2 = forest.pop(min(origin, destination))
                forest.append(f"{t1};{u}-{v}-{weight};{t2}")
        
        return forest