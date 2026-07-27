const precios: number[] = [1.50, 2.50, 3.00, 4.00, 5.00];
const conferencias: Array<string> = ["Keynote", "Workshop", "Panel"];

const inferido = [10, 20, 30];
console.log(`Arreglo Precios:$${precios}`)
console.log(`Arreglo de Conferencias:$${conferencias}`)
console.log(`Arreglo Inferido${inferido}`)
const dobles: number[] = precios.map((n) => n * 2);
const pares: number[] = precios.filter((n) => n % 2 === 0);
const suma: number = precios.reduce((acc, n) => acc + n, 0);
console.log(`Dobles:$${dobles}`)
console.log(`Pares:$${pares}`)
console.log(`Suma:$${suma}`)

precios.push(6.00);
console.log(`Arreglo Precios:$${precios}`)
precios.unshift(0.50);
console.log(`Arreglo Precios:$${precios}`)
const ultimo = precios.pop();
console.log(`Arreglo Precios:$${precios}`)
const primero = precios.shift();
console.log(`Arreglo Precios:$${precios}`)

const existe: boolean = precios.includes(3.00);
console.log(`Existe 3.00:${existe}`)
export const indice: number = precios.indexOf(3.00);
console.log(`Posicion de valor 3.00:${indice}`)
const encontrado: number | undefined = precios.find((n) => n > 4);
console.log(`Valor encontrado mayor a 4: ${encontrado}`)