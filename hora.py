# Solicitar la hora en formato HH:MM:SS
hora_str = input("Introduce la hora en formato HH:MM:SS: ")

# Extraer horas, minutos y segundos
HH = int(hora_str[0:2])
MM = int(hora_str[3:5])
SS = int(hora_str[6:8])

# Solicitar la cantidad de segundos a sumar
segundos_a_sumar = int(input("Introduce los segundos a sumar: "))

# Convertir la hora a segundos totales
total_segundos = HH * 3600 + MM * 60 + SS

# Sumar los segundos
total_segundos += segundos_a_sumar

# Calcular la nueva hora en segundos (usando módulo para 24 horas)
nueva_hora_segundos = total_segundos % 86400

# Convertir de vuelta a HH:MM:SS
nueva_HH = nueva_hora_segundos // 3600
nueva_MM = (nueva_hora_segundos % 3600) // 60
nueva_SS = nueva_hora_segundos % 60

# Imprimir la nueva hora en formato 24 horas con dos dígitos
print(f"{nueva_HH:02d}:{nueva_MM:02d}:{nueva_SS:02d}")