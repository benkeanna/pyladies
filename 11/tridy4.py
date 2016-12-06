class Zvire:
    def __init__(self, jmeno): # metoda te dane tridy
        self.jmeno = jmeno
    def snez(self, jidlo):
        print('{} jí {}'.format(self.jmeno, jidlo))

class Kotatko(Zvire): # trida
    def zamnoukej(self): # funkce
        print('{} mňouká'.format(self.jmeno))
    def snez(self, jidlo):
        print('{} kouká na {}'.format(self.jmeno, jidlo))
        if jidlo == 'cihlu':
            print('Fuj')
        else:
            super().snez(jidlo) # pouzije se fuknce nadrazene metody
    def __str__(self): # metoda / funkce vola se tehdy, kdyz nad objektem udelame print, vhodne pro uzivatele
        return 'Jmenuji se {} a jsem kotě.'.format(self.jmeno)
    def __repr__(self): # ukazuje identifikator daneho objektu, vhodne pro programatory
        return '<Kotatko(jmeno = {})>'.format(self.jmeno) # konvence, pouziva se u metody repr

micka = Kotatko(jmeno='Micka')
micka.snez('myš')

class Pes(Zvire):
    def snez(self, jidlo):
        print('{} jí {} a skáče radostí.'.format(self.jmeno, jidlo))

pes = Pes(jmeno='Alík')
pes.snez('granule')

zvire1 = Zvire(jmeno='Courek')
zvire1.snez('mléko')

print('....................')
zvirata = [Kotatko(jmeno='Micka'), Pes(jmeno='Alík'), Zvire(jmeno='Courek')]
for zvire in zvirata:
    zvire.snez('cihlu')
