import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))
from model.ahorro import * 

def main():
    print("\n📈 CALCULADORA DE AHORRO PROGRAMADO\n")

    valor = input("Ingrese la meta de ahorro: ")
    try:
        meta = float(valor)
    except ValueError:
        print(f"🚨 Error en 'meta': '{valor}' no es un número válido.")
        return

    valor = input("Ingrese el plazo en meses: ")
    try:
        plazo = int(valor)
    except ValueError:
        print(f"🚨 Error en 'plazo': '{valor}' no es un número entero válido.")
        return

    valor = input("Ingrese el monto extra (0 si no aplica): ")
    try:
        extra = float(valor)
    except ValueError:
        print(f"🚨 Error en 'extra': '{valor}' no es un número válido.")
        return

    if extra == 0:
        mes_extra = 1
    else:
        valor = input("Ingrese el mes del aporte extra: ")
        try:
            mes_extra = int(valor)
        except ValueError:
            print(f"🚨 Error en 'mes_extra': '{valor}' no es un número entero válido.")
            return

    
    try:
        ahorro = Ahorro(
            meta=meta,
            plazo=plazo,
            extra=extra,
            mes_extra=mes_extra
        )

        ap = AhorroProgramado()
        cuota = ap.calcular_ahorro(ahorro)

        print("\n✅ RESULTADO")
        print(f"Debes ahorrar mensualmente: ${round(cuota, 2)}")

    except (
        ErrorMetaMayorACero,
        ErrorPlazoMayorACero,
        ErrorAbonoSuperaMeta,
        ErrorMesExtraFueraDelRango
    ) as variableerror:
        print(f"\n🚨 {variableerror}")

    except Exception as e:
        print(f"\n⚠ Error inesperado: {e}")


if __name__ == "__main__":
    main()