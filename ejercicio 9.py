# resta las ventas al stock actual
def actualizar_stock(stock_actual, ventas):
    return stock_actual - ventas


# verifica si es necesario reponer el producto
def verificar_reposicion(stock_actual, punto_reposicion):
    if stock_actual <= punto_reposicion:
        return True
    else:
        return False


# Función principal que controla el inventario
def control_inventario():
    stock = 50                 # Stock inicial
    punto_reposicion = 10      # Punto de reposición

    # Bucle para simular las ventas diarias
    while True:
        print("Stock actual:", stock)

        # Solicitar las ventas del día
        ventas = int(input("digitar la cantidad vendida hoy: "))

        # Actualizar el stock
        stock = actualizar_stock(stock, ventas)

        # Verificar si se debe hacer reposición
        if verificar_reposicion(stock, punto_reposicion):
            print("Aviso de Reposición Urgente")
            print("Stock final:", stock)
            break   # Detiene el proceso de ventas

        # Condicional adicional por seguridad
        if stock <= 0:
            print("El stock se ha agotado.")
            break


# Llamar a la función principal
control_inventario()