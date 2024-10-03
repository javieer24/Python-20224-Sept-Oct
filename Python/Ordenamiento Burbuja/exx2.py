def bubble_sort(lista):
    n = len(lista)  # Obtener la longitud de la lista
    for i in range(n):  # Repetir n veces
        for j in range(0, n - i - 1):  # Comparar elementos
            if lista[j] > lista[j + 1]:  # Si el elemento actual es mayor
                # Intercambiar si es necesario
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

# Lista inicial con números negativos
numeros = [-64, -34, -25, -12, -22, -11, -90]
bubble_sort(numeros)
print("Lista ordenada:", numeros)

"""
Explicación:

Aunque los números son negativos, el algoritmo de burbuja sigue funcionando igual.
Se compara cada par de números adyacentes y se intercambian si el número actual es mayor que el siguiente.
La lista se ordena de menor a mayor.
"""