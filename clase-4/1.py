import pandas as pd
from sklearn.model_selection import train_test_split

# Crear el DataFrame
alumnos = {
    "horas_estudio": [5, 10, 8, 9, 10, 11, 6, 7, 4, 12, 3, 8],
    "asistencia": [65, 90, 100, 82, 85, 60, 70, 75, 68, 98, 62, 95],
    "tareas_entregadas": [3, 10, 5, 8, 9, 10, 8, 7, 4, 10, 2, 9],
    "promedio": [9.9, 8.8, 5.0, 10.0, 6.6, 4.0, 8.0, 7.5, 5.5, 9.8, 4.2, 8.7],
    "aprobado": [1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1]
}

df = pd.DataFrame(alumnos)

# Ver los primeros 5 registros
print(df.head())

# Información general del dataset
# df.info()

###################################################################
# Variables independientes (características)
X = df.drop("aprobado", axis=1)

# Variable dependiente (etiqueta)
y = df["aprobado"]

# Dividir el conjunto de datos
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print(f"Entrenamiento: {len(X_train)} muestras")
print(f"pruebas: {len(X_test)} muestras")
