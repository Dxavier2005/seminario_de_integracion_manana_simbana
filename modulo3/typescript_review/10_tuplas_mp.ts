type CoordenadaAsiento = [number, number];
type RGB = [number, number, number];
type Entrada = [string, number];

const ubicacionAsiento: CoordenadaAsiento = [2, 4];
const colorLogo: RGB = [255, 128, 0];
const par: Entrada = ["temperaturaSala", 65.5];

const [fila, columna] = ubicacionAsiento;
const [rojo, verde, azul] = colorLogo;
const [clave, valor] = par;

console.log(`Asiento: fila=${fila}, columna=${columna}`);
console.log(`Color logo: rgb(${rojo},${verde},${azul})`);

type Rango = [inicio: number, fin: number];
const horario: Rango = [8, 20];