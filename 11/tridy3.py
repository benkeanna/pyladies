class Zvire:
    pass

class Kotatko(Zvire): # trida
    def __init__(self, jmeno): # metoda te dane tridy
        self.jmeno = jmeno
    def zamnoukej(self): # funkce
        print('{} mňouká'.format(self.jmeno))
    def snez(self, jidlo):
        print('{} jí {}'.format(self.jmeno, jidlo))
    def __str__(self): # metoda / funkce vola se tehdy, kdyz nad objektem udelame print, vhodne pro uzivatele
        return 'Jmenuji se {} a jsem kotě.'.format(self.jmeno)
    def __repr__(self): # ukazuje identifikator daneho objektu, vhodne pro programatory
        return '<Kotatko(jmeno = {})>'.format(self.jmeno) # konvence, pouziva se u metody repr

micka = Kotatko(jmeno='Micka')
micka.snez('myš')

class Pes(Zvire):
    def __init__(self, jmeno):
        self.jmeno = jmeno
    def snez(self, jidlo):
        print('{} jí {} a skáče radostí.'.format(self.jmeno, jidlo))

pes = Pes(jmeno='Alík')
pes.snez('granule')
