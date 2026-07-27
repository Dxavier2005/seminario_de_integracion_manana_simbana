import math

print("Cálculos de gestión de presupuesto de evento")

presupuesto_actual = 1234.56
incremento = 0.075

nuevo_presupuesto = presupuesto_actual * (1 + incremento)

print(f"Presupuesto con incremento {incremento*100}%: {nuevo_presupuesto:.2f}")
print(f"Redondeado hacia arriba: {math.ceil(nuevo_presupuesto)}")
print(f"Redondeado hacia abajo: {math.floor(nuevo_presupuesto)}")
print(f"Redondeado normal: {round(nuevo_presupuesto, 2)}")

print(f"Valor absoluto: {abs(-1500)}")
print(f"Máximo: {max(1200, 1500, 1100)}")
print(f"Mínimo: {min(1200, 1500, 1100)}")

print(f"Raíz cuadrada de 16: {math.sqrt(16)}")
print(f"Potencia 2^8: {2**8}")