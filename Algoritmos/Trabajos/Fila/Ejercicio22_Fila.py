from list_ import Lista

# 1. Criterios de orden: Fundamentales para la búsqueda binaria
def por_nombre(jedi):
    return jedi['nombre']

def por_especie(jedi):
    return jedi['especie']

def preparar_lista_jedi():
    lista_jedi = Lista()
    # Vinculamos los criterios para que la lista sepa cómo operar
    lista_jedi.add_criterion('nombre', por_nombre)
    lista_jedi.add_criterion('especie', por_especie)
    
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
        lista_jedi.append(j)
    return lista_jedi

# --- RAZONAMIENTO DE LAS ACTIVIDADES ---

def ejecutar_actividades(lista):
    # [a] Listado ordenado (Uso de sort_by_criterion)
    print("\n[a] Orden por nombre:")
    lista.sort_by_criterion('nombre')
    lista.show()

    # [b] Búsqueda binaria por nombre
    print("\n[b] Buscando a Ahsoka Tano:")
    pos = lista.search("Ahsoka Tano", "nombre")
    if pos is not None:
        print(f"Encontrado: {lista[pos]}")

    # [c] Filtrado por Maestros (Uso de lógica booleana)
    print("\n[c] Padawans de Luke Skywalker:")
    for jedi in lista:
        if "Luke Skywalker" in jedi["maestros"]:
            print(f" - {jedi['nombre']}")

    # [f] Jedi con más de un color de sable
    print("\n[f] Usaron más de un color:")
    for jedi in lista:
        if len(jedi["colores_sable"]) > 1:
            print(f" - {jedi['nombre']}: {jedi['colores_sable']}")

if __name__ == "__main__":
    mi_lista_jedi = preparar_lista_jedi()
    ejecutar_actividades(mi_lista_jedi)