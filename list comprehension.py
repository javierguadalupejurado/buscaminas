#Usando enumerate con list comprehension:

# Lista de frutas
frutas = ['manzana', 'banana', 'naranja']

# Comprensión de lista con enumerate para obtener índices y valores
frutas_con_indices = [(indice, fruta) for indice, fruta in enumerate(frutas)]

# Imprimir la lista resultante
print(frutas_con_indices)