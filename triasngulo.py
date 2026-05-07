# Programa para clasificar un triángulo basado en sus lados

# Pedir los tres lados del triángulo
a = float(input("Ingresa el primer lado: "))
b = float(input("Ingresa el segundo lado: "))
c = float(input("Ingresa el tercer lado: "))

# Verificar si forman un triángulo válido usando la desigualdad triangular
if a + b > c and a + c > b and b + c > a:
    # Verificar si es rectángulo
    if (a ** 2 + b ** 2 == c ** 2) or (a ** 2 + c ** 2 == b ** 2) or (b ** 2 + c ** 2 == a ** 2):
        print("Es un triángulo rectángulo.")
    else:
        # Verificar si es acutángulo
        if (a ** 2 + b ** 2 > c ** 2) and (a ** 2 + c ** 2 > b ** 2) and (b ** 2 + c ** 2 > a ** 2):
            print("Es un triángulo acutángulo.")
        else:
            print("Es un triángulo obtusángulo.")
else:
    print("Los lados no forman un triángulo válido.")