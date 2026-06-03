print("Listas en sistema de gestión de eventos")

print("Crear una lista")
vacia = []
numeros = [1, 2, 3, 4, 5]
nombres = ["Juan", "Pedro", "Carlos", "María", "Petra", "Juana"]

print(nombres)

mixta = [1, "Hola", "Mundo", True, None, 3.4]
print(mixta)

anidada = [1, [5, 5, [6, 4, 4]], 5, 7]
print(anidada)

print("Acceder a elementos de la lista")
print(nombres[0])
print(nombres[-1])
print(nombres[1:3])
print(nombres[::-1])

print("CRUD de lista (eventos / participantes)")

frutas = ["manzana", "pera", "melón"]

# agregar
frutas.append("durazno")
print(frutas)

frutas.insert(1, "naranja")
print(frutas)

frutas.extend(["kiwi", "mango"])

# modificar
frutas[0] = "toronja"
print(frutas)

# eliminar elementos
frutas.remove("banana")
print(frutas)

eliminado = frutas.pop()
print(frutas)

eliminado = frutas.pop(0)
print(frutas)

del frutas[0]
print(frutas)

print("Buscar valores en la lista")
print("manzana" in frutas)
print(frutas.index("kiwi"))
print(frutas.count("kiwi"))

print("Ordenar lista")
numeros_desordenados = [5, 2, 9, 1, 5, 6]
numeros_desordenados.sort()
print(numeros_desordenados)
