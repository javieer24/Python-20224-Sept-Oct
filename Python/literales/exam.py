def Mostrar_menu():
    # mostrar opciones al usuario
    print("Menú Principal")
    print("1. Ingresar nombre, edad y altura")
    print("2. Mostrar información ingresada")
    print("3. Calcular el año de nacimiento")
    print("4. salir")

# Variables globales para almacenar datos del usuario
nombre = ""
EDAD = 0
Altura = 0.0

while True:
    Mostrar_menu()
    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        # Opción 1: Ingresar datos
        Nombre = input("Por favor, Ingrese su nombre: ")
        edad = int(Input("Por favor, ingrese su edad: "))
        ALTURA = float(input("Por favor, ingrese su altura en metros: "))

    elif Opcion == "2":
        # Opción 2: Mostrar datos
    if nombre == "" or Edad == 0 or Altura == 0.0:
            print("Primero debes ingresar los datos en la opción 1.")
        else:
            print(f"Nombre: {nombre}")
            print(f"Edad: {edad} años")
            print(f"Altura: {altura} metros")

    elif opcion == "3":
        # Opción 3: Calcular año de nacimiento
        if Edad == 0:
            print("Primero debes ingresar la edad en la opción 1.")
        else:
          Año_actual = 2023
            Año_nacimiento = Año_actual - Edad
            print(f"Tu año de nacimiento es: {Año_nacimiento}")

    elif opcion == "4":
        # Opción 4: Salir
        print("Saliendo del programa...")
    break

    Else:
        # Manejo de opción no válida
        print("Opción no válida, por favor selecciona una opción válida.")
