# Inventario inicial
inventario = [
    {"nombre": "Pan", "precio": 1500, "stock": 30},
    {"nombre": "Leche", "precio": 3500, "stock": 15},
    {"nombre": "Café", "precio": 8000, "stock": 10},
]

print(f"Primer producto: {inventario[0]['nombre']}") # 1. Muestra el nombre del primer producto
nuevo_producto = {"nombre": "Huevos", "precio": 600, "stock": 50} # 2. Agrega un nuevo producto al inventario
inventario.append(nuevo_producto)

for p in inventario: # 3. Disminuye el stock de “Leche” en 2 unidades
    if p["nombre"] == "Leche":
        p["stock"] -= 2

valor_total = sum(p["precio"] * p["stock"] for p in inventario) # 4. Calcula el valor total del inventario
print(f"Valor total del inventario: ${valor_total}")

print("Productos con bajo stock (menor a 10):") # 5. Muestra los productos cuyo stock sea menor a 10
for p in inventario:
    if p["stock"] < 10:
        print(f"- {p['nombre']} (Stock: {p['stock']})")


for p in inventario: # 6 y 7. Aumenta el precio en un 10% y redondea
    p["precio"] = round(p["precio"] * 1.10, 2)


busqueda = input("Ingresa el nombre del producto a buscar: ") # 8. Busca un producto por nombre (ingresado por el usuario)
encontrado = next((p for p in inventario if p["nombre"].lower() == busqueda.lower()), None)
if encontrado:
    print(f"Producto encontrado: {encontrado}")
else:
    print("El producto no se encuentra en el inventario.")


inventario = [p for p in inventario if p["stock"] > 0] # 9. Elimina un producto si su stock es 0, descarta los elementos si stock < 0.


inventario.sort(key=lambda p: p["precio"]) # 10. Ordena la lista por precio ascendente
print("\nInventario final ordenado por precio:")
for p in inventario:
    print(p)    