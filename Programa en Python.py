## Programa en Python


def permisos_desde_numero(valor):
    if not (0 <= valor <= 7):
        raise ValueError("El número debe estar entre 0 y 7")
    lectura = bool(valor & 4)
    escritura = bool(valor & 2)
    ejecucion = bool(valor & 1)
    return lectura, escritura, ejecucion

def main():
    try:
        n = int(input("Introduce un número entre 0 y 7: "))
        lectura, escritura, ejecucion = permisos_desde_numero(n)
    except ValueError as e:
        print("Error:", e)
        return

    print(f"Permisos para {n}:")
    print("Lectura:   ", "Sí" if lectura else "No")
    print("Escritura: ", "Sí" if escritura else "No")
    print("Ejecución: ", "Sí" if ejecucion else "No")

if __name__ == "__main__":
    main()