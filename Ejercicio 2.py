# El siguiente programa tiene como objetivo registrar los nombres y edades de los invitados a un evento. Al iniciar, el sistema debe preguntar cuántos invitados desea registrar.
# Por cada uno, se debe solicitar el nombre (sin repetir) y la edad. No se permite registrar invitados menores de 12 años. Los nombres deben almacenarse en mayúsculas.

# Una vez finalizado el proceso de ingreso, el sistema debe clasificar a los invitados según su edad y mostrar la distribución en mesas. La clasificación es la siguiente:
# Mesa 1: menores de edad (12 a 17 años)
# Mesa 2: adolescentes y jóvenes (18 a 29 años)
# Mesa 3: adultos (30 años o más)
# Cada mesa debe mostrar el nombre y la edad de los invitados asignados.


invitados_menores = {}
invitados_adolescentes = {}
invitados_adultos = {}

# Cantidad de personas a registrar.

while True:
    try:
        cantidad = int(input("¿Cuántas personas quieres registrar? "))

        if cantidad < 0:
            print("Debes ingresar al menos 1 usuario.")
            continue
        else:
            break
    except ValueError:
        print("Valor incorrecto. Debes ingresar un número.")
        continue

# Pregunta el nombre y edad de cada persona y finalmente lo agrega a los diccionarios según su edad.

print()

for i in range(1, cantidad + 1):
    while True:
        nombre = input(f"Nombre del invitado N°{i}: ").upper()

        if nombre in invitados_menores or nombre in invitados_adolescentes or nombre in invitados_adultos:
            print("Ese nombre ya está registrado en el sistema. Prueba con otro.")
            continue
        else:
            break

    while True:
        try:
            edad = int(input("- ¿Cuál es su edad? "))
            if edad < 0:
                print("Debes ingresar una edad mayor a 0.")
                continue
            else:
                break
        except ValueError:
            print("Valor incorrecto. Debes ingresar un número.")
            continue
    
    if edad < 12:
        print("Lo sentimos, pero la entrada no está permitida para esta persona, ya que sólo aceptamos a mayores de 12 años.\n")
    elif 12 <= edad <= 17:
        print(f"{nombre} ha sido agregado a la Mesa 1.\n")
        invitados_menores.update({nombre: edad})
    elif 18 <= edad <= 29:
        print(f"{nombre} ha sido agregado a la Mesa 2.\n")
        invitados_adolescentes.update({nombre: edad})
    elif edad >= 30:
        print(f"{nombre} ha sido agregado a la Mesa 3.\n")
        invitados_adultos.update({nombre: edad})


# Imprimir mesas con lista completa de invitados.

if len(invitados_menores) == 0:
    print("Mesa 1: No hay ningún invitado.")
else:
    lista_menores = [f"{nombre} ({edad} años)" for nombre, edad in invitados_menores.items()]
    print("Mesa 1: " + ", ".join(lista_menores))

if len(invitados_adolescentes) == 0:
    print("Mesa 2: No hay ningún invitado.")
else:
    lista_adolescentes = [f"{nombre} ({edad} años)" for nombre, edad in invitados_adolescentes.items()]
    print("Mesa 2: " + ", ".join(lista_adolescentes))

if len(invitados_adultos) == 0:
    print("Mesa 3: No hay ningún invitado.")
else:
    lista_adultos = [f"{nombre} ({edad} años)" for nombre, edad in invitados_adultos.items()]
    print("Mesa 3: " + ", ".join(lista_adultos))
