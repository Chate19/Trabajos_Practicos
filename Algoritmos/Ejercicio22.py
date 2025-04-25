def usar_la_fuerza(mochila):
    if not mochila:
        return False, None
    objeto_actual = mochila.pop(0)
    if objeto_actual == "sable de luz":
        return True, 1
    encontrado, cantidad_sacados = usar_la_fuerza(mochila)
    if encontrado:
        return True, 1 + cantidad_sacados
    else:
        return False, None

mochila_con_sable = ["botella de agua", "comida", "sable de luz", "mapa"]
encontrado_sable, objetos_sacados = usar_la_fuerza(mochila_con_sable.copy())

if encontrado_sable:
    print(f"Se necesitó sacar {objetos_sacados} objetos para encontrar el sable de luz.")
else:
    print("El sable de luz no estaba en esta mochila.")

mochila_sin_sable = ["botella de agua", "comida", "mapa"]
encontrado_sable_sin, objetos_sacados_sin = usar_la_fuerza(mochila_sin_sable.copy())

if encontrado_sable_sin:
    print(f"Se necesitó sacar {objetos_sacados_sin} objetos para encontrar el sable de luz.")
else:
    print("El sable de luz no estaba en esta mochila.")