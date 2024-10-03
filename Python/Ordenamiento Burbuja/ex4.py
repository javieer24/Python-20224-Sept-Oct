def bubble_sort(lista):
    n = len(lista)  # Obtener la longitud de la lista
    for i in range(n):  # Repetir n veces
        for j in range(0, n - i - 1):  # Comparar elementos
            if lista[j] > lista[j + 1]:  # Comparar y intercambiar
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

# Solicitar al usuario que ingrese los números
numeros = list(map(int, input("Ingresa los números separados por espacios: ").split()))
bubble_sort(numeros)
print("Lista ordenada:", numeros)

"""
Explicación:

Usamos input() para solicitar al usuario que ingrese una lista de números separados por espacios.
La función map() convierte cada valor en entero, y split() separa los números por espacios.
Después de obtener la lista, se utiliza el algoritmo de burbuja para ordenarla de menor a mayor.
"""