type ZonaConferencia = "local" | "nacional" | "internacional";

interface RegistroConferencia {
  descripcion: string;
  pesoKg: number;
  valorDeclarado: number;
  zona: ZonaConferencia;
}

const TARIFAS: Record<ZonaConferencia, number> = {
  local:         1.50,
  nacional:        3.00,
  internacional:   8.00,
};

const SEGURO_PCT = 0.005;

function cotizarConferencia(registro: RegistroConferencia): string {
  const tarifaBase = TARIFAS[registro.zona];
  const costoFlete = tarifaBase * registro.pesoKg;
  const costoSeguro = registro.valorDeclarado * SEGURO_PCT;
  const total = costoFlete + costoSeguro;

  return `
🎟️ Cotización de kit — Conferencia Tech
   Descripción : ${registro.descripcion}
   Peso        : ${registro.pesoKg} kg
   Zona        : ${registro.zona}
   Flete       : $${costoFlete.toFixed(2)}
   Seguro      : $${costoSeguro.toFixed(2)}
   ─────────────────────────
   TOTAL       : $${total.toFixed(2)}
  `.trim();
}

const registro1: RegistroConferencia = {
  descripcion: "Kit Keynote + Libro Oficial",
  pesoKg: 1.2,
  valorDeclarado: 25,
  zona: "nacional",
};

const registro2: RegistroConferencia = {
  descripcion: "Kit Workshop x12",
  pesoKg: 0.8,
  valorDeclarado: 40,
  zona: "internacional",
};

console.log(cotizarConferencia(registro1));
console.log("---");
console.log(cotizarConferencia(registro2));
