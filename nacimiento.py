fecha = int(input("ingresa año de nacimiento"))

if fecha >= 1946 and fecha <= 1964:
    print(">eres baby boomer")
elif fecha >= 1965 and fecha <= 1980:
    print("eres generacion x")
elif fecha >= 1981 and fecha <= 1996:
    print("eres milenial")
elif fecha >= 1999 and fecha <= 2012:
    print("eres generacion z")
else:
    print("no eres valido acá weon")
