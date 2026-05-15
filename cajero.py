pin_correcto = 2007
intentos = 0
acceso = False
saldo = 1000

while intentos < 3:
    pin = int(input("Ingresa PIN: "))

    if pin == pin_correcto:
        acceso = True
        break
    else:
        intentos += 1

if not acceso:
    print("Bloqueado")
else:

    while True:
        print("\n1. Consultar saldo")
        print("2. Depositar")
        print("3. Retirar")
        print("4. Salir")

        opcion = int(input("Opción: "))

        if opcion == 1:
            print("Saldo:", saldo)

        elif opcion == 2:
            deposito = int(input("Monto a depositar: "))
            saldo += deposito
            print("Nuevo saldo:", saldo)

        elif opcion == 3:
            monto = int(input("Monto a retirar: "))

            if monto > saldo or monto % 10 != 0:
                print("No válido")
            else:
                saldo -= monto

                b100 = monto // 100
                monto = monto % 100

                b50 = monto // 50
                monto = monto % 50

                b20 = monto // 20
                monto = monto % 20

                b10 = monto // 10

                print("Billetes:")
                print("100:", b100)
                print("50:", b50)
                print("20:", b20)
                print("10:", b10)

        elif opcion == 4:
            break