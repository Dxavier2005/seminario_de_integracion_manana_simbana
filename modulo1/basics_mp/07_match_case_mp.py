print("match case")
comando = input("Comando proceso iniciar/parar/reiniciar: ")

match comando:
    case "iniciar":
        print("Proceso de evento iniciado.")
    case "parar":
        print("Proceso detenido.")
    case "reiniciar":
        print("Sistema de eventos reiniciado.")
    case _:
        print(f"Comando {comando} no encontrado.")

print("match condicionales")
numero = 7

match numero:
    case n if n < 0:
        print(f"{n} es negativo")
    case 0:
        print("Es cero")
    case n if n % 2 == 0:
        print(f"{n} es par")
    case n:
        print(f"{n} es positivo e impar")