# Schleifen

Wir erstellen eine Datei "schleifen.py".

## WHILE

1. Beginnen wir mit der `while`-Schleife, bei der wir etwas so lange passieren lassen, wie eine bestimmte Bedingung wahr ist.
1. Ein einfaches Beispiel ist das Zählen von 1 bis 5. Dabei ist es **sehr wichtig** darauf zu achten, dass man in der Schleife den Wert der Bedingung verändert. Sonst baut ihr eine Endlosschleife, die euren Computer zum Abstürzen bringen kann.
   ```python
   # Zählen von 1 bis 5
   
   # Wir setzen den Startwert unseres Zähles
   zaehler = 1

   # Bedingung: Zähler kleiner oder gleich 5   
   while zaehler <= 5:
       print(zaehler)
    
       # Anpassen der Werte für unsere Abbruch-Bedingung, damit wir keine Endlosschleife haben
       zaehler = zaehler + 1
   ```

## FOR

1. Als nächstes schauen wir uns die `for`-Schleife an. Diese wird am häufigsten dazu verwendet um alle oder einen Teil der Elemente einer Liste oder eines Tupels zu durchlaufen.
1. Geben wir doch mal eine Liste von Freunden aus.
   ```python
   # Meine Freunde
   
   freunde = ["Peter", "Paul", "Anna", "Lena"]
   
   for freund in freunde:
       print(freund)
   ```
1. Man kann mit der `for`-Schleife aber auch zählen oder eine bestimmte Anzahl Durchläufe starten.
   ```python
   # Zählen wir nochmal
   
   for zahl in range(1, 6):
       print(zahl)
   ```
1. Bei der Funktion `range` bestimmt die erste Zahl den Startwert und die zweite den Wert bei dem aufgehört wird. Beim zwiten Wert muss man darauf achten immer die gewünschte letzte Zahl + 1 zu nehmen.  
1. Als letztes Beispiel schauen wir uns noch an wie man mit der `for`-Schleife ein Verzeichnis durchlaufen kann.
1. Geben wir doch mal alle Infos aus, die wir über Anna gespeichert haben.
```python
# Was wir über Anna wissen

anna = {
    "vorname": "Anna",
    "nachname": "Westermann",
    "alter": 16,
    "email": "anna.westermann@gmail.com"
}

# Geben wir das doch mal alles der Reihe nach aus

for (schluessel, wert) in anna.items():
    print(schluessel + ": " + str(wert))
```
1. Habt ihr was bemerkt? Da hat sich ein `str()` in unseren Code hinein gemogelt. Alle Datentypen (String, Integer, ...) haben auch eine Funktion um andere Typen umzuwandeln. In unserem Beispiel wandeln wir dabei zum Beispiel die Zahl 16 (Integer) von Annas Alter in die Zeichenkette "16" um.
1. In Python kann man, im Gegensatz zu Programmiersprachen wie PHP oder JavaScript, nicht einfach beliebige Datentypen aneinander hängen. Wenn man Zahlen in einem String verwenden möchte, muss man sie also **immer** erst umwandeln.

---

&gt; [5. Funktionen](./005%20-%20Funktionen.md)
  
&lt; [3. Kontrollstrukturen](./003%20-%20Kontrollstrukturen.md)