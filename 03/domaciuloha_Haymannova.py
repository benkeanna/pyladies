from turtle import shape
from turtle import forward, left, right, penup, pendown, circle, exitonclick
from random import randrange

odpoved = input('Těšíš se na zimu? Odpověz ano nebo ne. ')

if odpoved == 'ano':
    odpoved = True
    print('Mám pro tebe malé překvapení.')
    pocet_vlocek = int(input('Jak moc chceš aby sněžilo? Na stupnici od jedné do kolika chceš.. '))
elif odpoved == 'ne':
    odpoved = False
    print('Pro tebe bohužel překvapení nemám. Alespoň se ohřej na sluníčku.')
else:
    print('Odpověz prosím "ano" nebo "ne".')

if odpoved:
    for i in range (pocet_vlocek):
        right(90)
        for j in range(6):
            pendown()
            forward(30)
            penup()
            left(180)
            forward(15)
            left(135)
            pendown()
            forward(15)
            penup()
            left(180)
            forward(15)
            right(90)
            pendown()
            forward(15)
            penup()
            left(180)
            forward(15)
            right(45)
            forward(15)
            pendown()
            left(120)
        penup()
        otoceni = randrange(0,360)
        left(otoceni)
        posun = randrange(40,400)
        forward(posun)

if not odpoved:
    for k in range(12):
        circle(20,30)
        right(90)
        forward(10)
        penup()
        right(180)
        forward(10)
        right(90)
        pendown()

exitonclick()
