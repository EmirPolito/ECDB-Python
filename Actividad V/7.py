#EMIR POLITO GUEVARA
import pandas as pd

datos = {
    "Nombre": ["Emir", "Luis", "Pedro"],
    "Edad": [19, 25, 23]
}
df = pd.DataFrame(datos)

print(df.head())
print(df.info())
print(df.describe())