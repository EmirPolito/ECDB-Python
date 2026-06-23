# EMIR POLITO GUEVARA
# Parte V. Diccionarios Avanzados

ventas = {
    "Centro": {
        "Laptop": 5,
        "Mouse": 20,
        "Monitor": 8
    },
    "Norte": {
        "Laptop": 3,
        "Mouse": 15,
        "Monitor": 4
    },
    "Sur": {
        "Laptop": 7,
        "Mouse": 18,
        "Monitor": 6
    }
}

print("="*60)
print("DICCIONARIOS AVANZADOS")
print("="*60)

# 1. Calcular ventas totales por sucursal.
# 2. Calcular ventas totales por producto.
ventas_por_sucursal = {}
ventas_por_producto = {}

for sucursal, productos in ventas.items():
    total_sucursal = 0
    for producto, cantidad in productos.items():
        # Sumamos la cantidad al total de la sucursal
        total_sucursal = total_sucursal + cantidad
        
        # Sumamos la cantidad al total del producto
        if producto in ventas_por_producto:
            ventas_por_producto[producto] = ventas_por_producto[producto] + cantidad
        else:
            ventas_por_producto[producto] = cantidad
            
    # Guardamos el total de la sucursal en el diccionario
    ventas_por_sucursal[sucursal] = total_sucursal

print("1. Ventas totales por sucursal:")
for sucursal, total in ventas_por_sucursal.items():
    print(f"   - {sucursal}: {total} unidades")

print("\n2. Ventas totales por producto:")
for producto, total in ventas_por_producto.items():
    print(f"   - {producto}: {total} unidades")

# 3. Determinar la sucursal con mayores ventas.
lista_sucursales = []
for sucursal, total in ventas_por_sucursal.items():
    lista_sucursales.append([total, sucursal])

lista_sucursales.sort(reverse=True)
sucursal_mayor = lista_sucursales[0]

print(f"\n3. Sucursal con mayores ventas: {sucursal_mayor[1]} ({sucursal_mayor[0]} unidades)")

# 4. Determinar el producto más vendido.
lista_productos = []
for producto, total in ventas_por_producto.items():
    lista_productos.append([total, producto])

lista_productos.sort(reverse=True)
producto_mayor = lista_productos[0]

print(f"4. Producto más vendido: {producto_mayor[1]} ({producto_mayor[0]} unidades)")

# 5. Mostrar un reporte consolidado.
print("\n5. Reporte consolidado:")
print("-" * 40)
for sucursal, productos in ventas.items():
    print(f"SUCURSAL {sucursal.upper()}:")
    for producto, cantidad in productos.items():
        print(f"  • {producto}: {cantidad}")
    print(f"  > Total de la sucursal: {ventas_por_sucursal[sucursal]}")
    print("-" * 40)

print("\n" + "="*60)
