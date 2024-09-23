def saludar(nombre, fecha_nacimiento=2002, lugar_de_nacimiento="Guatemala"):
    """Saluda a una persona y le dice su edad.
    
    Parámetros
    ----------
    nombre: str
        Nombre de la persona a saludar
    fecha_nacimiento: int
        Año de nacimiento de la persona
    lugar_de_nacimiento: str
        Lugar de nacimiento de la persona
    """
    edad = 2023 - fecha_nacimiento
    print(f"Hola {nombre.title()}, ¿cómo estás? Tienes {edad} años y naciste en {lugar_de_nacimiento.title()}.")

nombre = input("Ingresa tu nombre: ")
saludar(nombre)
