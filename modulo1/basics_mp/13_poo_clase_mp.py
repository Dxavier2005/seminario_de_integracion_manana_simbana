
# Crear diccionarios
vacio = {}
asistente = {"nombre": "Ana", "edad": 28, "ciudad": "Madrid"}
config = dict(host="localhost", puerto=5432, debug=True)

# Acceso
print(asistente["nombre"])
print(asistente.get("email"))
print(asistente.get("email", "N/A"))

# Modificar
asistente["email"] = "ana@email.com"
asistente["edad"] = 29
del asistente["ciudad"]

valor = asistente.pop("email")
print(asistente)

# Verificar existencia
print("nombre" in asistente)
print("ciudad" in asistente)

# Métodos esenciales
print(asistente.keys())
print(asistente.values())
print(asistente.items())

# Iterar
for clave, valor in asistente.items():
    print(f"{clave}: {valor}")

# update — actualizar datos del asistente
asistente.update({"ciudad": "Barcelona", "tel": "600111222"})
print(asistente)

# Fusionar diccionarios
extra = {"cargo": "Asistente", "activo": True}
completo = asistente | extra
print(completo)

# Diccionarios anidados — sistema de eventos
evento = {
    "nombre": "Tech Conference",
    "asistentes": {
        1: {"nombre": "Ana", "depto": "tech"},
        2: {"nombre": "Luis", "depto": "ventas"},
    },
    "sedes": ["Madrid", "Barcelona"]
}

print(evento["asistentes"][1]["nombre"])
evento["asistentes"][3] = {"nombre": "Marta", "depto": "rrhh"}

# setdefault — registro automático de datos
asistente.setdefault("pais", "España")
asistente.setdefault("nombre", "Otro")