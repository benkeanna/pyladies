import turtle

class Kresli_ctverec(turtle.Turtle):
    def neco_udelej(self):
        for i in range(4):
            self.forward(200)
            self.left(90)

class Kresli_trojuhelnik(turtle.Turtle):
    def neco_udelej(self):
        for i in range(3):
            self.forward(300)
            self.left(120)

mz2 = Kresli_ctverec(shape="square")
mz3 = Kresli_trojuhelnik(shape='triangle')

objekty = [Kresli_ctverec(), Kresli_trojuhelnik]

for objekt in objekty:
    objekt.neco_udelej()

turtle.exitonclick()
