import math
import random

contador = 1
while contador <= 3:
    angulo = random.randint(0, 90)
    radianes = math.radians(angulo)
    coseno = math.cos(radianes)
    print("Angulo:", angulo)
    print("Coseno:", coseno)
    print("Radianes:", radianes)

    contador += 1