# Definition der Variablen
name = "Dominik"

print(name)

# Ändern der Variablen
name = "Peter"

print(name)

# Variablen für die Spieler anlegen
spieler_1 = "Anna"
spieler_2 = "Lena"

# Die Nachricht aus verschiedenen Teilen zusammen bauen
nachricht = "Hallo " + spieler_1 + " und " + spieler_2 + "!"

print(nachricht)

# Definition von zwei Variablen für unsere Zahlen
zahl_1 = 5
zahl_2 = 10

# Plus
ergebnis = zahl_1 + zahl_2

print(ergebnis)

# Minus
ergebnis = zahl_2 - zahl_1

print(ergebnis)

# Mal
ergebnis = zahl_1 * zahl_2

print(ergebnis)

# Geteilt
ergebnis = zahl_2 / zahl_1

print(ergebnis)

# Teilen durch Null
# ergebnis = zahl_1 / 0

# Listen

teilnehmer = ["Peter", "Paul", "Marie"]

print(teilnehmer)

# Wir lesen das zweite Dings aus unerer Liste
print(teilnehmer[1])

# Wir fügen Lena zu unserer Liste der Teilnehmer hinzu
teilnehmer.append("Lena")

print(teilnehmer)

# Wir werfen Paul aus der Liste der Teilnehmer raus
teilnehmer.remove("Paul")

print(teilnehmer)

# Wir werfen Lena aus der Liste der Teilnehmer raus
del teilnehmer[2]

print(teilnehmer)

# Wir ermitteln die Anzahl Teilnehmer in unserer Liste
anzahl_teilnehmer = len(teilnehmer)

print(anzahl_teilnehmer)

# Tupel

# Wir definieren den Tupel mit unseren Freunden
freunde = ('Alex', 'Maximilian', 'Anna', 'Sarah')

print(freunde)

# Wir versuchen Paul aus der Liste zu werfen
# freunde[0] = "Paul"

# Wir ermitteln die Anzahl Freunde in unserem Tupel
anzahl_freunde = len(freunde)

print(anzahl_freunde)

# Wir definieren eine verschachtelte Liste unserer Freunde
adressbuch = [
    ["Anna", "Westermann", 16, "anna.westermann@gmail.com"],
    ["Paul", "Franke", 17, "paul.franke@gmail.com"]
]

# Wir geben den Nachnamen von Anna aus (Anna = index 0 und dann Nachname = index 1)
print(adressbuch[0][1])

# Wir definieren eine Liste von Verzeichnissen
adressbuch = [
    {"vorname": "Anna", "nachname": "Westermann", "alter": 16, "email": "anna.westermann@gmail.com"},
    {"vorname": "Paul", "nachname": "Franke", "alter": 17, "email": "paul.franke@gmail.com"}
]

# Wir machen unsere Liste mit Verzeichnissen etwas leichter lesbar
adressbuch = [
  {
      "vorname": "Anna",
      "nachname": "Westermann",
      "alter": 16,
      "email": "anna.westermann@gmail.com"
  },
  {
      "vorname": "Paul",
      "nachname": "Franke",
      "alter": 17,
      "email": "paul.franke@gmail.com"
  }
]

# Wir geben Annas Nachnamen aus
print(adressbuch[0]["nachname"])

# Wir löschen Pauls Alter
del adressbuch[1]["alter"]

print(adressbuch[1])
