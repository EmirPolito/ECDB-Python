# EMIR POLITO GUEVARA
# Parte I. Análisis de Ventas con Listas

ventas = [1500, 2500, 1800, 3200, 2100, 4000, 1700, 2800]

print("="*60)
print("ANÁLISIS DE VENTAS")
print("="*60)

# 1. Calcular el total vendido.
total_vendido = sum(ventas)
print(f"1. El total vendido es: ${total_vendido}")

# 2. Calcular el promedio de ventas.
promedio_ventas = total_vendido / len(ventas)
print(f"2. El promedio de ventas es: ${promedio_ventas}")

# 3. Obtener la venta más alta.
venta_mas_alta = max(ventas)
print(f"3. La venta más alta es: ${venta_mas_alta}")

# 4. Obtener la venta más baja.
venta_mas_baja = min(ventas)
print(f"4. La venta más baja es: ${venta_mas_baja}")

# 5. Contar cuántas ventas son mayores al promedio.
ventas_mayores_promedio = 0
for venta in ventas:
    if venta > promedio_ventas:
        ventas_mayores_promedio = ventas_mayores_promedio + 1

print(f"5. Cantidad de ventas mayores al promedio: {ventas_mayores_promedio}")

# 6. Crear una nueva lista únicamente con las ventas superiores a 2500.
ventas_superiores_2500 = []
for venta in ventas:
    if venta > 2500:
        ventas_superiores_2500.append(venta)

print(f"6. Lista de ventas superiores a 2500: {ventas_superiores_2500}")

print("\n" + "="*60)
















