# Operadores para cálculos de gestión de eventos (presupuesto)

presupuesto_base = 1500
costo_extra = 200

print("Suma")
print(presupuesto_base, "+", costo_extra, "=", presupuesto_base + costo_extra)

print("Resta")
print(presupuesto_base, "-", costo_extra, "=", presupuesto_base - costo_extra)

print("Multiplicación")
print(presupuesto_base, "*", costo_extra, "=", presupuesto_base * costo_extra)

print("División")
print(presupuesto_base, "/", costo_extra, "=", presupuesto_base / costo_extra)

print("Módulo")
print(presupuesto_base, "%", costo_extra, "=", presupuesto_base % costo_extra)

print("Operador de Asignación")
print("=" * 25)

n = 1000
n += 100
print("n += 100:", n)

n -= 50
print("n -= 50:", n)

n *= 2
print("n *= 2:", n)

n /= 2
print("n /= 2:", n)

n **= 2
print("n **= 2:", n)