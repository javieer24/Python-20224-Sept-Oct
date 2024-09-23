# Inicializar la suma en 0
suma_positivos = 0

while True:
    # Pedir al usuario que ingrese un número entero
    numero = int(input("Introduce un número entero (ingresa un número negativo para terminar): "))
    
    # Si el número es negativo, salir del bucle
    if numero < 0:
        break
    
    # Si el número es positivo, añadirlo a la suma
    suma_positivos += numero

# Imprimir la suma de los números positivos ingresados
print(f"La suma de los números positivos ingresados es: {suma_positivos}")
