# Übungsaufgabe 01

# Wir definieren die aktuelle Stunde
stunde = 0

# Bedingung: 0 Uhr ist die Geisterstunde
if stunde == 0:
    print("Es ist Geisterstunde.")
# Bedingung: Alle anderen Stunden sind es nicht
else:
    print("Es ist noch nicht soweit.")

# Übungsaufgabe 02

# Wir definieren den Namen
name = "Dominik"

# Wir definieren die Stunde
stunde = 6

# Wir prüfen ob es Abend ist (18 - 21 Uhr)
if stunde >= 18:
    begruessung = "Guten Abend"
# Wir prüfen ob es Tag ist  (12 - 17 Uhr)
elif stunde >= 12:
    begruessung = "Guten Tag"
# Wir prüfen ob es Morgen ist  (6 - 11 Uhr)
elif stunde >= 6:
    begruessung = "Guten Morgen"
# Alle anderen Zeiten sind Nacht
else:
    begruessung = "Gute Nacht"

print(begruessung + " " + name)

# Übungsaufgabe 03

# Wir definieren die Anzahl Freunde
anzahl_freunde = 2
anzahl_sitzplaetze = 5
taschengeld = 10
eintrittspreis = 2
anzahl_mitfahrer = anzahl_freunde + 1
eintrittspreis_gesamt = anzahl_mitfahrer * eintrittspreis

if anzahl_mitfahrer > anzahl_sitzplaetze:
    print("Das Auto ist leider zu klein.")
elif eintrittspreis_gesamt > taschengeld:
    print("Ich habe leider nicht genug Taschengeld.")
else:
    print("Cool! Wir können in den Trampolinpark fahren!")
