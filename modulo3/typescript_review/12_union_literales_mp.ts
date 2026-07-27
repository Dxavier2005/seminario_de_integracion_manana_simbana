type EstadoRegistro = "pendiente" | "confirmado" | "asistio" | "cancelado";
type Prioridad = "baja" | "media" | "alta";

function procesarRegistro(id: number, estado: EstadoRegistro): void {
  console.log(`Registro #${id}: ${estado}`);
}

procesarRegistro(1, "confirmado");

type PrioridadConferencia = "baja" | "media" | "alta" | "critica";

interface SolicitudConferencia {
  id: number;
  titulo: string;
  prioridad: PrioridadConferencia;
  resuelto: boolean;
}

function etiquetarSolicitud(t: SolicitudConferencia): string {
  const prefijos: Record<PrioridadConferencia, string> = {
    baja:    "⚪",
    media:   "🟡",
    alta:    "🟠",
    critica: "🔴",
  };
  const estado = t.resuelto ? "✅" : "⏳";
  return `${estado} ${prefijos[t.prioridad]} [#${t.id}] ${t.titulo}`;
}

const solicitudes: SolicitudConferencia[] = [
  { id: 1, titulo: "Falta proyector en sala 3", prioridad: "baja",    resuelto: true  },
  { id: 2, titulo: "Falla de audio en keynote", prioridad: "critica", resuelto: false },
  { id: 3, titulo: "Demora en acreditación",    prioridad: "media",    resuelto: false },
];

for (const t of solicitudes) {
  console.log(etiquetarSolicitud(t));
}