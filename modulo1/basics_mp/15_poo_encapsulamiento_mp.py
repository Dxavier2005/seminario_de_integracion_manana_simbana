
from abc import ABC, abstractmethod

# Clase abstracta — base para distintos tipos de eventos
class Evento(ABC):
    def __init__(self, nombre, lugar):
        self.nombre = nombre
        self.lugar = lugar

    # Método abstracto — cada tipo de evento lo define
    @abstractmethod
    def costo_organizacion(self) -> float:
        pass

    @abstractmethod
    def duracion(self) -> int:
        pass

    # Método común
    def describir(self) -> str:
        return (f"{self.__class__.__name__} {self.nombre} en {self.lugar}: "
                f"costo={self.costo_organizacion():.2f}, duración={self.duracion()}h")


class Conferencia(Evento):
    def __init__(self, nombre, lugar, ponentes):
        super().__init__(nombre, lugar)
        self.ponentes = ponentes

    def costo_organizacion(self):
        return 500 + (len(self.ponentes) * 150)

    def duracion(self):
        return 4


class Taller(Evento):
    def __init__(self, nombre, lugar, horas):
        super().__init__(nombre, lugar)
        self.horas = horas

    def costo_organizacion(self):
        return 300 + (self.horas * 100)

    def duracion(self):
        return self.horas


class Seminario(Evento):
    def __init__(self, nombre, lugar, sesiones):
        super().__init__(nombre, lugar)
        self.sesiones = sesiones

    def costo_organizacion(self):
        return 200 + (self.sesiones * 120)

    def duracion(self):
        return self.sesiones * 2


# Polimorfismo — mismo código para distintos eventos
eventos = [
    Conferencia("Tech Summit", "Quito", 5),
    Taller("Flutter Bootcamp", "Guayaquil", 6),
    Seminario("IA Aplicada", "Cuenca", 3)
]

for e in eventos:
    print(e.describir())

costo_total = sum(e.costo_organizacion() for e in eventos)
print(f"Costo total del evento: {costo_total:.2f}")