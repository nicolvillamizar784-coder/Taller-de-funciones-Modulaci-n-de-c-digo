#pide la cantidad de unidades y registra si son ok o defectuosas 
def analizar_lote_con_registro():
    unidades = int(input("digitar la cantidad de unidades del lote: "))
#contador de unidades defectuosas 
    defectuosas = 0
#lista para guardar el registro de cada unidad
    registro = ()
    
    for i in range(1, unidades + 1):
        estado = input(f"unidad {i} (O=ok, D=defectuosa): ")
#condicional para evaluar el estado ingresado 
        if estado == "D":
#incrementa el contador de defectuosas             
            defectuosas += 1
#se guarda el fallo en el regitro 
            registro(f"fallo en unidad {i} ")
        elif estado == "O":
#se guarda la unidad como correcta
            registro(f"unidad {i} OK")
        else:
            print(" estado invalido. se marcara como defectuosa. ")    
            defectuosas += 1
            registro(f"fallo en unidad {i}")
            
#calcula el porcentaje de unidades defectuosas     
    porcentaje = (defectuosas / unidades) * 100
    return unidades, defectuosas, porcentaje, registro        

def mostrar_datos(unidades, defectuosas, porcentaje, registro):
    print(" detalles del lote ")
    for linea in registro:
        print(linea)
#detalles del registro        
    print("resumen")
    print("total de unidades: ", unidades)
    print("defectuosas: ", defectuosas)
    print(f"porcentaje defectuosas: {porcentaje:.2f}%")

#--codigo principal--
def menu_principal():
    while True:
        opcion = input(" ingrese 'L'para procesar lote o 'stop' para terminar: ")
        
        if opcion == "STOP":
            print("proceso finalizado")
            break
        
        elif opcion == "L":
            unidades, defectuosas, porcentaje, registro = analizar_lote_con_registro()
            mostrar_datos(unidades, defectuosas, porcentaje, registro)
#opcion invalida          
        else:
            print("opcion invalida. intentar de nuevo.")
            
menu_principal()