def vrat_obsah_souboru(jmeno):
    with open('basnicka2.txt', encoding = 'utf-8') as soubor:
        return soubor.read()

obsah = vrat_obsah_souboru('basnicka2.txt')
print(obsah)
