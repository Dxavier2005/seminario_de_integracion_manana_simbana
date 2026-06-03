# polimorfismo.py (adaptado a sistema de notificaciones de eventos)

# POLIMORFISMO POR HERENCIA
class Notificacion:
    def __init__(self, destinatario, mensaje):
        self.destinatario = destinatario
        self.mensaje = mensaje

    def enviar(self):
        raise NotImplementedError("Las subclases deben implementar enviar()")

    def __str__(self):
        return f"{self.__class__.__name__} → {self.destinatario}"


class NotificacionEmail(Notificacion):
    def __init__(self, destinatario, mensaje, asunto="Sin asunto"):
        super().__init__(destinatario, mensaje)
        self.asunto = asunto

    def enviar(self):
        return f"📧 Email a {self.destinatario}: [{self.asunto}] {self.mensaje}"


class NotificacionSMS(Notificacion):
    MAX_CHARS = 160

    def enviar(self):
        msg = self.mensaje[:self.MAX_CHARS]
        return f"📱 SMS a {self.destinatario}: {msg}"


class NotificacionPush(Notificacion):
    def enviar(self):
        return f"🔔 Push a {self.destinatario}: {self.mensaje[:50]}..."


class NotificacionSistema(Notificacion):
    def __init__(self, canal, mensaje):
        super().__init__(canal, mensaje)

    def enviar(self):
        return f"💬 Sistema de eventos #{self.destinatario}: {self.mensaje}"


# Polimorfismo en acción
def notificar_asistentes(notificaciones: list):
    for notif in notificaciones:
        print(f"  {notif.enviar()}")


alertas = [
    NotificacionEmail("ana@email.com", "Tu inscripción fue confirmada", "Evento #1234"),
    NotificacionSMS("600111222", "Tu entrada está lista"),
    NotificacionPush("device-abc", "¡Nuevo evento disponible!"),
    NotificacionSistema("admin-eventos", "Capacidad completa en sala principal"),
]

print("Enviando notificaciones de eventos:")
notificar_asistentes(alertas)


# DUCK TYPING aplicado a gestión de archivos de eventos
class ArchivoRegistro:
    def leer(self): return "registros de asistentes"
    def escribir(self, datos): print(f"Guardando registro: {datos[:30]}...")


class ArchivoReportes:
    def leer(self): return "reportes del evento"
    def escribir(self, datos): print(f"Generando reporte: {datos[:30]}...")


class ArchivoLog:
    def leer(self): return "logs del sistema del evento"
    def escribir(self, datos): print(f"Guardando log: {datos[:30]}...")


def procesar_archivo(archivo):
    contenido = archivo.leer()
    print(f"Procesando: {contenido}")
    archivo.escribir(f"resultado_{contenido}")


for archivo in [ArchivoRegistro(), ArchivoReportes(), ArchivoLog()]:
    procesar_archivo(archivo)