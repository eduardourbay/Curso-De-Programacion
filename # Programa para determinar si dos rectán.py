# Programa para determinar si dos rectángulos se superponen en un plano 2D

# Pedir coordenadas del primer rectángulo
print("Ingrese las coordenadas del primer rectángulo:")
x1_1 = float(input("x1 (inferior izquierda): "))
y1_1 = float(input("y1 (inferior izquierda): "))
x2_1 = float(input("x2 (superior derecha): "))
y2_1 = float(input("y2 (superior derecha): "))

# Pedir coordenadas del segundo rectángulo
print("\nIngrese las coordenadas del segundo rectángulo:")
x1_2 = float(input("x1 (inferior izquierda): "))
y1_2 = float(input("y1 (inferior izquierda): "))
x2_2 = float(input("x2 (superior derecha): "))
y2_2 = float(input("y2 (superior derecha): "))

# Verificar si los rectángulos NO se superponen
no_superpone = (x2_1 < x1_2) or (x1_1 > x2_2) or (y2_1 < y1_2) or (y1_1 > y2_2)

# Si no_superpone es False, entonces se superponen
if not no_superpone:
    print("\nLos rectángulos se superponen o chocan.")
else:
    print("\nLos rectángulos no se superponen.")