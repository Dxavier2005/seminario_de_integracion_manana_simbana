class TemperaturaSala {
  valorCelsius: number;
  valorFahrenheit: number;

  constructor(celsius: number, fahrenheit?: number) {
    this.valorCelsius = celsius ?? 0;
    this.valorFahrenheit = fahrenheit ?? 0;
  }

  aFahrenheit(): number {
    return this.valorCelsius * 9 / 5 + 32;
  }

  aCelsius(): void {
    this.valorCelsius = (this.valorFahrenheit - 32) * 5 / 9;
  }

  aKelvin(): number {
    return this.valorCelsius + 273.15;
  }

  describir(): string {
    return (
      `${this.valorCelsius}°C = ` +
      `${this.aFahrenheit()}°F = ` +
      `${this.aKelvin()}K`
    );
  }
}

const salaCalefaccion = new TemperaturaSala(100, 0);
const salaFria = new TemperaturaSala(0, 0);
const convertirACelsius = new TemperaturaSala(0, 50);

console.log(salaCalefaccion.describir());
console.log(salaFria.describir());
console.log(convertirACelsius.aCelsius());