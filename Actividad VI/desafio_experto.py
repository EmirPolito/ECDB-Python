# EMIR POLITO GUEVARA
# Parte VIII. Desafío Experto

import pandas as pd

print("="*60)
print("DESAFÍO EXPERTO - TELECOMUNICACIONES")
print("="*60)

# DATASET (Con datos adicionales agregados a petición de las instrucciones)
clientes = [
    ("Juan", "Postpago", 25),
    ("Ana", "Prepago", 10),
    ("Luis", "Postpago", 40),
    ("Pedro", "Prepago", 5),
    ("Maria", "Postpago", 60),
    ("Juan", "Postpago", 25),  # Duplicado original
    ("Carlos", "Prepago", 15),
    ("Sofia", "Postpago", 55),
    ("Jorge", "Prepago", 8),
    ("Elena", "Postpago", 30),
    ("Carlos", "Prepago", 15)  # Nuevo duplicado agregado para pruebas
]

print("\n--- NIVEL INTERMEDIO ---")

# 1. Eliminar clientes duplicados.
# 2. Obtener clientes únicos.
# Al convertir la lista de tuplas a un 'set', los duplicados exactos desaparecen de forma rápida.
clientes_unicos_set = set(clientes)
clientes_unicos = list(clientes_unicos_set)

print(f"Total de registros originales: {len(clientes)}")
print(f"Total de registros únicos: {len(clientes_unicos)}")

# 3. Calcular el consumo promedio.
suma_consumo = 0
for cliente in clientes_unicos:
    suma_consumo += cliente[2] # El consumo está en el índice 2 de la tupla
    
promedio = suma_consumo / len(clientes_unicos)
print(f"Consumo promedio calculado: {promedio:.2f} GB")


print("\n--- NIVEL AVANZADO ---")

# 4. Crear un diccionario agrupando clientes por tipo de plan.
clientes_por_plan = {"Postpago": [], "Prepago": []}

for nombre, plan, consumo in clientes_unicos:
    clientes_por_plan[plan].append((nombre, consumo))

print("Agrupación por plan:")
for plan, lista in clientes_por_plan.items():
    print(f"- {plan}: {len(lista)} clientes")

# 5. Determinar qué plan consume más datos.
consumo_por_plan = {}
for plan, lista in clientes_por_plan.items():
    total_plan = 0
    for nombre, consumo in lista:
        total_plan += consumo
    consumo_por_plan[plan] = total_plan

# Pasamos a lista para encontrar el mayor ordenándolo, como hemos estado practicando
lista_consumos = []
for plan, total in consumo_por_plan.items():
    lista_consumos.append([total, plan])

lista_consumos.sort(reverse=True)
plan_mayor = lista_consumos[0]
print(f"El plan que consume más datos es: {plan_mayor[1]} con {plan_mayor[0]} GB en total.")


# 6. Identificar clientes con consumo superior al promedio.
clientes_alto_consumo = list(filter(lambda x: x[2] > promedio, clientes_unicos))

print("\nClientes con consumo superior al promedio (Filtrados con filter y lambda):")
for cliente in clientes_alto_consumo:
    print(f"- {cliente[0]} ({cliente[2]} GB)")


print("\n--- NIVEL EXPERTO ---")

# 7. Convertir los datos a DataFrame.
# Usamos los clientes únicos limpios para hacer nuestro DataFrame principal
df = pd.DataFrame(clientes_unicos, columns=["Nombre", "Plan", "Consumo_GB"])
print("7. DataFrame creado con éxito.")

# 8. Generar estadísticas descriptivas.
print("\n8. Estadísticas Descriptivas del consumo:")
print(df.describe())

# 9. Crear una columna de clasificación.
def clasificar_consumo(consumo):
    if consumo < 15:
        return "Bajo consumo"
    elif consumo <= 40:
        return "Consumo medio"
    else:
        return "Alto consumo"

df["Clasificacion"] = df["Consumo_GB"].apply(clasificar_consumo)
print("\n9. DataFrame con nueva columna de clasificación:")
print(df.to_string())

# 10. Generar un reporte final.
total_clientes_final = len(df)
consumo_promedio_final = df["Consumo_GB"].mean()
consumo_maximo = df["Consumo_GB"].max()
consumo_minimo = df["Consumo_GB"].min()

print("\n" + "="*60)
print("10. REPORTE FINAL DE CONSUMO DE DATOS")
print("="*60)
print(f"• Total de clientes activos: {total_clientes_final}")
print(f"• Consumo promedio global: {consumo_promedio_final:.2f} GB")
print(f"• Consumo máximo registrado: {consumo_maximo} GB")
print(f"• Consumo mínimo registrado: {consumo_minimo} GB")

print("\n• Distribución de clientes por tipo de plan:")
distribucion = df["Plan"].value_counts()
for plan, cantidad in distribucion.items():
    print(f"  - Plan {plan}: {cantidad} clientes")
print("="*60)
