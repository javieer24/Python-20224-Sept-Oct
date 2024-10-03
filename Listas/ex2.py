# Ejercicio 2: Insertar elemento en lista
numeros = [10, 20, 30, 40, 50]
print("Lista original:", numeros)

# Ingresar número asegurando que sea entero
while True:
    try:
        nuevo_numero = int(input("Ingrese el número a insertar: "))
        break
    except ValueError:
        print("Por favor, ingrese un número válido.")

# Asegurar que la posición esté dentro del rango de la lista
while True:
    try:
        posicion = int(input(f"Ingrese la posición (0-{len(numeros)}): "))
        if 0 <= posicion <= len(numeros):
            break
        else:
            print(f"Por favor, ingrese una posición entre 0 y {len(numeros)}.")
    except ValueError:
        print("Por favor, ingrese un número válido.")

# Insertar el número en la lista
numeros.insert(posicion, nuevo_numero)

# Imprimir la lista actualizada
print("Lista actualizada:", numeros)
