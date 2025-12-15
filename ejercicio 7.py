# verifica si el vendedor cumplió la meta
def cumplir_meta(ventas, meta):
    # Retorna True si las ventas son iguales o mayores a la meta
    return ventas >= meta


# Función principal del programa
def verificar_metas():
    META = 5000  # Meta mensual de ventas
    total_vendedores = 0
    vendedores_con_meta = 0
    felicitaciones = ()

    # Bucle para ingresar las ventas de cada vendedor
    while True:
        ventas = float(input("Ingrese el monto de ventas del vendedor: "))

        # Condición para finalizar el programa
        if ventas <= 0:
            break

        total_vendedores += 1

        # Verificamos si cumple la meta usando la función
        if cumplir_meta(ventas, META):
            vendedores_con_meta += 1
            felicitaciones.append(
                f"¡Felicitaciones! Vendedor {total_vendedores} cumplió la meta."
            )

    # Resultados finales
    print("RESULTADOS")
    print("Total de vendedores procesados:", total_vendedores)
    print("Vendedores que cumplieron la meta:", vendedores_con_meta)

    print("Mensajes de felicitación:")
    for mensaje in felicitaciones:
        print(mensaje)


# Llamamos a la función principal
verificar_metas()