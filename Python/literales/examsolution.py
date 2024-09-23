def mostrar_menu():
    # Mostrar opciones al usuario
    print("Menú Principal")
    print("1. Ingresar nombre, edad y altura")
    print("2. Mostrar información ingresada")
    print("3. Calcular el año de nacimiento")
    print("4. Salir")

# Variables globales para almacenar datos del usuario
nombre = ""
edad = 0
altura = 0.0

while True:
    mostrar_menu()
    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        # Opción 1: Ingresar datos
        nombre = input("Por favor, ingrese su nombre: ")
        edad = int(input("Por favor, ingrese su edad: "))
        altura = float(input("Por favor, ingrese su altura en metros: "))

    elif opcion == "2":
        # Opción 2: Mostrar datos
        if nombre == "" or edad == 0 or altura == 0.0:
            print("Primero debes ingresar los datos en la opción 1.")
        else:
            print(f"Nombre: {nombre}")
            print(f"Edad: {edad} años")
            print(f"Altura: {altura} metros")

    elif opcion == "3":
        # Opción 3: Calcular año de nacimiento
        if edad == 0:
            print("Primero debes ingresar la edad en la opción 1.")
        else:
            año_actual = 2024
            año_nacimiento = año_actual - edad
            print(f"Tu año de nacimiento es: {año_nacimiento}")

    elif opcion == "4":
        # Opción 4: Salir
        print("Saliendo del programa...")
        break

    else:
        # Manejo de opción no válida
        print("Opción no válida, por favor selecciona una opción válida.")
