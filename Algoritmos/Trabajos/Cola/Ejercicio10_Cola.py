#10. Dada una cola con las notificaciones de las aplicaciones de redes sociales de un Smartphone, de las cual se cuenta con la hora de la notificación, la aplicación que la emitió y el mensaje, resolver las siguientes actividades:
    #a. escribir una función que elimine de la cola todas las notificaciones de Facebook;
    #b. escribir una función que muestre todas las notificaciones de Twitter, cuyo mensaje incluya la palabra ‘Python’, si perder datos en la cola;
    #c. utilizar una pila para almacenar temporáneamente las notificaciones producidas entre las 11:43 y las 15:57, y determinar cuántas son.

from queue_ import Queue # Importamos TU librería
from datetime import datetime

# --- FUNCIONES DE LÓGICA ---

def eliminar_facebook(cola):
    """
    Razonamiento: Para eliminar elementos de una cola sin perder el resto, 
    debemos rotar la cola completa.
    """
    tamanio_original = cola.size()
    for _ in range(tamanio_original):
        noti = cola.attention() # Sacamos el primero
        if noti["aplicacion"].lower() != "facebook":
            cola.arrive(noti) # Lo volvemos a meter solo si NO es Facebook
    return cola

def mostrar_twitter_python(cola):
    """
    Razonamiento: Para no perder datos, usamos el método move_to_end 
    o simplemente desencolamos y encolamos.
    """
    print("\n Notificaciones de Twitter que contienen 'Python':")
    for _ in range(cola.size()):
        noti = cola.attention()
        if noti["aplicacion"].lower() == "twitter" and "python" in noti["mensaje"].lower():
            print(f"[{noti['hora']}] {noti['aplicacion']}: {noti['mensaje']}")
        cola.arrive(noti) # Siempre vuelve a la cola
    return cola

def contar_en_intervalo(cola, h_ini="11:43", h_fin="15:57"):
    """
    Razonamiento: Usamos una lista de Python como Pila (Stack).
    """
    pila_temporal = [] # Actuará como Stack
    formato = "%H:%M"
    inicio = datetime.strptime(h_ini, formato)
    fin = datetime.strptime(h_fin, formato)
    
    for _ in range(cola.size()):
        noti = cola.attention()
        hora_noti = datetime.strptime(noti["hora"], formato)
        
        if inicio <= hora_noti <= fin:
            pila_temporal.append(noti) # Push a la pila[cite: 5, 8]
        
        cola.arrive(noti)
    
    print(f"\n Cantidad en intervalo: {len(pila_temporal)}")
    return pila_temporal

# --- BLOQUE PRINCIPAL ---

if __name__ == "__main__":
    cola = Queue()
    
    # Carga de datos
    datos = [
        {"hora": "10:30", "aplicacion": "Facebook", "mensaje": "Nueva foto."},
        {"hora": "11:45", "aplicacion": "Twitter", "mensaje": "Aprende Python."},
        {"hora": "12:00", "aplicacion": "Instagram", "mensaje": "Historia nueva."},
        {"hora": "14:10", "aplicacion": "Twitter", "mensaje": "Python es vida."},
        {"hora": "16:00", "aplicacion": "Facebook", "mensaje": "Comentario."},
    ]
    
    for d in datos:
        cola.arrive(d) # Usamos arrive de tu TDA

    cola = eliminar_facebook(cola)
    cola = mostrar_twitter_python(cola)
    pila_resultado = contar_en_intervalo(cola)