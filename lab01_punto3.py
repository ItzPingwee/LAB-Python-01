import requests

url = "https://jsonplaceholder.typicode.com/users"
response = requests.get(url)
usuarios = response.json()

print("Usuarios con correo .biz:")
for u in usuarios:
    # Accedemos a la clave "email" dentro del diccionario de cada usuario
    if u["email"].endswith(".biz"):
        print(f"- Nombre: {u['name']} | Email: {u['email']}")

print("="*30)

nombre_pokemon = input("Ingrese el nombre de un Pokémon: ").lower()
url = f"https://pokeapi.co/api/v2/pokemon/{nombre_pokemon}"
respuesta = requests.get(url)

if respuesta.status_code == 200:
    datos = respuesta.json()

    # Modelado del estado
    pokemon = {
        "nombre": datos["name"],
        "altura": datos["height"],
        "peso": datos["weight"],
        "tipos": [t["type"]["name"] for t in datos["types"]],
        "habilidades": [h["ability"]["name"] for h in datos["abilities"]],
        "estadisticas": datos["stats"] # Agregamos esto para el uso extra
    }

    print("\nInformación del Pokémon")
    print(f"Nombre: {pokemon['nombre'].capitalize()}")
    
    # --- Condicionales Adicionales ---
    # 1. Tipo mixto
    if len(pokemon["tipos"]) > 1:
        print("Estado: Pokémon de tipo mixto")
    
    # 2. Peso y tamaño
    if pokemon["peso"] > 100:
        print("Clasificación: Pokémon de gran tamaño")
    else:
        print("Clasificación: Pokémon ligero")

    # --- Listado de Habilidades con for ---
    print("\nHabilidades:")
    for hab in pokemon["habilidades"]:
        print(f"  * {hab}")

    # --- Uso extra interesante: Estadísticas Base ---
    print("\nEstadísticas Base:")
    for s in pokemon["estadisticas"]:
        nombre_stat = s["stat"]["name"]
        valor_stat = s["base_stat"]
        # Creamos una pequeña barra visual
        print(f"  {nombre_stat.upper():<10}: {valor_stat}")

else:
    print("Pokémon no encontrado. Verifique el nombre ingresado.")