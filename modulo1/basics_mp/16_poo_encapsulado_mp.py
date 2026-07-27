# encapsulamiento.py (adaptado a sistema de pagos de eventos)

class CuentaAsistente:
    def __init__(self, nombre, saldo_inicial=0):
        self.nombre = nombre
        self.__saldo = saldo_inicial
        self.__historial = []
        self.__activa = True
        self.__registrar(f"Cuenta creada con saldo {saldo_inicial}")

    @property
    def saldo(self):
        return self.__saldo

    @property
    def activa(self):
        return self.__activa

    @property
    def historial(self):
        return list(self.__historial)

    # método público
    def pagar_evento(self, cantidad):
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser positiva")
        self.__saldo -= cantidad
        self.__registrar(f"Pago de evento: -{cantidad}")
        return self

    def recargar(self, cantidad):
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser positiva")
        self.__saldo += cantidad
        self.__registrar(f"Recarga de saldo: +{cantidad}")
        return self

    def transferir_inscripcion(self, destino, cantidad):
        self.pagar_evento(cantidad)
        destino.recargar(cantidad)
        self.__registrar(f"Transferencia de inscripción a {destino.nombre}: -{cantidad}")
        return self

    # método privado
    def __registrar(self, operacion):
        from datetime import datetime
        hora = datetime.now().strftime("%H:%M:%S")
        self.__historial.append(f"[{hora}] {operacion}")

    def __str__(self):
        return f"Asistente({self.nombre}: {self.__saldo})"


# uso
a1 = CuentaAsistente("Ana García", 1000)
a2 = CuentaAsistente("Luis Pérez", 500)

a1.recargar(500).pagar_evento(200)
a1.transferir_inscripcion(a2, 300)

print(a1)
print(a2)

print(f"Saldo Ana: {a1.saldo}")

for h in a1.historial:
    print(f"  {h}")