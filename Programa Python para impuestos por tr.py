## Programa Python para impuestos por tramos
def calcular_impuesto(ingreso):
    impuesto = 0.0

    if ingreso > 60000:
        tramo = ingreso - 60000
        impuesto += tramo * 0.35
        ingreso = 60000

    if ingreso > 30000:
        tramo = ingreso - 30000
        impuesto += tramo * 0.25
        ingreso = 30000

    if ingreso > 10000:
        tramo = ingreso - 10000
        impuesto += tramo * 0.15
        ingreso = 10000

    return impuesto

def main():
    try:
        ingreso = float(input("Ingresa tu ingreso anual: ").strip())
    except ValueError:
        print("Valor inválido.")
        return

    if ingreso < 0:
        print("El ingreso no puede ser negativo.")
        return

    total_impuesto = calcular_impuesto(ingreso)
    print(f"Impuesto a pagar: ${total_impuesto:,.2f}")

if __name__ == "__main__":
    main()