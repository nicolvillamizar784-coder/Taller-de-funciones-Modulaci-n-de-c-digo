# Sistema de Calificación de Pedidos de Clientes

#le pide al usuario las calificaciones de los pedidos 
#las guarda en una lista y la devuele cuando el usuario escriba 0

def capturar_datos():
    print("Captura de calificaciones de pedidos ")
    pedidos = []

    while True:
        calificacion = int(input("Ingresa la calificación del pedido (1 a 5) o 0 para terminar:"))

        if calificacion == 0:
            break
        
    
        if calificacion < 1 or calificacion > 5:
            print("Calificación inválida. Debe ser entre 1 y 5.")
        else:
            pedidos.append(calificacion)

    return pedidos


# recibe la lista de calificaciones y se hace los calculos,
#como el total de pedidos, la suma, el promedio y los pedidos excelentes 

def procesar_datos(pedidos):
    total_pedidos =len(pedidos)
    suma_puntajes = 0
    pedidos_excelentes = 0

    for calificacion in pedidos:
        suma_puntajes = calificacion

        if calificacion == 5:
            pedidos_excelentes = 1

    if total_pedidos > 0:
        promedio = suma_puntajes / total_pedidos
    else:
        promedio = 0

    # se guarda los datos procesados en un diccionario sencillo
    datos = {
        "total_pedidos": total_pedidos,
        "suma_puntajes": suma_puntajes,
        "promedio": promedio,
        "pedidos_excelentes": pedidos_excelentes}
    

    return datos

#muestra los resultados ya calculados 
#como el total de pedidos, la suma, el promedio y los pedidos excelentes 
def mostrar_resultados(resultados):
    print("Resultados del sistema")
    print("Total de pedidos procesados:")
    resultados["total_pedidos"]
    print("Puntuación total acumulada:")
    resultados["suma_puntajes"]
    print("Promedio general de satisfacción:")
    resultados["promedio"]
    print("Cantidad de pedidos excelentes (5 estrellas):")
    resultados["pedidos_excelentes"]

# Programa Principal
pedidos_capturados = capturar_datos()
datos_procesados = procesar_datos(pedidos_capturados)
mostrar_resultados(datos_procesados)

