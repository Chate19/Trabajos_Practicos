class Lista:
    def __init__(self):
        self.elementos = []

    def insertar(self, dato):
        self.elementos.append(dato)

    def eliminar(self, clave, valor):
        idx = -1
        for i, elem in enumerate(self.elementos):
            if elem.get(clave) == valor:
                idx = i
                break
        if idx != -1:
            return self.elementos.pop(idx)
        return None

    def buscar(self, clave, valor):
        for elem in self.elementos:
            if elem.get(clave) == valor:
                return elem
        return None

    def filtrar(self, condicion):
        return [e for e in self.elementos if condicion(e)]

    def contar_por(self, clave):
        cont = {}
        for elem in self.elementos:
            cont[elem[clave]] = cont.get(elem[clave], 0) + 1
        return cont

    def ordenar(self, clave):
        self.elementos.sort(key=lambda x: x[clave])

    def mostrar_todos(self):
        for e in self.elementos:
            print(e)


# ACTIVIDADES

def actividad_a(lista):
    print("\n[a] Listado ordenado por nombre:")
    lista.ordenar("nombre")
    for j in lista.elementos:
        print(" -", j["nombre"])
    print("\n[a] Listado ordenado por especie:")
    lista.ordenar("especie")
    for j in lista.elementos:
        print(" -", j["nombre"], f"({j['especie']})")


def actividad_b(lista):
    print("\n[b] Info completa de Ahsoka Tano y Kit Fisto:")
    for nom in ["Ahsoka Tano", "Kit Fisto"]:
        j = lista.buscar("nombre", nom)
        print(f" - {nom}: {j if j else 'No encontrado'}")


def actividad_c(lista):
    print("\n[c] Padawans de Yoda y Luke Skywalker:")
    maestros = ["Yoda", "Luke Skywalker"]
    for m in maestros:
        print(f"   Padawans de {m}:")
        pads = lista.filtrar(lambda j: m in j["maestros"])
        for p in pads:
            print("    -", p["nombre"])


def actividad_d(lista):
    print("\n[d] Jedi de especie humana y twi'lek:")
    resultado = lista.filtrar(lambda j: j["especie"].lower() in ("humana", "humano", "twi'lek"))
    for j in resultado:
        print(" -", j["nombre"], f"({j['especie']})")


def actividad_e(lista):
    print("\n[e] Jedi cuyo nombre comienza con 'A':")
    resultado = lista.filtrar(lambda j: j["nombre"].startswith("A"))
    for j in resultado:
        print(" -", j["nombre"])


def actividad_f(lista):
    print("\n[f] Jedi que usaron sable de más de un color:")
    resultado = lista.filtrar(lambda j: len(j["colores_sable"]) > 1)
    for j in resultado:
        print(" -", j["nombre"], "->", j["colores_sable"])


def actividad_g(lista):
    print("\n[g] Jedi que usaron sable amarillo o violeta:")
    resultado = lista.filtrar(
        lambda j: any(c.lower() in ("amarillo", "violeta") for c in j["colores_sable"])
    )
    for j in resultado:
        print(" -", j["nombre"], "->", j["colores_sable"])


def actividad_h(lista):
    print("\n[h] Padawans de Qui-Gon Jinn y Mace Windu:")
    for m in ["Qui-Gon Jinn", "Mace Windu"]:
        print(f"   Padawans de {m}:")
        pads = lista.filtrar(lambda j: m in j["maestros"])
        for p in pads:
            print("    -", p["nombre"])



# PROGRAMA PRINCIPAL

if __name__ == "__main__":
    lista = Lista()


jedi_data = [
    {"nombre": "Anakin Skywalker", "maestros": ["Qui-Gon Jinn"], "colores_sable": ["azul"], "especie": "humano"},
    {"nombre": "Ahsoka Tano", "maestros": ["Anakin Skywalker"], "colores_sable": ["verde", "blanco"], "especie": "togruta"},
    {"nombre": "Kit Fisto", "maestros": ["Yoda"], "colores_sable": ["verde"], "especie": "nautolano"},
    {"nombre": "Luke Skywalker", "maestros": ["Yoda", "Obi-Wan Kenobi"], "colores_sable": ["azul", "verde"], "especie": "humano"},
    {"nombre": "Aayla Secura", "maestros": ["Quinlan Vos"], "colores_sable": ["azul"], "especie": "twi'lek"},
    {"nombre": "Mace Windu", "maestros": ["Yoda"], "colores_sable": ["violeta"], "especie": "humano"},
    {"nombre": "Yoda", "maestros": [], "colores_sable": ["verde"], "especie": "desconocida"},
    {"nombre": "Qui-Gon Jinn", "maestros": ["Dooku"], "colores_sable": ["verde"], "especie": "humano"},
    {"nombre": "Obi-Wan Kenobi", "maestros": ["Qui-Gon Jinn"], "colores_sable": ["azul"], "especie": "humano"},
    {"nombre": "Ezra Bridger", "maestros": ["Kanan Jarrus"], "colores_sable": ["azul", "verde"], "especie": "humano"},
    {"nombre": "Grogu", "maestros": ["Luke Skywalker"], "colores_sable": ["verde"], "especie": "desconocida"},
    {"nombre": "Ben Solo", "maestros": ["Luke Skywalker"], "colores_sable": ["azul", "rojo"], "especie": "humano"},
    {"nombre": "Depa Billaba", "maestros": ["Mace Windu"], "colores_sable": ["verde"], "especie": "humano"},
    {"nombre": "Eeth Koth", "maestros": ["Mace Windu"], "colores_sable": ["azul"], "especie": "zorro"}
]
    
for j in jedi_data:
    lista.insertar(j)

actividad_a(lista)
actividad_b(lista)
actividad_c(lista)
actividad_d(lista)
actividad_e(lista)
actividad_f(lista)
actividad_g(lista)
actividad_h(lista)