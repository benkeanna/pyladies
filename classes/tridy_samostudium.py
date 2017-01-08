class Kotatko: # trida Kotatko
    def zamnoukej(self): # metoda tridy Kotatko
        print('mňau') # co metoda dela

kotatko1 = Kotatko() # vytvoreni konkretni instance tridy Kotatko
kotatko1.zamnoukej() # zavolani metody tridy Kotatko na konkretni instanci tridy Kotatko

mourek = Kotatko()
mourek.jmeno = 'Mourek'

micka = Kotatko()
micka.jmeno = 'Micka'

print(mourek.jmeno, micka.jmeno)
print('***********************')

class Kote:
    def mnoukej(self):
        print(self.jmeno, 'mňouká')

micinka = Kote()
micinka.jmeno = 'Micinka'
mourecek = Kote()
mourecek.jmeno = 'Moureček'

micinka.mnoukej()
mourecek.mnoukej()

print('*************************')

class Kote_ji:
    def snez(self,jidlo):
        print(self.jmeno,'mňouká,', jidlo, 'mu chutná.')

courek = Kote_ji()
courek.jmeno = 'Courek'
courek.snez('ryba')
print('************************')

class Kotatecko:
    def __init__(self, jmeno):
        self.jmeno = jmeno
    def __str__(self):
        return '<Kotatko jmenem {}>'.format(self.jmeno)
    def mnouk(self):
        print('{} mnouka'.format(self.jmeno))

mouris = Kotatecko('Mouris')
mouris.mnouk()
