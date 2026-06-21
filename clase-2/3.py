temperaturas = [28, 30, 29, 31, 27, 33, 26]

promedio = sum(temperaturas) / len(temperaturas)
print (f"Promedio semanal: {promedio:2f} C")

print(f"Mexima: {max(temperaturas)} C")
print(f"Minima: {min(temperaturas)} C")

caluroso  = [t for t in temperaturas if t > 29]
print(f"Dias calurosos: {len(caluroso)}")