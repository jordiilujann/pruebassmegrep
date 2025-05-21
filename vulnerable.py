import os

# Uso inseguro de eval (ejecuta código arbitrario)
def ejecutar(cadena):
    eval(cadena)

# Contraseña hardcodeada (clave visible)
def login():
    password = "123456"
    if password == "123456":
        print("Acceso concedido")

# Lectura insegura de input (sin validación)
user_input = input("Introduce algo:")
os.system("echo " + user_input)
