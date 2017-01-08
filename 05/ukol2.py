from math import sqrt
from turtle import shape
from turtle import forward, left, right, exitonclick

side = int(input('Zadej velikost domečku. '))

shape('turtle')
left(90)
forward(side)
right(90)
forward(side)
right(135)
forward(sqrt(2)*side)
left(135)
forward(side)
left(90)
forward(side)
left(45)
forward((sqrt(2)*side)/2)
left(90)
forward((sqrt(2)*side)/2)
left(90)
forward(sqrt(2)*side)
left(45)

exitonclick()
