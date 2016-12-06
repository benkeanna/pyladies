class Kotatko: # trida ma velke prvni pismeno
    pass

kotatko1 = Kotatko()
kotatko2 = Kotatko()

kotatko1.jmeno = 'Micka'
kotatko2.jmeno = 'Mourek'

tmp = kotatko1
print(tmp.jmeno)

def zamnoukej_f(kote):
    print('{} mňouká'.format(kote.jmeno))

print(zamnoukej_f(kotatko1))


class Kotatko2: # trida
    def __init__(self, jmeno): # metoda te dane tridy
        self.jmeno = jmeno
    def zamnoukej(self): # funkce
        print('{} mnouka'.format(self.jmeno))

kotatko1
