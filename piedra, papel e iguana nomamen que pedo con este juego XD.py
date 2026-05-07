choices = ("piedra", "papel", "tijeras", "lagarto", "spock")


def pedir_eleccion(jugador):
    while True:
        eleccion = input(f"Jugador {jugador}, elige ({', '.join(choices)}): ").strip().lower()
        if eleccion in choices:
            return eleccion
        print("Opción inválida. Intenta de nuevo.")


def gana_jugador(player, rival):
    return (
        (player == "tijeras" and (rival == "papel" or rival == "lagarto")) or
        (player == "papel" and (rival == "piedra" or rival == "spock")) or
        (player == "piedra" and (rival == "tijeras" or rival == "lagarto")) or
        (player == "lagarto" and (rival == "spock" or rival == "papel")) or
        (player == "spock" and (rival == "tijeras" or rival == "piedra"))
    )


def main():
    print("Piedra, papel, tijeras, lagarto, Spock")
    jugador1 = pedir_eleccion(1)
    jugador2 = pedir_eleccion(2)

    print(f"Jugador 1: {jugador1} | Jugador 2: {jugador2}")

    if jugador1 == jugador2:
        print("Empate.")
    elif gana_jugador(jugador1, jugador2):
        print("Gana Jugador 1.")
    else:
        print("Gana Jugador 2.")


if __name__ == "__main__":
    main()