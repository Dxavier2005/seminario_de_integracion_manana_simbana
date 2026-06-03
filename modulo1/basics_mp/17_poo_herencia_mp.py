# herencia.py (adaptado a sistema de transporte para eventos y conferencias)

class TransporteEvento:
    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self._velocidad = 0

    def acelerar(self, incremento):
        self._velocidad += incremento
        return self

    def frenar(self, decremento):
        self._velocidad = max(0, self._velocidad - decremento)
        return self

    def __str__(self):
        return f"{self.marca} {self.modelo} ({self.año}) — {self._velocidad} km/h"


class BusEvento(TransporteEvento):
    def __init__(self, marca, modelo, año, capacidad=40):
        super().__init__(marca, modelo, año)
        self.capacidad = capacidad

    def abrir_puertas(self):
        return f"{self.marca} {self.modelo}: puertas abiertas para asistentes"

    def __str__(self):
        return f"{super().__str__()} ({self.capacidad} pasajeros)"


class MotoTaxiEvento(TransporteEvento):
    def __init__(self, marca, modelo, año, tipo):
        super().__init__(marca, modelo, año)
        self.tipo = tipo

    def traslado_rapido(self):
        return f"🏍 {self.marca} traslado rápido al evento"

    def __str__(self):
        return f"{super().__str__()} ({self.tipo})"


class BusElectricoEvento(BusEvento):
    def __init__(self, marca, modelo, año, autonomia):
        super().__init__(marca, modelo, año)
        self.__autonomia = autonomia
        self.__bateria = 100

    def cargar(self, porcentaje=100):
        self.__bateria = min(100, self.__bateria + porcentaje)
        return self

    @property
    def autonomia_restante(self):
        return self.__autonomia * self.__bateria / 100

    def __str__(self):
        return (f"{super().__str__()} | "
                f"Batería: {self.__bateria}% | "
                f"Autonomía: {self.autonomia_restante:.0f}km")


# uso — sistema de transporte para eventos
bus = BusElectricoEvento("Tesla", "Bus X", 2025, 400)
bus.acelerar(80)
print(bus)

print(isinstance(bus, BusElectricoEvento))
print(isinstance(bus, BusEvento))
print(isinstance(bus, TransporteEvento))

print(BusElectricoEvento.__mro__)