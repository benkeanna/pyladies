# Při plánování Ježíškových cest za doručením dárků se počítá s co nejčastějšími zastávkami, aby si Ježíšek při tom shonu zvládl taky trochu odpočinout.
# Proto se plánovací oddělení Ježíškových spojených závodů již dávno rozhodlo, že cesty mezi jednotlivými obdarovanými mají být co nejkratší.
# Pomoz jim s řešením tohoto problému.
# Mapy, které toto oddělení používá, jsou ve zobrazení SJTSK (Systém Ježíškovy trigonometrické sítě katastrální) speciálně uzpůsobeny tak,
# že se jedná o karteziánskou soustavu souřadnic (nám známé na sebe kolmé osy x a y z matematiky) a jednotky měření jsou v metrech.
# Díky tomu můžeme jednotlivé body na mapě, na nichž se nachází vánoční stromky obdarovaných, mezi sebou porovnat a odhalit, který bod je od současné souřadnice nejblíže.
# Vytvoř funkci, která vezme tyto body ve tvaru [x, y] a seřadí je tak, že prvním výchozím bodem bude vždy [0, 0] a druhým bodem bude bod, který je prvnímu bodu nejblíže.
# Třetím bodem bude bod, který je druhému bodu nejblíže a zároveň tam Ježíšek ještě nebyl.
# Počítej s tím, že žádný bod se v seznamu nebude opakovat a jeho souřadnice x a y budou vždy kladné (to je výhoda právě toho speciálního zobrazení).
# Vstupem je seznam bodů ve formátu [x, y] a výstupem seznam bodů seřazený podle definovaného pravidla.
# Příklad:
# planTheRoad([[1,0], [1, 2], [3, 2], [2, 2], [1, 1], [12, 5], [123, 321], [50, 5] , [100, 100], [4, 4]])
# Nápověda: Vzpomeň si na Pythagora
