# Das Passwort, das der Benutzer eingegeben hat
passwort_eingabe = ""

# Das Passwort, das wir für die Überprüfung brauchen
passwort = "yolo"

if passwort_eingabe == passwort:
    print("Das Passwort ist korrekt!")
else:
    print("Das Passwort stimmt nicht!")

# Ein Kind diskutiert mit jemandem und sagt, abhängig von Alter und Beziehung dann folgendes ...

alter = 60
mama = True

# Wenn der andere älter als 60 ist, wird er ganz bestimmt Recht haben.
if alter > 60:
    print("Du hast Recht.")
# Wenn der andere noch nicht so alt ist, aber die Mama, dann hat sie natürlich auch Recht.
elif mama == True:
    print("Ja Mama.")
# Wenn der andere aber nun weder alt ist, noch die Mama, dann haben wir selbstverständlich Recht.
else:
    print("Das stimmt nicht.")

# Der Freibad-Check

taschengeld = 10
eintritt = 2
geoeffnet = True

if taschengeld >= eintritt and geoeffnet == True:
    print("Cool! Ich kann ins Freibad gehen!")
elif taschengeld < eintritt:
    print("Ich habe leider nicht mehr genug Taschengeld.")
else:
    print("Das Freibad hat leider nicht offen.")

# Der Kino-Check

taschengeld = 1
eintritt = 5
mama_zahlt = True

if taschengeld >= eintritt or mama_zahlt == True:
    print("Cool! Ich kann ins Kino gehen!")
else:
    print("Ich habe leider nicht mehr genug Taschengeld.")

# Der Schul-Check

wochentag = 1  # 1 = Montag, 2 = Dienstag, ... 7 = Sonntag

if not(wochentag == 6) and not(wochentag == 7):
    print("Ich muss zur Schule gehen.")
else:
    print("Es ist Wochenende!")