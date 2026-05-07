# Simulador de Compuertas Lógicas
# Este programa pide dos valores booleanos y una compuerta lógica (XOR, NAND, NOR, XNOR)
# e implementa las operaciones usando únicamente 'and', 'or' y 'not'.

def xor(a, b):
    # XOR: Verdadero si exactamente uno es verdadero
    return (a and not b) or (not a and b)

def nand(a, b):
    # NAND: Negación de AND
    return not (a and b)

def nor(a, b):
    # NOR: Negación de OR
    return not (a or b)

def xnor(a, b):
    # XNOR: Verdadero si ambos son iguales
    return (a and b) or (not a and not b)

def main():
    print("Simulador de Compuertas Lógicas")
    print("Ingresa dos valores booleanos (True o False) y una compuerta lógica.")

    # Pedir primer valor booleano
    while True:
        try:
            a_input = input("Ingresa el primer valor booleano (True/False): ").strip().lower()
            if a_input == 'true':
                a = True
                break
            elif a_input == 'false':
                a = False
                break
            else:
                print("Por favor, ingresa 'True' o 'False'.")
        except:
            print("Entrada inválida. Intenta de nuevo.")

    # Pedir segundo valor booleano
    while True:
        try:
            b_input = input("Ingresa el segundo valor booleano (True/False): ").strip().lower()
            if b_input == 'true':
                b = True
                break
            elif b_input == 'false':
                b = False
                break
            else:
                print("Por favor, ingresa 'True' o 'False'.")
        except:
            print("Entrada inválida. Intenta de nuevo.")

    # Pedir la compuerta lógica
    while True:
        gate = input("Ingresa la compuerta lógica (XOR, NAND, NOR, XNOR): ").strip().upper()
        if gate in ['XOR', 'NAND', 'NOR', 'XNOR']:
            break
        else:
            print("Compuerta inválida. Las opciones son: XOR, NAND, NOR, XNOR.")

    # Calcular el resultado
    if gate == 'XOR':
        result = xor(a, b)
    elif gate == 'NAND':
        result = nand(a, b)
    elif gate == 'NOR':
        result = nor(a, b)
    elif gate == 'XNOR':
        result = xnor(a, b)

    # Mostrar el resultado
    print(f"\nValores de entrada: A = {a}, B = {b}")
    print(f"Compuerta: {gate}")
    print(f"Resultado: {result}")

if __name__ == "__main__":
    main()