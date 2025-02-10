Miny
Implementace klasické hry Minesweeper s funkcionalitou "férovosti"
Férovost znamená, že jsou přidána 2 nová pravidla
1) jestliže hráč nemá žádnou 100% jistotu u žádné buňky tak platí, že ať klikne na jakoukoliv tak tam bomba nebude
2) Jestliže hráč má 100% jistotu na nějaké buňce a rozhodne se kliknout jinam, tak na dané buňce vždy bomba bude a hráč prohraje

How to play:
po zapnutí hry se otevře okno s výběrem parametrů, zde si může hráč vybrat obtížnost,
po výběru se hra sama zapne v novém okně, při výběru custom bude hráčovi nabídnuta možnost 
sám si vybrat parametry hry, toto je přirozené číslo v rozmezí 1 - 999, zadá se stisknutím ENTER.

Po spuštění hry hráč odkryje minu levým tlačítkem myši, pravým tlačítkem myši položí vlaječku.
Stisknutím tlačítka R se restartuje hra v aktuální obtížnosti.

Hra používá následující knihovny:
- Pygame - pro rendero- vání vizuálů hry
- Random - pro možnost náhodně vygenerovat hrací pole
- Time - pro snímání času pro skóre

Dokumentace programu a funkcí:
program se skládá ze dvou hlavních souborů: funkce.py a miny.py
- v souboru funkce.py jsou definované hlavní funkce zodpovědné za fungování kódu
- zde jsou následující funkce
1. new_game_grid(šířka, výška, počet min)
    - vrátí pole dane velikosti s 1 nebo 0 lokacema min
2. empty_grid(šířka, výška) 
    - vrátí pole None o dané velikosti
3. is_in_grid(šířka, výška, pozice ve tvaru (x, y))
    - vrátí True zda leží v daném souřadnicovém prostoru
4. surrounding_cells((x, y), grid)
    - vrátí list všech buněk v okruhu 1 buňky
5. cell_number((x, y), pole s bombama)
    - spočítá a vrátí číslo buňky na základu počtu bomb v okolních buňkách
    - toto je provedeno využitím funkce surrounding_cells ze kterých se podívá zda jejich souřadnice v poli s bombama dávají  1 a jestli ano tak přičtou k čísle buňky 1 
6. lostgame(odkryté pole, pole bomb)
    - vrátí plně odkryté pole, v případě že celé odkryté není - označí špatně označené miny
7. wongame(odkryté pole, pole bomb)
    - vrátí plně odkryté pole, v případě že celé odkryté není
8. zero_chain(odkryté pole, pole bomb, list nulových buňěk)
    - pro každou buňku z odkrytého pole která má číslo 0 a nenachází se v listu již odkrytých buněk odkryje 8 okolních a přidá ji do listu odkrytých buňěk. Toto se opakuje dokud všechny 0 buňky nejsou v listu odkrytých nulových buňěk.
    - následně vrátí pole odrytých buňěk a upravený list nulových buňěk

9. simple_filter(pole odkryté, pole min, pole jistých kroků)
    - pro každou buňku z odkrytých buněk se podívá jestli počet správně položený vlajek a počet jistých min v okolních buňkách roven číslu buňky, jestliže ano tak označí ostatní buňky které nejsou označené v poli jistých kroků a zároveň ještě nejsou odkryté za False.
    - Podobně když se počet vlajek a jistých min v okolí společně s počtem neodkrytých okolních buněk rovná číslu buňky tak tyto neodkryté buňky jsou bomby a označeny za True
    - vrací pole jistých kroků
10. complex_filter(pole odkryté, pole min, pole jistých kroků):
    - vytvoří si list krajních buněk z odkrytého pole 
    - pro každou tuto krajní buňku si to najde její dynamické číslo (číslo buňky minus počet jistých min a vlajek v okolí), list okolních krajních min, a také list okolních buňěk které zatím nejsou odkryty a nejsme si jisti zda na nich je nebo není mina   
    - poté pro každou okolní krajní minu to najde její dynamické číslo a počet okolních buňěk kterými si nejsme jisti zda jsou miny.
    - následně to vytvoří dva listy nejistých buněk, jeden pouze z těch kolem 1. buňky a jeden pouze z naší 2. buňky    
    - jestliže rozdíl dynamického čísla 2. buňky a dynamického čísla 1. buňky je roven velikosti listu 2. buňky tak to všechny buňky 1. listu v poli jistých kroků nastaví na False a naopak všechny buňky 2. listu v poli jistých kroků nastaví na True
    - vrací pole jistých kroků
11. is_there_next_step(odkryté pole, pole min):
    - vytvoří to prázdné pole jistých kroků se kterým provede simple_filter, complex_filter a opět simple_filter
    - poté si zkontroluje že je v tomto poli nějaký jakýkoliv jistý tah do proměnné possible_step    
    - vrací tuto proměnnou possible_step a také list jistých tahů
    - v souboru miny.py je hlavní kód, který využívá funkce z druhého souboru, dále 
jsou zde načteny vizuály a pár základních funkcí pro renderování okna a hry.
nachází se zdevykreslovací funkce, které není potřeba moc vysvětlovat:
parameters()
    - vytvoří okno ve kterém si hráč může zvolit jednu z obtížností, případně zvolit náhodnou obtížnost či obtížnost volitelných rozměrů a počtu min
start_game(výška, šířka, počet min)
    - nastartuje hru a nastaví hlavní proměnné a okno s herním polem
draw_frame(okno, odkryté pole, velikost buňky)
    - vykreslí daný stav hracího pole do okna pomocí spritů či textu
v průběhu hry se každý frame program podívá zda hráč někam kliknul a na základě toho updatuje hrací pole. K tomu využívá funkce z funkce.py, na konci každého framu se vykreslí znovu stav hracího pole.

- oba soubory jsou blíže popsané jako součást kódu

- dále je v příloze dalších 15 png souborů ze kterých se skládá vizuál hry

Zdroje
- https://www.youtube.com/watch?v=y9VG3Pztok8&ab_channel=CodingWithRuss
- https://www.youtube.com/watch?v=8j7bkNXNx4M&ab_channel=AppleMaths
- http://datagenetics.com/blog/june12012/index.html
- https://www.pygame.org/docs/