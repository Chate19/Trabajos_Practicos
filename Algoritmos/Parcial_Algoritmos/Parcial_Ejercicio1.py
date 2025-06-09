#Ejercicio 1: Dado una lista simple de python (array) de 15 superheroes realizar dos funciones recursivas:
#funcion recursiva  para buscar, determinar si Capitan America esta en la lista.
#funcion recursiva para listar los superheroes de la lista.

superheroes: list = [
    "Iron Man",
    "Capitan America",
    "Thor",
    "Hulk",
    "Black Widow",
    "Hawkeye",
    "Spider-Man",
    "Doctor Strange",
    "Black Panther",
    "Ant-Man",
    "Capitana Marvel",
    "Vision",
    "Scarlet Witch",
    "Falcon",
    "Winter Soldier"
]

def buscar_capitan_america(superheroes: list, indice: int=0):
    if indice >= len(superheroes):
        return False
    if superheroes[indice] == "Capitan America":
        return True
    return buscar_capitan_america(superheroes, indice + 1)

def listar_superheroes(superheroes: list, indice: int=0):
    if indice >= len(superheroes):
        return []
    return [superheroes[indice]] + listar_superheroes(superheroes, indice + 1)  


print("Ejercicio 1: Parcial Algoritmos - Chatelain Agustin")
print("-" * 75)
if buscar_capitan_america(superheroes):
    print("Capitan America esta en la lista.")
print("-" * 75)
if listar_superheroes(superheroes):
    print("Listado de superheroes:")
    for heroe in listar_superheroes(superheroes):
        print(heroe)