import turtle

class MojeZelvicka(turtle.Turtle):
    def neco_udelej(self):
        self.forward(50)

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

# sipka = turtle.Turtle(shape='arrow')
# krouzek = turtle.Turtle(shape='circle')

mz1 = MojeZelvicka(shape="turtle")
mz2 = Kresli_ctverec(shape="square")
mz3 = Kresli_trojuhelnik(shape='triangle')

# sipka.forward(100)
# sipka.left(10)
# sipka.forward(100)

# krouzek.forward(100)
# krouzek.left(20)
# krouzek.forward(100)

mz1.neco_udelej()
mz2.neco_udelej()
mz3.neco_udelej()

turtle.exitonclick()
