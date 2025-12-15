#  verifica si el uso es crítico
def uso_critico(uso_cpu):
    # Retorna True si el uso es mayor al 90%
    return uso_cpu > 90


# Función principal del monitoreo
def monitorear_cpu():
    total_mediciones = 0      # Contador de mediciones
    alertas_criticas = 0      # Contador de alertas

    while True:
        # Se pide el uso de CPU
        uso_cpu = float(input("Ingrese el uso de CPU (%): "))

        # Condición para salir del bucle
        if uso_cpu < 0:
            break

        total_mediciones += 1

        # Se verifica si el uso es crítico
        if uso_critico(uso_cpu):
            print("Alerta: Uso Crítico")
            alertas_criticas += 1

    # Resultados finales
    print(" Resumen del Monitoreo")
    print("Total de mediciones:", total_mediciones)
    print("Total de alertas críticas:", alertas_criticas)


# Llamada a la función principal
monitorear_cpu()