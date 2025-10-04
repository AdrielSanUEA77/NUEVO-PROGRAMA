# Escritura de Archivo de Texto ADRIEL

# Creamos el archivo 'my_notes.txt' en modo escritura ('w')
with open('my_notes.txt', 'w') as file:
    # Escribimos tres líneas de notas personales en el archivo
    file.write("Nota 1: Recordar enviar el práctico experimental antes del domingo.\n")
    file.write("Nota 2: Comprar pupillos para jugar fútbol el sábado.\n")
    file.write("Nota 3: Llamar al odontólogo para agendar cita de revisión.\n")
    # El archivo se cerrará automáticamente al salir del bloque 'with'

# Lectura de Archivo de Texto ADRIEL

# Abrimos el archivo 'my_notes.txt' en modo lectura ('r')
with open('my_notes.txt', 'r') as file:
    # Leemos y mostramos cada línea del archivo utilizando readline()
    while True:
        linea = file.readline()  # Lee una línea del archivo
        if not linea:  # Si no hay más líneas, salimos del bucle
            break
        print(linea.strip())  # Mostramos la línea sin el salto de línea final

# El archivo se cierra automáticamente al salir del bloque 'with'