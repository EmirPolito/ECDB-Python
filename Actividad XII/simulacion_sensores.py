# pyrefly: ignore [missing-import]
import numpy as np

# ==========================================
# Parte II: Generación de temperaturas
# ==========================================
print("--- Parte II: Simulación de Sensores ---")
# Generamos 50 temperaturas aleatorias entre 18 y 42 grados
# Usamos randint(18, 43) para incluir el 42
temperaturas = np.random.randint(18, 43, size=50)

print("Arreglo de temperaturas registradas (°C):")
print(temperaturas)
print(f"Cantidad total de sensores simulados: {temperaturas.size}\n")

# ==========================================
# Parte III: Estadísticas básicas (sin ciclos)
# ==========================================
print("--- Parte III: Estadísticas Básicas ---")
# Se usan las funciones propias de NumPy
promedio = np.mean(temperaturas)
temp_max = np.max(temperaturas)
temp_min = np.min(temperaturas)
suma_total = np.sum(temperaturas)

print(f"Temperatura promedio: {promedio:.2f} °C")
print(f"Temperatura máxima registrada: {temp_max} °C")
print(f"Temperatura mínima registrada: {temp_min} °C")
print(f"Suma total de todas las temperaturas: {suma_total} °C\n")

# ==========================================
# Parte IV: Análisis de valores extremos
# ==========================================
print("--- Parte IV: Análisis de Temperaturas Altas ---")
# Filtramos directamente las que son mayores a 38
altas = temperaturas[temperaturas > 38]
cantidad_altas = altas.size
porcentaje_altas = (cantidad_altas / temperaturas.size) * 100

print(f"Temperaturas que superan los 38°C: {altas}")
print(f"¿Cuántas hay? {cantidad_altas} temperaturas")
print(f"Porcentaje respecto al total: {porcentaje_altas:.1f}%\n")

# ==========================================
# Parte V: Simulación de fallas
# ==========================================
print("--- Parte V: Estado de los Sensores ---")
# Creamos un arreglo de 50 sensores activos (1 = activo)
sensores_estado = np.ones(50, dtype=int)

# Simulamos fallas cambiando 5 posiciones aleatorias a 0 (manual como pide la actividad)
sensores_estado[3] = 0
sensores_estado[15] = 0
sensores_estado[27] = 0
sensores_estado[41] = 0
sensores_estado[49] = 0

# Contamos cuántos tienen 1 (activos) y cuántos 0 (fallas)
activos = np.sum(sensores_estado == 1)
fallas = np.sum(sensores_estado == 0)

print(f"Sensores que siguen activos (1): {activos}")
print(f"Sensores que presentan fallas (0): {fallas}\n")

# ==========================================
# Parte VI: Matriz semanal
# ==========================================
print("--- Parte VI y VII: Matriz Semanal ---")
# Creamos una matriz de 7 filas (días) por 50 columnas (sensores)
matriz_semanal = np.random.randint(18, 43, size=(7, 50))
print("Matriz semanal generada (7x50). Omitiendo impresión completa por tamaño.\n")

# ==========================================
# Parte VII: Cálculos con la matriz semanal
# ==========================================
max_semanal = np.max(matriz_semanal)
min_semanal = np.min(matriz_semanal)
promedio_semanal = np.mean(matriz_semanal)

# Para sacar el promedio por día, calculamos el promedio de cada fila (axis=1)
promedios_por_dia = np.mean(matriz_semanal, axis=1)

# argmax y argmin devuelven la posición, le sumamos 1 para que sea Día 1, 2, 3... en vez de 0, 1, 2
dia_mayor_temp = np.argmax(promedios_por_dia) + 1
dia_menor_temp = np.argmin(promedios_por_dia) + 1

print(f"Temperatura máxima en toda la semana: {max_semanal} °C")
print(f"Temperatura mínima en toda la semana: {min_semanal} °C")
print(f"Temperatura promedio de toda la semana: {promedio_semanal:.2f} °C")
print(f"El día con MAYOR temperatura promedio fue el Día {dia_mayor_temp} ({promedios_por_dia[dia_mayor_temp-1]:.2f} °C)")
print(f"El día con MENOR temperatura promedio fue el Día {dia_menor_temp} ({promedios_por_dia[dia_menor_temp-1]:.2f} °C)\n")

# ==========================================
# Parte VIII: Clasificación automática
# ==========================================
print("--- Parte VIII: Clasificación de las Temperaturas ---")
# Clasificamos usando np.where
# Criterio: < 22 es Baja, entre 22 y 30 es Normal, > 30 es Alta
clasificacion = np.where(temperaturas < 22, "Baja",
                         np.where(temperaturas <= 30, "Normal", "Alta"))

cantidad_bajas = np.sum(clasificacion == "Baja")
cantidad_normal = np.sum(clasificacion == "Normal")
cantidad_altas_clasif = np.sum(clasificacion == "Alta")

print(f"Temperaturas clasificadas como Bajas: {cantidad_bajas}")
print(f"Temperaturas clasificadas como Normales: {cantidad_normal}")
print(f"Temperaturas clasificadas como Altas: {cantidad_altas_clasif}")
print("\nJustificación de los rangos:")
print("Elegí menor a 22°C para 'Baja' porque suele sentirse algo fresco. Entre 22°C y 30°C lo tomé como 'Normal' porque es una temperatura ambiente cálida y agradable, y mayor a 30°C como 'Alta' porque ya se considera bastante calor.")

