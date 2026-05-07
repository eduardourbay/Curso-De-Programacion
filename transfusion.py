
def convertir_grupo(texto):
    texto = texto.strip().upper()
    if texto in ("A", "B", "AB", "O"):
        return texto
    return None

def convertir_rh(texto):
    texto = texto.strip().upper()
    if texto in ("+", "POS", "POSITIVO", "P"):
        return "+"
    if texto in ("-", "NEG", "NEGATIVO", "N"):
        return "-"
    return None

def es_compatible(donante_grupo, donante_rh, receptor_grupo, receptor_rh):
    # Compatibilidad ABO
    if donante_grupo == "O":
        abo_ok = True
    elif donante_grupo == "A":
        if receptor_grupo == "A" or receptor_grupo == "AB":
            abo_ok = True
        else:
            abo_ok = False
    elif donante_grupo == "B":
        if receptor_grupo == "B" or receptor_grupo == "AB":
            abo_ok = True
        else:
            abo_ok = False
    elif donante_grupo == "AB":
        if receptor_grupo == "AB":
            abo_ok = True
        else:
            abo_ok = False
    else:
        abo_ok = False

    # Compatibilidad Rh
    if donante_rh == "-":
        rh_ok = True
    elif donante_rh == "+":
        if receptor_rh == "+":
            rh_ok = True
        else:
            rh_ok = False
    else:
        rh_ok = False

    return abo_ok and rh_ok

donante_grupo = convertir_grupo(input("Ingrese el grupo sanguíneo del donante (A, B, AB, O): "))
donante_rh = convertir_rh(input("Ingrese el factor Rh del donante (+ o -): "))
receptor_grupo = convertir_grupo(input("Ingrese el grupo sanguíneo del receptor (A, B, AB, O): "))
receptor_rh = convertir_rh(input("Ingrese el factor Rh del receptor (+ o -): "))

if donante_grupo is None or donante_rh is None or receptor_grupo is None or receptor_rh is None:
    print("Entrada no válida. Use grupos A, B, AB, O y factores Rh + o -.")
else:
    if es_compatible(donante_grupo, donante_rh, receptor_grupo, receptor_rh):
        print("La transfusión es compatible.")
    else:
        print("La transfusión NO es compatible.")