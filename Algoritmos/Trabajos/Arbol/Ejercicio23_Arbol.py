# 23. Implementar un algoritmo que permita generar un árbol con los datos de la siguiente tabla y
# resuelva las siguientes consultas:


# a. listado inorden de las criaturas y quienes la derrotaron;
# b. se debe permitir cargar una breve descripción sobre cada criatura;
# c. mostrar toda la información de la criatura Talos;
# d. determinar los 3 héroes o dioses que derrotaron mayor cantidad de criaturas;
# e. listar las criaturas derrotadas por Heracles;
# f. listar las criaturas que no han sido derrotadas;
# g. además cada nodo debe tener un campo “capturada” que almacenará el nombre del héroe
# o dios que la capturo;
# h. modifique los nodos de las criaturas Cerbero, Toro de Creta, Cierva Cerinea y Jabalí de
# Erimanto indicando que Heracles las atrapó;
# i. se debe permitir búsquedas por coincidencia;
# j. eliminar al Basilisco y a las Sirenas;
# k. modificar el nodo que contiene a las Aves del Estínfalo, agregando que Heracles
# derroto a varias;
# l. modifique el nombre de la criatura Ladón por Dragón Ladón;
# m. realizar un listado por nivel del árbol;
# n. muestre las criaturas capturadas por Heracles.


# ┌───────────────────────────────┬────────────────────┬───────────────────────────────┬────────────────────┐
# │ Criaturas                     │ Derrotado por      │ Criaturas                     │ Derrotado por      │
# ├───────────────────────────────┼────────────────────┼───────────────────────────────┼────────────────────┤
# │ Ceto                          │ -                  │ Cerda de Cromión              │ Teseo              │
# │ Tifón                         │ Zeus               │ Ortro                         │ Heracles           │
# │ Equidna                       │ Argos Panoptes     │ Toro de Creta                 │ Teseo              │
# │ Dino                          │ -                  │ Jabalí de Calidón             │ Atalanta           │
# │ Pefredo                       │ -                  │ Carcinos                      │ -                  │
# │ Enio                          │ -                  │ Gerión                        │ Heracles           │
# │ Escila                        │ -                  │ Cloto                         │ -                  │
# │ Caribdis                      │ -                  │ Láquesis                      │ -                  │
# │ Euríale                       │ -                  │ Átropos                       │ -                  │
# │ Esteno                        │ -                  │ Minotauro de Creta            │ Teseo              │
# │ Medusa                        │ Perseo             │ Harpías                       │ -                  │
# │ Ladón                         │ Heracles           │ Argos Panoptes                │ Hermes             │
# │ Águila del Cáucaso            │ -                  │ Aves del Estínfalo            │ -                  │
# │ Quimera                       │ Belerofonte        │ Talos                         │ Medea              │
# │ Hidra de Lerna                │ Heracles           │ Sirenas                       │ -                  │
# │ León de Nemea                 │ Heracles           │ Pitón                         │ Apolo              │
# │ Esfinge                       │ Edipo              │ Cierva de Cerinea             │ -                  │
# │ Dragón de la Cólquida         │ -                  │ Basilisco                     │ -                  │
# │ Cerbero                       │ -                  │ Jabalí de Erimanto            │ -                  │
# └───────────────────────────────┴────────────────────┴───────────────────────────────┴────────────────────┘


from list_ import Lista
from queue_ import Queue

# Datos iniciales
criaturas_data = [
    ("Ceto", "-"), ("Tifon", "Zeus"), ("Equidna", "Argos Panoptes"),
    ("Dino", "-"), ("Pefredo", "-"), ("Enio", "-"), ("Escila", "-"),
    ("Caribdis", "-"), ("Euriale", "-"), ("Esteno", "-"),
    ("Medusa", "Perseo"), ("Ladon", "Heracles"), ("Aguila del Caucaso", "-"),
    ("Quimera", "Belerofonte"), ("Hidra de Lerna", "Heracles"),
    ("Leon de Nemea", "Heracles"), ("Esfinge", "Edipo"),
    ("Dragon de la Colquida", "-"), ("Cerbero", "-"),
    ("Cerda de Cromion", "Teseo"), ("Ortro", "Heracles"),
    ("Toro de Creta", "Teseo"), ("Jabali de Calidon", "Atalanta"),
    ("Carcinos", "-"), ("Gerion", "Heracles"), ("Cloto", "-"),
    ("Laquesis", "-"), ("Atropos", "-"), ("Minotauro de Creta", "Teseo"),
    ("Argos Panoptes", "Hermes"), ("Aves del Estinfalo", "-"),
    ("Talos", "Medea"), ("Sirenas", "-"), ("Piton", "Apolo"),
    ("Cierva de Cerinea", "-"), ("Basilisco", "-"), ("Jabali de Erimanto", "-"),
]

class NodoCriatura:
    def __init__(self, nombre: str, derrotado_por: str):
        # Datos del nodo
        self.nombre = nombre
        self.derrotado_por = derrotado_por
        self.descripcion = ""           
        self.capturada = None           
        # Punteros a los hijos
        self.izq = None
        self.der = None

class ArbolMitologico:
    def __init__(self):
        self.raiz = None

    def insertar(self, nodo_raiz: NodoCriatura, nombre: str, derrotado_por: str) -> NodoCriatura:
        # Si el arbol/subarbol esta vacio, creamos el nodo aca
        if nodo_raiz is None:
            return NodoCriatura(nombre, derrotado_por)
        
        # Insercion recursiva manteniendo el orden alfabetico (BST)
        if nombre < nodo_raiz.nombre:
            nodo_raiz.izq = self.insertar(nodo_raiz.izq, nombre, derrotado_por)
        elif nombre > nodo_raiz.nombre:
            nodo_raiz.der = self.insertar(nodo_raiz.der, nombre, derrotado_por)
        
        return nodo_raiz

    def inorden(self, nodo: NodoCriatura):
        # Recorrido inorden: Izquierda -> Raiz -> Derecha (imprime ordenado alfabeticamente)
        if nodo is not None:
            self.inorden(nodo.izq)
            print(f"Criatura: {nodo.nombre} | Derrotada por: {nodo.derrotado_por}")
            self.inorden(nodo.der)

    def buscar(self, nodo: NodoCriatura, nombre: str) -> NodoCriatura:
        # Caso base: llegamos a nulo o encontramos la criatura
        if nodo is None or nodo.nombre == nombre:
            return nodo
        
        # Buscamos por la rama correspondiente segun el nombre
        if nombre < nodo.nombre:
            return self.buscar(nodo.izq, nombre)
        return self.buscar(nodo.der, nombre)

    def buscar_por_heroe(self, nodo: NodoCriatura, heroe: str, campo: str = "derrotado_por"):
        # Barrido completo del arbol buscando en el campo que le pasemos por parametro
        if nodo is not None:
            self.buscar_por_heroe(nodo.izq, heroe, campo)
            
            if campo == "derrotado_por" and nodo.derrotado_por == heroe:
                print(f"- {nodo.nombre}")
            elif campo == "capturada" and nodo.capturada == heroe:
                print(f"- {nodo.nombre}")
                
            self.buscar_por_heroe(nodo.der, heroe, campo)

    def listar_no_derrotadas(self, nodo: NodoCriatura):
        # Recorre todo y filtra las que tienen el guion "-"
        if nodo is not None:
            self.listar_no_derrotadas(nodo.izq)
            if nodo.derrotado_por == "-":
                print(f"- {nodo.nombre}")
            self.listar_no_derrotadas(nodo.der)

    def busqueda_coincidencia(self, nodo: NodoCriatura, subcadena: str):
        # Busca si el string que pasamos es parte del nombre de la criatura (case insensitive)
        if nodo is not None:
            self.busqueda_coincidencia(nodo.izq, subcadena)
            if subcadena.lower() in nodo.nombre.lower():
                print(f"- Encontrado: {nodo.nombre}")
            self.busqueda_coincidencia(nodo.der, subcadena)

    def contar_heroes(self, nodo: NodoCriatura, conteo: dict):
        # Llena el diccionario sumando 1 cada vez que encuentra a un heroe que derroto a alguien
        if nodo is not None:
            self.contar_heroes(nodo.izq, conteo)
            if nodo.derrotado_por != "-":
                conteo[nodo.derrotado_por] = conteo.get(nodo.derrotado_por, 0) + 1
            self.contar_heroes(nodo.der, conteo)

    def _min_valor_nodo(self, nodo: NodoCriatura) -> NodoCriatura:
        # Helper para la funcion eliminar. Busca el nodo mas a la izquierda del subarbol derecho
        actual = nodo
        while actual.izq is not None:
            actual = actual.izq
        return actual

    def eliminar(self, raiz: NodoCriatura, nombre: str):
        # Busqueda recursiva del nodo a eliminar
        if raiz is None:
            return raiz
        if nombre < raiz.nombre:
            raiz.izq = self.eliminar(raiz.izq, nombre)
        elif nombre > raiz.nombre:
            raiz.der = self.eliminar(raiz.der, nombre)
        else:
            # Lo encontramos. Evaluamos los 3 casos de eliminacion en BST:
            
            # 1. Tiene solo el hijo derecho (o ninguno)
            if raiz.izq is None: return raiz.der
            # 2. Tiene solo el hijo izquierdo
            elif raiz.der is None: return raiz.izq
            
            # 3. Tiene dos hijos. Buscamos el sucesor inorden (el menor de los mayores)
            temp = self._min_valor_nodo(raiz.der)
            
            # Copiamos los datos del sucesor al nodo actual
            raiz.nombre = temp.nombre
            raiz.derrotado_por = temp.derrotado_por
            raiz.descripcion = temp.descripcion
            raiz.capturada = temp.capturada
            
            # Eliminamos el sucesor original
            raiz.der = self.eliminar(raiz.der, temp.nombre)
            
        return raiz

    def recorrido_por_niveles(self):
        # Barrido por niveles (BFS). Usamos la clase Queue de la catedra.
        if not self.raiz:
            return
        
        cola = Queue() 
        cola.arrive(self.raiz) 

        while cola.size() > 0: 
            nodo_actual = cola.attention() 
            print(f"- {nodo_actual.nombre}")
            
            # Vamos encolando los hijos de izquierda a derecha
            if nodo_actual.izq is not None:
                cola.arrive(nodo_actual.izq) 
            if nodo_actual.der is not None:
                cola.arrive(nodo_actual.der) 

if __name__ == "__main__":
    arbol = ArbolMitologico()
    
    # Cargamos el arbol con la lista de tuplas
    for criatura, derrotado in criaturas_data:
        arbol.raiz = arbol.insertar(arbol.raiz, criatura, derrotado)

    print("\n--- a. Listado inorden de criaturas ---")
    arbol.inorden(arbol.raiz)

    print("\n--- b. Cargar descripción ---")
    nodo_medusa = arbol.buscar(arbol.raiz, "Medusa")
    if nodo_medusa:
        nodo_medusa.descripcion = "Gorgona con serpientes en lugar de cabello."
        print("Descripción de Medusa cargada.")

    print("\n--- c. Información de Talos ---")
    nodo_talos = arbol.buscar(arbol.raiz, "Talos")
    if nodo_talos:
        print(f"Nombre: {nodo_talos.nombre}, Derrotado por: {nodo_talos.derrotado_por}, "
              f"Descripción: '{nodo_talos.descripcion}', Capturada por: {nodo_talos.capturada}")

    print("\n--- d. Top 3 Héroes/Dioses ---")
    conteo_heroes = {}
    arbol.contar_heroes(arbol.raiz, conteo_heroes)

    lista_heroes = Lista() 
    # Pasamos el dict a la Lista para ordenarla con los metodos provistos
    for heroe, cantidad in conteo_heroes.items():
        lista_heroes.append({"heroe": heroe, "cantidad": cantidad}) 

    # Seteamos el criterio de ordenamiento apuntando a la key 'cantidad'
    lista_heroes.add_criterion("cantidad_derrotas", lambda x: x["cantidad"]) 
    lista_heroes.sort_by_criterion("cantidad_derrotas") 

    print("Los 3 héroes con más criaturas derrotadas:")
    for i in range(1, 4):
        # Controlamos por las dudas que la lista no tenga menos de 3 heroes
        if len(lista_heroes) >= i:
            h = lista_heroes[-i] # Leemos de atras para adelante (descendente)
            print(f"{i}. {h['heroe']} ({h['cantidad']} criaturas)")

    print("\n--- e. Criaturas derrotadas por Heracles ---")
    arbol.buscar_por_heroe(arbol.raiz, "Heracles", "derrotado_por")

    print("\n--- f. Criaturas no derrotadas ---")
    arbol.listar_no_derrotadas(arbol.raiz)

    print("\n--- g y h. Modificar nodos indicando que Heracles las atrapó ---")
    a_capturar = ["Cerbero", "Toro de Creta", "Cierva de Cerinea", "Jabali de Erimanto"]
    for nombre in a_capturar:
        nodo = arbol.buscar(arbol.raiz, nombre)
        if nodo:
            nodo.capturada = "Heracles"
    print("Modificaciones realizadas. (Verificar en el punto n)")

    print("\n--- i. Búsquedas por coincidencia ('Cer') ---")
    arbol.busqueda_coincidencia(arbol.raiz, "Cer")

    print("\n--- j. Eliminar Basilisco y Sirenas ---")
    arbol.raiz = arbol.eliminar(arbol.raiz, "Basilisco")
    arbol.raiz = arbol.eliminar(arbol.raiz, "Sirenas")
    print("Eliminados correctamente.")

    print("\n--- k. Modificar Aves del Estinfalo ---")
    nodo_aves = arbol.buscar(arbol.raiz, "Aves del Estinfalo")
    if nodo_aves:
        nodo_aves.derrotado_por = "Heracles (derrotó a varias)"
        print(f"Modificado: {nodo_aves.nombre} -> Derrotado por: {nodo_aves.derrotado_por}")

    print("\n--- l. Modificar Ladon por Dragon Ladon ---")
    nodo_ladon = arbol.buscar(arbol.raiz, "Ladon")
    if nodo_ladon:
        derrotado = nodo_ladon.derrotado_por
        arbol.raiz = arbol.eliminar(arbol.raiz, "Ladon")
        # Volvemos a insertarlo con el nombre nuevo asi no rompe la logica del arbol
        arbol.raiz = arbol.insertar(arbol.raiz, "Dragon Ladon", derrotado)
        print("Ladon renombrado y reubicado en el árbol como Dragon Ladon.")

    print("\n--- m. Listado por nivel del árbol (Usando Queue) ---")
    arbol.recorrido_por_niveles()

    print("\n--- n. Criaturas capturadas por Heracles ---")
    arbol.buscar_por_heroe(arbol.raiz, "Heracles", "capturada")