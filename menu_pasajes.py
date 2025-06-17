asientos_disponibles = [1, 2, 3, 4, 5]


while True:
    opcion = int(input("""
***** SISTEMA DE PASAJES PASAJEBUS *****

1.- Ver asientos disponibles
2.- Comprar pasaje
3.- Salir

Seleccione una opción: """))

    if opcion == 1:
        print(f"Asientos disponibles: {asientos_disponibles}")
    elif opcion == 2:
        opcion_compra = int(input("Ingrese número de asiento a comprar: "))

        if opcion_compra in asientos_disponibles:
            print(f"Asiento {opcion_compra} comprado con éxito.")
            asientos_disponibles.remove(opcion_compra)
        else:
            if opcion_compra in (1, 2, 3, 4, 5):
                print("Lo sentimos, ese asiento ya no está disponible. Prueba con otro.")
            else:
                print("Elige un asiento valido.")
    elif opcion == 3:
        print("¡Hasta luego! Vuelva pronto.")
        break
    else:
        print("Opción incorrecta. Por favor, seleccione una opción entre 1-3.")

    continue