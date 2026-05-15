matriz = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

suma = 0

for fila in matriz:
    for num in fila:
        suma += num

print(suma)