# verificar si la edad está en el rango del público objetivo
def clasificar_edad(edad):
    if edad >= 25 and edad <= 45:
        return True
    else:
        return False


# Función principal del programa
def recolector_datos():
    contador_clasificados = 0        # Cuenta cuántas personas están en el rango 25-45
    suma_edades = 0              # Suma total de las edades
    total_personas = 0           # Total de participantes
    mensaje_edades = ""         # Acumula las edades del público objetivo

    while True:
        edad = int(input("Ingrese la edad del participante (0 para terminar): "))

        # Condición para terminar el bucle
        if edad == 0:
            break

        # Se acumulan datos generales
        suma_edades += edad
        total_personas += 1

        # Se verifica si pertenece al público objetivo
        if clasificar_edad(edad):
            contador_clasificados += 1
            mensaje_edades += str(edad) + " "

    # Cálculo del promedio
    if total_personas > 0:
        promedio = suma_edades / total_personas
    else:
        promedio = 0

    # Resultados
    print("Resultados de la encuesta:")
    print("Total de participantes:", total_personas)
    print("Personas en el público objetivo:", contador_clasificados)
    print("Edades del público objetivo:", mensaje_edades)
    print("Edad promedio:", promedio)


# Llamado a la función principal
recolector_datos()