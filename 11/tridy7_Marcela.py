
import turtle

class KreslimObecne(turtle.Turtle):
    POCET_HRAN = 0
    UHEL_OTOCENI = 0

    def neco_udelej(self):
        for x in range(self.POCET_HRAN):
            self.forward(50)
            self.left(self.UHEL_OTOCENI)

class KreslimCtverec(KreslimObecne):
    POCET_HRAN = 4
    UHEL_OTOCENI = 90

class KreslimTroj(KreslimObecne):
    POCET_HRAN = 3
    UHEL_OTOCENI = 120

class KreslimMnohouhelnik(KreslimObecne):
    POCET_HRAN = 18
    UHEL_OTOCENI = 20



objekty = [KreslimCtverec(), KreslimTroj(), KreslimMnohouhelnik()]
for objekt in objekty:
    objekt.neco_udelej()


turtle.exitonclick()
