#EMIR POLITO GUEVARA
"""
ACTIVIDAD V.- Colecciones y Estructuras de Datos en Python
Partes I-VII: Ejemplos y Análisis
"""

print("="*60)
print("PARTE I. LISTAS")
print("="*60)

# Código original
frutas = ["Manzana", "Pera", "Uva", "Mango"]
print("\nLista inicial:", frutas)
print(f"Elemento en posición 0: {frutas[0]}")

# Agregar frutas
frutas.append("Sandía")
print("\nDespués de append('Sandía'):", frutas)

# Experimenta: Agrega dos frutas más
frutas.append("Fresa")
frutas.append("Kiwi")
print("Después de agregar dos frutas más:", frutas)

# Respuestas
print("\n--- ANÁLISIS PARTE I ---")
print(f"¿Cuántos elementos contiene la lista inicialmente? 4")
print(f"¿Qué elemento se encuentra en la posición 0? {frutas[0]}")
print(f"¿Qué sucede después de ejecutar append()? Se agrega un nuevo elemento al final")

print("\n" + "="*60)
print("PARTE II. TUPLAS")
print("="*60)

# Código original
coordenadas = (10, 20)
print("\nTupla:", coordenadas)
print(f"Elemento 0: {coordenadas[0]}")
print(f"Elemento 1: {coordenadas[1]}")

# Experimenta: Intentar modificar una tupla
print("\n--- INTENTO DE MODIFICACIÓN ---")
try:
    coordenadas[0] = 100
except TypeError as e:
    print(f"ERROR: {e}")
    print("Las tuplas son INMUTABLES, no se pueden modificar sus elementos.")

print("\n--- ANÁLISIS PARTE II ---")
print("¿Por qué sucede esto? Las tuplas son estructuras inmutables.")
print("¿Situaciones útiles? Para proteger datos que no deben cambiar (constantes).")

print("\n" + "="*60)
print("PARTE III. SETS (CONJUNTOS)")
print("="*60)

# Código original
numeros = {1, 2, 3, 3, 3, 4, 5}
print("\nConjunto con duplicados: {1, 2, 3, 3, 3, 4, 5}")
print(f"Resultado real: {numeros}")

print("\n--- ANÁLISIS PARTE III ---")
print(f"¿Cuántos elementos escribiste? 7")
print(f"¿Cuántos aparecen realmente? {len(numeros)}")
print("¿Qué ocurrió? Los duplicados fueron eliminados automáticamente.")

# Experimenta: Agregar más números repetidos
numeros_exp = {1, 2, 2, 2, 3, 3, 4, 5, 5, 5, 6}
print(f"\nConjunto con más duplicados: {numeros_exp}")

print("\n" + "="*60)
print("PARTE IV. OPERACIONES CON SETS")
print("="*60)

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print(f"\nConjunto A: {a}")
print(f"Conjunto B: {b}")

union = a.union(b)
interseccion = a.intersection(b)
diferencia = a.difference(b)

print(f"\n--- UNIÓN ---")
print(f"a.union(b) = {union}")
print("Resultado: Todos los elementos de ambos conjuntos")

print(f"\n--- INTERSECCIÓN ---")
print(f"a.intersection(b) = {interseccion}")
print("¿Qué elementos tienen en común? 3 y 4")

print(f"\n--- DIFERENCIA ---")
print(f"a.difference(b) = {diferencia}")
print("¿Qué elementos pertenecen únicamente a A? 1 y 2")

print("\n" + "="*60)
print("PARTE V. DICCIONARIOS")
print("="*60)

alumno = {
    "nombre": "Juan",
    "edad": 20,
    "carrera": "TI"
}

print(f"\nDiccionario: {alumno}")
print(f"alumno['nombre']: {alumno['nombre']}")

print("\n--- ANÁLISIS ---")
print(f"Claves del diccionario: {list(alumno.keys())}")
print(f"Valores del diccionario: {list(alumno.values())}")

# Experimenta: Agregar nueva clave
alumno["correo"] = "correo@ejemplo.com"
print(f"\nDespués de agregar correo:\n{alumno}")

print("\n--- REFLEXIÓN ---")
print("¿Por qué un diccionario es más útil que una lista?")
print("- Las claves son descriptivas (nombre, edad, etc.)")
print("- Acceso directo sin necesidad de conocer la posición")
print("- Más legible y mantenible")

print("\n" + "="*60)
print("PARTE VI. DataFrames")
print("="*60)

import pandas as pd

datos = {
    "Nombre": ["Ana", "Luis", "Pedro"],
    "Edad": [22, 25, 23]
}
df = pd.DataFrame(datos)

print(f"\nDataFrame:\n{df}")

print("\n--- ANÁLISIS ---")
print(f"¿Cuántas filas tiene el DataFrame? {len(df)}")
print(f"¿Cuántas columnas tiene? {len(df.columns)}")
print(f"Nombres de columnas: {list(df.columns)}")

print("\n" + "="*60)
print("PARTE VII. EXPLORANDO DataFrames")
print("="*60)

print("\n--- df.head() ---")
print(df.head())
print("Propósito: Mostrar las primeras filas del DataFrame")

print("\n--- df.info() ---")
df.info()
print("Propósito: Mostrar información sobre el tipo de datos y memoria")

print("\n--- df.describe() ---")
print(df.describe())
print("Propósito: Mostrar estadísticas descriptivas (media, máx, mín, etc.)")

print("\n" + "="*60)
print("PARTE VIII. COMPARACIÓN DE ESTRUCTURAS")
print("="*60)

comparacion = """
Estructura      | ¿Modifica? | ¿Duplicados? | Caso de Uso
---------------------------------------------------------------
Lista           |    Sí      |    Sí        | Datos ordenados y variables
Tupla           |    No      |    Sí        | Constantes e inmutables
Set             |    Sí      |    No        | Eliminar duplicados
Diccionario     |    Sí      |    No        | Datos clave-valor
DataFrame       |    Sí      |    Sí        | Análisis tabular/datos
"""
print(comparacion)

print("\n" + "="*60)
print("CONCLUSIONES")
print("="*60)
print("\n¿Cuál estructura te pareció más sencilla? Lista")
print("¿Cuál te pareció más útil? DataFrame")
print("¿Cuál utilizarías para almacenar información de estudiantes? Diccionario o DataFrame")
print("¿Cuál utilizarías para analizar ventas de una empresa? DataFrame")



