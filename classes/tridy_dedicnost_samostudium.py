class Animal(): # nadtrida zahrnujici vsechny zvirata
    def __init__(self, name): # jmeno se definuje uz tady a ne ay pak u kaydeho zvirete zvlast
        self.name = name
    def eat(self, food): # metoda snez se muze definovat tady a ne u kazdeho zvirete zvlast
        print(self.name,'eats',food)

class Kitty(Animal): # podtrida Kitty dedi y nadtridy Animal
    def make_sound(self): # metoda se stejnym principem jako u psa, da se pojemnovat stejne, aby se mohla najednou zavolat
        print(self.name,'meows') # neda se napsat jednou v nadtride, protoze ma odlisne vysledky
    def eat(self, food):
        print(self.name,'do not like',food) # nadrazena metoda, kdyz chci prepsat metodu pouzitou v nadtride
        super().eat(food) # pouziti metody y nadtridy

class Doggy(Animal):
    def make_sound(self): # metoda se stejnym principem jako u psa, da se pojemnovat stejne, aby se mohla najednou zavolat
        print(self.name,'barks') # neda se napsat jednou v nadtride, protoze ma odlisne vysledky

class Sneaky(Animal):
    def __init__(self, name): # nadrazena metoda, kdy krome metody z nadtridy chci udelat jeste neco jineho
        name = name.replace('S','Ssss')
        super().__init__(name)  # pouziti metody y nadtridy


cate = Kitty('Cate') # vytvoreni instace tridy Kitty a prirazeni atributu
cate.eat('tuna') # zavolani metody, kam je nutne vlozit argument
cate.make_sound() # zavolani metody

doge = Doggy('Doge') # vytvoreni instace tridy Kitty a prirazeni atributu
doge.eat('pizza') # zavolani metody, kam je nutne vlozit argument
doge.make_sound() # zavolani metody

snek = Sneaky('Snek') # vytvoreni instace tridy Kitty a prirazeni atributu
snek.eat('elephant') # zavolani metody, kam je nutne vlozit argument

animals = [Kitty('Small Cate'),Doggy('Small Doge')] # vytvoreni seznamu instaci tridy Kitty a prirazeni atributu

for animal in animals:
    animal.make_sound() # pouziti metody pro vsechny instance v seznamu
    animal.eat('steak') # pouziti metody s argumentem pro vsechny instance v seznamu
