# Definimos la matriz 3x3
matriz = [
    [5, 8, 3],
    [2, 9, 4],
    [7, 1, 6]
]

# Función para buscar un valor en la matriz
def buscar_valor(matriz, valor):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == valor:
                return (i, j)  # Retorna la posición si se encuentra
    return None  # Retorna None si no se encuentra

# Valor a buscar
valor_buscado = int(input("Ingresa el valor que deseas buscar en la matriz: "))

# Ejecutamos la búsqueda
resultado = buscar_valor(matriz, valor_buscado)

# Mostramos el resultado
if resultado:
    print(f"✅ Valor {valor_buscado} encontrado en la posición: fila {resultado[0]}, columna {resultado[1]}")
else:
    print(f"❌ Valor {valor_buscado} no se encontró en la matriz.")