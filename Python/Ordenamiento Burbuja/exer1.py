def bubble_sort(lista):
    n = len(lista)  # Obtener la longitud de la lista
    for i in range(n):  # Repetir n veces, donde n es el número de elementos
        for j in range(0, n - i - 1):  # Cada vez revisar hasta un elemento menos
            if lista[j] > lista[j + 1]:  # Comparar elementos adyacentes
                # Intercambiar si el actual es mayor que el siguiente
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

# Lista inicial
numeros = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(numeros)
print("Lista ordenada:", numeros)

"""
Explicación:

Primero se obtiene la longitud de la lista.
Se utilizan dos bucles: el externo para repetir las pasadas necesarias, y el interno para comparar cada par de elementos adyacentes.
Si el elemento actual es mayor que el siguiente, se intercambian usando la asignación múltiple.
Al finalizar, la lista estará ordenada.
"""