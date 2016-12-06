class Kotatko:
    pass

kotatko1 = Kotatko()
kotatko2 = Kotatko()

kotatko1.jmeno = 'Micka'
kotatko2.jmeno = 'Mourek'

class Kotatko: # trida
    def __init__(self, jmeno): # metoda te dane tridy
        self.jmeno = jmeno
    def zamnoukej(self): # funkce
        print('{} mňouká'.format(self.jmeno))
    def __str__(self): # metoda / funkce vola se tehdy, kdyz nad objektem udelame print, vhodne pro uzivatele
        return 'Jmenuji se {} a jsem kotě.'.format(self.jmeno)
        def __repr__(self): # ukazuje identifikator daneho objektu, vhodne pro programatory
            return '<Kotatko(jmeno = {})>'.format(self.jmeno) # konvence, pouziva se u metody repr

kotatko1 = Kotatko('Micka')
kotatko1.zamnoukej() # zavolani tridy, ktera vytiskne mnoukani ve funkci zamnoukej

micka = Kotatko(jmeno='Micka')
micka.zamnoukej()
print(micka)

mourek = Kotatko(jmeno='Mourek')
mourek.zamnoukej()
print(mourek)

kotata = [micka, mourek]
for kote in kotata:
    kote.zamnoukej()

print(kotata)
