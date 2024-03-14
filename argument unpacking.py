#Argument unpacking 
# Definir una función que recibe tres argumentos
def saludar(nombre, saludo, exclamacion):
    print(f"{saludo}, {nombre} {exclamacion}")

# Lista de argumentos
argumentos = ['Juan', 'Hola', '!']

# Llamada a la función utilizando argument unpacking
saludar(*argumentos)