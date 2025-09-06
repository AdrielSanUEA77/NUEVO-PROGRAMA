import random

# Definir dimensiones
ciudades = ["Quito", "Puyo", "Guayaquil"]
dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
num_semanas = 4

#Crear matriz 3D: [ciudades][días][semanas]
#Inicializamos con ceros
temperaturas = [[[0 for _ in range(num_semanas)] for _ in range(len(dias_semana))] for _ in range(len(ciudades))]

#Llenar con temperaturas aleatorias (simuladas entre 15 y 35 grados)
for c in range(len(ciudades)):
    for d in range(len(dias_semana)):
        for s in range(num_semanas):
            temperaturas[c][d][s] = round(random.uniform(15, 35), 1)

#Mostrar estructura
print("Datos de temperaturas generados:")
for c, ciudad in enumerate(ciudades):
    print(f"\n{ciudad}:")
    for s in range(num_semanas):
        print(f"  Semana {s+1}: ", end="")
        for d in range(len(dias_semana)):
            print(f"{temperaturas[c][d][s]}°C ", end="")
        print()  # nueva línea

print("\n" + "="*60)

#Calcular el promedio semanal por ciudad usando bucles anidados
print(" Promedio semanal de temperaturas por ciudad:")

for c, ciudad in enumerate(ciudades):
    print(f"\n{ciudad}:")
    for s in range(num_semanas):
        suma = 0
        for d in range(len(dias_semana)):
            suma += temperaturas[c][d][s]
        promedio = suma / len(dias_semana)
        print(f"  Semana {s+1}: {promedio:.2f}°C")