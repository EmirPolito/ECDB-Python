import pandas as pd

datos = {
    "nombre": ["Emir", "Luis", "Maria", "Karla"],
    "edad": [19, 20, 25, 18],
    "calificacion": [100, 95, 90, 60]
}

#Tabla completa
df = pd.DataFrame(datos)

#Columna nombre
# print(df["nombre"])

#Filas
# print(df.loc[0])
# print(df.loc[0, "nombre"])
# print(df.loc[1:3])

#Filtrado de datos - simple
aprobados = df[df["calificacion"] >= 90]
print(aprobados)

#Filtrado de datos - multiples condiciones
