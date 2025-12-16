def calcular_bonificacion(horas_extra):
    # Si trabaja más de 5 horas extra, la tarifa es 15 por hora
    if horas_extra > 5:
        return horas_extra * 15
    else:
        # Si trabaja 5 horas o menos, la tarifa es 10 por hora
        return horas_extra * 10


# Función principal controla el proceso
def control_bonificaciones():
    total_bonificaciones = 0      # Acumula el dinero total pagado
    empleados_con_bono = 0        # Cuenta empleados que recibieron bonificación

    # Bucle para ingresar datos de varios empleados
    while True:
        horas_extra = int(input("Ingrese las horas extra trabajadas (negativo para terminar): "))

        # Condición para terminar el proceso
        if horas_extra < 0:
            break

        # Calcula bonificación del empleado
        bonificacion = calcular_bonificacion(horas_extra)

        # Acumula resultados
        total_bonificaciones += bonificacion
        empleados_con_bono += 1

        # Mostrar bonificación individual
        print("Bonificación del empleado: $", bonificacion)

    # Mostrar resultados finales
    print("Resumen semanal")
    print("Total pagado en bonificaciones: $", total_bonificaciones)
    print("Cantidad de empleados con bonificación:", empleados_con_bono)


# Llamar a la función principal
control_bonificaciones()