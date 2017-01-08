from random import randrange

def vyhodnot(pole):
    "vrati kod pdole stavu hry"
    #pole je napr ------x--o---xxx---
    if "xxx" in pole:
        return "x"
    elif "ooo" in pole:
        return "o"
    elif "-" not in pole:
        return "!"
    else:
        return "-"
def tah(pole, cislo_policka, symbol):

    return (pole[:cislo_policka] + symbol + pole[cislo_policka+1:])

def tah_hrace (pole):
        while True:
            pozice = int(input("Na kterou pozici chces hrat?"))
            if pozice < 0:
                print("zaporna policka nejsou")
            elif pozice >= len(pole):
                print("to je moc")
            elif pole[pozice] != "-":
                print("tam uz to nejde")
            else:
                break
        return tah(pole, pozice, "o")
def tah_pocitace (pole):
    while True:
        pozice = randrange(0,20) #nebo randrange(len(pole))
        if pole[pozice] == '-':
            return tah(pole, pozice, "x")

def piskvorky1d():
    pole = "-" * 20
    while True:
        print(pole)
        pole = tah_hrace(pole)
        pole = tah_pocitace(pole)
        if vyhodnot(pole) != "-":
            break
    print(pole)
    print("Vyhrál", vyhodnot(pole))

piskvorky1d()
