def vrat_obsah_souboru(jmeno):
    soubor = open('basnicka.txt', encoding = 'utf-8')
    try:
        return soubor.read()
    finally:
        soubor.close()

obsah = vrat_obsah_souboru('basnicka.txt')
print(obsah)
