# Lista inicial de temperaturas en °C
temperaturas = [22.5, 23.0, 21.8, 24.3, 25.1]
temperaturas.append(26.0) #agregar nueva temp al final de la lista
temperaturas.remove(22.5) #eliminar primera temperatura
temperaturas.insert(1, 30.0) #inserta temp a posicion 2, es decir index [1]
temperaturas.sort() #organiza temps de menor a mayor
# indice = temperaturas.index(23.7) No existe por lo que genera un ValueError
dif = temperaturas[-1] - temperaturas[0]
promedio = sum(temperaturas) / len(temperaturas)

# Operaciones básicas
print("Temperaturas:", temperaturas)
print(f"La diferencia entre la primera y la ultima posicion es de: {dif}. ")
print(f"El promedio de las temperaturas es: {promedio:.2f}")
# print(f"El indice de la temp 23.7 es: {indice}")
for i in range(1, 4):
    print(f"La temp en posicion #{i+1} = {temperaturas[i]}")
print("-"*20)
for i in range(3):
    print(f"La temp en posicion #{i+1} = {temperaturas[i]}")
