# 1 Creación de un diccionario con información ficticia (usando mis datos base)
informacion_personal = \
{
    "Nombre": "Adriel Sánchez",
    "Edad": 23,
    "Ciudad": "Puyo",
    "Profesion": "Ingeniero en TIC"
}

# 2 Acceder y modificar el valor de la clave "ciudad" (cambiar a otra ciudad)
#    Primero accedemos:
ciudad_actual = informacion_personal["Ciudad"]  # "Puyo"
#    Ahora lo modificamos por otra ciudad (por ejemplo, "Ambato")
informacion_personal["Ciudad"] = "Ambato"

# 3 Agregar una nueva clave-valor relacionada con la profesión
#    Dado que "profesion" ya existe, añadimos un detalle complementario, como el "cargo".
informacion_personal["Cargo"] = "Analista de Soporte TIC"

# 4 Verificar si la clave "telefono" existe; si no existe, agregarla
if "Telefono" not in informacion_personal:
    # Número ficticio con formato ecuatoriano (móvil de 10 dígitos iniciando en 09)
    informacion_personal["Telefono"] = "0991234567"

# 5 Eliminar la clave "edad" porque no es necesaria
informacion_personal.pop("Edad", None)  # .pop con valor por defecto evita error si no existe

# 6 Imprimir el diccionario resultante
print(informacion_personal)
