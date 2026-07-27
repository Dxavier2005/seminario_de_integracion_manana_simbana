const precioEntrada: number      = 2.50;
const numeroAsiento: number      = 12;
const temperaturaSala: number = -5.3;
const colorConferencia: number    = 0xff5733;

const emailAsistente: string    = "asistente@conferencias.com";
const metodoPago: string = 'EFECTIVO';
const rutaRegistro: string     = `/registro/v2/ponentes`;

const eventoAbierto: boolean  = true;
const requiereInvitacion: boolean = false;
const esPonenteVip: boolean      = false;

const subtotal = 15.00;
const descuento = 1.50;
const total = subtotal - descuento;

const asistente = "  carlos@conferencias.com  ";
console.log(asistente.trim().toLowerCase());
console.log(emailAsistente.includes("conferencias"));
console.log(emailAsistente.split("@"));
console.log(emailAsistente.split("@")[1]);
let datosRegistro: string = "Keynote;Auditorio A;2;12-12-2026";
console.log(datosRegistro.split(";"));
const puedeIngresar: boolean = eventoAbierto && !requiereInvitacion;
console.log(puedeIngresar);