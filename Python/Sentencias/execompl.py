def mostrar_menu():
    print("\nMenú de Operaciones:")
    print("1. Sumar dos números")
    print("2. Restar dos números")
    print("3. Multiplicar dos números")
    print("4. Dividir dos números")
    print("5. Salir")

# Variable booleana para controlar el bucle
continuar = True

while continuar:
    # Mostrar el menú
    mostrar_menu()
    
    # Pedir al usuario que elija una opción
    opcion = input("Elige una opción (1-5): ")
    
    # Verificar que la opción sea válida
    if opcion not in ['1', '2', '3', '4', '5']:
        print("Opción no válida. Por favor, elige una opción entre 1 y 5.")
        continue  # Volver al inicio del bucle y mostrar el menú de nuevo

    # Convertir la opción a entero
    opcion = int(opcion)

    # Si la opción es salir (5), romper el bucle
    if opcion == 5:
        print("¡Hasta luego!")
        break  # Salir del bucle y finalizar el programa

    # Pedir al usuario que ingrese dos números
    num1 = float(input("Ingresa el primer número: "))
    num2 = float(input("Ingresa el segundo número: "))

    # Ejecutar la operación según la opción elegida
    if opcion == 1:
        resultado = num1 + num2
        print(f"La suma de {num1} y {num2} es: {resultado}")
    elif opcion == 2:
        resultado = num1 - num2
        print(f"La resta de {num1} y {num2} es: {resultado}")
    elif opcion == 3:
        resultado = num1 * num2
        print(f"La multiplicación de {num1} y {num2} es: {resultado}")
    elif opcion == 4:
        if num2 == 0:
            print("Error: No se puede dividir entre cero.")
        else:
            resultado = num1 / num2
            print(f"La división de {num1} entre {num2} es: {resultado}")
