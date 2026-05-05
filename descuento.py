categoria = input("Categoria")
cantidad = int(input("cantidad"))
precio = float(input("precio unitario"))

total = cantidad * precio

if categoria == "electronica" and cantidad >= 3:
    descuento = total * 0.10
elif categoria == "ropa" and cantidad >= 5:
    descuento = total * 0.15
else:
    descuento = 0

total_final = total - descuento
print("descuento", descuento)
print("total a pagar", total_final)