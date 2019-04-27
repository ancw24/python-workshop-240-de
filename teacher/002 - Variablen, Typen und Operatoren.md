# Variablen, Typen und Operatoren

1. Was ist eine Variable?
1. Variablen werden verwendet um Informationen zu speichern und an anderer Stelle wieder abrufen oder manipulieren zu können.
1. Tippen wir doch mal ein Beispiel.
   ```python
   my_name = "Dominik"    
   ```
1. Wenn wir diesen Code ausführen, wird der Wert `Dominik` in der Variablen `my_name` gespeichert.
1. Es ist wichtig sprechende Namen zu für Variablen verwenden. Bitte schreibt euren Code, wenn es euch möglich ist, auch immer in Englisch. Wenn nicht, ist das für den Anfang natürlich auch okay, aber deutscher Programmcode ist selten und schränkt euch dabei ein, wen ihr im Internet um Hilfe bitten möchtet.
1. In Python ist es Quasi-Standard bei mehreren Worten einen Unterstrich zu verwenden. Dies ist in anderen Sprachen (wie z.B. Java) nicht so, da man dort im sogenannten CamelCase schreibt, also `myName` anstatt von `my_name`.
1. Nun schauen wir doch mal, ob wir den gespeicherten Namen auch verwenden können. Testen wir das doch mit einem einfachen print-Befehl.
   ```python
   my_name = "Dominik"
   
   print(my_name)
   ```
   Das Ergebnis sollte so aussehen:
   ```bash
   Dominik
   
   Process finished with exit code 0
   ```
1. Wir haben nun gesehen, dass wir Variablen erstellen und auch verwenden können, aber was ist wenn ich den Wert meiner Variablen ändern möchte? Das ist ganz einfach.
1. Gehen wir mal davon aus dass ich lieber Peter heißen würde und das gerne so in meinem Programm eintragen möchte. Dazu muss ich nur den Namen der Variablen, gefolgt von einem Gleichheitszeichen, verwenden.
   ```python
   my_name = "Dominik"
   
   print(my_name)

   my_name = "Peter"
   ```
1. Dem ein oder anderen ist vielleicht schon aufgefallen, dass uns PyCharm, wie die meisten Programmier-Umgebungen, per Autovervollständigung dabei hilft keine Tippfehler zu machen und uns an unsere Variablennamen zu erinnern.
1. Wenn ich die Variable ein zweites Mal ausgebe, sehe ich erst `Dominik` und dann `Peter` in der Konsole.
   ```python
   my_name = "Dominik"
   
   print(my_name)

   my_name = "Peter"
 
   print(my_name)
   ```
   Das Ergebnis sollte so aussehen:
   ```bash
   Dominik
   Peter
   
   Process finished with exit code 0
   ```
1. Nach diesem ersten kleinen Beispiel, schauen wir uns doch mal an welche Typen von Variablen wir am häufigsten brauchen werden. Für unseren Namen haben wir den Typ `String` verwendet. Das ist eine beliebige Zeichenkette, die alles mögliche enthalten kann. Strings erkennen wir daran, dass sie ein einfachen oder doppelten Anführungszeichen geschrieben sind.
   ```python
   player_1 = "Dominik"
   player_2 = 'Peter'
   ```
1. Neu hinzu kommen nun auch einfache Operatoren. Das sind bestimmte Zeichen, die eine Aktion darstellen und aus der Mathematik und Logik übernommen worden sind. Ein Operator ist in der Lage einen bestimmten Wert oder Operanden zu manipulieren.
1. Klingt kompliziert? Na dann machen wir es doch einfach mal und sehen was passiert.
   ```python
   player_1 = "Dominik"
   player_2 = "Peter"

   welcome_message = "Hallo " + player_1 + " und " + player_2 + "!"

   print(welcome_message)
   ```
1. Habt ihr was bemerkt? Das Plus-Symbol ist in diesem Fall unser Operator, der bei Variablen vom Typ `String` dafür verwendet wird, um diese miteinander zu verbinden (das sogenannte Konkatenieren).
1. Ein paar weitere, einfache, Operatoren können wir lernen, in dem wir etwas Mathe in Python aufleben lassen. Aber keine Sorge, wir halten es wirklich ganz einfach und schreiben keine komplizierten Formeln auf.
1. Python unterstützt alle klassischen Rechen-Operationen für die Datentypen `Integer` und `Float`. `Integer` wird für ganze Zahlen verwendet und `Float` für Fließkommazahlen.
   ```python
   number_1 = 5
   number_2 = 10
   ```
1. Addieren
   ```python
   # Addition
   result_1 = number_1 + number_2

   print(result_1)
   ```
   Ergebnis:
   ```bash
   15
   ```
1. Subtrahieren
   ```python
   # Subtraction
   result_2 = number_1 - number_2

   print(result_2)
   ```
   Ergebnis:
   ```bash
   -15
   ```
1. Nanu ... was ist denn jetzt passiert? Wir sehen, dass Python auch it negativen Zahlen arbeiten kann. Wenn ihr also eine größere Zahl von einer kleineren abzieht, erhaltet ihr einen Wert der kleiner ist als Null. Das kennt ihr sicher vom Thermometer, wo es -10 Grad kalt sein kann.
1. Multiplizieren
   ```python
   # Multiplication
   result_3 = number_1 * number_2

   print(result_3)
   ```
   Ergebnis:
   ```bash
   50
   ```
1. Dividieren
   ```python
   # Division
   result_4 = number_2 / number_1

   print(result_4)
   ```
   Ergebnis:
   ```bash
   2.0
   ```
1. Es fällt auf, dass wir eine Kommazahl zurück bekommen, obwohl wir vorher nur ganze Zahlen verwendet haben. Das liegt an den internen Berechnungen und Rundungen (Stichwort Genauigkeit) von Python und spielt für uns erst einmal keine Rolle.
1. Beim Dividieren gibt es eine Besonderheit, denn auch in Python gelten mathematische Grundgesetze. Wenn wir versuchen durch Null zu teilen, fliegt uns das Programm um die Ohren.
   ```python
   # Division by zero
   result_5 = number_1 / 0
 
   print(result_5)
   ```  
   Ergebnis:
   ```python
   Dominik
   Traceback (most recent call last):
   Peter
   Hallo Dominik und Peter!
   15
     File variables.py, line 40, in <module>
   -5
       result_5 = number_1 / 0
   50
   ZeroDivisionError: division by zero
   2.0
   
   Process finished with exit code 1
   ```
1. Hier sehen wir eine klassische Fehlermeldung in Python, bei der uns die letzten Schritte des Programmablaufs angezeigt werden, zusammen mit einer Fehlermeldung, was das Problem ist.
1. Kommen wir zum nächsten Datentyp `List`. Listen werden dazu verwendet um mehrere Elemente in einer geordneten Reihenfolge zu speichern, wobei der Inhalt jedes einzelnen Elementes veränderbar ist. Eine Liste erkennt man daran, dass ihre Werte in eckigen Klammern aufgelistet werden.
   ```python
   students = ["Peter", "Paul", "Marie"]
   
   print(students)
   ```
1. Listen sind von Hause aus numerisch indexiert, doch was heißt das? Das bedeutet dass jeder Eintrag in unserer Liste über einen numerischen Wert angesprochen werden kann, den sogennanten Index. Wichtig: Der Index einer Liste startet immer bei Null.
1. Lesen wir doch mal das zweite Element aus unserer Liste aus und geben es aus.
   ```python
   print(students[1])
   ```    
   Ergebnis:
   ```bash
   Paul
   ```
1. Unsere Liste hat aktuell einen deutlichen Herrenüberschuss, also fügen wir doch mal noch eine Dame hinzu. Dafür verwenden wir die Methode `append`, die Listen von Hause aus schon mitbringen.
   ```python
   students.append("Lena")
   
   print(students)
   ```
   Ergebnis:
   ```bash
   ['Peter', 'Paul', 'Marie', 'Lena']
   ```
1. Natürlich können wir auch einen Eintrag löschen. Dazu brauchen wir die Methode `remove`.
   ```python
   students.remove(0)
   
   print(students)
   ```
   Ergebnis:
   ```bash
   ['Peter', 'Marie', 'Lena']
   ```
1. Wenn wir einen Eintrag nicht anhand seines Wertes, sondern über seinen Index löschen möchten (wir erinnern uns dass der Index die numerische Zuordnung aller Einträge ist und bei 0 startet), dann verwenden wir die Funktion `del`. Was Funktionen genau sind erklären wir später noch.
   ```python
   del students[2]
   
   print(students)
   ```
   Ergebnis:
   ```bash
   ['Peter', 'Marie']
   ```
1. Möchten wir wissen wie viele Einträge eine Liste hat, verwenden wir die Funktion `len`.
   ```python  
   student_count = len(students)
   
   print(student_count)
   ```
   Ergebnis:
   ```bash
   2
   ```
1. Das soll uns für Listen erst einmal genügen. Kommen wir zum Datentyp `Tuple`, der wie eine Liste funktioniert, jedoch nach dem Erstellen nicht mehr veränderbar ist. Tupel erkennt man daran, dass ihre Werte in runden Klammern aufgelistet werden.
   ```python
   friends = ('Alex', 'Maximilian', 'Anna', 'Sarah') 
   
   print(friends)
   ```
   Ergebnis:
   ```bash
   ['Alex', 'Maximilian', 'Anna', 'Sarah']
   ```
1. Versuchen wir unseren Tupel `friends` zu verändern, dann bekommen wir eine Fehlermeldung.
   ```python
   friends[0] = "Paul"
   ```
   Ergebnis:
   ```bash
   Dominik
   Traceback (most recent call last):
   Peter
     File variables.py, line 73, in <module>
   Hallo Dominik und Peter!
       friends[0] = "Paul"
   15
   TypeError: 'tuple' object does not support item assignment
   ```
1. Wie schon bei den Listen, können wir auch beim Tupel die Methode `len` verwenden, um die Anzahl Elemente zu ermitteln.
   ```python  
   friend_count = len(friends)
   
   print(friend_count)
   ```
   Ergebnis:
   ```bash
   4
   ```
1. So. Und schon sind wir bei unserem letzten Datentyp für dieesn Kurs, dem Verzeichnis `Dict` (= Dictionary). Was das ist erfahren wir gleich, aber fangen wir mal mit einem Beispiel an wo Listen an ihre Grenzen kommen.
1. Wenn man die Kontaktdaten von Personen in einer Liste speichern würde, könnte das z.B. so aussehen.
   ```python
   contacts = [
     ["Anna", "Westermann", 16, "anna.westermann@gmail.com"],
     ["Paul", "Franke", 17, "paul.franke@gmail.com"]
   ]
   ```
1. Ihr seht => man kann Liste nauch ineinander verschachteln. Das ist ja ganz cool, aber wenn ich den Nachnamen von Anna ausgeben möchte, müsste ich den folgenden Code schreiben.
   ```python
   print(contacts[0][1])
   ```
   Das ist nicht wirklich gut lesbar und je mehr Verschachtelungen man hat, desto unmöglicher wird es im Code später noch "auf Anhieb" nachvollziehen zu können was man da gerade ausliest. 
1. Deshalb kommen wir nun zum Verzeichnis, dass uns das Leben etwas einfacher macht. Bei einem Verzeichnis werden die Werte mit einem frei defiierbaren Schlüssel verknüpft `{"schlüssel": wert}`. Als Wert sind dann wieder alle Datentypen möglich, die wir zur Verfügung haben, egal ob `String`, `Integer`, oder `Tuple`, etc..
   ```python
   contacts = [
     {"firstname": "Anna", "lastname": "Westermann", "age": 16, "email": "anna.westermann@gmail.com"},
     {"firstname": "Paul", "lastname": "Franke", "age": 17, "email": "paul.franke@gmail.com"}
   ]
   ```
   In diesem Beispiel speichern wir mehrere Verzeichnisse in einer Liste. So sehen Daten später häufig aus, wenn wir sie aus verschiedenen Quellen (z.B. Datenbanken) lesen.
1. Möchten wir jetzt Annas Nachnamen ausgeben, wird das nun deutlich lesbarer, da wir statt einem Zahlenschlüssel nun auch einen Textschlüssel haben.
   ```python
   print(contacts[0]["firstname"])
   ``` 
1. Ist euch etwas aufgefallen? Ich habe in diesem Beispiel die Variable `contacts` mit einem neuen Wert überschrieben. Die verschachtelte Liste der Kontakte ist also weg und nur noch die Liste mit Verzeichnissen ist übrig.
1. Möchten wir einen Wert aus einem Verzeichnis löschen, nutzen wir wieder die Funktion `del`, die wir vorher schon kennen gelernt haben. Nehmen wir bei Paul doch mal das Alter weg.
   ```python
   del contacts[1]["age"]
   
   print(contacts[1])
   ``` 
1. 