ja = {'jmeno': 'Anna', 'misto': 'Brno','cisla': [3,7]}

print(ja)
print(ja['jmeno'])
#print(ja['vek']) Key error

ja['vek'] = 24 # pridani prvku
print(ja)

ja['cisla'] = [3,7,23] # pridani do slovniku
print(ja)

del ja['vek'] # smazani seznamu
print(ja)



barvy = {'jablko': 'cervene',
    'hruska': 'zelena',
    'meloun':'zeleny',
}
print(barvy)
print('jablko:', barvy['jablko'])

for ovoce in sorted(barvy):
    print(barvy[ovoce])

for barva in barvy.values(): # hodnoty
    print('values',barva)

for zaznam in barvy.items(): # dvojice klic hodnota
    ovoce, barva = zaznam
    print('items',ovoce,barva)

for ovoce, barva in barvy.items(): # dvojice klic hodnota
    print('items2',ovoce,barva)

for ovoce, barva in barvy.items(): # dvojice klic hodnota
    print('{ovoce} je {barva}'.format(ovoce = ovoce, barva = barva))


popisky_funkci = {
len: 'delka',
str: 'prevod na retezec',
print:' vypis',
}
print(popisky_funkci)

for funkce, popisek in popisky_funkci.items():
    print(funkce)
    print('     ', popisek)

barvy_po_tydnu = (dict(barvy))
print(barvy)

for ovoce, barva in barvy_po_tydnu.items():
    barvy_po_tydnu[ovoce] = 'cerno-hnedo' + barva

print(barvy_po_tydnu)


seznam_dvojic = [('svestka', 'modra'), ('citron', 'zluty')]
print(seznam_dvojic)

print(dict(seznam_dvojic))

print(dict(jmeno = 'Anna', misto ='Brno'))
