from random import randrange

def vyhodnot(pole):
    "Vrátí jednoznakový řetězec podle stavu hry."
    if 'xxx' in pole:
        return 'x' # Vyhrál hráč s křížky.
    elif 'ooo' in pole:
        return 'o' # Vyhrál hráč s kolečky.
    elif '-' not in pole:
        return '!' # Remíza.
    else:
        return '-' # Nikdo nevyhrál, neprohrál a není remíza.

def tah (pole, cislo_policka, symbol):
    "Vrátí herní pole s daným symbolem umístěným na danou pozici."
    return pole[:cislo_policka] + symbol + pole[cislo_policka + 1:]

def tah_hrace (pole):
        while True:
            try:
                pozice = int(input("Na kterou pozici chceš hrát? 0-19 "))
            except ValueError:
                print('To není číslo, zadej číslo. ')
            else:
                if pozice < 0 or pozice >= len(pole):
                    print("Nemůžeš hrát venku z pole, zadej číslo 0-19. ")
                elif pole[pozice] != "-":
                    print("Tam už to nejde, zvol jinou pozici. ")
                else:
                    break
        return tah(pole, pozice, "x")

def tah_pocitace (pole):
    while True:
        pozice = randrange(0,len(pole)) #nebo randrange(len(pole))
        if pole[pozice] == '-':
            return tah(pole, pozice, "o")

def piskvorky1d():
    pole = "-" * 20
    while True:
        print(pole)
        pole = tah_hrace(pole)
        pole = tah_pocitace(pole)
        if vyhodnot(pole) != "-":
            break
    print(pole)
    if vyhodnot(pole) == 'x':
        print('Vyhrála jsi!')
    elif vyhodnot(pole) == 'o':
        print('Počítač vyhrál.')
    else:
        print('Remíza.')
