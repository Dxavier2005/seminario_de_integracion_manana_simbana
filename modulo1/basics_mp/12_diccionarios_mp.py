# tuplas en sistema de gestión de eventos

# Crear tuplas
vacia = ()
unitaria = (42,)  # tupla de un solo elemento
ubicacion = (3, 4)
rgb = (255, 128, 0)
asistente = ("Ana", 28, "Madrid")

# Tupla sin paréntesis — empaquetado implícito
punto = 10, 20
print(type(punto))

# Acceso — igual que listas
print(asistente[0])
print(asistente[-1])
print(asistente[1:])

# Las tuplas son INMUTABLES
# asistente[0] = "Luis"  # error

# Desempaquetado
nombre, edad, ciudad = asistente
print(nombre, edad, ciudad)

# Desempaquetado con *
primero, *resto = (1, 2, 3, 4, 5)
print(primero)
print(resto)

*inicio, ultimo = (1, 2, 3, 4, 5)
print(inicio)
print(ultimo)

# Tuplas de retorno en sistema de eventos
def dividir(a, b):
    if b == 0:
        return None, "Error en registro de evento"
    return a / b, None

resultado, error = dividir(10, 3)

if error:
    print(f"Error: {error}")
else:
    print(f"Resultado: {resultado:.4f}")

# Tuplas como claves de diccionario (coordenadas de salas)
coordenadas = {
    (0, 0): "entrada principal",
    (1, 0): "auditorio",
    (0, 1): "sala VIP"
}

print(coordenadas[(0, 0)])

# Uso en eventos
# tuple → datos fijos del evento (ubicación, coordenadas, códigos)
# list  → datos dinámicos (asistentes, inscripciones)