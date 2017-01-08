from random import randrange
cislo = randrange (3)
def ano_nebo_ne(otazka):
    "Vrátí True nebo False, podle odpovědi uživatele"
    while True:
        odpoved = input(otazka)
        if odpoved == 'ano':
            return True
        elif odpoved == 'ne':
            return False
        else:
            print('Nerozumím! Odpověz "ano" nebo "ne".')

odpoved = True

while odpoved:
    tah_cloveka = input('kámen, nůžky, nebo papír? ')
    if cislo == 0:
        tah_pocitace = 'kámen'
    elif cislo == 1:
        tah_pocitace = 'nůžky'
    elif cislo == 2:
        tah_pocitace = 'papír'
    else:
        print ("Nerozumím.")

    print ('Tvůj tah: ',tah_cloveka)
    print ('Tah počítače: ',tah_pocitace)

    if tah_pocitace == tah_cloveka:
        print ('Plichta.')
    elif (tah_pocitace == 'kámen' and tah_cloveka == 'papír') or (tah_pocitace == 'papír' and tah_cloveka == 'nůžky') or (tah_pocitace == 'nůžky' and tah_cloveka == 'kámen'):
        print ('Vyhrála jsi.')
    elif (tah_pocitace == 'kámen' and tah_cloveka == 'nůžky') or (tah_pocitace == 'nůžky' and tah_cloveka == 'papír') or (tah_pocitace == 'papír'and tah_cloveka == 'kámen'):
        print ('Prohrála jsi.')
    else:
        print('Nerozumím.')

    odpoved = ano_nebo_ne('Chceš pokračovat ve hře? ')

    if odpoved == False:
        break
print('Konec hry.')
