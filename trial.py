def main():
    try:
        num1 = float(input("Ingresa el primer número: "))
        num2 = float(input("Ingresa el segundo número: "))
        op = input("Ingresa la operación (+, -, *, /): ")
        
        if op == '+':
            result = num1 + num2
        elif op == '-':
            result = num1 - num2
        elif op == '*':
            result = num1 * num2
        elif op == '/':
            if num2 == 0:
                print("Error: División por cero")
                return
            result = num1 / num2
        else:
            print("Operación no válida")
            return
        
        print(f"El resultado es: {result}")
    except ValueError:
        print("Por favor ingresa números válidos")

if __name__ == "__main__":
    main()