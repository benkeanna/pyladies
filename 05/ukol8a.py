from random import randrange
soucet = 0


for hrac in range(1,5)
    hod = 0
    print('Házíhráč ', hrac)
    while True:
        soucet1 = soucet1 + hod1
        hod1 = randrange(1,7)
        soucet1 = soucet1 + hod1
        if hod1 == 6:
            break

    print('Skóre hráče je: ',soucet1)


if soucet1 >= soucet2 and soucet1 >= soucet3 and soucet1 >= soucet4:
    print('První hráč vyhrál.')
elif soucet2 > soucet1 and soucet2 >= soucet3 and soucet2 >= soucet4:
    print('Druhý hráč vyhrál.')
elif soucet3 > soucet1 and soucet3 > soucet2 and soucet3 >= soucet4:
    print('Třetí hráč vyhrál.')
elif soucet4 > soucet1 and soucet4 > soucet2 and soucet4 > soucet3:
    print('Třetí hráč vyhrál.')
