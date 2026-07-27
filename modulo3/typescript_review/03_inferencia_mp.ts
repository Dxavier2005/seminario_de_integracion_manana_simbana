export const asientoDefault = 5;
const auditorio: string = "Principal";
const disponible: boolean = true;

const asientoDefault2 = 5;
const auditorio2 = "Principal";
const disponible2 = true;

let tiempoEspera: number;
tiempoEspera = 15;

let codigoRegistro: number | string = 101;
codigoRegistro = "REG-OK";

function consultarAsiento(asiento: string, intentos: number): string {
  return `Consulta asiento ${asiento} — ${intentos} intento(s)`;
}


const NOMBRE_EVENTO = "Conferencia Tech Principal";
const ASIENTOS_TOTALES  = 28;
const ES_HORARIO_PICO   = true;

let asistentesAtendidos: number = 0;
let ultimoErrorRegistro: string | null = null;

function registrarAsistente(ponencia: string, asiento: number): void {
  asistentesAtendidos++;
  console.log(`[${NOMBRE_EVENTO}] Asiento ${asiento} — ${ponencia} — total: ${asistentesAtendidos}`);
}

registrarAsistente("Keynote Inteligencia Artificial", 5);
registrarAsistente("Workshop Ciberseguridad", 12);