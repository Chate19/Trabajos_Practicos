#10. Dada una cola con las notificaciones de las aplicaciones de redes sociales de un Smartphone, de las cual se cuenta con la hora de la notificación, la aplicación que la emitió y el mensaje, resolver las siguientes actividades:
	#a. escribir una función que elimine de la cola todas las notificaciones de Facebook;
	#b. escribir una función que muestre todas las notificaciones de Twitter, cuyo mensaje incluya la palabra ‘Python’, si perder datos en la cola;
	#c. utilizar una pila para almacenar temporáneamente las notificaciones producidas entre las 11:43 y las 15:57, y determinar cuántas son.

from queue import Queue
from datetime import datetime

def crear_notificacion(hora, aplicacion, mensaje):
    """
    Crea un diccionario representando una notificación.

    Parámetros:
    - hora (str): hora en formato "HH:MM"
    - aplicacion (str): nombre de la aplicación
    - mensaje (str): contenido del mensaje

    Retorna:
    - dict: notificación
    """
    return {"hora": hora, "aplicacion": aplicacion, "mensaje": mensaje}

def eliminar_facebook(cola):
    """
    Elimina todas las notificaciones de Facebook de la cola.

    Parámetros:
    - cola (Queue): cola original de notificaciones

    Retorna:
    - Queue: cola sin notificaciones de Facebook
    """
    cola_aux = Queue()
    while not cola.empty():
        noti = cola.get()
        if noti["aplicacion"].lower() != "facebook":
            cola_aux.put(noti)
    return cola_aux

def mostrar_twitter_python(cola):
    """
    Muestra por pantalla todas las notificaciones de Twitter cuyo mensaje contenga 'Python',
    sin perder las notificaciones de la cola.

    Parámetros:
    - cola (Queue): cola original de notificaciones

    Retorna:
    - Queue: cola restaurada sin modificaciones
    """
    cola_aux = Queue()
    print("\n Notificaciones de Twitter que contienen 'Python':")
    while not cola.empty():
        noti = cola.get()
        if noti["aplicacion"].lower() == "twitter" and "python" in noti["mensaje"].lower():
            print(f"[{noti['hora']}] {noti['aplicacion']}: {noti['mensaje']}")
        cola_aux.put(noti)
    return cola_aux

def contar_notificaciones_intervalo(cola, hora_inicio="11:43", hora_fin="15:57"):
    """
    Cuenta cuántas notificaciones ocurrieron en un intervalo de tiempo dado,
    almacenándolas en una pila temporal.

    Parámetros:
    - cola (Queue): cola de notificaciones
    - hora_inicio (str): hora inicial en formato "HH:MM"
    - hora_fin (str): hora final en formato "HH:MM"

    Retorna:
    - Queue: cola restaurada
    - list: pila con notificaciones del intervalo
    """
    pila = []
    formato = "%H:%M"
    h_inicio = datetime.strptime(hora_inicio, formato)
    h_fin = datetime.strptime(hora_fin, formato)
    cola_aux = Queue()
    contador = 0

    while not cola.empty():
        noti = cola.get()
        hora_noti = datetime.strptime(noti["hora"], formato)
        if h_inicio <= hora_noti <= h_fin:
            pila.append(noti)
            contador += 1
        cola_aux.put(noti)

    print(f"\n Cantidad de notificaciones entre {hora_inicio} y {hora_fin}: {contador}")
    return cola_aux, pila


#            BLOQUE PRINCIPAL DE PRUEBA

if __name__ == "__main__":
    # === Cargar notificaciones de prueba ===
    cola_notificaciones = Queue()
    notificaciones = [
        crear_notificacion("10:30", "Facebook", "Nueva foto etiquetada."),
        crear_notificacion("11:45", "Twitter", "Aprende Python con nosotros."),
        crear_notificacion("12:00", "Instagram", "Nueva historia de tu amigo."),
        crear_notificacion("14:10", "Twitter", "Python es increíble."),
        crear_notificacion("16:00", "Facebook", "Alguien comentó tu estado."),
    ]

    for noti in notificaciones:
        cola_notificaciones.put(noti)

    # === Punto a: Eliminar notificaciones de Facebook ===
    cola_notificaciones = eliminar_facebook(cola_notificaciones)

    # === Punto b: Mostrar notificaciones de Twitter que contengan 'Python' ===
    cola_notificaciones = mostrar_twitter_python(cola_notificaciones)

    # === Punto c: Usar pila para contar notificaciones en intervalo ===
    cola_notificaciones, pila_notis = contar_notificaciones_intervalo(cola_notificaciones)

    # === Mostrar el contenido final de la cola ===
    print("\n Contenido final de la cola:")
    while not cola_notificaciones.empty():
        noti = cola_notificaciones.get()
        print(f"[{noti['hora']}] {noti['aplicacion']}: {noti['mensaje']}")
