domaci_zvirata = ['andulka', 'pes', 'kocka', 'kralik', 'had']

def hadovo_razeni(seznam):

    seznam_dvojic = []
    for zvire in seznam:
        seznam_dvojic.append((zvire[1], zvire))

    #print(seznam_dvojic)

    seznam_dvojic.sort()
    #print(seznam_dvojic)

    vysledek = []
    for prvek in seznam_dvojic:
        vysledek.append(prvek[1])

    print(vysledek)

hadovo_razeni(domaci_zvirata)
