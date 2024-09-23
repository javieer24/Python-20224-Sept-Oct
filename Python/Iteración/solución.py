
### Ejercicio 1: Solución

def check_number(num):
    if num > 0:
        print("El número es positivo")
    elif num == 0:
        print("El número es cero")
    else:
        print("El número es negativo")

check_number(10)


### Ejercicio 2: Solución

for i in range(5):
    print(f"Iteración {i}")
    if i % 2 == 0:
        print("El número es par")
    else:
        print("El número es impar")
    print("Fin de la iteración")


### Ejercicio 3: Solución

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

print(factorial(5))


### Ejercicio 4: Solución

def greet_user(username):
    print(f"Hola, {username}!")
    if username == "admin":
        print("Tienes privilegios de administrador")
    else:
        print("No tienes privilegios de administrador")

greet_user("admin")


### Ejercicio 5: Solución

def calculate_average(grades):
    total = 0
    for grade in grades:
        total += grade
    average = total / len(grades)
    return average

grades_list = [85, 90, 78, 92, 88]
print(f"El promedio es: {calculate_average(grades_list)}")

