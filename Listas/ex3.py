# Ejercicio 3: Contar y eliminar elemento de la lista
numeros = [5, 10, 15, 20, 25]
print("Lista original:", numeros)
print("Longitud de la lista:", len(numeros))

# Asegurar que se ingrese una posición válida para eliminar
while True:
    try:
        posicion = int(input(f"Ingrese la posición del número a eliminar (0-{len(numeros)-1}): "))
        if 0 <= posicion < len(numeros):
            break
        else:
            print(f"Por favor, ingrese una posición entre 0 y {len(numeros)-1}.")
    except ValueError:
        print("Por favor, ingrese un número válido.")

# Eliminar el elemento de la lista
del numeros[posicion]

# Imprimir la lista y su nueva longitud
print("Lista actualizada:", numeros)
print("Nueva longitud de la lista:", len(numeros))
