# Aplikacja do prezentowania obiektów 3D

Maciej Stefanowski

# Opis projektu

Chciałbym stworzyć aplikację, która pozwalałaby na prezentowanie obiektów 3D załadowanych z pliku. Miałaby ona następujące funkcje:

1. Rysowanie modelu 3D przy użyciu operacji macierzowych do rzutowania na płaszczyznę.
2. Wczytywanie obiektu z pliku
3. Ustawienie pozycji i kierunku patrzenia kamery
4. Eliminacja powierzchni zasłoniętych
5. Ustawienie oświetlenia
6. Ustawianie powiększenia obiektu
7. Obracanie obiektu myszką przy użyciu macierzy przekształceń

# Użyte biblioteki i materiały

1. PyQT – nakładka na bibliotekę Qt umożliwiająca tworzenie interfejsu graficznego dla programów komputerowych pisanych w języku Python.
2. [http://wazniak.mimuw.edu.pl/index.php?title=Grafika\_komputerowa\_i\_wizualizacja&amp;fbclid=IwAR1u5oGGkvIgct-f87ulT31D9IWDt\_FLEBw1ByJLqiZJqKLQ49byiNoB0qM](http://wazniak.mimuw.edu.pl/index.php?title=Grafika_komputerowa_i_wizualizacja&amp;fbclid=IwAR1u5oGGkvIgct-f87ulT31D9IWDt_FLEBw1ByJLqiZJqKLQ49byiNoB0qM) – kurs grafiki komputerowej
3. D. Foley, A. van Dam, St.K.Feiner, J.F. Hughes, _„Wprowadzenie do grafiki komputerowej&quot;_, Wydawnictwa Naukowo-Techniczne Warszawa.

# Problemy

Nie będę korzystał z żadnych bibliotek do rysowania 3D, tylko sam będę dokonywał obliczeń. Do przesuwania będę wykorzystywał macierze przekształceń, do rzutowania. Kwestią otwartą jest jeszcze to w jaki sposób zaprogramuję eliminacje powierzchni zasłoniętych i oświetlenia.

Kolejnym problemem może być przechwytywanie ruchów myszką podczas obracania obiektu.





# Wygląd Aplikacji

 [![ekran.png](https://i.postimg.cc/Jhbs62f3/ekran.png)](https://postimg.cc/zLGD30X3)
