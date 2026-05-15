x = int(input("escriba un numero"))
numero = x
resultado = 1
for i in range(1, numero + 1):
    resultado *= i
    print(resultado)
print(f"El factorial de {numero} es {resultado}")

