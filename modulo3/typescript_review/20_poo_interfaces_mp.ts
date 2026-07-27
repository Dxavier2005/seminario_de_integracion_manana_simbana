interface Serializable {
  serializar(): string;
}

interface Validable {
  esValido(): boolean;
}

class RegistroConferencia implements Serializable, Validable {
  constructor(
    public id: string,
    public productos: string[],
    public total: number
  ) {}

  serializar(): string {
    return JSON.stringify({ id: this.id, productos: this.productos, total: this.total });
  }

  esValido(): boolean {
    return this.productos.length > 0 && this.total > 0;
  }
}

const registro = new RegistroConferencia("CONF-001", ["Keynote AI", "Workshop TS"], 5.50);
console.log(registro.esValido());
console.log(registro.serializar());