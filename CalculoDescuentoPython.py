# Definición de la función
def calcular_descuento(monto_total, porcentaje_descuento=10):
    descuento = monto_total * (porcentaje_descuento / 100)
    return descuento

# Llamadas a la función
# Primera llamada: solo se proporciona el monto total
monto1 = 100.0
descuento1 = calcular_descuento(monto1)
monto_final1 = monto1 - descuento1

# Segunda llamada: se proporciona el monto total y el porcentaje de descuento
monto2 = 200.0
porcentaje2 = 15
descuento2 = calcular_descuento(monto2, porcentaje2)
monto_final2 = monto2 - descuento2

# Salida de resultados
print("Primera compra:")
print(f"Monto total: ${monto1}")
print(f"Descuento aplicado: ${descuento1}")
print(f"Monto final a pagar: ${monto_final1}")

print("\nSegunda compra:")
print(f"Monto total: ${monto2}")
print(f"Descuento aplicado: ${descuento2}")
print(f"Monto final a pagar: ${monto_final2}")
