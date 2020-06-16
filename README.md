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

# Raport nr 2

Maciej Stefanowski

#

Pierwszym krokiem w stworzeniu mojej aplikacji było utworzenie głównego okna. Stworzyłem go za pomocą programu Qt Designer. Zapisałem plik jako .ui, a później w terminalu przekonwertowałem go na .py za pomocą komendy „pyuic5 main\_window.ui -o main\_window.py&quot;

Zrefaktorowałem kod wygenerowany przez Qt Designer, żeby był on bardziej czytelny.

Okno główne zawiera następujące elementy:

1. Pole podania pozycji kamery
2. Pole podania kierunku patrzenia
3. Opcja zaznaczenia powierzchni zasłoniętych
4. Opcja zaznaczenia oświetlenia
5. Pole podania kierunku oświetlenia
6. Slider do zoomowania
7. Przycisk do wczytywania obiektu

W ramach poszerzenia wiedzy w grafice komputerowej zacząłem się uczyć z kursu Grafiki komputerowej i wizualizacji udostępnionego przez Wydział Matematyki, Informatyki i Mechaniki Uniwersytetu Warszawskiego Autorstwa Dariusza Sawickiego.

Kolejnym krokiem w tworzeniu projektu będzie załadowanie obrazka 3D z pliku i wyświetlenie samych jego krawędzi bez powierzchni. W następnych krokach dodam możliwość przesuwania i obracania obrazka, a ostatnimi elementami będzie wyświetlanie powierzchni i dodanie oświetlenia.

# RAPORT NR 3

Maciej Stefanowski 

#

W ramach projektu udało mi się zrobić część rzeczy założonych w pierwszym raporcie.

Najważniejszą rzeczą jest rysowanie obiektów 3D. Był to główny punkt mojego projektu i cała reszta była oparta o to.

Udało mi się zaimplementować wczytywanie obiektów z pliku. Pliki, których używałem podczas prezentacji były pobranymi z internetu obiektami 3D stworzonymi w blenderze, zapisane w pliku ".obj". Jeden z obiektów stworzyłem sam dla lepszego zrozumienia konstrukcji.

Zamiast zmiany położenia i obracania kamery zdecydowałem, że lepszym sposobem jest obracanie i zmiana położenia obiektu. Robie to za pomocą macierzy przekształceń. Do obracania korzystam z suwaka, który wcześniej miał być do zoomowania.

Zrezygnowałem z przybliżania obiektu, gdyż można przybliżyć obiekt za pomocą zmiany jego położenia.

#

Do ukończenia wszystkich założonych rzeczy pozostało mi usunięcie powierzchni zasłoniętych, ustawienia światła oraz obracanie obiektu myszką. Myślę, że to ostatnie jest najłatwiejsze z podanych, gdyż mam już zaimplementowane macierze przekształceń i wystarczy pobrać wartości z kliknięcia i przesunięcia myszką. 

# README

do zainstalowania - pip3 install PyQt5

do uruchomienia - python3 main_window.py

lpm - przesuwanie obiektu

ppm - obracanie obiektu w OX i OY

scroll - przyblizanie obiektu

suwak - obracanie obiektu w OZ
