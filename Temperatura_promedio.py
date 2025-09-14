# Función para calcular la temperatura promedio de cada ciudad

def calcular_temperatura_promedio(datos_temperaturas):
    promedios = {}
    for ciudad, temperaturas in datos_temperaturas.items():
        promedio = sum(temperaturas) / len(temperaturas)
        promedios[ciudad] = promedio
    return promedios

# Datos de ejemplo: temperaturas de 3 ciudades durante 4 semanas
datos = {
    "Puyo": [20.5, 21.0, 19.8, 20.2],
    "Guayaquill": [28.0, 29.5, 30.1, 28.7],
    "Quito": [17.5, 18.0, 17.8, 18.2]
}

# Prueba de la función
resultados = calcular_temperatura_promedio(datos)

# Mostrar los resultados
for ciudad, promedio in resultados.items():
    print(f"La temperatura promedio en {ciudad} fue de {promedio:.2f}°C")
