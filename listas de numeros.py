
# Lista de números
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Comprensión de sets para crear un set de números pares
numeros_pares = {num for num in numeros if num % 2 == 0}

# Imprimir el set resultante
print(numeros_pares)