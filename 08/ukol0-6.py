domaci_zvirata = ['pes', 'kočka', 'králík', 'had']

def jmena_kratsi_5(domaci_zvirata): # ukol1
    ukol1 = []
    for zvire in domaci_zvirata:
        if len(zvire) < 5:
            ukol1.append(zvire)
    return ukol1
print(jmena_kratsi_5(domaci_zvirata))


def jmena_k(domaci_zvirata): # ukol2
    ukol2 = []
    for zvire in domaci_zvirata:
        if zvire[0] == 'k':
            ukol2.append(zvire)
    return ukol2
print(jmena_k(domaci_zvirata))


#ukol3 = input('Zadej slovo, podívám se, jestli se v seznamu zvířat. ')
def je_v_seznamu(ukol3):
    if ukol3 in domaci_zvirata:
        return True
    return False
print(je_v_seznamu('pes'))

ukol4 = ['klokan','pes','had','tygr',]
def porovnani_ukol4(ukol4, domaci_zvirata):
    oba_seznamy = []
    prvni_seznam = []
    druhy_seznam = []
    for zvire2 in ukol4:
        for zvire in domaci_zvirata:
            if zvire == zvire2:
                oba_seznamy.append(zvire)
            elif zvire not in ukol4:
                if zvire not in druhy_seznam: # zajisti, aby se zvirata do seznamu nezapsala pri kazdem pruchodu polem
                    druhy_seznam.append(zvire)
            elif zvire2 not in domaci_zvirata:
                if zvire2 not in prvni_seznam: # zajisti, aby se zvirata do seznamu nezapsala pri kazdem pruchodu polem
                    prvni_seznam.append(zvire2)
    return oba_seznamy, prvni_seznam, druhy_seznam
print(porovnani_ukol4(ukol4, domaci_zvirata))

def serad(domaci_zvirata):
    ukol5 = sorted(domaci_zvirata)
    return ukol5
print(serad(domaci_zvirata))
