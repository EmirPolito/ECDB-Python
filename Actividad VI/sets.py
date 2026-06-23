# EMIR POLITO GUEVARA
# Parte III. Limpieza de Datos con Sets

clientes = [
    "Juan",
    "Ana",
    "Luis",
    "Juan",
    "Pedro",
    "Ana",
    "Carlos",
    "Pedro",
    "Luis"
]

print("="*60)
print("LIMPIEZA DE DATOS CON SETS")
print("="*60)

# 1. Obtener la lista de clientes únicos.
# Convertimos la lista a un set para eliminar los duplicados, y luego de vuelta a lista (opcional)
clientes_unicos_set = set(clientes)
clientes_unicos_lista = list(clientes_unicos_set)
print(f"1. Lista original con repetidos:\n   {clientes}")
print(f"   Lista de clientes únicos:\n   {clientes_unicos_lista}")

# 2. Calcular cuántos clientes únicos existen.
cantidad_unicos = len(clientes_unicos_set)
print(f"\n2. Existen {cantidad_unicos} clientes únicos en total.")

# 3. Ordenar alfabéticamente los clientes únicos.
clientes_ordenados = list(clientes_unicos_set)
clientes_ordenados.sort()
print(f"\n3. Clientes únicos ordenados alfabéticamente:")
for cliente in clientes_ordenados:
    print(f"   - {cliente}")

# 4. Comparar los clientes de dos sucursales utilizando: Unión, Intersección, Diferencia
print("\n" + "-"*40)
print("4. Comparación de sucursales")
print("-"*40)

sucursal_a = {"Juan", "Ana", "Luis", "Pedro"}
sucursal_b = {"Ana", "Pedro", "Carlos", "Miguel"}

print(f"Sucursal A: {sucursal_a}")
print(f"Sucursal B: {sucursal_b}")

# Unión
union_sucursales = sucursal_a.union(sucursal_b)
print(f"\n• Unión (Todos los clientes de ambas sucursales):")
print(f"  {union_sucursales}")

# Intersección
interseccion_sucursales = sucursal_a.intersection(sucursal_b)
print(f"\n• Intersección (Clientes que compran en ambas sucursales):")
print(f"  {interseccion_sucursales}")

# Diferencia
diferencia_a_b = sucursal_a.difference(sucursal_b)
print(f"\n• Diferencia (Clientes exclusivos de la Sucursal A):")
print(f"  {diferencia_a_b}")

print("\n" + "="*60)



