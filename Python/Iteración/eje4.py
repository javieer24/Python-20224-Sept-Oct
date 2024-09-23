def greet_user(username):
print(f"Hola, {username}!")
if username == "admin":
    print("Tienes privilegios de administrador")
else:
print("No tienes privilegios de administrador")

greet_user("admin")
