class Empleado {
  constructor(public nombre: string) {}

  saludar(): string {
    return `${this.nombre} saluda al asistente.`;
  }
}

class Ponente extends Empleado {
  constructor(nombre: string, public zona: string) {
    super(nombre);
  }

  override saludar(): string {
    return `${this.nombre} presenta en la sala ${this.zona}: ¡Bienvenidos a la Conferencia!`;
  }

  tomarPedido(plato: string): string {
    return `${this.nombre} responde la pregunta: ${plato}.`;
  }
}

const e = new Empleado("Trabajador");
const m = new Ponente("Luis", "Auditorio A");

console.log(e.saludar());
console.log(m.saludar());
console.log(m.tomarPedido("Inteligencia Artificial"));
console.log(m.zona);