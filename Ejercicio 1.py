# Creen un programa que solicite a los usuarios ingresar nombres y edades.
# Almacenen estos datos en un diccionario. Luego, imprima solo las edades.

usuarios = {}

while True:
    try:
        cantidad = int(input("¿Cuántos usuarios quieres agregar? "))
        if 0 < cantidad:
            break
    except ValueError:
        print("Valor incorrecto. Vuelve a intentarlo.")

print()

for i in range(cantidad):
    nombre = input(f"Dime el nombre del usuario número {i + 1}: ")
    while True:
        try:
            edad = int(input("- Edad del usuario: "))
            if 0 < edad <= 120:
                break
            else:
                print("Pon un valor que este en el rango de 1 a 120 años.")
        except ValueError:
            print("Valor incorrecto. Vuelve a intentarlo.")

    usuarios.update({nombre: edad})

print("Todas las edades: \n")
for edades in usuarios.values():
    print(f"- {edades} años.")
