enum ZonaConferencia {
  AuditorioPrincipal,
  SalaTalleres,
  Plenaria,
  VIP,
}

const zona: ZonaConferencia = ZonaConferencia.AuditorioPrincipal;
console.log(zona);
console.log(ZonaConferencia[0]);

enum CodigoRegistro {
  Recibido = 200,
  NoEncontrado = 404,
  ErrorSistema = 500,
}

enum RolOrganizador {
  Admin    = "ADMIN",
  Ponente  = "PONENTE",
  Asistente = "ASISTENTE",
}

const miRol: RolOrganizador = RolOrganizador.Ponente;
console.log(miRol);