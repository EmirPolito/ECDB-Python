# EMIR POLITO GUEVARA
# Parte VII. DataFrames Avanzados

import pandas as pd

ventas = {
    "Sucursal": ["Centro", "Centro", "Norte", "Norte", "Sur", "Sur"],
    "Producto": ["Laptop", "Mouse", "Laptop", "Monitor", "Mouse", "Monitor"],
    "Ingreso": [45000, 6000, 30000, 16000, 5400, 24000]
}

df = pd.DataFrame(ventas)

print("="*60)
print("DATAFRAMES AVANZADOS")
print("="*60)

# 1. Calcular ingresos por sucursal utilizando groupby()
ingresos_sucursal = df.groupby("Sucursal")["Ingreso"].sum()
print("1. Ingresos por sucursal:")
print(ingresos_sucursal.to_string())

# 2. Calcular ingresos por producto utilizando groupby()
ingresos_producto = df.groupby("Producto")["Ingreso"].sum()
print("\n2. Ingresos por producto:")
print(ingresos_producto.to_string())

# 3. Determinar la sucursal con mayores ingresos.
sucursal_mayor = ingresos_sucursal.idxmax()
ingreso_sucursal_max = ingresos_sucursal.max()
print(f"\n3. La sucursal con mayores ingresos es '{sucursal_mayor}' (${ingreso_sucursal_max})")

# 4. Determinar el producto más rentable.
producto_rentable = ingresos_producto.idxmax()
ingreso_producto_max = ingresos_producto.max()
print(f"4. El producto más rentable es '{producto_rentable}' (${ingreso_producto_max})")

# 5. Generar una tabla resumen.
# Agrupamos por ambas columnas para crear una tabla de resumen limpia usando groupby
# y reset_index() para que se vea como un DataFrame normal en lugar de tener multi-índices
tabla_resumen = df.groupby(["Sucursal", "Producto"])["Ingreso"].sum().reset_index()

print("\n5. Tabla resumen de ingresos:")
print(tabla_resumen.to_string(index=False))
print("\n" + "="*60)


