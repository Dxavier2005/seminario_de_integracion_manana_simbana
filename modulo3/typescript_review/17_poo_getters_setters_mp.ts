class GafeteAsistente {
  private _capacidadMl: number;

  constructor(capacidadMl: number) {
    this._capacidadMl = capacidadMl;
  }

  get capacidadMl(): number {
    return this._capacidadMl;
  }

  set capacidadMl(valor: number) {
    if (valor <= 0) throw new Error("La capacidad debe ser positiva");
    this._capacidadMl = valor;
  }

  get precioEstimado(): number {
    return this._capacidadMl * 0.02;
  }
}

const gafete = new GafeteAsistente(250);
console.log(gafete.capacidadMl);
console.log(gafete.precioEstimado.toFixed(2));

gafete.capacidadMl = 350;
console.log(gafete.precioEstimado.toFixed(2));