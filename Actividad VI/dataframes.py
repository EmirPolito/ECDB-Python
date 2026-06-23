# EMIR POLITO GUEVARA
# Parte VI. DataFrames Intermedios

import pandas as pd

datos = {
    "Producto": ["Laptop", "Mouse", "Monitor", "Teclado", "Laptop", "Monitor"],
    "Categoria": ["Computo", "Accesorios", "Pantallas", "Accesorios", "Computo", "Pantallas"],
    "Precio": [15000, 300, 4000, 700, 15000, 4000],
    "Cantidad": [3, 20, 5, 10, 2, 4]
}

df = pd.DataFrame(datos)

print("="*60)
print("DATAFRAMES INTERMEDIOS")
print("="*60)

# 1. Crear una columna llamada Ingreso.
df["Ingreso"] = df["Precio"] * df["Cantidad"]
print("1. DataFrame con la columna 'Ingreso' creada:")
print(df)

# 2. Calcular ingresos totales.
ingresos_totales = df["Ingreso"].sum()
print(f"\n2. Ingresos totales de todas las ventas: ${ingresos_totales}")

# 3. Calcular ingresos por categoría.
# Agrupamos por la columna 'Categoria' y sumamos la columna 'Ingreso'
ingresos_por_categoria = df.groupby("Categoria")["Ingreso"].sum()
print("\n3. Ingresos por categoría:")
print(ingresos_por_categoria.to_string()) # Usamos to_string para que se imprima limpio

# 4. Identificar el producto más rentable.
# Agrupamos por producto y sumamos los ingresos para saber cuál generó más dinero en total, 
# ya que hay productos que aparecen varias veces (como Laptop)
ingresos_por_producto = df.groupby("Producto")["Ingreso"].sum()

# Encontramos el producto con el ingreso máximo usando idxmax() que vimos en la Actividad V
producto_mas_rentable = ingresos_por_producto.idxmax()
ingreso_maximo = ingresos_por_producto.max()
print(f"\n4. El producto más rentable es '{producto_mas_rentable}' con un ingreso total de ${ingreso_maximo}")

# 5. Mostrar estadísticas descriptivas.
print("\n5. Estadísticas descriptivas del DataFrame:")
print(df.describe())

# 6. Ordenar por ingreso descendente.
# Ordenamos el DataFrame original basándonos en la columna Ingreso
df_ordenado = df.sort_values(by="Ingreso", ascending=False)
print("\n6. DataFrame ordenado por ingreso de forma descendente:")
print(df_ordenado)

print("\n" + "="*60)


