radek = 5
sloupec = 4
for i in range(radek):
    nula = 0
    print(nula)
    for j in range(sloupec):
        end = ' '
        if j == sloupec-1:
            end = "\n"
        print(nula, end=end)
        nula = nula +j
