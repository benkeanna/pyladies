from random import randrange

def nakresli_mapu(souradnice, ovoce): # vytvoreni hraciho pole
    print('-'*20)
    for radek in range(10):
        for sloupec in range(10):
            if (sloupec, radek) in ovoce:
                print('?', end = ' ')
            elif (sloupec, radek) in souradnice:
                print('x', end = ' ')
            else:
                print('.', end=' ')
        print()

souradnice = [(0,0),(0,1),(0,2)]
nakresli_mapu(souradnice)

def pohyb(souradnice, ovoce, strana):
    posledni_bod = souradnice[-1]
    x, y = posledni_bod
    if strana == 'j':
        novy_bod = x ,y + 1
    elif strana == 's':
        novy_bod = x ,y - 1
    elif strana == 'v':
        novy_bod = x + 1 ,y
    elif strana == 'z':
        novy_bod = x - 1 ,y
    else:
        raise ValueError(strana)
    x, y = novy_bod
    if x < 0 or y < 0 or x >= 10 or y >= 10:
        raise ValueError('game over')
    if novy_bod in souradnice:
        raise ValueError('game over')
    if novy_bod in ovoce:
        ovoce.remove(novy_bod)
        x = randrange(0,10)
        y = randrange(0,10)
        nove_ovoce = x,y
        ovoce.append(nove_ovoce)
    else:
        del souradnice[0]
    souradnice.append(novy_bod)
    del souradnice[0]

souradnice = [(0,0)]
while True:
    nakresli_mapu(souradnice)
    strana = input('Zadej stranu: ')
    pohyb(souradnice, strana)
