x = input("escribe una palabra:")

vocales = "aeiouAEIOU"
contador_vocales = 0
for letra in x:
    if letra in vocales:
        contador_vocales += 1
print(f"El número de vocales en '{x}' es: {contador_vocales}")