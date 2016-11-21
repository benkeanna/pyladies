size = 10 # velikost hraciho pole
def make_play_field(size): # vytvoreni hraciho pole
    pole = []
    for i in range(size):
        radek = []
        for j in range(size):
            radek.append('.')
        pole.append(radek)
    return pole
play_field = make_play_field(size)

def exchange(x,y):
    play_field[x][y] = 'x'
    return play_field

def pohyb(smer, seznam_souradnic):
    if smer == 'v':
        souradnice = ([pozicex,pozicey+1])
        pozicey += 1
        seznam_souradnic.append(souradnice)
        exchange(pozicex,pozicey)
    elif smer =='z':
        souradnice = ([pozicex,pozicey-1])
        pozicey -= 1
        seznam_souradnic.append(souradnice)
        exchange(pozicex,pozicey)
    elif smer == 'j':
        souradnice = ([pozicex + 1, pozicey])
        pozicex += 1
        seznam_souradnic.append(souradnice)
        exchange(pozicex,pozicey)
    elif smer == 's':
        souradnice = ([pozicex - 1 ,pozicey])
        pozicex -= 1
        seznam_souradnic.append(souradnice)
        exchange(pozicex,pozicey)
    else:
        pass
    return seznam_souradnic

seznam_souradnic = []
pozicex = 0
pozicey = 0
while True:
    smer = input('Zadej směr pohybu (s,j,v,z) nebo konec: ')
    pohyb(smer, seznam_souradnic)
    for line in play_field:
        for part in line:
            print(part,end=' ')
        print()
