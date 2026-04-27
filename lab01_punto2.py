edad = int(input("Ingrese su edad: "))
tiene_licencia = input("¿Tiene licencia? (s/n): ").lower()
sancionado = input("¿Está sancionado actualmente? (s/n): ").lower()

# Determinamos si puede conducir (Debe ser mayor de edad, tener licencia y NO estar sancionado)
if edad >= 16 and tiene_licencia == "s" and sancionado == "n":
    print("Puedes conducir legalmente.")
else:
    print("No cumples con los requisitos para conducir.")
# ---------------------------------------------------------------
print("-"*45)
n = int(input("Hasta qué número quieres sumar?: "))
suma_total = 0
print("Números pares encontrados:")
for i in range(1, n + 1):
    if i % 2 == 0:
        print(i)
    suma_total += i
print(f"La suma de los primeros {n} números es: {suma_total}")
# --- Temperaturas ---
temperaturas = [18, 22, 15, 30, 25] # Ejemplo de datos
promedio = sum(temperaturas) / len(temperaturas)
print(f"Promedio: {promedio}")
print("Temperaturas mayores al promedio:")
for t in temperaturas:
    if t > promedio:
        print(f"- {t} C")
# ---------------------------------------------------------------
print("-"*45)
contador = 5
while contador > 0:
    print("Contador:", contador)
    contador -= 1
while True:
    num = float(input("Ingresa un número (0 para salir): "))
    if num == 0:
        break
# Explicación del estado: El "estado" del ciclo lo representa la variable 'contador' (en el primer caso) 
# o la entrada del usuario en el segundo. Es el valor que determina si la condición de permanencia sigue siendo verdadera o falsa.
# ---------------------------------------------------------------
print("-"*45)
suma_pares = 0
suma_impares = 0
for i in range(1, 11):
    if i % 2 == 0:
        suma_pares += i
    else:
        suma_impares += i

estado_final = {
    "suma_pares": suma_pares,
    "suma_impares": suma_impares
}
print(estado_final)

# Explicación del cambio de estado: Dentro del bucle, el estado cambia en cada iteración. En el paso 'i', se evalúa una condición y se 
# actualiza UNA de las dos variables acumuladoras. El estado es "incremental": el valor nuevo depende del valor anterior más 'i'.
# ---------------------------------------------------------------
print("-"*45)
productos = []
while True:
    nombre = input("Ingrese producto (o 'fin' para salir): ")
    if nombre == "fin":
        break
    
    precio = float(input("Precio: "))
    cantidad = int(input("Cantidad: "))
    
    # Uso de continue para saltar datos erróneos
    if precio < 0 or cantidad < 0:
        print("Error: No se admiten valores negativos. Intente de nuevo.")
        continue
        
    productos.append({"nombre": nombre, "precio": precio, "cantidad": cantidad})

# Mostrar el producto más caro usando max()
if productos:
    # Usamos la clave 'precio' para comparar dentro de los diccionarios
    mas_caro = max(productos, key=lambda p: p["precio"])
    print(f"El producto más caro es: {mas_caro['nombre']} (${mas_caro['precio']})")
    
    # Total
    total = sum(p["precio"] * p["cantidad"] for p in productos)
    print("Total del inventario:", total)
    print("Estado final de la lista:", productos)
else:
    print("No se ingresaron productos válidos.")