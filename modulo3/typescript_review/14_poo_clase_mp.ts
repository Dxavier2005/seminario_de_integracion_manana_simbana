class Conferencia {
  nombre: string;
  precio: number;
  enStock: boolean;

  constructor(nombre: string, precio: number, enStock: boolean) {
    this.nombre = nombre;
    this.precio = precio;
    this.enStock = enStock;
  }

  describir(): string {
    const estado = this.enStock ? "disponible" : "agotado";
    return `${this.nombre} — $${this.precio} (${estado})`;
  }
}

const keynote = new Conferencia("Keynote Principal", 2.50, true);
const workshop = new Conferencia("Workshop de TypeScript", 3.00, false);

console.log(keynote.describir());
console.log(workshop.describir());