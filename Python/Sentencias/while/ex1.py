numero_secreto = 7
adivinanza = int(input("Adivina el número entre 1 y 10: "))

while adivinanza != numero_secreto:
    print("¡Incorrecto! Intenta de nuevo.")
    adivinanza = int(input("Adivina el número entre 1 y 10: "))

print("¡Correcto! Has adivinado el número.")
