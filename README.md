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
Pygame - pro renderování vizuálů hry
Random - pro možnost náhodně vygenerovat hrací pole
Time - pro snímání času pro skóre

Dokumentace:
program se skládá ze dvou hlavních souborů: funkce.py a miny.py
v souboru funkce.py jsou definované hlavní funkce zodpovědné za fungování kódu
v souboru miny.py je hlavní kód, který využívá funkce z druhého souboru, dále 
jsou zde načteny vizuály a pár základních funkcí pro renderování okna a hry.
oba soubory jsou blíže popsané jako součást kódu

dále je v příloze dalších 15 png souborů ze kterých se skládá vizuál hry

Zdroje
https://www.youtube.com/watch?v=y9VG3Pztok8&ab_channel=CodingWithRuss
https://www.youtube.com/watch?v=8j7bkNXNx4M&ab_channel=AppleMaths
http://datagenetics.com/blog/june12012/index.html
https://www.pygame.org/docs/
