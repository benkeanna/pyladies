def nakresli_mapu(velikost = 10):
    pole = []
    for i in range(velikost):
        radek = []
        for j in range(velikost):
            radek.append('.')
        pole.append(radek)
    return pole
play_field = nakresli_mapu()


def exchange(x,y):
    play_field[x][y] = 'x'
    return play_field

#exchange(2,3)
pohyb = input('Zadej světovou stranu S,J,V,Z.  ')

had = [(0,0), (1,0), (2,0)]

def pohyb(had, pohyb):
    if pohyb == 's':
        return had


print(pohyb(had,pohyb))





for line in play_field:
    for part in line:
        print(part,end=' ')
    print()
