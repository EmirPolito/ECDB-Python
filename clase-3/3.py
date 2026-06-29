import pandas as pd

# Agrupación de Datos con gruopby()
ventas = pd.DataFrame({
    "Sucursal": ["Centro", "Centro", "Norte", "Norte", "Sur"],
    "Producto": ["Laptop", "Mouse", "Laptop", "Teclado", "Mouse"],
    "Cantidad": [2, 5, 1, 3, 4],
    "Precio":   [15000, 300, 15000, 800, 300]
})


# Muestra tabla completa
# ventas["Total"] = (ventas["Cantidad"] * ventas["Precio"])
# print(ventas)


# ventas["Total"] = (ventas["Cantidad"] * ventas["Precio"])
# resumen = ventas.groupby("Sucursal")["Total"].sum()
# print(resumen)

# 
