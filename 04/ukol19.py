cislo1 = int(input('Zadej první číslo: '))
cislo2 = int(input('Zadej druhé číslo: '))
cislo3 = int(input('Zadej třetí číslo: '))

vysledek = cislo1 + cislo2 + cislo3
print(vysledek)

if vysledek > 10:
    print('Výsledek je větší než 10.')
else:
    print('Výsledek je menší nebo rovno 10.')
