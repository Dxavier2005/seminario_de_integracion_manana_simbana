abstract class ItemConferencia {
  abstract precio(): number;
  abstract descripcion(): string;

  presentar(): string {
    return (
      `${this.descripcion()} | ` +
      `Precio: $${this.precio().toFixed(2)}`
    );
  }
}

class Keynote extends ItemConferencia {
  constructor(private nombre: string, private costo: number) {
    super();
  }

  override precio(): number {
    return this.costo;
  }

  override descripcion(): string {
    return `Keynote: ${this.nombre}`;
  }
}

class Workshop extends ItemConferencia {
  constructor(private nombre: string, private costo: number) {
    super();
  }

  override precio(): number {
    return this.costo;
  }

  override descripcion(): string {
    return `Workshop: ${this.nombre}`;
  }
}

const keynote = new Keynote("Inteligencia Artificial", 2.50);
const workshop = new Workshop("Desarrollo en TypeScript", 4.50);

console.log(keynote.presentar());
console.log(workshop.presentar());