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

print(f"\n🚶 {nombre} avanza más profundo...\n")

# 🩸 HABITACIÓN 2
print("🩸 Marcas de arrastre cubren el suelo.")
print("👣 Alguien intentó escapar... no lo logró.")

op = elegir(
    "🏚️ HABITACIÓN 2:\n"
    "1) 🔎 SEGUIR LAS MARCAS\n"
    "2) 🧭 BUSCAR OTRA RUTA\n",
    {"1": ["seguir", "1"], "2": ["buscar", "2"]}
)

print("\n🌫️ El pasillo se vuelve más estrecho...\n")

# 🎒 HABITACIÓN 3 (EASTER EGG INICIO)
print("🎒 Encuentras una mochila desgarrada en el suelo...")
print("📛 Dentro hay una placa de identificación rota.")

op = elegir(
    "🏚️ HABITACIÓN 3:\n"
    "1) 📦 REVISAR LA MOCHILA\n"
    "2) ❌ IGNORAR\n"
    "3) 👈 GIRAR A LA IZQUIERDA\n",
    {"1": ["revisar", "1"], "2": ["ignorar", "2"], "3": ["izquierda", "3"]}
)

if op == "op1":
    print("📛 La placa dice: 'Zoey'... cubierta de sangre seca.\n")

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
    {"1": ["tomar", "1"], "2": ["dejar", "2"], "3": ["izquierda", "3"]}
)

if op == "op1":
    print("🔦 Es una linterna rota con el nombre 'Bill' grabado.\n")

if op == "op3":
    izquierda += 1
    print("👣 Pasos inexistentes resuenan detrás de ti...\n")

# 🧪 HABITACIÓN 5
print("🧪 Restos de experimentos cubren las paredes...")

op = elegir(
    "🏚️ HABITACIÓN 5:\n"
    "1) 🔍 INVESTIGAR\n"
    "2) 🚪 SALIR\n"
    "3) 👈 GIRAR A LA IZQUIERDA\n",
    {"1": ["investigar", "1"], "2": ["salir", "2"], "3": ["izquierda", "3"]}
)

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
    {"1": ["entrar", "1"], "2": ["escapar", "2"], "3": ["izquierda", "3"]}
)

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

# 🏆 FINAL NORMAL
print("\n🌅 La luz del exterior finalmente aparece...")
print(f"👤 {nombre}, logras escapar de la mazmorra...")
print("⚠️ Pero algo dentro de ti sabe que no era un lugar normal...")
print("🏁 FIN DEL JUEGO")