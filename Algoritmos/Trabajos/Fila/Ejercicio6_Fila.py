from list_ import Lista

# 1. Definimos los criterios de orden para la lista profesional
def por_nombre(superheroe):
    return superheroe['nombre']

def por_casa(superheroe):
    return superheroe['casa']

def preparar_lista():
    lista_heroes = Lista()
    # Agregamos los criterios a la estructura para que sepa cómo ordenar/buscar
    lista_heroes.add_criterion('nombre', por_nombre)
    lista_heroes.add_criterion('casa', por_casa)
    
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
        lista_heroes.append(d)
    return lista_heroes

# --- ACTIVIDADES RAZONADAS ---

def actividades(lista):
    # [a] Eliminar Linterna Verde
    # La búsqueda binaria requiere ordenar por el criterio primero
    pos = lista.search("Linterna Verde", "nombre")
    if pos is not None:
        eliminado = lista.pop(pos)
        print(f"Eliminado: {eliminado['nombre']}")

    # [b] Año de Wolverine
    pos = lista.search("Wolverine", "nombre")
    if pos is not None:
        print(f"Wolverine apareció en: {lista[pos]['anio']}")

    # [c] Cambiar casa de Dr. Strange a Marvel
    pos = lista.search("Dr. Strange", "nombre")
    if pos is not None:
        lista[pos]['casa'] = "Marvel"
        print("Casa de Dr. Strange actualizada a Marvel")

    # [d] Filtrado por Bio (Traje o Armadura)
    # Como no hay un criterio específico, recorremos la lista
    print("Héroes con traje o armadura:")
    for h in lista:
        if "traje" in h["bio"].lower() or "armadura" in h["bio"].lower():
            print(f" - {h['nombre']}")

    # [e] Superhéroes anteriores a 1963
    print("Héroes anteriores a 1963:")
    for h in lista:
        if h["anio"] < 1963:
            print(f" - {h['nombre']} ({h['casa']})")

    # [i] Conteo por casa
    # Razonamiento: Usamos un diccionario para contar frecuencias
    conteo = {}
    for h in lista:
        casa = h['casa']
        conteo[casa] = conteo.get(casa, 0) + 1
    print(f"Conteo por casa: {conteo}")

if __name__ == "__main__":
    mi_lista = preparar_lista()
    actividades(mi_lista)