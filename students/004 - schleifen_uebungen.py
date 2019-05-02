# Übungsaufgabe 01

# Wir setzen den Startwert unseres Zähles
zaehler = 5

# Bedingung: Zähler größer oder gleich 1
while zaehler >= 1:
    print(zaehler)

    # Anpassen der Werte für unsere Abbruch-Bedingung, damit wir keine Endlosschleife haben
    zaehler = zaehler - 1

# Übungsaufgabe 02

# Wir definieren unsere Farben
farben = ["Rot", "Grün", "Blau"]

# Wir geben die Farben nacheinander aus
for farbe in farben:
    print(farbe)
