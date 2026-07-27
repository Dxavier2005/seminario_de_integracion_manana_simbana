print("Funciones en sistema de gestión de eventos")

print("funciones básicas")
def saludar():
    print("Bienvenido al sistema de eventos de la UTE")

saludar()

print("función con parámetro")
def saludarConNombre(nombre):
    print(f"Hola {nombre}, bienvenido al evento")

saludarConNombre("John")

print("función que devuelve valor con return")
def sumar(a, b):
    return a + b

print(sumar(5, 6))

print("función parámetros por posición")
def presentar(nombre, edad, ciudad):
    print(f"{nombre}, {edad}, {ciudad}")

presentar("Pedro", 60, "Quito")
presentar(ciudad="Guayaquil", nombre="Juan", edad=40)

print("función con parámetros por defecto")
def saludo_con_parametros_por_defecto(nombre, saludo="Hola", puntuacion="!"):
    print(f"{saludo}, {nombre}, {puntuacion}")

saludo_con_parametros_por_defecto("Pedro", "Buenos días", "...")
saludo_con_parametros_por_defecto("Juan", puntuacion="...")
saludo_con_parametros_por_defecto("Carlos", "Buenas tardes")

print("función con *args")
def sumar_todos(*args):
    print(f"Argumentos recibidos {args}")
    return sum(args)

print(sumar_todos(1, 2, 3))
print(sumar_todos(1, 2, 3, 4, 5, 6, 7))
print(sumar_todos(10, 20, 22))

print("función con parámetros combinados")
def mostrar_info(titulo, *datos):
    print(f"{titulo} {datos}")
    print(titulo)
    for dato in datos:
        print(f"- {dato}")

mostrar_info("Eventos", "Conferencia", "Workshop", "Seminario", "Meetup")

print("función con **kwargs")
def crear_perfil(**kwargs):
    print(f"Datos del asistente: {kwargs}")
    for clave, valor in kwargs.items():
        print(f"{clave}: {valor}")

crear_perfil(nombre="Ana", apellido="Paris", edad=26, ciudad="Quito")

print("función con combinación completa")
def configurar(host, *eventos, debug=False, **opciones):
    print(f"Host: {host}")
    print(f"Eventos: {eventos}")
    print(f"Debug: {debug}")
    print(f"Opciones: {opciones}")

configurar("localhost", 80, 443, 8080, debug=True, timeout=30, ssl=True)

print("Devolver múltiples valores")
def minmax(numeros):
    return min(numeros), max(numeros)

minimo, maximo = minmax([3, 5, 7, 8, 9])
print(f"Mínimo {minimo}, Máximo {maximo}")

_, maximo = minmax([12, 13, 16, 24, 100])
print(f"Solo máximo {maximo}")

print("Devolver diccionario en sistema de eventos")
def analizar(numeros):
    n = len(numeros)
    total = sum(numeros)
    return {
        "total": total,
        "media": total / n if n > 0 else 0,
        "minimo": min(numeros) if numeros else None,
        "maximo": max(numeros) if numeros else None,
        "count": n
    }

datos = [12, 88, 44, 55, 23, 45]
stats = analizar(datos)

print(f"Total: {stats['total']}")
print(f"Media: {stats['media']:.2f}")
print(f"Rango: {stats['minimo']}-{stats['maximo']}")

print("funciones lambda")
def doble(x):
    return x * 2

doble_lambda = lambda x: x * 2

print(doble(2))
print(doble_lambda(2))

suma = lambda a, b: a + b
print(suma(5, 4))