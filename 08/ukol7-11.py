soubor = open('basnicka.txt', encoding = 'utf-8')
basnicka = soubor.read()

basnicka_split = basnicka.split('\n')
print(basnicka_split)

basnicka_split.reverse()
print(basnicka_split)

basnicka_split2 = basnicka.split('\n\n')
print(basnicka_split2)

basnicka_split2.reverse()
print(basnicka_split2)
