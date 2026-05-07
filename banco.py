print("=== Sistema de scoring bancario ===")

ingresos = float(input("Ingrese sus ingresos mensuales: "))
deudas = float(input("Ingrese el total de sus deudas: "))
edad = int(input("Ingrese su edad: "))
morosidad = input("¿Tiene morosidad? (si/no): ").strip().lower()

puntaje_base = 10
puntaje_ingresos = 0
puntaje_deudas = 0
puntaje_edad = 0
puntaje_morosidad = 0

if ingresos >= 10000:
    puntaje_ingresos += 7
if ingresos >= 5000:
    puntaje_ingresos += 4
if ingresos < 2000:
    puntaje_ingresos -= 5

if deudas <= 2000:
    puntaje_deudas += 5
if deudas > 5000:
    puntaje_deudas -= 4
if deudas > 10000:
    puntaje_deudas -= 6

if edad < 21:
    puntaje_edad -= 5
if 21 <= edad < 35:
    puntaje_edad += 3
if edad >= 35:
    puntaje_edad += 5

if morosidad == "si":
    puntaje_morosidad -= 10
if morosidad == "no":
    puntaje_morosidad += 3

puntaje_total = (
    puntaje_base
    + puntaje_ingresos
    + puntaje_deudas
    + puntaje_edad
    + puntaje_morosidad
)

print(f"\nPuntaje total: {puntaje_total}")

if puntaje_total >= 15:
    print("Crédito aprobado")
else:
    print("Crédito rechazado")