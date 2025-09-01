# Matriz 3x3 original
matriz = [
    [9, 3, 5],
    [4, 8, 1],
    [7, 2, 6]
]

# Función Bubble Sort para ordenar una fila
def bubble_sort_fila(fila):
    n = len(fila)
    for i in range(n):
        for j in range(0, n - i - 1):
            if fila[j] > fila[j + 1]:
                fila[j], fila[j + 1] = fila[j + 1], fila[j]
    return fila

# Mostrar matriz original
print("🔢 Matriz original:")
for fila in matriz:
    print(fila)

# Fila a ordenar (por ejemplo, la fila 1)
indice_fila = int(input("Ingresa el índice de la fila que deseas ordenar (0, 1 o 2): "))

# Validar índice
if 0 <= indice_fila < len(matriz):
    matriz[indice_fila] = bubble_sort_fila(matriz[indice_fila])
    print("\n✅ Matriz con la fila ordenada:")
    for fila in matriz:
        print(fila)
else:
    print("❌ Índice de fila inválido. Debe ser 0, 1 o 2.")