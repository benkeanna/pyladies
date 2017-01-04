class Dog:
    def __init__(self, legs, colour):
        self.legs = legs
        self.colour = colour
        self.alive = True
    def zastekej(self):
        print('Haf')
    def umri(self): # setter
        self.alive = False
    def zije(self): # getter
        return self.alive
    def set_legs_count(self, legss):
        self.legs = legss

fido = Dog(4, "brown")
spot = Dog(3, "mostly yellow")

print(fido.legs)
print(spot)

fido.zastekej()
print(fido.zije())
fido.umri()
print(fido.zije())
fido.set_legs_count(32)
print(fido.legs)
