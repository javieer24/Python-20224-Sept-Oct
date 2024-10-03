def bubble_sort_descendente(lista):
    n = len(lista)  # Obtener la longitud de la lista
    for i in range(n):  # Repetir n veces
        for j in range(0, n - i - 1):  # Comparar elementos
            if lista[j] < lista[j + 1]:  # Modificar para ordenar en orden descendente
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

# Lista inicial
numeros = [15, 20, 30, 10, 5]
bubble_sort_descendente(numeros)
print("Lista ordenada en orden descendente:", numeros)

"""
Explicación:

El único cambio con respecto al burbuja normal es el operador de comparación: en lugar de >, usamos < para que los números mayores se muevan al principio de la lista.
Esto ordena los números de mayor a menor.

"""