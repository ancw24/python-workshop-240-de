# Eine freundliche Begrüßung


def hallo(name):
    print("Hallo " + name + "!")


hallo("Paul")
# hallo()

# Eine freundliche Begrüßung für jedermann


def hallo_alle(name="Unbekannter"):
    print("Hallo " + name + "!")


hallo_alle()


# Rechnen wir doch mal zusammen

def plus(zahl_1, zahl_2):
    loesung = zahl_1 + zahl_2

    return loesung


ergebnis = plus(5, 10)

print(ergebnis)