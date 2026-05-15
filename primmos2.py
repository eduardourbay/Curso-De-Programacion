N = int(input("Hasta: "))

for n in range(2, N + 1):
    primo = True

    for i in range(2, n):
        if n % i == 0:
            primo = False

    if primo:
        print(n)