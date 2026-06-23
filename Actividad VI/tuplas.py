# EMIR POLITO GUEVARA
# Parte II. Procesamiento de Tuplas

ventas = [
    ("Laptop", 15000, 3),
    ("Mouse", 300, 15),
    ("Monitor", 4000, 5),
    ("Teclado", 700, 10),
    ("Laptop", 15000, 2)
]

print("="*60)
print("PROCESAMIENTO DE TUPLAS")
print("="*60)

# 1. Calcular el ingreso generado por cada venta.
print("1. Ingreso generado por cada venta:")
ingreso_total = 0
ingresos_por_venta = [] 

for producto, precio, cantidad in ventas:
    ingreso = precio * cantidad
    ingreso_total = ingreso_total + ingreso
    ingresos_por_venta.append((producto, ingreso))
    print(f"- {producto} (x{cantidad}): ${ingreso}")

# 2. Calcular el ingreso total.
print(f"\n2. El ingreso total de todas las ventas es: ${ingreso_total}")

# Para los puntos 3, 4 y 5 necesitamos acumular los ingresos por producto
# (nota que Laptop aparece dos veces en la lista de ventas)
ingresos_por_producto = {}

for producto, ingreso in ingresos_por_venta:
    if producto in ingresos_por_producto:
        ingresos_por_producto[producto] = ingresos_por_producto[producto] + ingreso
    else:
        ingresos_por_producto[producto] = ingreso

# Convertimos el diccionario a una lista para poder ordenarla
lista_ingresos = []
for producto, ingreso in ingresos_por_producto.items():
    lista_ingresos.append([ingreso, producto]) # Ponemos el ingreso primero para ordenar fácilmente

# Ordenamos de mayor a menor basándose en el primer elemento (el ingreso)
lista_ingresos.sort(reverse=True)

# 3. Identificar el producto con mayor ingreso acumulado.
producto_mayor_ingreso = lista_ingresos[0]
print(f"3. El producto con mayor ingreso acumulado es: {producto_mayor_ingreso[1]} (${producto_mayor_ingreso[0]})")

# 4. Identificar el producto con menor ingreso acumulado.
producto_menor_ingreso = lista_ingresos[-1]
print(f"4. El producto con menor ingreso acumulado es: {producto_menor_ingreso[1]} (${producto_menor_ingreso[0]})")

# 5. Generar un reporte ordenado de mayor a menor ingreso.
print("\n5. Reporte ordenado de mayor a menor ingreso acumulado:")
for ingreso, producto in lista_ingresos:
    print(f"- {producto}: ${ingreso}")

print("\n" + "="*60)



