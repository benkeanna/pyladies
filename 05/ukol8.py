from random import randrange
soucet = 0

for hrac in range(1,5)
    hod = 0
    while hod1 != 6:
        if hod1 == 6:
            break
        print(hod1)
        soucet1 = soucet1 + hod1
        hod1 = randrange(1,7)
    print('Skóre prvního hráče je: ',soucet1)

while hod2 != 6:
    if hod2 == 6:
        break
    print(hod2)
    soucet2 = soucet2 + hod2
    hod2 = randrange(1,7)
print('Skóre druhého hráče je: ',soucet2)

while hod3 != 6:
    if hod3 == 6:
        break
    print(hod3)
    soucet3 = soucet3 + hod3
    hod3 = randrange(1,7)
print('Skóre třetího hráče je: ',soucet3)

while hod4 != 6:
    if hod4 == 6:
        break
    print(hod4)
    soucet4 = soucet4 + hod4
    hod4 = randrange(1,7)
print('Skóre třetího hráče je: ',soucet4)

if soucet1 >= soucet2 and soucet1 >= soucet3 and soucet1 >= soucet4:
    print('První hráč vyhrál.')
elif soucet2 > soucet1 and soucet2 >= soucet3 and soucet2 >= soucet4:
    print('Druhý hráč vyhrál.')
elif soucet3 > soucet1 and soucet3 > soucet2 and soucet3 >= soucet4:
    print('Třetí hráč vyhrál.')
elif soucet4 > soucet1 and soucet4 > soucet2 and soucet4 > soucet3:
    print('Třetí hráč vyhrál.')
