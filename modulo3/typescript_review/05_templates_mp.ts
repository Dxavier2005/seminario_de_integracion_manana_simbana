const nombre: string = "Carlos";
const rol: string    = "coordinador";
const conferenciasAtendidas: number = 42;

const bienvenida: string = `Bienvenido, ${nombre}. Rol: ${rol}. Conferencias: ${conferenciasAtendidas}.`;
console.log(bienvenida);

export const precio: number = 12.00;
const iva: number    = 0.19;
const total: string  = `Precio con IVA: $${(precio * (1 + iva)).toFixed(2)}`;
console.log(total);


let sucursal: string = "Auditorio Principal Norte";
let estadoLocal: boolean = true;
let ocupacion: number = 85.5;
const reporte: string = `
=== Reporte del evento ===
Sucursal : Auditorio Principal Centro
Estado   : abierto
Ocupación: 90.0%
`;
console.log(reporte);

const reporte2: string = `
=== Reporte del evento ===
Sucursal : ${sucursal}
Estado   : ${estadoLocal ? "Abierto" : "Cerrado"}
Ocupación: ${ocupacion}%
`;
console.log(reporte2);