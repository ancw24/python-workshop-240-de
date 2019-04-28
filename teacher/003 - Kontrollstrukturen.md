# Kontrollstrukturen

Wir erstellen eine Datei "kontrollstrukturen.py".

## IF - ELSE

1. Nachdem wir die Grundlagen von Variablen und Datentypen gelernt haben, möchten wir auch verschiedene Bedingungen in unserem Code verarbeiten können. Dafür benötigen wir die sogenannten Kontrollstrukturen und starten mit einem einfachen `if - else`.
1. Ein einfaches Beispiel ist die Prüfung ob ein eingegebenes Kennwort richtig ist.
   ```python
   # Das Passwort, das der Benutzer eingegeben hat
   passwort_eingabe = ""

   # Das Passwort, das wir für die Überprüfung brauchen
   passwort = "yolo"

   if passwort_eingabe == passwort:
       print("Das Passwort ist korrekt!")
   else:
       print("Das Passwort stimmt nicht!")
   ```
1. Da ist jetzt schon eine ganze Menge Neues dabei. Das Wort `if` (= wenn) sagt Python dass wir eine Bedingung prüfen möchten. Darauf folgt dann eine `Bedingung`, bei der wir sagen dass das eingegebene Passwort mit dem gespeicherten übereinstimmen muss.
1. In der Bedingung entdecken wir zwei Gleichheitszeichen als Operator und die haben eine wichtige Bedeutung. Welche das ist sehen wir später in einer kleinen Auflistung der wichtigsten, Vergleichs-Operatoren die wir wohl am häufigsten brauchen werden.
1. Bei Bedingungen kommt immer ein Warheitswert heraus, vom Typ `Boolean`, der nur 2 Werte haben kann: `True` (= wahr) und `False` (= unwahr).
1. Wenn wir es übersetzen bedeutet der Code unserer IF-Bedingung also:
   ```
   wenn {passwort_eingabe} genau gleich {passwort}
   ```
1. Mit dem darauf folgenden Doppelpunkt sagen wir Python dass alles was danach eingerückt kommt (dabei muss man auf die genaue Anzahl Zeichen zum Einrücken achten), ausgeführt werden soll wenn unsere Bedingung wahr ist.
   ```
   wenn {passwort_eingabe} genau gleich {passwort}
       dann mache alles was eingerückt steht
   ```
1. Da wir auch etwas ausgeben möchten, wenn unsere Bedingung nicht wahr ist, fügen wir den `else`-Teil hinzu. Alles was eingerückt nach `else` kommt wird immer dann ausgeführt, wenn die Bedingung von unserem `if` **nicht** wahr ist.
1. Wenn wir zum Testen den Wert von `passwort_eingabe` mal auf den gleichen Wert setzen wie den von `passwort`, sollten wir die Meldung sehen `Das Passwort ist korrekt!`.
   ```python
   passwort_eingabe = "yolo"
   ```

## Vergleichsoperatoren

1. Lasst uns nun, wie angekündigt, einen kurzen Blick auf die am meisten verwendeten Vergleichsoperatoren werfen.
   
   Zur Erinnerung:  
   Ein Operator ist ein bestimmtes Zeichen dass einen Wert veränderen oder vergleichen kann.
   
   ```python
   # Ist genau gleich
   genau_gleich = passwort_eingabe == passwort
   
   # Ist nicht genau gleich
   nicht_gleich = passwort_eingabe != passwort
   
   # Ist größer als
   zahl = 10
   groesser_als = zahl > 5
   
   # Ist größer als oder genauso groß
   groesser_oder_gleich = zahl >= 10
   
   # Ist kleiner als
   kleiner_als = zahl < 10
   
   # Ist kleiner als oder genauso groß
   kleiner_oder_gleich = zahl <= 10
   ```

## IF - ELIF - ELSE

1. Manchmal möchte man verschiedene Bedingungen nacheinander prüfen. Dafür gib es z.B. das `elif`, das wir im folgenden Beispiel kennen lernen.

   ```python
   # Wir diskutieren mit jemandem und abhängig von ein paar Bedingungen sagen wir ...
   
   alter = 60
   mama = True
   
   # Wenn der / die andere älter als 60 ist, wird er ganz bestimmt Recht haben.
   if alter > 60:
       print("Du hast Recht.")
   # Wenn der / die andere noch nicht so alt ist, aber die Mama, dann hat sie natürlich auch Recht.
   elif mama == True:
       print("Ja Mama.")
   # Wenn der / die andere aber nun weder alt ist, noch die Mama, dann haben wir selbstverständlich Recht.
   else:
       print("Das stimmt nicht.")
   ``` 
   
   Die Bedingung im `elif` wird nur geprüft, wenn die Bedingung im `if` nicht schon wahr ist.  
   Die Bedingung im `else` wird immer dann geprüft wenn gar keine vorige Bedingung wahr ist.

## Logische Operatoren

1. Wenn wir mehrere Bedingungen gleichzeitig prüfen wollen, brauchen wir logische Operatoren. Das sind `and` (= und), `or` (= oder) und `not` (= nicht).
1. Prüfen wir doch mal ob wir noch genug Taschengeld für den Eintritt haben und ob das Freibad geöffnet hat.
   ```python
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
   ```
1. Spielen wir doch mal ein Bisschen mit den Werten herum, um zu sehen wie sich unsere Bedingungen verhalten. Ändern wir also mal das Taschengeld und mal den Wert ob das Freibad geöffnet hat.
1. Danach können wir uns den zweiten logischen Operator anschauen, das `or`.
1. Prüfen wir doch mal ob wir noch genug Taschengeld fürs Kino haben oder ob Mama bezahlt.
   ```python
   # Der Kino-Check

   taschengeld = 1
   eintritt = 5
   mama_zahlt = True

   if taschengeld >= eintritt or mama_zahlt == True:
       print("Cool! Ich kann ins Kino gehen!")
   else:
       print("Ich habe leider nicht mehr genug Taschengeld.")
   ```
1. Als letzten logischen Operator schauen wir uns `not` an. `not` brauchen wir, wenn wir prüfen wollen ob eine Bedingung nicht wahr ist.
1. Prüfen wir doch mal, ob wir zur Schule gehen müssen.
   ```python
   # Der Schul-Check
   
   wochentag = 1  # 1 = Montag, 2 = Dienstag, ... 7 = Sonntag
   
   if not(wochentag == 6) and not(wochentag == 7):
       print("Ich muss zur Schule gehen.")
   else:
       print("Es ist Wochenende!")
   ```

---

&gt; [4. Schleifen](./004%20-%20Schleifen.md)
  
&lt; [2. Variablen, Typen und Operatoren](./002%20-%20Variablen,%20Typen%20und%20Operatoren.md)