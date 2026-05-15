n = int(input("Número: "))
primo = True

for i in range(2, n):
    if n % i == 0:
        primo = False

if primo and n > 1:
    print("Es primo")
else:
    print("No es primo")
    