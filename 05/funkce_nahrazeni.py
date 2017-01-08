retezec = input('Zadej slovo: ')
pozice = int(input('Kolikaty znak se vymeni? '))
znak = input('Za co vymenime? ')

def nahrazeni (retezec, pozice, znak):
    '''Zameni znak na urcite pozici'''
    return retezec[:pozice-1] + znak + retezec[pozice:]

vysledek = nahrazeni(retezec,pozice,znak)
print(vysledek)
