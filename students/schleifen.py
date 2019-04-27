# Zählen von 1 bis 5

# Wir setzen den Startwert unseres Zähles
zaehler = 1

# Bedingung: Zähler kleiner oder gleich 5
while zaehler <= 5:
    print(zaehler)

    # Anpassen der Werte für unsere Abbruch-Bedingung, damit wir keine Endlosschleife haben
    zaehler = zaehler + 1

# Meine Freunde

freunde = ["Peter", "Paul", "Anna", "Lena"]

for freund in freunde:
    print(freund)

# Zählen wir nochmal

for zahl in range(1, 5):
    print(zahl)

# Was wir über Anna wissen

anna = {
    "vorname": "Anna",
    "nachname": "Westermann",
    "alter": 16,
    "email": "anna.westermann@gmail.com"
}

# Geben wir das doch mal alles der Reihe nach aus

for (schluessel, wert) in anna.items():
    # print(schluessel + ": " + str(wert))
    print(schluessel.title() + ": " + str(wert))
