biblioteca = {
    "libros": [
        {"titulo": "1984", "autor": "George Orwell", "prestado": False},
        {"titulo": "El Principito", "autor": "Antoine de Saint-Exupéry", "prestado": True},
    ],
    "usuarios": ["Ana", "Luis", "María"]
}

# 1. Muestra cuántos libros están prestados y cuántos disponibles
prestados = 0
disponibles = 0

for libro in biblioteca["libros"]:
    if libro["prestado"]:
        prestados += 1
    else:
        disponibles += 1

print(f"Libros prestados: {prestados}")
print(f"Libros disponibles: {disponibles}")

# 2. Agrega un nuevo libro
nuevo_libro = {"titulo": "Cien años de soledad", "autor": "Gabriel García Márquez", "prestado": False}
biblioteca["libros"].append(nuevo_libro)

# 3. Marca como prestado el libro “1984”
for libro in biblioteca["libros"]:
    if libro["titulo"] == "1984":
        libro["prestado"] = True

# 4. Muestra el estado actualizado del sistema
print("ESTADO DE LA BIBLIOTECA:")
print("Libros:")
for libro in biblioteca["libros"]:
    print(f"  - {libro}")

print(f"Usuarios: {biblioteca['usuarios']}")