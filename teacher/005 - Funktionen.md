# Funktionen

Wir erstellen eine Datei "funktionen.py".

1. Funktionen sind dazu da um einen bestimmten Code immer wieder verwenden zu können. Dabei können auch verschiedene Werte übergeben werden, die den Ablauf beeinflussen.
1. Schreiben wir als erstes eine ganz einfache Funktion, die jemanden begrüßen kann.
   ```python
   # Eine freundliche Begrüßung
   
   def hallo(name):
       print("Hallo " + name + "!")
   
   hallo("Paul")
   ```
   Ergebnis:
   ```text
   Hallo Paul!
   ```
   
   Erklärung:  
   Zuerst sagen wir Python mit dem Schlüsselwort `def` dass wir eine Funktion definieren wollen.
   
   Darauf folgt ein Name für die Funktion, über den wir diese später ansprechen können. Achtet hier bitte, wie schon bei Variablen, auf sinnvolle Namen, die ihr auch Jahre später noch verstehen könnt.
   
   In einem runden Klammernpaar legen wir dann fest, welche Variablen  beim Aufrufen der Funktion übergeben werden können.  Diese Variablen nennt man bei Funktionen auch "Parameter".
   
   Alles was innerhalb der Funktion (= eingerückt) ist, wird beim Aufrufen ausgeführt.
1. Jetzt hat unsere kleine Funktion aber noch ein Problem. Wenn wir den Namen gar nicht wissen, bekommen wir eine Fehlermeldung.
   ```python
   hallo()
   ```
   Ergebnis:
   ```text
   Traceback (most recent call last):
     File "funktionen.py", line 7, in <module>
       hallo()
   TypeError: hallo() missing 1 required positional argument: 'name'
   ```

   Python sagt uns also:  
   Das ist ein Typ-Fehler, denn die Funktion hallo() benötigt 1 Parameter "name".
1. Wenn wir diesen Fall verhindern wollen, geben wir unserem Parameter einen Standardwert (= Default) mit.
   ```python
   # Eine freundliche Begrüßung für jedermann
   
   def hallo_alle(name = None):
       if name:
           print("Hallo " + name + "!")
       else:
           print("Hallo Unbekannter!")
   
   hallo_alle()
   ```
   Ergebnis:
   ```text
   Hallo Unbekannter
   ```
   
   Der Wert `None` ist in diesem Fall etwas Besonderes. Damit kann man sagen dass der Parameter zwar angegeben werden kann, andernfalls aber einfach den Wert "Nichts" hat.
   
   Die Prüfung `if name` sorgt dann dafür dass wir nur dann versuchen den Namen zu verwenden, wenn er **nicht** `None` ist.
   
   Und schon ist das Angeben eines Namens keine Pflicht mehr.
1. Theoretisch kann eine Funktion beliebig viele Parameter haben. Wir sollten uns jedoch auf einige wenige beschränken, da der Code später sonst sehr unlesbar und auch schlechter pflegbar wird.
1. Ein Beispiel mit 2 Parametern is das Zusammenzählen von zwei Zahlen.
   ```python
   # Rechnen wir doch mal zusammen
   
   def plus(zahl_1, zahl_2):
       loesung = zahl_1 + zahl_2 
       
       return loesung
   
   ergebnis = plus(5, 10)

   print(ergebnis)
   ```
   Ergebnis:
   ```text
   15
   ```
   
   Nanu ... was ist denn das? Da steht ja ein `return` in unserer Funktion.
   
   In der Regel möchten wir eine Funktion dazu benutzen etwas bestimmtes zu tun und manchmal möchten wir dabei auch etwas zurück bekommen. Denn im echten Programmierer-Leben würden wir so gut wie niemals `print` in einer Funktion verwenden.
   
   Also sagen wir in unserer Funktion, dass wir die Lösung der einfachen Mathe-Aufgabe als Wert zurück bekommen möchten. Diesen Wert können wir dann entweder direkt ausgeben oder noch (wie im Beispiel) einer neuen Variablen zuweisen.
---

&lt; [4. Schleifen](./004%20-%20Schleifen.md)