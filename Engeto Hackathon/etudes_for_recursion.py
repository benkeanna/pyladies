number = 5

def factorial(number):
    if number == 0:
        return 1
    else:
        return (factorial(number -1) * number)

print(factorial(number))


def fibbonaci(number):
    if number == 1 or number == 2:
        return 1
    return fibbonaci(number - 1) + fibbonaci (number - 2)

print (fibbonaci(number))

u = 40902
w = 24140 #Mějme dána dvě přirozená čísla, uložená v proměnných u a w.
def divisor(u, w):
    while w != 0: # Dokud w není nulové, opakuj:
        r = u % w #  Do r ulož zbytek po dělení čísla u číslem w
        u = w #  Do u ulož w
        w = r #  Do w ulož r
    return u

print(divisor(u,w)) #Konec algoritmu, v u je uložen největší společný dělitel původních čísel.
# vysledek je 34
