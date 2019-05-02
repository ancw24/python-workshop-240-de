## Variablen

1. Erstellt eine neue Datei mit dem Namen "variablen.py".
1. Als erstes fragen wir uns natürlich: "Was ist eine Variable?"
1. Variablen benutzt man um bestimmte Informationen zu speichern um diese später wieder auslesen oder verändern zu können.
1. Eine Variable wird zu Beginn ihres Lebens einmal definiert. Das bedeutet dass wir Python darum bitten eine Information unter einem bestimmten Namen zu speichern. 
   ```python
   # Definition der Variablen
   name = "Dominik"
   ```
1. Wenn wir diesen Code ausführen, wird der die Information `Dominik` in der Variablen `name` gespeichert. Python kennt nun also meinen Namen. Das ist doch schon mal was.
1. Wichtig ist, dass ihr immer "sprechende" Namen für Variablen verwendet. Wenn ihr nämlich statt `name` einfach nur `n = "dominik"` schreiben würdet, wüsste niemand was die Abkürzung `n` bedeutet. Man könnte dann ja auch vermuten `n` stünde für `nikolaus`oder `niemand`.  
1. In Python sollten Variablen in den meisten Fällen auch klein geschrieben werden und später schrebt man Code nur noch auf Englisch.
1. Wenn ihr einer Variablen einen Namen geben möchtet, der aus mehreren Worten besteht, dann nehmt ihr den Unterstrich zur Hilfe. Beispiel: `mein_name` 
1. Nun schauen wir doch mal, ob wir mit meinem gespeicherten Namen auch irgendetwas anfangen können. Wie wäre es denn damit den Namen einfach mal anzuzeigen?
   ```python
   # Definition der Variablen
   name = "Dominik"
   
   # Ausgabe (= Anzeige) einer Variablen in der Konsole
   print(name)
   ```
   Das Ergebnis sollte so aussehen:
   ```text
   Dominik
   
   Process finished with exit code 0
   ```
   
   Python hat also ganz richtig den gespeicherten Namen ausgegeben und uns mitgeteilt dass alles okay ist und es keine Fehler in unserem Programm gegeben hat.
1. **Übungsaufgabe 01:**
   - Definiere eine Variablen und speichere deine Lieblingsfarbe
   - Gib die Farbe auf der Konsole aus 
   
   **Lösung:**
   ```python
   # Wir definieren eine Variable
   lieblingsfarbe = "blau"
   
   # und geben sie auf der Konsole aus
   print(lieblingsfarbe)
   ```
   
   **Konsole:**
   
   ```text
   blau
   ```
1. Wir haben nun gesehen, dass wir Variablen zum Speichern von Informationen benutzen können, aber was ist eigentlich wenn ich den Inhalt meiner Variablen ändern möchte?
1. Stellen wir uns mal vor dass ich lieber Peter heißen würde - also rein theoretisch. Ich möchte meinen Namen also ändern, nachdem ich ihn schon gespeichert habe.
1. Das Ändern einer Variablen ist genau so einfach wie die Definition am Anfang und sieht irgendwie auch ziemlich genau so aus.
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
   
   Wir sehen also dass mein Name erst `Dominik` ist und dann zu `Peter` wechselt, wenn wir ihn auf der Konsole ausgeben.
1. Dem ein oder anderen ist vielleicht auch schon aufgefallen, dass uns PyCharm (wie die meisten Programmier-Umgebungen) dabei hilft keine Tippfehler zu machen und uns an die Namen unserer Variablen erinnert.
1. Nachdem wir nun wissen wie wir eine Variable definieren und ändern können, schauen wir uns einmal an welche Typen von Variablen wir am häufigsten brauchen werden. Der Typ einer Variablen entscheidet darüber was wir damit später so alles anstellen können.
1. Für unseren Namen haben wir den Typ `String` verwendet. Das ist eine beliebige Zeichenkette (= Aneinanderreihung von Zeichen), die alles mögliche enthalten kann.
1. Und woher weiß Python dass wir den Typ `String` verwenden wollen? Strings erkennt Python daran, dass sie in einfachen oder doppelten Anführungszeichen geschrieben sind.
   ```python
   # Beide Schreibweisen sind richtig
   spieler_1 = "Dominik"
   spieler_2 = 'Peter'
   ```

## Operatoren und Datentypen

1. Neu hinzu kommen nun, neben den Typen von Variablen, auch einfache Operatoren. Operatoren sind bestimmte Zeichen, die aus der Mathematik oder Logik kommen und in der Lage sind Werte zu verändern oder zu vergleichen.
1. Das klingt ein kleine Wenig kompliziert oder? Na dann gucken wir uns das doch mal in einem Beispiel genauer an.
   ```python
   # Variablen für zwei Mitspieler anlegen
   spieler_1 = "Anna"
   spieler_2 = "Lena"

   # Eine Nachricht aus verschiedenen Strings zusammenbauen
   nachricht = "Hallo " + spieler_1 + " und " + spieler_2 + "!"

   print(nachricht)
   ```
   Ergebnis:
   ```text
   Hallo Anna und Lena!
   ```
1. Habt ihr etwas bemerkt? Das Plus-Symbol ist in diesem Fall unser **Operator**, der bei Variablen vom Typ `String` dafür verwendet wird, um diese miteinander zu verbinden. Das Zusammenfügen von Zeichenketten nennt man auch "Konkatenieren", falls ihr mal ein Bisschen Fachchinesisch sprechen wollt.
1. **Übungsaufgabe 02:**
   - Definiere zwei Variablen mit deinen Lieblingsfarben
   - Gib folgende Nachricht auf der Konsole aus "Meine Lieblingsfarben sind {Farbe 1} und {Farbe 2}." 
   
   **Lösung:**
   ```python
   lieblingsfarbe_1 = "blau"
   lieblingsfarbe_2 = "gelb"
   
   print("Meine Lieblingsfarben sind " + lieblingsfarbe_1 + " und " + lieblingsfarbe_2)
   ```
   
   **Konsole:**
   
   ```text
   Meine Lieblingsfarben sind blau und gelb
   ```
1. Ein paar weitere einfache Operatoren können wir lernen, in dem wir ein kleines Bisschen Mathe in unseren Beispielen aufleben lassen. Aber keine Sorge, wir halten es wirklich ganz einfach und ich verspreche euch dass es nicht weh tut.
1. Python unterstützt alle "klassischen" Berechnungen, die ihr auch aus der Schule kennt.
1. Dabei gibt es 2 neue Typen für unsere Variablen, die wir kennen müssen.
1. Der Typ `Integer` steht für ganze Zahlen und der Typ `Float` für Zahlen mit einem Komma (auch Fließkommazahlen genannt).
1. Im Gegensatz zur deutschen Schreibweise verwendet man in allen gängigen Programmiersprachen nicht das Komma als Trennzeichen, sondern den Punkt. Das liegt einfach daran dass Programmiersprachen in der Regel Englisch sind und im englischen Sprachraum Punkt und Komma in der Mathematik genau vertauscht verwendet werden.
1. Komma = Tausendertrennzeichen (1,000 = Eintausend)
1. Punkt = Dezimaltrennzeichen (1.0 = Eins Komma Null)
1. Definieren wir doch mal zwei Variablen mit Zahlen, die wir zum Rechnen verwenden können.
   ```python
   # Definition einer Variablen vom Typ "Integer"
   zahl_1 = 5

   # Definition einer Variablen vom Typ "Float"
   zahl_2 = 10.0

   # Da wir nicht immer eine Kommazahl als Ergebnis haben wollen, nehmen wir
   # doch lieber "Integer" für unsere zweite Zahl
   zahl_2 = 10
   ```
1. Plus
   ```python
   # Plus
   ergebnis = zahl_1 + zahl_2

   print(ergebnis)
   ```
   Ergebnis:
   ```text
   15
   ```
1. Minus
   ```python
   # Minus
   ergebnis = zahl_2 - zahl_1

   print(ergebnis)
   ```
   Ergebnis:
   ```text
   5
   ```
1. Mal
   ```python
   # Mal
   ergebnis = zahl_1 * zahl_2

   print(ergebnis)
   ```
   Ergebnis:
   ```text
   50
   ```
1. Geteilt
   ```python
   # Geteilt
   ergebnis = zahl_2 / zahl_1

   print(ergebnis)
   ```
   Ergebnis:
   ```text
   2.0
   ```
1. Komisch. Da ist ja ein Punkt bei unserem letzten Ergebnis, als wir geteilt haben.
1. Wenn wir in Python Zahlen teilen, dann bekommen wir immer eine Kommazahl dabei heraus, weil ... ist einfach so. :)
1. Beim Teilen gibt es auch noch eine Besonderheit, denn in Python gelten natürlich auch alle mathematischen Grundregeln. Wenn wir versuchen durch Null zu teilen, fliegt uns das Programm ziemlich eindeutig um die Ohren.
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
1. Hier sehen wir eine klassische Fehlermeldung in Python, bei der uns die letzten Schritte des Programmes angezeigt werden und auch eine Beschreibung, was das Problem ist.
1. Python sagt uns auf Englisch dass wir eben nicht durch Null (= zero) teilen (= division) können.
1. **Übungsaufgabe 03:**
   - Definiere zwei Variablen mit beliebigen Zahlen
   - Schreibe Beispiele für alle Grundrechenarten (Plus, Minus, Mal, Geteilt) und gib das Ergebnis auf der Konsole aus  
   
   **Lösung:**
   ```python
   zahl_1 = 3
   zahl_2 = 9

   print(zahl_1 + zahl_2)
   print(zahl_2 - zahl_1)
   print(zahl_1 * zahl_2)
   print(zahl_2 / zahl_1)
   ```
   
   **Konsole:**
   
   ```text
   12
   6
   27
   3.0
   ```
1. So weit so gut. Schauen wir uns den nächsten Datentyp an, `List`. Listen werden dazu verwendet um mehrere Dinge in einer geordneten Reihenfolge zu speichern, wobei der Inhalt jedes einzelnen Dings veränderbar ist. Eine Liste erkennt man daran, dass ihr Inhalt in **eckigen** Klammern aufgelistet wird.
   ```python
   teilnehmer = ["Peter", "Paul", "Anna"]
   
   print(teilnehmer)
   ```
1. Listen sind von Hause aus numerisch indexiert, aber was heißt das denn bitte? Das heißt, dass jedes Dings in unserer Liste über einen numerischen Wert (= eine Zahl) angesprochen werden kann, den sogennanten Index.
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
1. **Übungsaufgabe 04:**
   - Definiere eine Liste mit 5 Freunden
   - Gib den zweiten und fünften Freund in der Konsole aus   
   
   **Lösung:**
   ```python
   freunde = ["Paul", "Peter", "Mark", "Anna", "Lena"]
   
   print(freunde[1])
   print(freunde[4])
   ```

   **Konsole:**
   
   ```text
   Peter
   Lena
   ```
1. Unsere Teilnehmer-Liste hat aktuell einen deutlichen Jungs-Überschuss, also fügen wir mal schnell noch Sarah hinzu. Dafür verwenden wir die Methode `append`, die unsere Listen von Hause aus schon mitbringen.
   ```python
   teilnehmer = ["Peter", "Paul", "Anna"]

   # Wir fügen Sarah zu unserer Liste der Teilnehmer hinzu
   teilnehmer.append("Sarah")
   
   print(teilnehmer)
   ```
   Ergebnis:
   ```text
   ['Peter', 'Paul', 'Anna', 'Sarah']
   ```
   
   Was genau Methoden sind und was die alles können ist für uns im Moment noch nicht wichtig. Ein Bisschen was lernen wir darüber später aber noch.
1. Natürlich können wir auch ein Dings löschen, wenn wir es nicht mehr haben möchten. Dafür brauchen wir die Methode `remove`.
   ```python
   # Wir werfen Paul aus der Liste der Teilnehmer heraus
   teilnehmer.remove("Paul")
   
   print(teilnehmer)
   ```
   Ergebnis:
   ```text
   ['Peter', 'Anna', 'Sarah']
   ```
   
   Wir geben der Methode `remove` das Dings mit das wir löschen möchten und schon ist es weg.
1. Wenn wir ein Dings nicht anhand seines Wertes, sondern über seinen Index löschen möchten dann verwenden wir die Methode `del`.
   ```python
   # Wir werfen Sarah wieder aus der Liste der Teilnehmer heraus
   del teilnehmer[2]
   
   print(teilnehmer)
   ```
   Ergebnis:
   ```text
   ['Peter', 'Anna']
   ```
   
   Wir erinnern uns dass der Index einer Liste immer bei 0 startet. Wir löschen also das dritte Dings (= Lena) aus unserer Liste.
1. **Übungsaufgabe 05:**
   - Füge der Liste von Freunden neue hinzu und lösche welche, um zu üben
   - Schreibe am Ende die letzte Version deiner Liste in die Konsole 
   
   **Lösung:**
   ```python
   # Wir definieren unsere Liste von Freunden
   freunde = ["Paul", "Maxi", "Anna", "Lena"]

   # Wir fügen Sarah als Freundin hinzu
   freunde.append("Sarah")

   # Wir werfen Anna aus der Liste heraus
   freunde.remove("Anna")
   
   print(freunde)
   ```

   **Konsole:**
   
   ```text
   ['Paul', 'Maxi', 'Lena', 'Sarah']
   ```
1. Möchten wir wissen wie viele Einträge eine Liste hat, verwenden wir die Funktion `len`.
   ```python
   # Wir ermitteln die Anzahl Teilnehmer in unserer Liste
   anzahl_teilnehmer = len(teilnehmer)
   
   print(anzahl_teilnehmer)
   ```
   Ergebnis:
   ```text
   2
   ```
1. Kleiner Tipp: Die Funktion `len` kann man auch verwenden um herauszufinden wie lang eine Variable vom Typ `String` ist.
1. ```python
   # Wir ermitteln die Anzahl Zeichen eines Strings
   name = 'Dominik'
   
   print(len(name))
   ```
1. Das soll uns für Listen erst einmal genügen. Kommen wir zum nächsten Datentyp dem `Tuple`. Ein Tupel funktioniert wie Liste, ist aber nicht veränderbar. Tupel erkennt man daran, dass ihr Inhalt in **runden** Klammern aufgelistet wird.
   ```python
   # Wir definieren einen Tupel mit unseren Freunden
   freunde = ('Alex', 'Maximilian', 'Anna', 'Sarah') 
   
   print(freunde)
   ```
   Ergebnis:
   ```text
   ('Alex', 'Maximilian', 'Anna', 'Sarah')
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
1. **Übungsaufgabe 06:**
   - Definiere einen Tupel deiner Freunde
   - Gib den Tupel in der Konsole aus
   - Gib die Länge des Tupels in der Konsole aus 
   
   **Lösung:**
   ```python
   freunde = ("Paul", "Maxi", "Anna", "Lena")
   
   print(freunde)
   print(len(freunde))
   ```
   
   **Konsole:**
   
   ```text
   ('Paul', 'Maxi', 'Anna', 'Lena')
   4
   ```
1. So. Und schon sind wir bei unserem vorletzten Datentyp für heute, dem Verzeichnis `Dict` (= Dictionary). Was das genau ist erfahren wir gleich, aber fangen wir mal mit einem Beispiel an. Ich zeige euch wo Listen an ihre Grenzen kommen.
1. Wenn man die Namen, das Alter und die E-Mail-Adressen von Freunden in einer Liste speichern würde, könnte das so aussehen:
   ```python
   # Wir definieren eine verschachtelte Liste unserer Freunde
   adressbuch = [
     ["Anna", "Westermann", 16, "anna.westermann@gmail.com"],
     ["Paul", "Franke", 17, "paul.franke@gmail.com"]
   ]
   ```
1. Ihr seht => man kann Listen auch ineinander verschachteln. Das ist ja ganz cool, aber wenn ich den Nachnamen von Anna ausgeben möchte, müsste ich den folgenden Code schreiben.
   ```python
   # Wir geben den Nachnamen von Anna aus (Anna = index 0 und dann Nachname = index 1)
   print(adressbuch[0][1])
   ```
   Das ist nicht wirklich gut lesbar und je mehr Verschachtelungen man hat, desto unmöglicher wird es im Code später noch nachvollziehen zu können was man da gerade ausliest. 
1. Deshalb kommen wir nun zum Verzeichnis, dass uns das Leben etwas einfacher macht. Bei einem Verzeichnis werden alle Dingse mit einem frei defiierbaren Schlüssel verknüpft `{"schlüssel": dings}`. Als Dings sind dann wieder alle Datentypen möglich, die wir zur Verfügung haben, egal ob `String`, `Integer`, oder `Tuple`.
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
   
   In unserem Beispiel speichern wir mehrere Verzeichnisse in einer Liste. So sehen viele Daten später auch aus, wenn wir sie aus Quellen wie z.B. Datenbanken auslesen.
1. Möchten wir jetzt Annas Nachnamen ausgeben, wird das deutlich lesbarer, da wir neben einem Zahlenschlüssel nun auch einen Textschlüssel haben.
   ```python
   # Wir geben Annas Nachnamen aus
   print(adressbuch[0]["nachname"])
   ``` 
1. Möchten wir einen Wert aus einem Verzeichnis löschen, nutzen wir wieder die Funktion `del`, die wir vorher schon kennen gelernt haben. Nehmen wir bei Paul doch mal das Alter weg.
   ```python
   # Wir löschen Pauls Alter
   del adressbuch[1]["alter"]
   
   print(adressbuch[1])
   ```
   
   **Ergebnis:**
   
   ```text
   {'vorname': 'Paul', 'nachname': 'Franke', 'email': 'paul.franke@gmail.com'}

   # lesbarer formatiert
   {
       'vorname': 'Paul',
       'nachname': 'Franke',
       'email': 'paul.franke@gmail.com'
    }
   ```
1. **Übungsaufgabe 07:**
   - Speichere 2 Autos in einer Liste mit Verzeichnissen
   - Jedes Verzeichnis hat mindestens die beiden Schlüssel "marke" und "modell" 
   - Gib deine Liste in der Konsole aus 
   
   **Lösung:**
   ```python
   autos = [
       {
           "marke": "Audi",
           "modell": "A4"
       },
       {
           "marke": "BMW",
           "modell": "3 Cabrio"
       },    
   ]
   
   print(autos)
   ```
   
   **Konsole:**
   
   ```text
   [{'marke': 'Audi', 'modell': 'A4'}, {'marke': 'BMW', 'modell': '3 Cabrio'}]
   
   # lesbarer formatiert
   [
       {
           'marke': 'Audi',
           'modell': 'A4'
       },
       {
           'marke': 'BMW',
           'modell': '3 Cabrio'
       }
   ]
   ```
1. Als letzten Datentyp schauen wir uns nun den Wahrheitswert `Boolean` an.
1. Eine Variable vom Typ `Boolean` kann nur 2 Werte haben: `True` (= wahr) und `False` (= falsch).
1. Man könnte zum Beispiel speichern ob das Freibad gerade geöffnet ist.    
   `freibad_geoeffnet = True`
1. Warum dieser Datentyp sehr häufig gebraucht wird und sehr nützlich ist lernen wir im nächsten Schritt.  

---

&gt; [3. Kontrollstrukturen](./003%20-%20Kontrollstrukturen.md)
  
&lt; [1. Hallo Welt](./001%20-%20Hallo%20Welt.md)