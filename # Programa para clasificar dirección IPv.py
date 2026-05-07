# Programa para clasificar dirección IPv4

# Solicitar los 4 octetos
octeto1 = int(input("Ingrese el primer octeto: "))
octeto2 = int(input("Ingrese el segundo octeto: "))
octeto3 = int(input("Ingrese el tercer octeto: "))
octeto4 = int(input("Ingrese el cuarto octeto: "))

# Validar que cada octeto esté entre 0 y 255
if not (0 <= octeto1 <= 255):
    print("El primer octeto no es válido.")
elif not (0 <= octeto2 <= 255):
    print("El segundo octeto no es válido.")
elif not (0 <= octeto3 <= 255):
    print("El tercer octeto no es válido.")
elif not (0 <= octeto4 <= 255):
    print("El cuarto octeto no es válido.")
else:
    # Clasificar según el primer octeto
    if octeto1 <= 126:
        clase = "A"
    elif octeto1 <= 191:
        clase = "B"
    elif octeto1 <= 223:
        clase = "C"
    elif octeto1 <= 239:
        clase = "D"
    else:
        clase = "E"
    
    print(f"La dirección IP {octeto1}.{octeto2}.{octeto3}.{octeto4} pertenece a la clase {clase}.")