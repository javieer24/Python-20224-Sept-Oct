def bubble_sort(lista):
    n = len(lista)  # Obtener la longitud de la lista
    i = 0  # Inicializar el índice del bucle externo
    while i < n:  # Bucle externo usando while
        j = 0  # Inicializar el índice del bucle interno
        while j < n - i - 1:  # Bucle interno usando while
            if lista[j] > lista[j + 1]:  # Comparar elementos
                # Intercambiar si es necesario
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
            j += 1  # Incrementar el índice del bucle interno
        i += 1  # Incrementar el índice del bucle externo

# Lista inicial
numeros = [29, 10, 14, 37, 13]
bubble_sort(numeros)
print("Lista ordenada:", numeros)

"""
Explicación:

En lugar de usar for, utilizamos while para los dos bucles.
El bucle while externo repite el proceso de ordenamiento hasta que todos los elementos estén en su lugar.
El bucle interno con while recorre la lista y realiza las comparaciones e intercambios.
"""