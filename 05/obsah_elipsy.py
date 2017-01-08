from math import pi
def obsah_elipsy(velka_poloosa, mala_poloosa):
    "Funkce počítá obsah elipsy."
    return pi * velka_poloosa * mala_poloosa

vysledek = obsah_elipsy(3,4)
print(vysledek)
