from math import sin

print(sin(8))
print(sin)

magicke_cislo = sin
vysledek = magicke_cislo(8)
print(vysledek)



zvirata = ['liška','kočka','pes','had']

def radici_klic(zvire):
    return zvire[1:]
print(radici_klic('housenka'))

zvirata.sort(key = radici_klic)
print(zvirata)
