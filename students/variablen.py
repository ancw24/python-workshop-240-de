name = "Dominik"

print(name)

name = "Peter"

print(name)

spieler_1 = "Dominik"
spieler_2 = 'Peter'

nachricht = "Hallo " + spieler_1 + " und " + spieler_2 + "!"

print(nachricht)

zahl_1 = 5
zahl_2 = 10

# Plus
ergebnis_1 = zahl_1 + zahl_2

print(ergebnis_1)

# Minus
ergebnis_2 = zahl_1 - zahl_2

print(ergebnis_2)

# Mal
ergebnis_3 = zahl_1 * zahl_2

print(ergebnis_3)

# Geteilt
ergebnis_4 = zahl_2 / zahl_1

print(ergebnis_4)

# Teilen durch Null
# ergebnis_5 = zahl_1 / 0

# print(ergebnis_5)

# Listen

teilnehmer = ["Peter", "Paul", "Marie"]

print(teilnehmer)
print(teilnehmer[1])

teilnehmer.append("Lena")

print(teilnehmer)

teilnehmer.remove("Paul")

print(teilnehmer)

del teilnehmer[2]

print(teilnehmer)

student_count = len(teilnehmer)

print(student_count)

# Tupel

freunde = ('Alex', 'Maximilian', 'Anna', 'Sarah')

print(freunde)

# freunde[0] = "Paul"

anzahl_freunde = len(freunde)

print(anzahl_freunde)

adressbuch = [
    ["Anna", "Westermann", 16, "anna.westermann@gmail.com"],
    ["Paul", "Franke", 17, "paul.franke@gmail.com"]
]

print(adressbuch[0][1])

adressbuch = [
    {"firstname": "Anna", "lastname": "Westermann", "age": 16, "email": "anna.westermann@gmail.com"},
    {"firstname": "Paul", "lastname": "Franke", "age": 17, "email": "paul.franke@gmail.com"}
]

print(adressbuch[0]["firstname"])

del adressbuch[1]["age"]

print(adressbuch[1])
