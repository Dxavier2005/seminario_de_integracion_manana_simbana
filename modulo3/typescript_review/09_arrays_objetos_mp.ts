type Conferencia = {
  id: number;
  nombre: string;
  precio: number;
  disponible: boolean;
  existencias: number;
};

const agenda: Conferencia[] = [
  { id: 1, nombre: "Keynote de Introducción", precio: 1.50, disponible: true,  existencias: 50 },
  { id: 2, nombre: "Workshop de TypeScript",   precio: 2.50, disponible: true,  existencias: 40 },
  { id: 3, nombre: "Panel de Ciberseguridad",  precio: 2.75, disponible: false, existencias: 10 },
  { id: 4, nombre: "Charla de Inteligencia Artificial", precio: 3.00, disponible: false, existencias: 15 },
  { id: 5, nombre: "Conferencia Magistral Cloud",    precio: 4.50, disponible: true,  existencias: 20 },
  { id: 6, nombre: "Seminario de DevOps",         precio: 2.00, disponible: false, existencias: 8  },
];

const disponibles: Conferencia[] = agenda.filter((c) => c.disponible);
const nombres: string[] = agenda.map((c) => c.nombre);
const masBarato: Conferencia | undefined = agenda.reduce((min, c) =>
  c.precio < min.precio ? c : min
);

console.log(nombres);
console.log(masBarato?.nombre);
console.log(disponibles.length);
console.log(disponibles.map((c) => c.nombre));
console.log(agenda[3]);