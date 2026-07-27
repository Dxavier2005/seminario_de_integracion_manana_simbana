const entero: number = 42;
const decimal: number = 3.14;
const negativo: number = -100;
const hexadecimal: number = 0xff;
const binario: number = 0b1010;
const octal: number = 0o17;
const grande: number = 1_000_000;

console.log(hexadecimal);
console.log(binario);
console.log(grande);

console.log(Number.MAX_SAFE_INTEGER);
console.log(Number.isFinite(1 / 0));
console.log(Number.isNaN(0 / 0));


const simple: string = "Bienvenido a la Conferencia";
const doble: string = 'También funciona';
const template: string = `Hola ${"asistente"}`;

const nombre: string = "Carlos";
const edad: number = 28;

export const saludo: string = `Hola, ${nombre}. Tienes ${edad} años. Bienvenido a la Conferencia.`;
const mayoria: string = `Eres ${edad >= 18 ? "mayor" : "menor"} de edad.`;

const mensaje: string = `
  Asiento 5
  Keynote Inteligencia Artificial
  Workshop Ciberseguridad
`.trim();

console.log("  ponente  ".trim());
console.log("keynote".toUpperCase());
console.log("KEYNOTE".toLowerCase());
console.log("2026-06-15".split("-"));
console.log("error: cupo lleno".includes("error"));
console.log("registro.ts".startsWith(".ts"));

const abierto: boolean = true;
const cerrado: boolean = false;

const esMayor = 25 >= 18;
const tieneCupos = 0 > 0;

if (!tieneCupos) {
  console.log("Sin cupos disponibles para la conferencia");
}

let sinAsignar: undefined = undefined;
let sinValor: null = null;

function buscarAsistente(id: number): string | null {
  if (id === 1) return "Carlos";
  return null;
}

const asistente = buscarAsistente(5);

const nombreAsistente = asistente ?? "Invitado";
console.log(nombreAsistente);

const longitud = asistente?.length;
console.log(longitud);