import random
import time
import colores

def usar_la_fuerza(mochila:list, contador:int=0):
    '''Busca en la mochila el sable de luz, si no lo encuentra, lo busca de nuevo'''
    
    if not mochila:
        print(colores.color("[x] El sable de luz no se encuentra en la mochila.", colores.ROJO))  
        return -1  # -Retorna -1 si no se encuentra el sable de luz
    
    print(colores.color("[*] Buscando sable de luz...",colores.CIAN))
    time.sleep(1)  # -Simula el tiempo de búsqueda
    print(colores.color("[*] concentrando la fuerza...",colores.CIAN))
    time.sleep(2)  # -Simula el tiempo de concentración
    
    item = mochila.pop() # -Saca un objeto de la mochila al azar
    
    if item == "Sable de luz":
        print(colores.color(f"¡Lo encontreee! me llevo {contador + 1} intentos!",colores.VERDE))
        return contador + 1  # -Retorna el número de intentos si se encuentra el sable de luz
    else:
        print(colores.color(f"[?] Qué es esto...? '{item}'. Mmmm no es el sable",colores.AMARILLO))
        time.sleep(0.5)
    return usar_la_fuerza(mochila, contador + 1)
    

def generar_mochila() -> list:
    '''Genera una mochila con 20 objetos aleatorios de la lista de posibles objetos'''
    # - Lista de objetos posibles
    posibles_objetos: list = [
        "Holocrón Jedi",
        "Comunicador galáctico",
        "Medpac",
        "Comida racionada",
        "Filtro de agua portátil",
        "Cable de agarre",
        "Manta térmica",
        "Repulsor de emergencia",
        "Módulo de traducción",
        "Sensor de vida",
        "Lentes de visión nocturna",
        "Mapa estelar portátil",
        "Cristal Kyber",
        "Mochila de entrenamiento Jedi",
        "Medidor de midiclorianos",
        "Diario de meditación Jedi",
        "Amuleto de su maestro",
        "Grabador de sonido"
    ]
    mochila = random.choices(posibles_objetos, k=20)    # - Se genera una mochila con 20 objetos aleatorios de la lista de posibles objetos

    if random.random() < 0.5:                           # - 50% de probabilidad de agregar un sable de luz
        indice = random.randint(0, 19)
        mochila[indice] = "Sable de luz"
    
    return mochila

def main():
    mochila = generar_mochila()
    usar_la_fuerza(mochila, 0)
    

if __name__ == "__main__":
    main()