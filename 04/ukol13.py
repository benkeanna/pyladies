radky = 5
sloupce = 6
for i in range(5):
    for j in range(6):
        if (i == 0) or (j == 0) or (i == radky-1) or (j == sloupce-1):
            print("X", end=" ")
        else:
            print(" ", end=" ")

    print()
