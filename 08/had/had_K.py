pozicex = 0
pozicey = 0
seznam_souradnic = []

while True:
    smer = input("Zadej směr pohybu (s,j,v,z):")
    # for souradnice in hraci_pole:
    souradnice = ([pozicex,pozicey])
    # potrebuji aby se to prepisovalo - jak - tzn aby se to vzdy ulozilo - hotovo problem z v na z a z j na s
    if smer == 'v':
        souradnice = ([pozicex,pozicey+1])
        pozicey += 1
    elif smer =='z':
        souradnice = ([pozicex,pozicey-1])
        pozicey -= 1
    elif smer == 'j':
        souradnice = ([pozicex + 1, pozicey])
        pozicex += 1
    elif smer == 's':
        souradnice = ([pozicex - 1 ,pozicey])
        pozicex -= 1
    seznam_souradnic.append(souradnice)

    # if len(seznam_souradnic) == 2:
    #     seznam_souradnic.pop(0)
    #    
