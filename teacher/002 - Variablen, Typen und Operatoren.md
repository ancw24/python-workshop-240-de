# Variablen, Typen und Operatoren

Wir erstellen eine Datei "variablen.py".

## Variablen

1. Als erstes fragen wir uns natürlich: "Was ist eine Variable?"
1. Variablen benutzt man um bestimmte Informationen zu speichern und später wieder auszulesen oder verändern zu können.
1. Schauen wir uns das doch mal an einem einfachen Beispiel an, damit es "sichtbar" wird. Wir definieren (= Erstellen) unsere erste Variable.
   ```python
   # Definition der Variablen
   name = "Dominik"
   ```
1. Wenn wir diesen Code ausführen, wird der Wert `Dominik` in der Variablen `name` gespeichert. Python kennt nun also meinen Namen. Das ist ja schon mal was.
1. Wichtig ist, dass ihr immer "sprechende" Namen für Variablen verwendet. Wenn ihr statt `name` einfach nur `n = "dominik"` schreibt, wird niemand wissen was die Abkürzung `n` bedeutet. Man könnte dann ja auch vermuten es stünde für `nikolaus`oder `niemand`.  
1. Wenn ihr einer Variable einen Namen geben möchtet, der aus mehreren Worten besteht, dann nehmt ihr den Unterstrich zur Hilfe. Beispiel: `mein_name` 
1. Nun schauen wir doch mal, ob wir mit meinem gespeicherten Namen auch etwas anfangen können. Wie wäre es denn den Namen einfach mal anzuzeigen?
   ```python
   # Definition der Variablen
   name = "Dominik"
   
   print(name)
   ```
   Das Ergebnis sollte so aussehen:
   ```text
   Dominik
   
   Process finished with exit code 0
   ```
1. Wir haben nun gesehen, dass wir Variablen zum Speichern von Informationen benutzen können, aber was ist wenn ich den Inhalt meiner Variablen später ändern möchte?
1. Stellen wir uns mal vor dass ich lieber Peter heißen würde - also rein theoretisch. Ich möchte meinen Namen also ändern, nachdem er schon gespeichert ist.
1. Das Ändern einer Variablen ist genauso einfach wie die Definition (= das Erstellen) am Anfang und sieht irgendwie auch ziemlich genau so aus.
   ```python
   # Definition der Variablen
   name = "Dominik"
   
   print(name)

   # Ändern der Variablen
   name = "Peter"

   print(name)
   ```
   Ergebnis:
   ```text
   Dominik
   Peter
   
   Process finished with exit code 0
   ```
   
   Wir sehen also dass mein Name erst `Dominik` ist und dann zu `Peter` wechselt.
1. Dem ein oder anderen ist vielleicht auch schon aufgefallen, dass uns PyCharm (wie die meisten Programmier-Umgebungen) dabei hilft keine Tippfehler zu machen und uns an unsere Variablennamen zu erinnern.
1. Nach diesem ersten kleinen Beispiel, schauen wir uns mal an welche Typen von Variablen wir am häufigsten brauchen werden. Der Typ einer Variablen entscheidet darüber was wir damit später alles anstellen können.
1. Für unseren Namen haben wir den Typ `String` verwendet. Das ist eine beliebige Zeichenkette (= Aneinanderreihung von Zeichen), die alles mögliche enthalten kann. Strings erkennen wir daran, dass sie n einfachen oder doppelten Anführungszeichen geschrieben sind.
   ```python
   spieler_1 = "Dominik"
   spieler_2 = 'Peter'
   ```

## Operatoren und Datentypen

1. Neu hinzu kommen nun auch einfache Operatoren. Operatoren sind bestimmte Zeichen, die aus der Mathematik oder Logik übernommen worden sind und in der Lage sind einen Wert zu verändern oder zu vergleichen.
1. Das klingt ein kleine Wenig kompliziert oder? Na dann gucken wir uns das doch mal in einem Beispiel an.
   ```python
   # Variablen für die Spieler anlegen
   spieler_1 = "Anna"
   spieler_2 = "Lena"

   # Die Nachricht aus verschiedenen Teilen zusammen bauen
   nachricht = "Hallo " + spieler_1 + " und " + spieler_2 + "!"

   print(nachricht)
   ```
   Ergebnis:
   ```text
   Hallo Anna und Lena!
   ```
   
1. Habt ihr was bemerkt? Das Plus-Symbol ist in diesem Fall unser Operator, der bei Variablen vom Typ `String` dafür verwendet wird, um diese miteinander zu verbinden. Das Zusammenfügen von Zeichenketten nennt man auch Konkatenieren.
1. Ein paar weitere, einfache, Operatoren können wir lernen, in dem wir ein kleines Bisschen Mathe in unseren Beispielen aufleben lassen. Aber keine Sorge, wir halten es wirklich ganz einfach und schreiben keine komplizierten Formeln auf.
1. Python unterstützt alle klassischen Berechnungen. Dies gilt aber nur für die neuen Datentypen `Integer` und `Float`. `Integer` wird für ganze Zahlen verwendet und `Float` für eine Zahl mit Komma (die sogennante Fließkommazahl).
   ```python
   # Definition von zwei Variablen für unsere Zahlen
   zahl_1 = 5
   zahl_2 = 10
   ```
1. Addieren
   ```python
   # Plus
   ergebnis = zahl_1 + zahl_2

   print(ergebnis)
   ```
   Ergebnis:
   ```text
   15
   ```
1. Subtrahieren
   ```python
   # Minus
   ergebnis = zahl_2 - zahl_1

   print(ergebnis)
   ```
   Ergebnis:
   ```text
   5
   ```
1. Nanu ... was ist denn jetzt passiert? Wir sehen, dass Python auch it negativen Zahlen arbeiten kann. Wenn ihr also eine größere Zahl von einer kleineren abzieht, erhaltet ihr einen Wert der kleiner ist als Null. Das kennt ihr sicher vom Thermometer, wo es -10 Grad kalt sein kann.
1. Multiplizieren
   ```python
   # Mal
   ergebnis = zahl_1 * zahl_2

   print(ergebnis)
   ```
   Ergebnis:
   ```text
   50
   ```
1. Dividieren
   ```python
   # Geteilt
   ergebnis = zahl_2 / zahl_1

   print(ergebnis)
   ```
   Ergebnis:
   ```text
   2.0
   ```
1. Komisch. Da ist ja ein Punkt bei unserem Ergebnis.
1. Wenn wir in Python teilen, dann bekommen wir immer eine Kommazahl raus. Im Englischen ist der Punkt das was wir im Deutschen mit dem Komma machen und Programmiersprachen sind fast ausschließlich Englisch. Python  sagt uns alsodass das Ergebnis "zwei komma null" ist.
1. Beim Teilen gibt es auch noch eine Besonderheit, denn in Python gelten natürlich alle mathematischen Regeln. Wenn wir versuchen durch Null zu teilen, fliegt uns das Programm um die Ohren.
   ```python
   # Teilen durch Null
   ergebnis = zahl_1 / 0
   ```  
   Ergebnis:
   ```python
   Traceback (most recent call last):
     File variablen.py, line 40, in <module>
       ergebnis_5 = zahl_1 / 0
   ZeroDivisionError: division by zero
   
   Process finished with exit code 1
   ```
1. Hier sehen wir eine klassische Fehlermeldung in Python, bei der uns die letzten Schritte des Programmablaufs angezeigt werden und eine Beschreibung, was das Problem ist.
1. Python sagt uns auf Englisch dass wir eben nicht durch Null (= zero) teilen (= division) können.
1. So weit so gut. Schauen wir uns den nächsten Datentyp an, `List`. Listen werden dazu verwendet um mehrere Dinge in einer geordneten Reihenfolge zu speichern, wobei der Inhalt jedes einzelnen Dings veränderbar ist. Eine Liste erkennt man daran, dass ihre Werte in eckigen Klammern aufgelistet werden.
   ```python
   teilnehmer = ["Peter", "Paul", "Marie"]
   
   print(teilnehmer)
   ```
1. Listen sind von Hause aus numerisch indexiert, aber was heißt das denn? Das heißt dass jedes Dings in unserer Liste über einen numerischen Wert (= eine Zahl) angesprochen werden kann, den sogennanten Index.
1. Wichtig: Der Index einer Liste startet **immer** bei Null und nicht bei Eins.
1. Wenn das erste Dings den Index Null hat, dann hat das zweite Dings die ... 1 => Genau! Wenn wir nun den Namen unserer Variablen nehmen und dahinter die Zahl 1 in Klammern schreiben, sollten wir unser zweites Dings bekommen.
   ```python
   # Wir lesen das zweite Dings aus unerer Liste
   print(teilnehmer[1])
   ```    
   Ergebnis:
   ```text
   Paul
   ```
1. Unsere Liste hat aktuell einen deutlichen Herren-Überschuss, also fügen wir mal schnell noch eine Dame hinzu. Dafür verwenden wir die Methode `append`, die Listen von Hause aus schon mitbringen.
   ```python
   # Wir fügen Lena zu unserer Liste der Teilnehmer hinzu
   teilnehmer.append("Lena")
   
   print(teilnehmer)
   ```
   Ergebnis:
   ```text
   ['Peter', 'Paul', 'Marie', 'Lena']
   ```
   
   Was genau Methoden sind ist für uns im Moment noch nicht wichtig. Ein Bisschen was lernen wir darüber später aber noch.
1. Natürlich können wir auch ein Dings löschen, wenn wir es nicht mehr haben möchten. Dafür brauchen wir die Methode `remove`.
   ```python
   # Wir werfen Paul aus der Liste der Teilnehmer raus
   teilnehmer.remove("Paul")
   
   print(teilnehmer)
   ```
   Ergebnis:
   ```text
   ['Peter', 'Marie', 'Lena']
   ```
   
   Wir geben der Methode `remove` das Dings mit das wir löschen möchten und schon ist es weg.
1. Wenn wir ein Dings nicht anhand seines Wertes, sondern über seinen Index löschen möchten dann verwenden wir die Methode `del`.
   ```python
   # Wir werfen Lena aus der Liste der Teilnehmer raus
   del teilnehmer[2]
   
   print(teilnehmer)
   ```
   Ergebnis:
   ```text
   ['Peter', 'Marie']
   ```
   
   Wir erinnern uns dass der Index einer Liste immer bei 0 startet. Wir löschen also das dritte Dings (= Lena) aus unserer Liste.
1. Möchten wir wissen wie viele Einträge eine Liste hat, verwenden wir die Methode `len`.
   ```python
   # Wir ermitteln die Anzahl Teilnehmer in unserer Liste
   anzahl_teilnehmer = len(teilnehmer)
   
   print(anzahl_teilnehmer)
   ```
   Ergebnis:
   ```text
   2
   ```
1. Das soll uns für Listen erst einmal genügen. Kommen wir zum nächsten Datentyp dem `Tuple`. Ein Tupel funktioniert wie Liste, ist nach der Definition aber nicht veränderbar. Tupel erkennt man daran, dass ihre Werte in runden Klammern aufgelistet werden.
   ```python
   # Wir definieren den Tupel mit unseren Freunden
   freunde = ('Alex', 'Maximilian', 'Anna', 'Sarah') 
   
   print(freunde)
   ```
   Ergebnis:
   ```text
   ['Alex', 'Maximilian', 'Anna', 'Sarah']
   ```
1. Versuchen wir unseren Tupel `freunde` zu verändern, dann bekommen wir eine Fehlermeldung.
   ```python
   # Wir versuchen Paul aus der Liste zu werfen
   freunde[0] = "Paul"
   ```
   Ergebnis:
   ```text
   Traceback (most recent call last):
     File variablen.py, line 73, in <module>
       freunde[0] = "Paul"
   TypeError: 'tuple' object does not support item assignment
   ```
1. Wie schon bei Listen, können wir auch bei einem Tupel die Methode `len` verwenden, um die Anzahl Dingse zu ermitteln.
   ```python
   # Wir ermitteln die Anzahl Freunde in unserem Tupel  
   anzahl_freunde = len(freunde)
   
   print(anzahl_freunde)
   ```
   Ergebnis:
   ```text
   4
   ```
1. So. Und schon sind wir bei unserem letzten Datentyp für heute, dem Verzeichnis `Dict` (= Dictionary). Was das genau ist erfahren wir gleich, aber fangen wir mal mit einem Beispiel an. Ich zeige euch wo Listen an ihre Grenzen kommen.
1. Wenn man die Namen, das Alter und die E-Mail-Adressen von Freunden in einer Liste speichern würde, könnte das z.B. so aussehen.
   ```python
   # Wir definieren eine verschachtelte Liste unserer Freunde
   adressbuch = [
     ["Anna", "Westermann", 16, "anna.westermann@gmail.com"],
     ["Paul", "Franke", 17, "paul.franke@gmail.com"]
   ]
   ```
1. Ihr seht => man kann Liste nauch ineinander verschachteln. Das ist ja ganz cool, aber wenn ich den Nachnamen von Anna ausgeben möchte, müsste ich den folgenden Code schreiben.
   ```python
   # Wir geben den Nachnamen von Anna aus (Anna = index 0 und dann Nachname = index 1)
   print(adressbuch[0][1])
   ```
   Das ist nicht wirklich gut lesbar und je mehr Verschachtelungen man hat, desto unmöglicher wird es im Code später noch nachvollziehen zu können was man da gerade ausliest. 
1. Deshalb kommen wir nun zum Verzeichnis, dass uns das Leben etwas einfacher macht. Bei einem Verzeichnis werden die Werte mit einem frei defiierbaren Schlüssel verknüpft `{"schlüssel": wert}`. Als Wert sind dann wieder alle Datentypen möglich, die wir zur Verfügung haben, egal ob `String`, `Integer`, oder `Tuple`.
   ```python
   # Wir definieren eine Liste von Verzeichnissen
   adressbuch = [
     {"vorname": "Anna", "nachname": "Westermann", "alter": 16, "email": "anna.westermann@gmail.com"},
     {"vorname": "Paul", "nachname": "Franke", "alter": 17, "email": "paul.franke@gmail.com"}
   ]
   ```
   Je nach persönlicher Vorliebe kann man das Ganze auch etwas lesbarer schreiben, denn Python ignoriert Leerzeichen, so dass wir diese für die lesbare Gestaltung unseres Codes benutzen können.
   ```python
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
   ```
   
   In unserem Beispiel speichern wir mehrere Verzeichnisse in einer Liste. So sehen viele Daten später auch aus, wenn wir sie aus verschiedenen Quellen (wie z.B. Datenbanken) auslesen.
1. Möchten wir jetzt Annas Nachnamen ausgeben, wird das nun deutlich lesbarer, da wir statt einem Zahlenschlüssel nun auch einen Textschlüssel haben.
   ```python
   # Wir geben Annas Nachnamen aus
   print(adressbuch[0]["nachname"])
   ``` 
1. Ist euch etwas aufgefallen? Ich habe in diesem Beispiel die Variable `adressbuch` mit einem neuen Wert überschrieben. Die verschachtelte Liste der Adressen ist also weg und nur noch die Liste mit Verzeichnissen ist übrig.
1. Möchten wir einen Wert aus einem Verzeichnis löschen, nutzen wir wieder die Funktion `del`, die wir vorher schon kennen gelernt haben. Nehmen wir bei Paul doch mal das Alter weg.
   ```python
   # Wir löschen Pauls Alter
   del adressbuch[1]["alter"]
   
   print(adressbuch[1])
   ```
   
---

&gt; [3. Kontrollstrukturen](./003%20-%20Kontrollstrukturen.md)
  
&lt; [1. Hallo Welt](./001%20-%20Hallo%20Welt.md)