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


class NodoArbol:
    def __init__(self, nombre, es_heroe):
        self.nombre = nombre
        self.es_heroe = es_heroe
        self.izq = None
        self.der = None



def insertar_nodo(raiz, nombre, es_heroe):
    if raiz is None:
        return NodoArbol(nombre, es_heroe)
    if nombre.lower() < raiz.nombre.lower():
        raiz.izq = insertar_nodo(raiz.izq, nombre, es_heroe)
    else:
        raiz.der = insertar_nodo(raiz.der, nombre, es_heroe)
    return raiz


def inorden(raiz):
    if raiz:
        inorden(raiz.izq)
        print("  -", raiz.nombre)
        inorden(raiz.der)


def inorden_descendente(raiz):
    if raiz:
        inorden_descendente(raiz.der)
        print("  -", raiz.nombre)
        inorden_descendente(raiz.izq)


def listar_villanos(raiz):
    if raiz:
        listar_villanos(raiz.izq)
        if not raiz.es_heroe:
            print("  -", raiz.nombre)
        listar_villanos(raiz.der)


def mostrar_heroes_con_c(raiz):
    if raiz:
        mostrar_heroes_con_c(raiz.izq)
        if raiz.es_heroe and raiz.nombre.lower().startswith('c'):
            print("  -", raiz.nombre)
        mostrar_heroes_con_c(raiz.der)


def contar_heroes(raiz):
    if raiz is None:
        return 0
    return (1 if raiz.es_heroe else 0) + contar_heroes(raiz.izq) + contar_heroes(raiz.der)


def buscar_proximidad(raiz, texto):
    if raiz:
        if texto.lower() in raiz.nombre.lower():
            return raiz
        nodo = buscar_proximidad(raiz.izq, texto)
        if nodo:
            return nodo
        return buscar_proximidad(raiz.der, texto)
    return None


def generar_bosque(raiz, arbol_heroes=None, arbol_villanos=None):
    if arbol_heroes is None:
        arbol_heroes = None
    if arbol_villanos is None:
        arbol_villanos = None

    if raiz:
        if raiz.es_heroe:
            arbol_heroes = insertar_nodo(arbol_heroes, raiz.nombre, True)
        else:
            arbol_villanos = insertar_nodo(arbol_villanos, raiz.nombre, False)
        arbol_heroes, arbol_villanos = generar_bosque(raiz.izq, arbol_heroes, arbol_villanos)
        arbol_heroes, arbol_villanos = generar_bosque(raiz.der, arbol_heroes, arbol_villanos)
    return arbol_heroes, arbol_villanos


def contar_nodos(raiz):
    if raiz is None:
        return 0
    return 1 + contar_nodos(raiz.izq) + contar_nodos(raiz.der)



raiz = None

for personaje in superheroes:
    nombre = personaje["name"]
    es_heroe = not personaje["is_villain"]
    raiz = insertar_nodo(raiz, nombre, es_heroe)



print("=" * 60)
print("VILLANOS ORDENADOS ALFABÉTICAMENTE")
print("=" * 60)
listar_villanos(raiz)

print("\n" + "=" * 60)
print("SUPERHÉROES QUE EMPIEZAN CON 'C'")
print("=" * 60)
mostrar_heroes_con_c(raiz)

print("\n" + "=" * 60)
print("CANTIDAD TOTAL DE SUPERHÉROES")
print("=" * 60)
print("Cantidad de héroes en el árbol:", contar_heroes(raiz))

print("\n" + "=" * 60)
print("CORRECCIÓN DE NOMBRE POR BÚSQUEDA DE PROXIMIDAD")
print("=" * 60)
nodo = buscar_proximidad(raiz, "strann")
if nodo:
    print("  - Encontrado:", nodo.nombre)
    nodo.nombre = "Doctor Strange"
    print("  - Nombre corregido correctamente a:", nodo.nombre)
else:
    print("  - No se encontró ninguna coincidencia.")

print("\n" + "=" * 60)
print("SUPERHÉROES EN ORDEN DESCENDENTE")
print("=" * 60)
def listar_heroes_desc(raiz):
    if raiz:
        listar_heroes_desc(raiz.der)
        if raiz.es_heroe:
            print("  -", raiz.nombre)
        listar_heroes_desc(raiz.izq)
listar_heroes_desc(raiz)

print("\n" + "=" * 60)
print("BOSQUE DE HÉROES Y VILLANOS")
print("=" * 60)
arbol_heroes, arbol_villanos = generar_bosque(raiz)
print("Nodos en árbol de héroes:", contar_nodos(arbol_heroes))
print("Nodos en árbol de villanos:", contar_nodos(arbol_villanos))

print("\n" + "=" * 60)
print("BARRIDO ALFABÉTICO DE HÉROES")
print("=" * 60)
inorden(arbol_heroes)

print("\n" + "=" * 60)
print("BARRIDO ALFABÉTICO DE VILLANOS")
print("=" * 60)
inorden(arbol_villanos)
