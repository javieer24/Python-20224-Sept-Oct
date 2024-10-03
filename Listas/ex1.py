# Ejercicio 1: Intercambiando Elementos en una Lista de 8 Números
my_list = [4, 15, 23, 8, 42, 16, 9, 3]

# Intercambio de elementos
# Intercambiamos el primer número (índice 0) con el último (índice 7)
my_list[0], my_list[7] = my_list[7], my_list[0]  # [3, 15, 23, 8, 42, 16, 9, 4]

# Intercambiamos el segundo número (índice 1) con el penúltimo (índice 6)
my_list[1], my_list[6] = my_list[6], my_list[1]  # [3, 9, 23, 8, 42, 16, 15, 4]

# Intercambiamos el tercer número (índice 2) con el sexto (índice 5)
my_list[2], my_list[5] = my_list[5], my_list[2]  # [3, 9, 16, 8, 42, 23, 15, 4]

# Impresión de la lista modificada
print("Lista después de intercambiar elementos:", my_list)
