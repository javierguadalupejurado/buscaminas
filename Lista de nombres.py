# Lista de nombres
nombres = ['Juan', 'María', 'Carlos', 'Ana', 'Pedro']

# Creación de un diccionario utilizando comprensión de diccionarios
diccionario_nombres = {nombre: len(nombre) for nombre in nombres}

# Imprimir el diccionario resultante
print(diccionario_nombres)