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

    def mostrar_todos(self):
        for e in self.elementos:
            print(e)



# ACTIVIDADES (usando solo el TDA)

def actividad_a(lista):
    print("\n[a] Eliminar Linterna Verde")
    eliminado = lista.eliminar("nombre", "Linterna Verde")
    print("+ Eliminado:", eliminado["nombre"] if eliminado else "No encontrado")


def actividad_b(lista):
    print("\n[b] Anio de aparicion de Wolverine:")
    wol = lista.buscar("nombre", "Wolverine")
    print(wol["anio"] if wol else "No encontrado")


def actividad_c(lista):
    print("\n[c] Cambiar casa de Dr. Strange a Marvel...")
    doc = lista.buscar("nombre", "Dr. Strange")
    if doc:
        doc["casa"] = "Marvel"
        print("+ Casa actualizada")


def actividad_d(lista):
    print("\n[d] Nombres que mencionan 'traje' o 'armadura':")
    resultado = lista.filtrar(lambda h: "traje" in h["bio"].lower() or "armadura" in h["bio"].lower())
    for h in resultado:
        print(" -", h["nombre"])


def actividad_e(lista):
    print("\n[e] Superheroes anteriores a 1963:")
    resultado = lista.filtrar(lambda h: h["anio"] < 1963)
    for h in resultado:
        print(f" - {h['nombre']} ({h['casa']})")


def actividad_f(lista):
    print("\n[f] Casa de Capitana Marvel y Mujer Maravilla:")
    for nom in ["Capitana Marvel", "Mujer Maravilla"]:
        h = lista.buscar("nombre", nom)
        print(f" - {nom}: {h['casa'] if h else 'No encontrada'}")


def actividad_g(lista):
    print("\n[g] Info completa de Flash y Star-Lord:")
    for nom in ["Flash", "Star-Lord"]:
        h = lista.buscar("nombre", nom)
        print(f" - {nom}: {h if h else 'No encontrado'}")


def actividad_h(lista):
    print("\n[h] Nombres que empiezan con B, M o S:")
    resultado = lista.filtrar(lambda h: h["nombre"][0].upper() in "BMS")
    for h in resultado:
        print(" -", h["nombre"])


def actividad_i(lista):
    print("\n[i] Cantidad de superheroes por casa:")
    conteo = lista.contar_por("casa")
    for casa, cant in conteo.items():
        print(f" - {casa}: {cant}")



# PROGRAMA PRINCIPAL

if __name__ == "__main__":
    lista = Lista()

    datos = [
        {"nombre": "Linterna Verde", "anio": 1940, "casa": "DC", "bio": "Portador del anillo; traje energético."},
        {"nombre": "Wolverine", "anio": 1974, "casa": "Marvel", "bio": "Mutante con garras retráctiles."},
        {"nombre": "Dr. Strange", "anio": 1963, "casa": "DC", "bio": "Hechicero supremo."},
        {"nombre": "Flash", "anio": 1940, "casa": "DC", "bio": "El hombre más rápido; traje rojo."},
        {"nombre": "Capitana Marvel", "anio": 1968, "casa": "Marvel", "bio": "Heroína cósmica."},
        {"nombre": "Mujer Maravilla", "anio": 1941, "casa": "DC", "bio": "Amazona con armadura."},
        {"nombre": "Star-Lord", "anio": 1976, "casa": "Marvel", "bio": "Líder Guardianes."},
        {"nombre": "Batman", "anio": 1939, "casa": "DC", "bio": "Detective; traje murciélago."},
        {"nombre": "Spider-Man", "anio": 1962, "casa": "Marvel", "bio": "Hombre araña; traje rojo-azul."},
        {"nombre": "Superman", "anio": 1938, "casa": "DC", "bio": "Hombre de acero; capa y traje."}
    ]
    for d in datos:
        lista.insertar(d)

    actividad_a(lista)
    actividad_b(lista)
    actividad_c(lista)
    actividad_d(lista)
    actividad_e(lista)
    actividad_f(lista)
    actividad_g(lista)
    actividad_h(lista)
    actividad_i(lista)