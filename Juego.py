def elegir(pregunta, opciones):
    while True:
        op = input(pregunta).lower()

        if op in opciones["1"]:
            return "op1"
        elif op in opciones["2"]:
            return "op2"
        elif "3" in opciones and op in opciones["3"]:
            return "op3"
        else:
            print("❌ Opción no válida. Intenta otra vez.\n")


# 🎭 INICIO
nombre = input("🧍 Escribe tu nombre: ")

print(f"\n👤 {nombre}, despiertas dentro de una mazmorra olvidada...")
print("🌫️ El aire es frío y huele a metal oxidado.")
print("⚠️ Algo te observa desde la oscuridad...\n")

izquierda = 0

# 🔥 HABITACIÓN 1
print("🔥 Una antorcha sigue encendida en la pared...")
print("✋ Pero la mano que la sostenía ya no está.")

op = elegir(
    "🏚️ HABITACIÓN 1:\n"
    "1) 🕯️ TOMAR LA ANTORCHA\n"
    "2) 🚶 IGNORARLA\n",
    {"1": ["tomar", "1"], "2": ["ignorar", "2"]}
)

if op == "op1":
    print("🔥 La antorcha ilumina débilmente tu camino...\n")
else:
    print("🌑 decides avanzar sin luz, avanzas con cautela...\n")
# 🩸 HABITACIÓN 2
print("🩸 Marcas de arrastre cubren el suelo.")
print("👣 Alguien intentó escapar... no lo logró.")

op = elegir(
    "🏚️ HABITACIÓN 2:\n"
    "1) 🔎 SEGUIR LAS MARCAS\n"
    "2) 🧭 BUSCAR OTRA RUTA\n",
    {"1": ["seguir", "1"], "2": ["buscar", "2"]}
)

if op == "op1":
    print("Llegas a un cuerpo sin vida...\n")
else:
    print("No encuentras otra ruta y decides seguir las marcas...\n")

# 🎒 HABITACIÓN 3 (EASTER EGG INICIO)
print("🎒 Encuentras una mochila desgarrada en el suelo...")
print("📛 Dentro hay una placa de identificación rota.")

op = elegir(
    "🏚️ HABITACIÓN 3:\n"
    "1) 📦 REVISAR LA MOCHILA\n"
    "2) ❌ IGNORAR\n"
    "3) 👈 GIRAR A LA IZQUIERDA\n",
    {"1": ["revisar", "1"], "2": ["ignorar", "2"], "3": ["izquierda", "girar", "girar a la izquierda", "3"]}
)

if op == "op1":
    print("📛 La placa dice: 'Zoey'... cubierta de sangre seca.\n")

if op == "op2":
    print("🚶Ignoras la mochila, sientes que pudiste haber encontrado algo importante...\n")

if op == "op3":
    izquierda += 1
    print("👁️ Sientes que algo te observa desde la oscuridad...\n")

print("🚶 Sigues avanzando...\n")

# ☠️ HABITACIÓN 4
print("☠️ Un cuerpo recostado sostiene algo en su mano...")

op = elegir(
    "🏚️ HABITACIÓN 4:\n"
    "1) ✋ TOMAR EL OBJETO\n"
    "2) 🚫 DEJARLO\n"
    "3) 👈 GIRAR A LA IZQUIERDA\n",
    {"1": ["tomar", "1"], "2": ["dejar", "2"], "3": ["izquierda", "girar", "girar a la izquierda", "3"]}
)

if op == "op1":
    print("🔦 Es una linterna rota con el nombre 'Bill' grabado, le quitas las baterías para reemplazar las de tu linterna y ahora tienes mas luz.\n")

if op == "op2":
    print("🚶 No revisas el cuerpo pero al avanzar de sala tu linterna se queda sin energía y comienzas a caminar con cautela debido a la falta de luz que te guíe...\n")

if op == "op3":
    izquierda += 1
    print("👣 Pasos inexistentes resuenan detrás de ti, sientes que algo te observa y al cambiar de sala te quedas sin energía en la linterna y caminas con cautela ...\n")

# 🧪 HABITACIÓN 5
print("🧪 Restos de experimentos cubren las paredes...")

op = elegir(
    "🏚️ HABITACIÓN 5:\n"
    "1) 🔍 INVESTIGAR\n"
    "2) 🚪 SALIR\n"
    "3) 👈 GIRAR A LA IZQUIERDA\n",
    {"1": ["investigar", "1"], "2": ["salir", "2"], "3": ["izquierda", "girar", "girar a la izquierda", "3"]}
)
if op == "op1":
    print("🔬 Al investigar, encuentras un frasco con una etiqueta que dice 'Billis Boomer'... el líquido dentro burbujea inquietantemente.\n")
     
if op == "op2":
    print("🚶 Decides salir de la habitación, pero te encuentras con una habitación sin salida y decides regresar e investigar...\n")
    print("🔬 Al investigar, encuentras un frasco con una etiqueta que dice 'Billis de Boomer'... el líquido dentro burbujea inquietantemente.\n")

if op == "op3":
    izquierda += 1
    print("⚠️ La realidad parece romperse...\n")

# 🚪 HABITACIÓN 6
print("🚪 Una puerta final respira frente a ti...")

op = elegir(
    "🏚️ HABITACIÓN 6:\n"
    "1) 🚪 ENTRAR\n"
    "2) 🏃 ESCAPAR\n"
    "3) 👈 GIRAR A LA IZQUIERDA\n",
    {"1": ["entrar", "1"], "2": ["escapar", "2"], "3": ["izquierda", "girar", "girar a la izquierda", "3"]}
)
if op == "op1":
    print("🚪 La puerta se abre lentamente, revelando un pasillo iluminado por la luz del sol... pero algo no se siente bien...\n")

if op == "op2":
    print("🏃 Intentas escapar por la puerta, pero te encuentras con un muro invisible que te detiene... algo te impide salir...\n")

if op == "op3":
    izquierda += 1

# 💀 EASTER EGG FINAL
if izquierda >= 4:
    print("\n💀 ...el aire se detiene completamente...")
    print("🧱 Las paredes parecen respirar...")
    print("🔊 Un sonido metálico se arrastra detrás de ti...")
    print("⛏️ LA PALA TE HA ALCANZADO 💀")
    print("🎮 FINAL: LEFT 4 DEAD")
    exit()

# ☠️ FINAL MALO
if op == "op2":
    print("\n🚶 Corres desesperadamente buscando una salida tras ignorar la puerta e intentar escapar...\n")
    print("🧱 Pero de pronto chocas contra algo invisble que te impide avanzar")
    print("✖️ Un muro bloquea completamente el paso y te impide continuar")
    print("Intentas golpearlo... no tiene alguna reacción... no puedes avanzar ni retroceder...")
    print("👁️ Sientes que algo se acerca lentamente hacía tí")
    print("💀 FINAL MALO: QUEDAS ATRAPADO EN LA MAZMORRA Y QUEDAS SIN ESCAPATORIA")
    exit()

# 🏆 FINAL NORMAL
print("\n🌅 La luz del exterior finalmente aparece...")
print(f"👤 {nombre}, logras escapar de la mazmorra...")
print("⚠️ Pero algo dentro de ti sabe que no era un lugar normal...")
print("🏁 FIN DEL JUEGO")