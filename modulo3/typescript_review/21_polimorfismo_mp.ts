class ItemConferencia {
  nombre(): string { return "Item"; }
  precio(): number { return 0; }
}

class KeynoteCarta extends ItemConferencia {
  constructor(private costo: number) { super(); }
  override nombre(): string { return "Keynote"; }
  override precio(): number { return this.costo; }
}

class WorkshopCarta extends ItemConferencia {
  constructor(private costo: number) { super(); }
  override nombre(): string { return "Workshop"; }
  override precio(): number { return this.costo; }
}

class ComboCarta extends ItemConferencia {
  constructor(private costo: number) { super(); }
  override nombre(): string { return "Combo"; }
  override precio(): number { return this.costo; }
}

const carta: ItemConferencia[] = [
  new KeynoteCarta(2.50),
  new WorkshopCarta(4.00),
  new ComboCarta(6.50),
];

for (const item of carta) {
  console.log(`${item.nombre()}: precio = $${item.precio().toFixed(2)}`);
}