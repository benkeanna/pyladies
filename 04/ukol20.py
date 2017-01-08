cislo = int(input('Zadej číslo: '))
zbytek_po_deleni = cislo%2

print(zbytek_po_deleni)

odpoved = 'Číslo je sudé.' if zbytek_po_deleni == 0 else 'Číslo je liché.'

print(odpoved)
