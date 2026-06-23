# EMIR POLITO GUEVARA
# Parte IV. Diccionarios Intermedios

inventario = {
    "Laptop": 10,
    "Mouse": 50,
    "Monitor": 15,
    "Teclado": 25,
    "Impresora": 5
}

print("="*60)
print("DICCIONARIOS INTERMEDIOS")
print("="*60)

# 1. Calcular el total de productos en inventario.
total_productos = 0
for producto, cantidad in inventario.items():
    total_productos = total_productos + cantidad

print(f"1. El total de productos en inventario es: {total_productos}")

# Para los puntos 2, 3 y 4 pasamos los datos a una lista y los ordenamos
lista_inventario = []
for producto, cantidad in inventario.items():
    lista_inventario.append([cantidad, producto])

# Ordenamos la lista de mayor a menor según la cantidad (que es el primer elemento)
lista_inventario.sort(reverse=True)

# 2. Identificar el producto con mayor existencia.
producto_mayor = lista_inventario[0]
print(f"\n2. Producto con mayor existencia: {producto_mayor[1]} ({producto_mayor[0]} unidades)")

# 3. Identificar el producto con menor existencia.
producto_menor = lista_inventario[-1]
print(f"3. Producto con menor existencia: {producto_menor[1]} ({producto_menor[0]} unidades)")

# 4. Generar un listado ordenado de mayor a menor stock.
print("\n4. Listado ordenado de mayor a menor stock:")
for cantidad, producto in lista_inventario:
    print(f"   - {producto}: {cantidad} unidades")

# 5. Crear un diccionario nuevo que contenga únicamente productos con stock menor a 20.
inventario_bajo_stock = {}
for producto, cantidad in inventario.items():
    if cantidad < 20:
        inventario_bajo_stock[producto] = cantidad

print(f"\n5. Nuevo diccionario con productos de stock menor a 20:")
print(f"   {inventario_bajo_stock}")

print("\n" + "="*60)
