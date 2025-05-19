# 13. Dada una pila con los trajes de Iron Man utilizados en las películas de Marvel Cinematic Uni-verse (MCU) de los cuales se conoce el nombre del modelo, nombre de la película en la que se usó y el estado en que quedó al final de la película (Dañado, Impecable, Destruido), resolver las siguientes actividades:
#   a. determinar si el modelo Mark XLIV (Hukbuster) fue utilizado en alguna de las películas,además mostrar el nombre de dichas películas;
#   b. mostrar los modelos que quedaron dañados, sin perder información de la pila.
#   c. eliminar los modelos de los trajes destruidos mostrando su nombre;
#   d. un modelo de traje puede usarse en más de una película y en una película se pueden usar más de un modelo de traje, estos deben cargarse por separado;
#   e. agregar el modelo Mark LXXXV a la pila, tener en cuenta que no se pueden cargar modelos repetidos en una misma película; 
#   f. mostrar los nombre de los trajes utilizados en las películas “Spider-Man: Homecoming” y “Capitan America: Civil War”.

import stack
import random

class Trajes:
    def __init__(self, modelo, pelicula, estado):
        self.modelo = modelo
        self.pelicula = pelicula
        self.estado = estado
    def __str__(self):
        return f"Modelo: {self.modelo}, Pelicula: {self.pelicula}, Estado: {self.estado}"
    
modelo = {
    1: "Mark I",
    2: "Mark V",
    3: "Mark XLIV",
    4: "Mark LXXXV",
    5: "Mark L",
    6: "Mark III"
}

pelicula = {
    1: "Iron Man",
    2: "Iron Man 2",
    3: "Avengers: Age of Ultron",
    4: "Spider-Man: Homecoming",
    5: "Capitan America: Civil War"
}

estado = {
    1: "Impecable",
    2: "Dañado",
    3: "Destruido"
}

def cargar_pila(pila:stack.Stack):
    usados = set()
    mark_lxxxv_cargado = False

    for i in range(10):
        mod = random.choice(list(modelo.values()))
        peli = random.choice(list(pelicula.values()))
        est = random.choice(list(estado.values()))
        clave = (mod, peli)

        if mod == "Mark LXXXV" and not mark_lxxxv_cargado:
            usados.add(clave)
            mark_lxxxv_cargado = True
            pila.push(Trajes(mod, peli, est))
            continue

        if clave not in usados:
            usados.add(clave)
            traje = Trajes(mod, peli, est)
            pila.push(traje)
    return pila

#a)
def hulkbuster(pila:stack.Stack):
    aux = stack.Stack()
    encontrado = False
    while not pila.size() == 0:
        traje = pila.pop()
        if traje.modelo == "Mark XLIV":
            encontrado = True
            print(f"El Modelo: {traje.modelo} es utilizado en la Pelicula: {traje.pelicula}")
        aux.push(traje)
        
    while not aux.size() == 0:
        pila.push(aux.pop())
    return encontrado

#b)
def dañados(pila:stack.Stack):
    aux = stack.Stack()
    while not pila.size() == 0:
        traje = pila.pop()
        if traje.estado == "Dañado":
            print(f"El Modelo: {traje.modelo} es dañado en la Pelicula: {traje.pelicula}")
        aux.push(traje)
        
    while not aux.size() == 0:
        pila.push(aux.pop())
        
#c)
def destruidos(pila:stack.Stack):
    aux = stack.Stack()
    while not pila.size() == 0:
        traje = pila.pop()
        if traje.estado == "Destruido":
            print(f"El Modelo: {traje.modelo} es destruido en laPelicula: {traje.pelicula}")
        else:
            aux.push(traje)
            
    while not aux.size() == 0:
        pila.push(aux.pop())
        
#f)
def apariciones(pila:stack.Stack):
    aux = stack.Stack()
    while not pila.size() == 0:
        traje = pila.pop()
        if traje.pelicula in ["Spider-Man: Homecoming", "Capitan America: Civil War"]:
            print(f"El Modelo: {traje.modelo} aparece en la Pelicula: {traje.pelicula}")
        aux.push(traje)
        
    while not aux.size() == 0: 
        pila.push(aux.pop())
        

pila = stack.Stack()
cargar_pila(pila)
    
print("a) Hulkbuster")
hulkbuster(pila)
    
print("b) Trajes Dañados")
dañados(pila)
    
print("c) Trajes Destruidos")
destruidos(pila)
    
print("f) Trajes en peliculas especificadas")
apariciones(pila)