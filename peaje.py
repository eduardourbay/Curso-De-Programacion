vehiculo = input("Tipo(carro/moto/gandola)")
hora_pico = input("Es hora pico??(si/no)")

if vehiculo == "carro":
    precio = 5
elif vehiculo == "moto":
    precio = 2
elif vehiculo == "gandola":
    precio = 8
else:
    print("Vehiculo no valido")
    precio = None

if precio is not None:
    if hora_pico == "si":
        precio = precio * 1.2
    print("total a pagar:", precio)