n = int(input("Introduce un número entero positivo: "))
suma = 0

for i in range(1, n+1):
    suma += i

print(f"La suma de los primeros {n} números naturales es: {suma}")
