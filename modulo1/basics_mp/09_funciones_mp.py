print("ciclo while")

contador = 1
while contador <= 5:
    print(f"contador: {contador}")
    contador += 1

print("continue")
i = 1
while i <= 5:
    if i == 3:
        i += 1
        continue
    print(f"i: {i}")
    i += 1

print("break")
i = 1
while i <= 5:
    i += 1
    if i == 3:
        break
    print(f"contador: {i}")

print("ingreso de datos")

numero = int(input("Ingrese un numero: "))
while numero != 0:
    print(f"Ingresaste: {numero}")
    numero = int(input("Ingrese un numero: "))

contador = 1
while contador <= 5:
    print(f"contador: {contador}")
    contador += 1
else:
    print("fin del ciclo")