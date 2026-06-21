# EMIR POLITO GUEVARA
# DESAFÍO: Sistema de Gestión de Videojuegos
import pandas as pd

print("="*60)
print("1. LISTA DE VIDEOJUEGOS")
print("="*60)

# 1. Crear una lista con al menos 10 videojuegos
videojuegos = [
    "The Legend of Zelda: Breath of the Wild",
    "Super Mario Odyssey",
    "Red Dead Redemption 2",
    "Minecraft",
    "Grand Theft Auto V",
    "Elden Ring",
    "The Witcher 3: Wild Hunt",
    "Cyberpunk 2077",
    "Hollow Knight",
    "Hades"
]

print(f"Lista de videojuegos ({len(videojuegos)}):")
for juego in videojuegos:
    print(f"- {juego}")

print("\n" + "="*60)
print("2. TUPLA DE CONSOLA")
print("="*60)

# 2. Crear una tupla con información de una consola (marca, modelo, año)
consola = ("Sony", "PlayStation 5", 2020)
print(f"Información de la consola: {consola}")
print(f"Marca: {consola[0]}")
print(f"Modelo: {consola[1]}")
print(f"Año: {consola[2]}")

print("\n" + "="*60)
print("3. SET DE CATEGORÍAS")
print("="*60)

# 3. Crear un set con categorías de videojuegos eliminando duplicados
# Primero creamos una lista con duplicados para demostrar cómo el set los elimina
categorias_con_duplicados = ["Aventura", "Acción", "RPG", "Aventura", "Shooter",
"RPG", "Plataformas", "Indie"]
print(f"Lista original con duplicados: {categorias_con_duplicados}")

categorias_set = set(categorias_con_duplicados)
print(f"Set de categorías (sin duplicados): {categorias_set}")

print("\n" + "="*60)
print("4. DICCIONARIO DE CLIENTE")
print("="*60)

# 4. Crear un diccionario para almacenar información de un cliente
cliente = {
    "id_cliente": 10245,
    "nombre": "Emir",
    "apellido": "Polito",
    "correo": "emirpolitog@gmail.com",
    "es_premium": True
}
print("Información del cliente:")
for clave, valor in cliente.items():
    print(f"{clave}: {valor}")

print("\n" + "="*60)
print("5. DATAFRAME DE VENTAS")
print("="*60)

# 5. Crear un DataFrame con las ventas de la semana
datos_ventas = {
    "Videojuego": [
        "The Legend of Zelda: Breath of the Wild",
        "Super Mario Odyssey",
        "Red Dead Redemption 2",
        "Minecraft",
        "Elden Ring"
    ],
    "Categoría": ["Aventura", "Plataformas", "Acción", "Supervivencia", "RPG"],
    "Precio": [1200.0, 1100.0, 900.0, 450.0, 1300.0],
    "Unidades vendidas": [15, 20, 10, 50, 12]
}

df_ventas = pd.DataFrame(datos_ventas)

# Análisis solicitado
print("\n--- 1. Primeras filas del DataFrame (df.head) ---")
print(df_ventas.head())
print("\n--- 2. Estadísticas descriptivas (df.describe) ---")
print(df_ventas.describe())
print("\n--- 3. Videojuego más caro ---")

# Encontramos la fila donde el precio es el máximo
indice_mas_caro = df_ventas["Precio"].idxmax()
juego_mas_caro = df_ventas.loc[indice_mas_caro, "Videojuego"]
precio_maximo = df_ventas.loc[indice_mas_caro, "Precio"]
print(f"El videojuego más caro es '{juego_mas_caro}' con un precio de ${precio_maximo}")
print("\n--- 4. Videojuego con más ventas ---")

# Encontramos la fila donde las unidades vendidas son el máximo
indice_mas_ventas = df_ventas["Unidades vendidas"].idxmax()
juego_mas_ventas = df_ventas.loc[indice_mas_ventas, "Videojuego"]
max_unidades = df_ventas.loc[indice_mas_ventas, "Unidades vendidas"]
print(f"El videojuego con más ventas es '{juego_mas_ventas}' con {max_unidades} unidades")
print("\n--- 5. Agregar columna 'Ingreso' ---")

# Agregamos la columna antes del total para poder usarla si queremos, o simplemente mostrarla
df_ventas["Ingreso"] = df_ventas["Precio"] * df_ventas["Unidades vendidas"]
print(df_ventas)
print("\n--- 6. Ingreso total de la semana ---")

# Sumamos la columna de Ingreso
ingreso_total = df_ventas["Ingreso"].sum()
print(f"El ingreso total de la semana fue: ${ingreso_total}")
