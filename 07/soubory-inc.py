def iniciala():
    with open('basnicka.txt', encoding='utf-8') as soubor:
        obsah = soubor.read()
        return obsah[0]
print(iniciala())
