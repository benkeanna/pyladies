# V předchozím úkolu jsme vytvořili nástroj, který Ježíškovým pomocníkům umožňuje šifrovat dopisy Ježíškovi.
# Bohužel si u těch zašifrovaných textů zapomněli poznamenat, o kolik posunuli písmena, a teď nemohou texty přečíst.
# Naštěstí pro ně, nezvolili neprolomitelnou šifru a my tedy můžeme vytvořit nástroj, který jim pomůže si záznamy znovu přečíst.
# Využijeme toho, že každý text obsahuje spojení: “mily jezisku” (pamatujte, bez háčků a čárek a anglická abeceda) a právě pomocí slova “jezisku” šifru prolomíme.
# Anglická abeceda totiž obsahuje 26 písmen, a to je právě počet možných posunů.
# My vyzkoušíme všechny jeden po druhém a pokud posunutý text bude obsahovat slovo “jezisku”, podařilo se nám najít řešení a rozšifrovat text.
# Vstupem je řetězec zašifrovaný caesarovou šifrou a výstupem rozšifrovaný text.
