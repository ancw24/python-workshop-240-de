# Schleifen

1. Erstellt eine neue Datei mit dem Namen "schleifen.py".

## WHILE

1. Beginnen wir mit der `while`-Schleife, bei der wir etwas so lange passieren lassen, wie eine bestimmte Bedingung wahr ist.
1. Ein einfaches Beispiel ist das Zählen von 1 bis 5. Dabei ist es **sehr wichtig** darauf zu achten, dass man in der Schleife den Wert der Bedingung verändert. Sonst baut ihr eine Endlosschleife, die euren Computer zum Abstürzen bringen kann.
   ```python
   # Zählen von 1 bis 5
   
   # Wir setzen den Startwert unseres Zähles
   zaehler = 1

   # Bedingung: Zähler kleiner oder gleich 5 (wir könnten auch schreiben < 6)
   while zaehler <= 5:
       print(zaehler)
    
       # Anpassen der Werte für unsere Abbruch-Bedingung, damit wir keine Endlosschleife haben
       zaehler = zaehler + 1
   ```
   Ergebnis:
   ```text
   1
   2
   3
   4
   5
   ```
1. **Übungsaufgabe 01:**
   - Erstelle eine `while`-Schleife die von 5 bis 1 rückwärts zählt. 
   
   **Lösung:**
   ```python
   # Wir setzen den Startwert unseres Zähles
   zaehler = 5
   
   # Bedingung: Zähler größer oder gleich 1
   while zaehler >= 1:
       print(zaehler)
   
       # Anpassen der Werte für unsere Abbruch-Bedingung, damit wir keine Endlosschleife haben
       zaehler = zaehler - 1
   ```
   
   **Konsole:**
   
   ```text
   5
   4
   3
   2
   1
   ```
## FOR

1. Als nächstes schauen wir uns die `for`-Schleife an. Diese wird am häufigsten dazu verwendet um alle oder einen Teil der Dingse in einer Liste oder einem Tupels zu durchlaufen.
1. Geben wir doch mal eine Liste von Freunden aus.
   ```python
   # Meine Freunde
   
   freunde = ["Peter", "Paul", "Anna", "Lena"]
   
   for freund in freunde:
       print(freund)
   ```
   Ergebnis:
   ```text
    Peter
    Paul
    Anna
    Lena
   ```
1. **Übungsaufgabe 02:**
   - Erstelle eine Liste von Farben und gib diese nacheinander in der Konsole aus 
   
   **Lösung:**
   ```python
   # Wir definieren unsere Farben
   farben = ["Rot", "Grün", "Blau"]
   
   # Wir geben die Farben nacheinander aus
   for farbe in farben:
       print(farbe)
   ```
   
   **Konsole:**
   
   ```text
   Rot
   Grün
   Blau
   ```
1. Man kann mit der `for`-Schleife aber auch zählen oder eine bestimmte Anzahl Durchläufe starten, wie wir es bei der `while`-Schleife gesehen haben.
   ```python
   # Zählen wir mit FOR
   
   for zahl in range(1, 6):
       print(zahl)
   ```
1. Bei der Funktion `range` bestimmt die erste Zahl den Startwert und die zweite den Wert bei dem aufgehört wird. Beim zwiten Wert muss man darauf achten immer die gewünschte letzte Zahl + 1 zu nehmen.  
---

&gt; [5. Funktionen](./005%20-%20Funktionen.md)
  
&lt; [3. Kontrollstrukturen](./003%20-%20Kontrollstrukturen.md)