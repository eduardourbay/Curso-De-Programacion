temperatura = int(input("ingrese la temperatura: "))

if temperatura <= 0:
    print("Solido")

elif temperatura >= 1 and temperatura <= 99:
    print("Liquido")

else:
    print("Gaseoso")