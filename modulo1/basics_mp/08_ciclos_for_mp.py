print("ciclo for")
frutas = ["manzana", "banana", "pera"]

for fruta in frutas:
    print(fruta)

print("Recorre palabras")
for letra in "frutas":
    print(letra)

print("Recorrer rango")
for i in range(1, 6):
    print(i)

print("Recorrer rango con paso")
for i in range(1, 10, 2):
    print(i)

print("Enumerar lista")
for i, fruta in enumerate(frutas):
    print(i, fruta)

print("Dos listas a la vez")
nombres = ["Ana", "Luis"]
edades = [28, 25]

for nombre, edad in zip(nombres, edades):
    print(nombre, edad)

print("Control del ciclo - break")
for i in range(5):
    if i == 3:
        break
    print(i)

print("Control del ciclo - continue")
for i in range(5):
    if i == 2:
        continue
    print(i)

print("for anidado")
for i in range(3):
    for j in range(2):
        print("i,j")

print("lista comprensión forma corta")
cuadrados = [x**2 for x in range(5)]
print(cuadrados)

print("Ejercicio en clase - gestión de ventas de eventos")

ventas = [120, 80, 200, 50, 300]

ventas_validas = 0
bono_acumulado = 0

print("Procesando Ventas")

for venta in ventas:
    if venta > 100:
        ventas_validas += 1

        if venta > 250:
            bono = 30
        else:
            bono = 10

        bono_acumulado += bono
        print(f"Venta de {venta}: Válida - Bono de ${bono}")
    else:
        print(f"Venta de {venta}: No válida (Menor o igual a 100)")

print("-" * 25)
print(f"Total de ventas válidas: {ventas_validas}")
print(f"Total de bono acumulado: ${bono_acumulado}")