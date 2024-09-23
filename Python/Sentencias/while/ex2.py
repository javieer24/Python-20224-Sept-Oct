while True:
    # Pedir al usuario que ingrese un número entero positivo
    numero = int(input("Introduce un número entero positivo: "))

    # Verificar si el número es negativo
    if numero < 0:
        print("El número es negativo. Por favor, introduce un número positivo.")
        continue  # Volver a pedir un número positivo

    # Inicializar el contador
    contador = 0
    print(f"Los números pares desde 0 hasta {numero} son:")

    # Bucle para mostrar los números pares
    while contador <= numero:
        if contador % 2 == 0:
            print(contador)
        contador += 1

    # Preguntar si el usuario desea continuar o salir
    respuesta = input("¿Deseas ingresar otro número? (si/no): ").lower()

    # Romper el bucle si el usuario elige "no"
    if respuesta != "si":
        print("¡Gracias por usar el sistema! Hasta luego.")
        break  # Salir del bucle principal y finalizar el programa
