
class Asistente:
    # Atributo de clase — compartido por todos los asistentes
    tipo = "Participante de evento"

    # Constructor
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    # Método de instancia
    def presentarse(self):
        return f"Hola, soy {self.nombre} y asisto al evento."

    def validar_acceso(self):
        if self.edad >= 18:
            print(f"{self.nombre}: acceso permitido al evento")
        else:
            print(f"{self.nombre}: acceso restringido")

    # __str__ — salida amigable
    def __str__(self):
        return f"Asistente({self.nombre}, {self.edad})"

    # __repr__ — depuración
    def __repr__(self):
        return f"Asistente(nombre={self.nombre!r}, edad={self.edad!r})"


# Crear instancias (asistentes al evento)
ana = Asistente("Ana García", 28)
luis = Asistente("Luis Pérez", 16)

print(ana.presentarse())
print(luis.presentarse())

ana.validar_acceso()
luis.validar_acceso()

print(str(ana))
print(repr(ana))
print(Asistente.tipo)