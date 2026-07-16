import numpy as np
import pandas as pd

# ==========================================================
# Parte I. Importación de Bibliotecas
# ==========================================================

print("======================================")
print("PARTE II. CREACIÓN DEL DATAFRAME")
print("======================================")

# ==========================================================
# Parte II. Creación del DataFrame
# ==========================================================

df = pd.DataFrame()
print(df)

# ==========================================================
# Parte III. Agregar la primera columna
# ==========================================================

print("\n======================================")
print("PARTE III. AGREGAR LA PRIMERA COLUMNA")
print("======================================")

n = 100

df["IdUsuario"] = np.arange(1, n + 1)

print(df.head())

# ==========================================================
# Parte IV. Agregar la edad
# ==========================================================

print("\n======================================")
print("PARTE IV. AGREGAR LA EDAD")
print("======================================")

print("\nEdades para plataforma normal (18 a 65 años):")

df["Edad"] = np.random.randint(18, 66, n)

print(df.head())

print("\nEdades para plataforma infantil (5 a 11 años):")

df["Edad"] = np.random.randint(5, 12, n)

print(df.head())

# ==========================================================
# Parte V. Agregar el país
# ==========================================================

print("\n======================================")
print("PARTE V. AGREGAR EL PAÍS")
print("======================================")

df["Pais"] = np.random.choice(
    [
        "México",
        "Colombia",
        "Argentina",
        "Chile",
        "Perú",
        "España",
        "Brasil",
        "Estados Unidos",
        "Canadá"
    ],
    n
)

print(df.head())

print("\nPaíses presentes en la plataforma:")

print(df["Pais"].unique())

# ==========================================================
# Parte VI. Agregar el género favorito
# ==========================================================

print("\n======================================")
print("PARTE VI. GÉNERO FAVORITO")
print("======================================")

df["GeneroFavorito"] = np.random.choice(
    [
        "Acción",
        "Drama",
        "Comedia",
        "Terror",
        "Documental",
        "Ciencia Ficción",
        "Romance",
        "Animación"
    ],
    n
)

print(df.head())

print("\nGéneros disponibles:")

print(df["GeneroFavorito"].unique())

# ==========================================================
# Parte VII. Horas visualizadas
# ==========================================================

print("\n======================================")
print("PARTE VII. HORAS VISUALIZADAS")
print("======================================")

df["HorasVisualizadas"] = np.round(
    np.random.uniform(0.5, 12, n),
    2
)

print(df.head())

# ==========================================================
# Parte VIII. Dispositivo
# ==========================================================

print("\n======================================")
print("PARTE VIII. DISPOSITIVO")
print("======================================")

df["Dispositivo"] = np.random.choice(
    [
        "Smart TV",
        "Laptop",
        "Celular",
        "Tablet"
    ],
    n
)

print(df.head())

# ==========================================================
# Parte IX. Calificación
# ==========================================================

print("\n======================================")
print("PARTE IX. CALIFICACIÓN")
print("======================================")

df["Calificacion"] = np.random.randint(1, 6, n)

print(df.head())

# ==========================================================
# Parte X. Tipo de Suscripción
# ==========================================================

print("\n======================================")
print("PARTE X. TIPO DE SUSCRIPCIÓN")
print("======================================")

df["TipoSuscripcion"] = np.random.choice(
    [
        "Básica",
        "Estándar",
        "Premium"
    ],
    n
)

print(df.head())

# ==========================================================
# Parte XI. Exploración del DataFrame
# ==========================================================

print("\n======================================")
print("PARTE XI. EXPLORACIÓN DEL DATAFRAME")
print("======================================")

print("\nPrimeros registros:\n")
print(df.head())

print("\nInformación del DataFrame:\n")
print(df.info())

print("\nDescripción del DataFrame:\n")
print(df.describe(include="all"))




print("\nNúmero de columnas:")
print(df.shape[1])

print("\nNúmero de registros:")

print(df.shape[0])

print("\nTipo de dato de cada columna:")

print(df.dtypes)

# ==========================================================
# Parte XII. Análisis del Dataset
# ==========================================================

print("\n======================================")
print("PARTE XII. ANÁLISIS DEL DATASET")
print("======================================")

print("\nUsuarios por país:\n")

print(df["Pais"].value_counts())

print("\nGénero favorito:\n")

print(df["GeneroFavorito"].value_counts())

print("\nEdad promedio:")

print(df["Edad"].mean())

print("\nPromedio de horas visualizadas:")

print(df["HorasVisualizadas"].mean())

# ==========================================================
# Desafío
# ==========================================================

print("\n======================================")
print("DESAFÍO")
print("======================================")

# Tres columnas nuevas
df["Idioma"] = np.random.choice(
    [
        "Español",
        "Inglés",
        "Portugués"
    ],
    n
)

df["MetodoPago"] = np.random.choice(
    [
        "Tarjeta de Crédito",
        "PayPal",
        "Transferencia",
        "Tarjeta de Regalo"
    ],
    n
)

df["Resolucion"] = np.random.choice(
    [
        "720p",
        "1080p",
        "4K"
    ],
    n
)

# Nivel de usuario
condiciones = [
    df["HorasVisualizadas"] < 3,
    (df["HorasVisualizadas"] >= 3) & (df["HorasVisualizadas"] <= 7),
    df["HorasVisualizadas"] > 7
]

opciones = [
    "Ocasional",
    "Activo",
    "Frecuente"
]

df["NivelUsuario"] = np.select(
    condiciones,
    opciones,
    default="Desconocido"
)

print(df.head())

# ==========================================================
# Parte XIII. Exportación
# ==========================================================

print("\n======================================")
print("PARTE XIII. EXPORTACIÓN")
print("======================================")

df.to_csv("streaming_dataset.csv", index=False)

print("\nArchivo 'streaming_dataset.csv' exportado correctamente.")

print("\n======================================")
print("DATAFRAME FINAL")
print("======================================")

print(df.head(10))