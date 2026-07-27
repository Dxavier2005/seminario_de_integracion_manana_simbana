const CAPACIDAD_ASISTENTES: number = 250;
const NOMBRE_EVENTO: string = "Conferencia Global de Tecnología";
const INSCRIPCIONES_ABIERTAS: boolean = false;

let asistentesRegistrados: number = 0;
let estadoRegistro: string = "cerrado";
let auditorioDisponible: boolean = false;
asistentesRegistrados++;
estadoRegistro = "abierto";
auditorioDisponible = true;

console.log(`asistentesRegistrados:${asistentesRegistrados}
    estado registro:${estadoRegistro}
    auditorio disponible:${auditorioDisponible}`);