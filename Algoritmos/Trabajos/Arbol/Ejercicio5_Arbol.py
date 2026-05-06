# 5. Dado un árbol con los nombre de los superhéroes y villanos de la saga Marvel Cinematic Univer-
# se (MCU), desarrollar un algoritmo que contemple lo siguiente:

# a. además del nombre del superhéroe, en cada nodo del árbol se almacenará un campo boo-
# leano que indica si es un héroe o un villano, True y False respectivamente;
# b. listar los villanos ordenados alfabéticamente;
# c. mostrar todos los superhéroes que empiezan con C;
# d. determinar cuántos superhéroes hay el árbol;
# e. Doctor Strange en realidad está mal cargado. Utilice una búsqueda por proximidad para
# encontrarlo en el árbol y modificar su nombre;
# f. listar los superhéroes ordenados de manera descendente;
# g. generar un bosque a partir de este árbol, un árbol debe contener a los superhéroes y otro a
# los villanos, luego resolver las siguiente tareas:
# 	I. determinar cuántos nodos tiene cada árbol;
# 	II. realizar un barrido ordenado alfabéticamente de cada árbol.

from super_heroes_data import superheroes
from list_ import Lista

class ArbolBinarioBusqueda:
    # Clase privada para los nodos, siguiendo el estilo de tu clase Graph
    class __Nodo:
        def __init__(self, valor: str, es_heroe: bool):
            self.valor = valor
            self.es_heroe = es_heroe
            self.izquierdo = None
            self.derecho = None

    def __init__(self):
        self.raiz = None

    def insertar(self, valor: str, es_heroe: bool) -> None:
        def __insertar(raiz, valor, es_heroe):
            if raiz is None:
                return ArbolBinarioBusqueda.__Nodo(valor, es_heroe)
            # Orden alfabético para mantener la estructura de búsqueda
            if valor.lower() < raiz.valor.lower():
                raiz.izquierdo = __insertar(raiz.izquierdo, valor, es_heroe)
            else:
                raiz.derecho = __insertar(raiz.derecho, valor, es_heroe)
            return raiz
        self.raiz = __insertar(self.raiz, valor, es_heroe)

    def obtener_villanos_alfabetico(self) -> Lista:
        lista_villanos = Lista()
        def __inorden(raiz):
            if raiz:
                __inorden(raiz.izquierdo)
                if not raiz.es_heroe:
                    lista_villanos.append(raiz.valor)
                __inorden(raiz.derecho)
        __inorden(self.raiz)
        return lista_villanos

    def obtener_heroes_con_c(self) -> Lista:
        lista_c = Lista()
        def __inorden(raiz):
            if raiz:
                __inorden(raiz.izquierdo)
                if raiz.es_heroe and raiz.valor.lower().startswith('c'):
                    lista_c.append(raiz.valor)
                __inorden(raiz.derecho)
        __inorden(self.raiz)
        return lista_c

    def contar_heroes(self) -> int:
        def __contar(raiz):
            if raiz is None:
                return 0
            # Suma 1 si es héroe, más los conteos de sus ramas
            actual = 1 if raiz.es_heroe else 0
            return actual + __contar(raiz.izquierdo) + __contar(raiz.derecho)
        return __contar(self.raiz)

    def buscar_por_proximidad_y_modificar(self, texto_buscado: str, nuevo_nombre: str) -> bool:
        def __buscar(raiz, texto):
            if raiz:
                if texto.lower() in raiz.valor.lower():
                    return raiz
                resultado = __buscar(raiz.izquierdo, texto)
                if resultado:
                    return resultado
                return __buscar(raiz.derecho, texto)
            return None
        
        nodo = __buscar(self.raiz, texto_buscado)
        if nodo:
            nodo.valor = nuevo_nombre
            return True
        return False

    def obtener_heroes_descendente(self) -> Lista:
        lista_desc = Lista()
        def __inorden_inverso(raiz):
            if raiz:
                __inorden_inverso(raiz.derecho) # Primero el mayor
                if raiz.es_heroe:
                    lista_desc.append(raiz.valor)
                __inorden_inverso(raiz.izquierdo) # Luego el menor
        __inorden_inverso(self.raiz)
        return lista_desc

    def contar_nodos(self) -> int:
        def __contar(raiz):
            if raiz is None:
                return 0
            return 1 + __contar(raiz.izquierdo) + __contar(raiz.derecho)
        return __contar(self.raiz)

    def barrido_alfabetico(self) -> Lista:
        lista_barrido = Lista()
        def __inorden(raiz):
            if raiz:
                __inorden(raiz.izquierdo)
                lista_barrido.append(f"{raiz.valor} ({'Héroe' if raiz.es_heroe else 'Villano'})")
                __inorden(raiz.derecho)
        __inorden(self.raiz)
        return lista_barrido

# Función para generar el bosque (Punto G)
def generar_bosque(arbol_original: ArbolBinarioBusqueda):
    arbol_heroes = ArbolBinarioBusqueda()
    arbol_villanos = ArbolBinarioBusqueda()

    def __recorrer_e_insertar(raiz):
        if raiz:
            if raiz.es_heroe:
                arbol_heroes.insertar(raiz.valor, True)
            else:
                arbol_villanos.insertar(raiz.valor, False)
            __recorrer_e_insertar(raiz.izquierdo)
            __recorrer_e_insertar(raiz.derecho)
    
    __recorrer_e_insertar(arbol_original.raiz)
    return arbol_heroes, arbol_villanos

# --- PRUEBA DEL PROGRAMA ---
if __name__ == "__main__":
    arbol_mcu = ArbolBinarioBusqueda()

    # Carga inicial desde los datos proporcionados[cite: 7]
    for personaje in superheroes:
        nombre = personaje["name"]
        es_heroe = not personaje["is_villain"]
        arbol_mcu.insertar(nombre, es_heroe)

    print("--- Villanos ordenados alfabéticamente ---")
    villanos = arbol_mcu.obtener_villanos_alfabetico()
    villanos.show() # Método de tu clase Lista[cite: 3]

    print("\n--- Héroes que empiezan con la letra C ---")
    arbol_mcu.obtener_heroes_con_c().show()

    print(f"\n--- Total de superhéroes en el árbol: {arbol_mcu.contar_heroes()} ---")

    print("\n--- Modificación de Doctor Strange (Búsqueda por proximidad) ---")
    if arbol_mcu.buscar_por_proximidad_y_modificar("strann", "Doctor Strange"):
        print("Corrección realizada con éxito.")

    print("\n--- Héroes en orden descendente ---")
    arbol_mcu.obtener_heroes_descendente().show()

    print("\n--- Generación del Bosque ---")
    arb_h, arb_v = generar_bosque(arbol_mcu)
    print(f"Nodos en el árbol de Héroes: {arb_h.contar_nodos()}")
    print(f"Nodos en el árbol de Villanos: {arb_v.contar_nodos()}")

    print("\n--- Barrido del Árbol de Héroes ---")
    arb_h.barrido_alfabetico().show()