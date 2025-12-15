#  calcula el subtotal de un producto
def calcular_subtotal(precio, cantidad):
    return precio * cantidad


# calcula el descuento según el subtotal
def calcular_descuento(subtotal):
    if subtotal > 1000:
        return subtotal * 0.10
    elif subtotal > 500:
        return subtotal * 0.05
    else:
        return 0


# devuelve el mensaje del descuento
def mensaje_descuento(descuento):
    if descuento > 0:
        return "Se aplicó un descuento."
    else:
        return "No se aplicó ningún descuento."


# Programa principal
subtotal_total = 0
continuar = "s"

# Bucle para ingresar varios productos
while continuar == "s":
    precio = float(input("Ingrese el precio del producto: "))
    cantidad = int(input("Ingrese la cantidad: "))

    subtotal_producto = calcular_subtotal(precio, cantidad)
    subtotal_total += subtotal_producto

    continuar = input("¿Desea agregar otro producto? (s/n): ")

# Se calcula el descuento
descuento = calcular_descuento(subtotal_total)

# Se calcula el total a pagar
total_pagar = subtotal_total - descuento

# Se obtiene el mensaje
mensaje = mensaje_descuento(descuento)

# Resultados finales
print("resumne de compra")
print("Subtotal:", subtotal_total)
print("Descuento:", descuento)
print("Total a pagar:", total_pagar)
print(mensaje)