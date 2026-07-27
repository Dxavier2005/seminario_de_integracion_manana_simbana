class CuentaAsistente {
  readonly id: string;
  public titular: string;
  private saldo: number;
  protected moneda: string;

  constructor(id: string, titular: string, saldoInicial: number) {
    this.id = id;
    this.titular = titular;
    this.saldo = saldoInicial;
    this.moneda = "USD";
  }

  obtenerSaldo(): number {
    return this.saldo;
  }

  recargar(monto: number): void {
    if (monto <= 0) throw new Error("Monto inválido");
    this.saldo += monto;
  }
}

const cuenta = new CuentaAsistente("CONF-001", "Carlos García", 20);
console.log(cuenta.titular);
console.log(cuenta.id);
console.log(cuenta.obtenerSaldo());
cuenta.recargar(10);
console.log(cuenta.obtenerSaldo());