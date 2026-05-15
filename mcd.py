a = int(input("A: "))
b = int(input("B: "))

while b != 0:
    r = a % b
    a = b
    b = r

print(a)