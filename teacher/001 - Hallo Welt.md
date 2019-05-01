# Hallo Welt

1. Python ist eine Sprache die von einem sogenannten Interpreter, wie der Name schon vermuten lässt, interpretiert wird. Das bedeutet dass der Code direkt ausgeführt werden kann und nicht erst (wie z.B. bei Java und vielen anderen Sprachen) in ein anderes Format umgewandelt werden muss.
1. Deshalb können wir in Python unsere Programme schreiben und direkt starten, wenn wir Python auf dem Computer installiert haben.
1. Also los geht's!
1. Öffnet das Programm PyCharm und startet ein neues Projekt. Wählt, falls ihr gefragt werdet, den Standard-Interpreter aus, denn wir wollen uns erst einmal nicht geheimnisvollen und komplizierten Dingen wie virtuellen Umgebungen beschäftigen. 
1. Erstellt eine neue Datei mit dem Namen "hallo.py" als euer allererstes Python-Script.
1. In diese Datei schreiben wir dann:
   ```python
   print("Hallo Welt!")

   ```
1. Es ist weit verbreitet und sozusagen "Standard", dass man am Ende einer Python-Datei eine leere Zeile hat. Das können Programme wie PyCharm für euch auch automatisch machen, wenn ihr es einmal vergesst.  
1. In der Programmiersprache Python wird auf viele Zeichen verzichtet, die in anderen Sprachen häufig zu finden sind. So hat man z.B. keine Semikolons am Ende einer Zeile und auch nur sehr wenige Klammern. Falls ihr schon andere Sprachen gesehen habt mag das für einen Moment komisch sein, aber daran gewöhnt man sich schnell.
1. Zum Vergleich ein kleines Beispiel in PHP und Python.  
   **PHP**
   ```php
   if ($lernen_macht_spass == true) {
       print("Lernen macht Spaß!");
   } else {
       print("Lernen macht keinen Spaß!");
   }
   ```
   
   **Python**
   ```python
   if lernen_macht_spass == true:
       print("Lernen macht Spaß!")
   else:
       print("Lernen macht keinen Spaß!")
   ```   
   
1. Das war nur ein kurzer Ausflug und jetzt schauen wir uns wieder unser erstes Script an. Klickt in der geöffneten Datei (im Editor rechts) mit der rechten Maustaste und dann auf `Run "hallo"` um die Datei mit Python auszuführen.
1. Wenn alles geklappt hat, solltet ihr in der (automatisch geöffneten Konsole) sehen können dass "Hallo Welt!" ausgegeben wird.  
   ```text
   Hallo Welt!
   
   Process finished with exit code 0
   ```

   Die letzte Zeile verrät uns, dass es keine Fehler im Programm gegeben hat, denn der "exit code" 0 bedeutet "alles okay".
---

&gt; [2. Variablen, Typen und Operatoren](./002%20-%20Variablen,%20Typen%20und%20Operatoren.md)