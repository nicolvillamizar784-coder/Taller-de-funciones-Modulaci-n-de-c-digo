# Función que devuelve el saldo inicial
def saldo_inicial():
    return 1000


# Función para procesar un depósito
def depositar(saldo, monto):
    saldo = saldo + monto
    return saldo


# Función para procesar un retiro
def retirar(saldo, monto):
    # Condicional (solo se retira si el saldo no queda negativo)
    if saldo - monto >= 0:
        saldo = saldo - monto
        return saldo, True   # Retiro válido
    else:
        print("Saldo insuficiente. Retiro no realizado.")
        return saldo, False  # Retiro no válido


# Función principal que controla el proceso
def procesar_transacciones():
    saldo = saldo_inicial()
    contador = 0  # Cuenta las transacciones válidas

    while True:  # Bucle para repetir las transacciones
        tipo = input("Ingrese tipo de transacción (D, R o FIN): ")

        if tipo == "FIN":
            break  # Sale del bucle

        monto = float(input("Ingrese el monto: "))

        if tipo == "D":
            saldo = depositar(saldo, monto)
            contador += 1

        elif tipo == "R":
            saldo, valido = retirar(saldo, monto)
            if valido:
                contador += 1

        else:
            print("Tipo de transacción no válido.")

    # Resultados finales
    print("Saldo final:", saldo)
    print("Total de transacciones válidas:", contador)


# Llamado a la función principal
procesar_transacciones()