#prodcuto individual
producto = {
    "nombre": "Laptop",
    "precio": "15000",
    "stock": 10
}

#Inventario con varios productos 
inventario = {
    "laptop":{"precio":15000,"stock":10},
    "mouse":{"precio":300, "stock":50},
    "Teclado":{"precio":7000,"stock":30}
}

#Acceder al precio del mouse
print(inventario["mouse"]["precio"]) = 300

#Actualizar stock
inventario["laptop"]["stock"] -= 1