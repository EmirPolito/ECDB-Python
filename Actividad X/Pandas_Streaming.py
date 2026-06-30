#EMIR POLITO GUEVARA
import pandas as pd

# Dataset inicial de una plataforma de streaming
streaming = {
    "Usuario": ["Juan", "Ana", "Luis", "María", "Pedro", "Laura", "Carlos", "Sofía"],
    "Serie": ["Dark", "Wednesday", "Dark", "The Witcher", "Wednesday", "Dark", "Stranger Things", "The Witcher"],
    "Genero": ["Ciencia Ficción", "Terror", "Ciencia Ficción", "Fantasía", "Terror", "Ciencia Ficción", "Ciencia Ficción", "Fantasía"],
    "Pais": ["México", "México", "Colombia", "México", "Argentina", "Chile", "México", "Perú"],
    "Dispositivo": ["Smart TV", "Celular", "Laptop", "Tablet", "Smart TV", "Laptop", "Celular", "Smart TV"],
    "Minutos": [120, 45, 80, 60, 150, 95, 130, 75],
    "Calificacion": [5, 4, 5, 4, 5, 3, 5, 4]
}

df = pd.DataFrame(streaming)

print("DATASET ORIGINAL")
print(df)


#1 CÓDIGO
print("\nPRIMEROS REGISTROS")
print(df.head())

print("\nÚLTIMOS REGISTROS")
print(df.tail())

print("\nINFORMACIÓN GENERAL")
print(df.info())

print("\nESTADÍSTICAS DESCRIPTIVAS")
print(df.describe())

print("\nTAMAÑO DEL DATAFRAME")
print(df.shape)

print("\nCOLUMNAS")
print(df.columns)

#2 CÓDIGO
print("\nCOLUMNA SERIE")
print(df["Serie"])
print("\nCOLUMNAS USUARIO, SERIE Y MINUTOS")
print(df[["Usuario", "Serie", "Minutos"]])
print("\nCUARTO REGISTRO CON ILOC")
print(df.iloc[3])
print("\nPAÍS DEL PRIMER USUARIO CON LOC")
print(df.loc[0, "Pais"])
