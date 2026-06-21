alumno = {
    "nombre": "Emir",
    "edad": 18,
    "carrera": "TI"
}

#Leer valores
print(alumno["nombre"])
print(alumno["edad"])

#Modificar valor existente
alumno["edad"] = 19

#Afregar nueva clave
alumno["correo"] = "emirpolitog@gmail.com"

print(alumno)
#{"nombre": "Juan", "edad": 19, "carrera": "TI", "correo": "emirpolitog@gmail.com"}