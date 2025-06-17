# Una empresa de transporte PasajeBus necesita un sistema básico que permita vender pasajes de bus numerados. Cada pasaje corresponde a un asiento único.
# El sistema debe mantener una lista de los asientos disponibles, y cuando un pasajero compra, ese asiento se elimina de la lista.


asientos_disponibles = [1, 2, 3, 4, 5]

while True:
    try:
        opcion = int(input("""
***** SISTEMA DE PASAJES PASAJEBUS *****

1.- Ver asientos disponibles
2.- Comprar pasaje
3.- Salir

Seleccione una opción: """))
    except ValueError:
        print("- Error: Ingresa un número, por favor.")
        continue

    if opcion == 1:
        print(f"- Asientos disponibles: {asientos_disponibles}")
    elif opcion == 2:
        try:
            opcion_compra = int(input("Ingrese número de asiento a comprar: "))
        except ValueError:
            print("- Error: Ingresa un número, por favor.")
            continue

        if opcion_compra in asientos_disponibles:
            print(f"- Asiento {opcion_compra} comprado con éxito.")
            asientos_disponibles.remove(opcion_compra)
        else:
            if opcion_compra in (1, 2, 3, 4, 5):
                print("- Lo sentimos, ese asiento ya no está disponible. Prueba con otro.")
            else:
                print("- Elige un asiento valido.")
    elif opcion == 3:
        print("- ¡Hasta luego! Vuelva pronto.")
        break
    else:
        print("- Opción incorrecta. Por favor, seleccione una opción entre 1-3.")

    continue
