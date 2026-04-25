# Estado inicial
saldo = 500_000      # Saldo de la cuenta
deposito = float(input("Ingrese el valor a depositar: "))  # Monto a depositar
retiro = float(input("Ingrese el valor a retirar: "))      # Monto a retirar
interes = 0.02 
# Actualización del estado
saldo = saldo + deposito   # Se deposita dinero
saldo = saldo - retiro     # Se retira dinero
saldo_final = saldo + (saldo*interes) #rendimientos
# Salida del estado final
print("Saldo final de la cuenta:", saldo)
print(f"Saldo final con interés: ${saldo_final:.2f}")

""" ¿Qué representa el estado inicial y el estado final del programa?
Estado Inicial: Es el punto de partida del programa. Define las condiciones previas (en este caso, que ya existen 500,000 en la cuenta)
antes de que ocurra cualquier interacción o proceso nuevo.
Estado Final: Es el resultado de todas las transformaciones aplicadas a los datos. Refleja la realidad de la cuenta después
de haber procesado los flujos de dinero (entradas/salidas) y los cálculos financieros (intereses).

Explica cómo cada instrucción afecta la memoria.
- saldo = 500_000: Se reserva un espacio en memoria llamado saldo y se guarda el valor 500000.
- deposito = float(input(...)): El programa se detiene, recibe un texto del usuario, lo convierte en un número decimal
y crea un nuevo espacio llamada deposito para guardarlo.
- saldo = saldo + deposito: Esta es una instrucción de sobrescritura. La computadora busca el valor de saldo, le suma el valor de deposito
y guarda el resultado de nuevo en la caja saldo, borrando el número anterior.
- saldo_final = saldo + (saldo * interes): Aquí se crea un espacio nuevo en memoria. La computadora calcula el 2% de saldo, 
se lo suma al saldo actual y guarda ese total en una ubicación distinta llamada saldo_final.

"""
