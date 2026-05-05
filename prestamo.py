ingresos = float(input("Ingresos:"))
edad = int(input("Edad:"))

if ingresos > 3000 and edad > 25:
    print("prestamo aprobado")
elif ingresos >= 1500 and ingresos <= 3000:
    print("aprovacho con aval")
else:
    print("rechazado papu")