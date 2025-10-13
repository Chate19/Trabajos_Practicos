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


from collections import deque, Counter


# Datos iniciales
criaturas_data = [
    ("Ceto", "-"),
    ("Tifon", "Zeus"),
    ("Equidna", "Argos Panoptes"),
    ("Dino", "-"),
    ("Pefredo", "-"),
    ("Enio", "-"),
    ("Escila", "-"),
    ("Caribdis", "-"),
    ("Euriale", "-"),
    ("Esteno", "-"),
    ("Medusa", "Perseo"),
    ("Ladon", "Heracles"),
    ("Aguila del Caucaso", "-"),
    ("Quimera", "Belerofonte"),
    ("Hidra de Lerna", "Heracles"),
    ("Leon de Nemea", "Heracles"),
    ("Esfinge", "Edipo"),
    ("Dragon de la Colquida", "-"),
    ("Cerbero", "-"),
    ("Cerda de Cromion", "Teseo"),
    ("Ortro", "Heracles"),
    ("Toro de Creta", "Teseo"),
    ("Jabali de Calidon", "Atalanta"),
    ("Carcinos", "-"),
    ("Gerion", "Heracles"),
    ("Cloto", "-"),
    ("Laquesis", "-"),
    ("Atropos", "-"),
    ("Minotauro de Creta", "Teseo"),
    ("Argos Panoptes", "Hermes"),
    ("Aves del Estinfalo", "-"),
    ("Talos", "Medea"),
    ("Sirenas", "-"),
    ("Piton", "Apolo"),
    ("Cierva de Cerinea", "-"),
    ("Basilisco", "-"),
    ("Jabali de Erimanto", "-"),
]

# Normalizo evitando duplicados exactos
_seen = set()
criaturas = []
for name, defeated in criaturas_data:
    if name not in _seen:
        criaturas.append({"name": name, "defeated_by": defeated})
        _seen.add(name)


class Nodo:
    def __init__(self, name, defeated_by):
        self.name = name
        self.defeated_by = defeated_by  # string, '-' si no derrotada
        self.description = ""           # campo (b)
        self.capturada = ""             # campo (g), nombre del heroe/dios que la capturo
        self.left = None
        self.right = None

    def __repr__(self):
        return f"Nodo({self.name})"


def insertar(raiz, nodo):
    """Inserta por orden alfabetico por nombre (case-insensitive)."""
    if raiz is None:
        return nodo
    if nodo.name.lower() < raiz.name.lower():
        raiz.left = insertar(raiz.left, nodo)
    else:
        raiz.right = insertar(raiz.right, nodo)
    return raiz


def buscar(raiz, name):
    """Busca nodo por nombre exacto (case-insensitive). Retorna nodo o None."""
    if raiz is None:
        return None
    if name.lower() == raiz.name.lower():
        return raiz
    if name.lower() < raiz.name.lower():
        return buscar(raiz.left, name)
    return buscar(raiz.right, name)


def buscar_por_coincidencia(raiz, texto, resultado=None):
    """Busca nodos que contienen 'texto' en su nombre (case-insensitive)."""
    if resultado is None:
        resultado = []
    if raiz:
        if texto.lower() in raiz.name.lower():
            resultado.append(raiz)
        buscar_por_coincidencia(raiz.left, texto, resultado)
        buscar_por_coincidencia(raiz.right, texto, resultado)
    return resultado


def inorden_list(raiz, resultado=None):
    """Devuelve lista de nodos en orden alfabetico."""
    if resultado is None:
        resultado = []
    if raiz:
        inorden_list(raiz.left, resultado)
        resultado.append(raiz)
        inorden_list(raiz.right, resultado)
    return resultado


def inorden_print(raiz):
    """Imprime inorden: criatura - derrotado por."""
    nodes = inorden_list(raiz)
    print("=" * 60)
    print("INORDEN: Criatura  |  Derrotado por")
    print("=" * 60)
    for n in nodes:
        print(f"{n.name:<30} | {n.defeated_by}")
    print("=" * 60)


def nivel_print(raiz):
    """Listado por niveles (m)."""
    print("=" * 60)
    print("LISTADO POR NIVELES")
    print("=" * 60)
    if raiz is None:
        print("(arbol vacio)")
        return
    q = deque()
    q.append((raiz, 0))
    current_level = -1
    while q:
        node, lvl = q.popleft()
        if lvl != current_level:
            current_level = lvl
            print(f"\nNivel {lvl}:")
        print(f"  - {node.name} (Derrotado por: {node.defeated_by}; Capturada: {node.capturada})")
        if node.left:
            q.append((node.left, lvl + 1))
        if node.right:
            q.append((node.right, lvl + 1))
    print("\n" + "=" * 60)


def contar_nodos(raiz):
    if raiz is None:
        return 0
    return 1 + contar_nodos(raiz.left) + contar_nodos(raiz.right)


def encontrar_min(raiz):
    current = raiz
    while current.left:
        current = current.left
    return current


def eliminar(raiz, name):
    """Elimina nodo por nombre (case-insensitive)."""
    if raiz is None:
        return None
    if name.lower() < raiz.name.lower():
        raiz.left = eliminar(raiz.left, name)
    elif name.lower() > raiz.name.lower():
        raiz.right = eliminar(raiz.right, name)
    else:
        if raiz.left is None:
            return raiz.right
        elif raiz.right is None:
            return raiz.left
        else:
            temp = encontrar_min(raiz.right)
            raiz.name = temp.name
            raiz.defeated_by = temp.defeated_by
            raiz.description = temp.description
            raiz.capturada = temp.capturada
            raiz.right = eliminar(raiz.right, temp.name)
    return raiz


def listar_heracles_derrotados(raiz):
    """Lista criaturas derrotadas por Heracles."""
    nodes = inorden_list(raiz)
    return [n.name for n in nodes if n.defeated_by.lower() == "heracles"]


def listar_no_derrotadas(raiz):
    """Lista criaturas cuyo defeated_by es '-' o vacio."""
    nodes = inorden_list(raiz)
    return [n.name for n in nodes if (not n.defeated_by or n.defeated_by.strip() == "-" )]


def top_k_defensores(raiz, k=3):
    """Determina los k nombres que aparecen mas como 'defeated_by' (excluye '-' y vacios)."""
    nodes = inorden_list(raiz)
    cont = Counter()
    for n in nodes:
        who = (n.defeated_by or "").strip()
        if who and who != "-":
            cont[who] += 1
    return cont.most_common(k)


def criaturas_capturadas_por(raiz, capturador_name):
    nodes = inorden_list(raiz)
    return [n.name for n in nodes if n.capturada.lower() == capturador_name.lower()]


# Carga del arbol principal
root = None
for c in criaturas:
    node = Nodo(c["name"], c["defeated_by"])
    root = insertar(root, node)


# b) Funcion para anadir/actualizar descripcion
def set_description(raiz, nombre, texto):
    nodo = buscar(raiz, nombre)
    if nodo:
        nodo.description = texto
        return True
    return False

# h) marcar capturas por Heracles para los nodos indicados
def set_captured(raiz, nombre, capturador):
    nodo = buscar(raiz, nombre)
    if nodo:
        nodo.capturada = capturador
        return True
    return False


# k) actualizar Aves del Estinfalo: Heracles derroto a varias
def append_derrotado_por(raiz, nombre, nuevo_texto):
    nodo = buscar(raiz, nombre)
    if nodo:
        base = nodo.defeated_by.strip()
        if base == "-" or base == "":
            nodo.defeated_by = nuevo_texto
        else:
            nodo.defeated_by = f"{base}; {nuevo_texto}"
        return True
    return False


# l) renombrar Ladon por Dragon Ladon
def renombrar_nodo(raiz, antiguo, nuevo):
    nodo = buscar(raiz, antiguo)
    if nodo:
        # Guardar datos temporales
        desc = nodo.description
        cap = nodo.capturada
        defeated = nodo.defeated_by
        # Eliminar nodo antiguo e insertar nuevo con misma info
        raiz = eliminar(raiz, antiguo)
        nuevo_nodo = Nodo(nuevo, defeated)
        nuevo_nodo.description = desc
        nuevo_nodo.capturada = cap
        raiz = insertar(raiz, nuevo_nodo)
    return raiz


def main():
    global root

    # a) listado inorden de las criaturas y quienes la derrotaron
    print("\n" + "=" * 60)
    print("a) Listado inorden de criaturas y quienes la derrotaron")
    print("=" * 60)
    inorden_print(root)

    # b) cargar una breve descripcion (ejemplo para Talos y Quimera)
    set_description(root, "Talos", "Automata gigante de bronce creado por Hefesto, aparece en relatos cretenses.")
    set_description(root, "Quimera", "Bestia hibrida: cabeza de leon, cuerpo de cabra y cola de serpiente.")
    print("\n(b) Se cargaron descripciones de ejemplo para Talos y Quimera.")

    # c) mostrar toda la informacion de Talos
    print("\n" + "=" * 60)
    print("c) Informacion completa de Talos")
    print("=" * 60)
    nodo_talos = buscar(root, "Talos")
    if nodo_talos:
        print(f"Nombre      : {nodo_talos.name}")
        print(f"Derrotado por: {nodo_talos.defeated_by}")
        print(f"Capturada por: {nodo_talos.capturada or '(ninguna)'}")
        print(f"Descripcion : {nodo_talos.description or '(sin descripcion)'}")
    else:
        print("Talos no se encontro en el arbol.")

    # d) determinar los 3 heroes/dioses que derrotaron mayor cantidad de criaturas
    print("\n" + "=" * 60)
    print("d) Top 3 de heroes/dioses que derrotaron mas criaturas")
    print("=" * 60)
    top3 = top_k_defensores(root, 3)
    if top3:
        for i, (who, cnt) in enumerate(top3, 1):
            print(f"{i}. {who}  - {cnt} criaturas")
    else:
        print("No hay datos de derrotados.")

    # e) listar las criaturas derrotadas por Heracles
    print("\n" + "=" * 60)
    print("e) Criaturas derrotadas por Heracles")
    print("=" * 60)
    heracles_list = listar_heracles_derrotados(root)
    if heracles_list:
        for c in heracles_list:
            print("  -", c)
    else:
        print("Ninguna registrada.")

    # f) listar las criaturas que no han sido derrotadas
    print("\n" + "=" * 60)
    print("f) Criaturas que no han sido derrotadas")
    print("=" * 60)
    no_derrotadas = listar_no_derrotadas(root)
    for c in no_derrotadas:
        print("  -", c)

    # g) cada nodo ya dispone de campo 'capturada' (inicialmente vacio)
    print("\n(g) Campo 'capturada' disponible en cada nodo (inicialmente vacio).")

    # h) modificar nodos para indicar que Heracles atrapo ciertas criaturas
    targets_h = ["Cerbero", "Toro de Creta", "Cierva de Cerinea", "Jabali de Erimanto"]
    for t in targets_h:
        ok = set_captured(root, t, "Heracles")
        print(f"  - Marcado '{t}' como capturada por Heracles: {'OK' if ok else 'NO ENCONTRADO'}")

    # i) busqueda por coincidencia (ejemplo: buscar 'cer')
    print("\n" + "=" * 60)
    print("i) Busqueda por coincidencia (ejemplo: 'cer')")
    print("=" * 60)
    coincidencias = buscar_por_coincidencia(root, "cer")
    if coincidencias:
        for n in coincidencias:
            print(f"  - {n.name} (Derrotado por: {n.defeated_by}; Capturada: {n.capturada or '(ninguna)'})")
    else:
        print("No se encontraron coincidencias.")

    # j) eliminar Basilisco y Sirenas
    print("\n" + "=" * 60)
    print("j) Eliminando Basilisco y Sirenas")
    print("=" * 60)
    root = eliminar(root, "Basilisco")
    print("  - Basilisco eliminado (si existia).")
    root = eliminar(root, "Sirenas")
    print("  - Sirenas eliminadas (si existian).")

    # k) modificar Aves del Estinfalo, agregando que Heracles derroto a varias
    appended = append_derrotado_por(root, "Aves del Estinfalo", "Heracles (varios)")
    print("\n(k) Aves del Estinfalo modificado: " + ("OK" if appended else "NO ENCONTRADO"))

    # l) modificar Ladon por Dragon Ladon
    print("\n(l) Renombrando 'Ladon' a 'Dragon Ladon'")
    root = renombrar_nodo(root, "Ladon", "Dragon Ladon")
    print("  - Renombrado si Ladon existia.")

    # m) listado por nivel del arbol
    print("\n(m) Listado por nivel del arbol:")
    nivel_print(root)

    # n) mostrar criaturas capturadas por Heracles
    print("\n" + "=" * 60)
    print("n) Criaturas capturadas por Heracles")
    print("=" * 60)
    capturadas_heracles = criaturas_capturadas_por(root, "Heracles")
    if capturadas_heracles:
        for c in capturadas_heracles:
            print("  -", c)
    else:
        print("No hay criaturas capturadas por Heracles registradas.")

    # Extra: mostrar inorden final luego de modificaciones
    print("\n" + "=" * 60)
    print("Inorden final (despues de modificaciones y eliminaciones):")
    print("=" * 60)
    inorden_print(root)

    print("\nFin del programa.")
    print("=" * 60)

if __name__ == "__main__":
    main()

