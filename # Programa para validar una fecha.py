# Programa para validar una fecha
try:
    dia = int(input("Ingrese el día: "))
    mes = int(input("Ingrese el mes: "))
    anio = int(input("Ingrese el año: "))

    # Validar mes
    if mes < 1 or mes > 12:
        print("Fecha inválida: mes fuera de rango")
    else:
        # Validar días según el mes
        if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
            if dia < 1 or dia > 31:
                print("Fecha inválida: día fuera de rango para este mes")
            else:
                print("Fecha válida")
        elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
            if dia < 1 or dia > 30:
                print("Fecha inválida: día fuera de rango para este mes")
            else:
                print("Fecha válida")
        elif mes == 2:
            # Verificar si es año bisiesto
            if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
                if dia < 1 or dia > 29:
                    print("Fecha inválida: día fuera de rango para febrero en año bisiesto")
                else:
                    print("Fecha válida")
            else:
                if dia < 1 or dia > 28:
                    print("Fecha inválida: día fuera de rango para febrero")
                else:
                    print("Fecha válida")
except ValueError:
    print("Error: Debe ingresar números enteros válidos para día, mes y año.")