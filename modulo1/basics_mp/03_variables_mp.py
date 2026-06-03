# Tipos de datos en sistema de gestión de eventos

nombre = "Ana García"   # string (asistente del evento)
edad = 28              # int (edad del participante)
altura = 1.65          # float (dato opcional del registro)
activo = True          # bool (inscrito al evento)
nulo = None            # NoneType (dato no registrado)

print(type(nombre))
print(type(edad))
print(type(altura))
print(type(activo))
print(type(nulo))

# Asignar valores en una sola línea (cupos de eventos)
a, b, c = 12, 13, 14

print(a)
print(b)
print(c)

# Asignar el mismo valor (estado inicial de salas)
a = b = c = 0

print(a)
print(b)
print(c)

# Intercambio de valores (reasignación de cupos)
x, y = 10, 20
print(x, y)
x, y = y, x
print(x, y)

# Convenciones de nombres (gestión de eventos)
nombre_completo = "Rafael Urdaneta"
nombreCompleto = "Rafael Urdaneta"
MAX_REINTENTOS = 3
_variables_interna = "privada"

# Manejo de enteros (estadísticas del evento)
pequeno = 42
negativo = -17
grande = 1_000_000_000_000
enorme = 2 ** 100

print(pequeno)
print(negativo)
print(grande)
print(enorme)

# Bases numéricas (identificación de eventos)
binario = 0b1010
octal = 0o17
hexadecimal = 0xFF

print(binario, octal, hexadecimal)

# Conversión de bases
print(bin(255))
print(oct(255))
print(hex(255))