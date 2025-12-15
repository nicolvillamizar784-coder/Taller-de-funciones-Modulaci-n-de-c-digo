
# esta Función pide al usuario el código de acceso
def capturar_codigo():
    
    codigo = input("Ingrese el código de acceso (o escriba SALIR para terminar): ")
    # Se retorna el código ingresado
    return codigo


# esta función verifica si el código ingresado es correcto
def verificar_acceso(codigo_ingresado, codigo_correcto):
    # Se compara el código ingresado con el código correcto
    if codigo_ingresado == codigo_correcto:
        # Si son iguales, retorna verdadero (acceso permitido)
        return True
    else:
        # Si no son iguales, retorna falso (acceso denegado)
        return False


# Función principal que controla todo el programa
def control_acceso():
    # Código de acceso correcto
    codigo_correcto = "INV-001"

    # Contadores de accesos
    accesos_permitidos = 0
    accesos_denegados = 0

    # Bucle que se repite hasta que el usuario escriba SALIR
    while True:
        # Se captura el código ingresado por el usuario
        codigo = capturar_codigo()

        # Condición para salir del programa
        if codigo == "SALIR":
            break  # Termina el ciclo while

        # verifica si el código permite el acceso
        if verificar_acceso(codigo, codigo_correcto):
            # Mensaje de acceso correcto
            print("Acceso permitido")
            # Se incrementa el contador de accesos permitidos
            accesos_permitidos += 1
        else:
            
            print("Acceso denegado")
            # Se incrementa el contador de accesos denegados
            accesos_denegados += 1

    # Al finalizar el programa se muestran los resultados
    print("Resumen de accesos:")
    print("Accesos permitidos:", accesos_permitidos)
    print("Accesos denegados:", accesos_denegados)


# Llamado a la función principal para ejecutar el programa
control_acceso()