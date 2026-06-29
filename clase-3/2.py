import pandas as pd

datos = {
    "nombre": ["Emir", "Luis", "Lizet", "Karla"],
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
# aprobados = df[df["calificacion"] >= 90]
# print(aprobados)

# Nueva columna usando apply
# df["Estatus"] = df["calificacion"].apply(
#     lambda x: "Aprobado" if x >= 80
#     else "Reprobado"
# )
# print(df)

# Ordenar por columna
# df_ord = df.sort_values(
#     by="calificacion",
#     ascending=False
# )
# print(df)

