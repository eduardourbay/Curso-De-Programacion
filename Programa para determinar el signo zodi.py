# Programa para determinar el signo zodiacal
# Solicitar día y mes al usuario
dia = int(input("Ingresa el día (1-31): "))
mes = int(input("Ingresa el mes (1-12): "))

# Validar si la fecha existe
fecha_valida = True

if mes < 1 or mes > 12:
    fecha_valida = False
elif mes == 2:
    if dia < 1 or dia > 28:
        fecha_valida = False
elif mes in [4, 6, 9, 11]:
    if dia < 1 or dia > 30:
        fecha_valida = False
elif mes in [1, 3, 5, 7, 8, 10, 12]:
    if dia < 1 or dia > 31:
        fecha_valida = False

if not fecha_valida:
    print("Fecha inválida.")
else:
    # Determinar el signo zodiacal
    if (mes == 1 and dia >= 20) or (mes == 2 and dia <= 18):
        signo = "Acuario"
    elif (mes == 2 and dia >= 19) or (mes == 3 and dia <= 20):
        signo = "Piscis"
    elif (mes == 3 and dia >= 21) or (mes == 4 and dia <= 19):
        signo = "Aries"
    elif (mes == 4 and dia >= 20) or (mes == 5 and dia <= 20):
        signo = "Tauro"
    elif (mes == 5 and dia >= 21) or (mes == 6 and dia <= 20):
        signo = "Géminis"
    elif (mes == 6 and dia >= 21) or (mes == 7 and dia <= 22):
        signo = "Cáncer"
    elif (mes == 7 and dia >= 23) or (mes == 8 and dia <= 22):
        signo = "Leo"
    elif (mes == 8 and dia >= 23) or (mes == 9 and dia <= 22):
        signo = "Virgo"
    elif (mes == 9 and dia >= 23) or (mes == 10 and dia <= 22):
        signo = "Libra"
    elif (mes == 10 and dia >= 23) or (mes == 11 and dia <= 21):
        signo = "Escorpio"
    elif (mes == 11 and dia >= 22) or (mes == 12 and dia <= 21):
        signo = "Sagitario"
    elif (mes == 12 and dia >= 22) or (mes == 1 and dia <= 19):
        signo = "Capricornio"
    else:
        signo = "Fecha inválida"  # Aunque ya validamos, por si acaso

    print(f"Tu signo zodiacal es: {signo}")