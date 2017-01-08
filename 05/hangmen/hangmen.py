import random
import hangmen_men

words =  ['vločka','sníh','kopec']
word = random.choice(words) # vyber slova pro hru
string = '-' * len(word)
print(string) # vypsani prvniho prazdneho pole
mistakes = 0


def hangmen_choice(mistakes): # funkce vrati obrazek obesence podle poctu chyb
    index = mistakes - 1
    return hangmen_men.hangmen[index]

def change_letter(string, letter, position): # funkce zameni pismenko v retezci pokud tam je
    return string[:position] + letter + string[position + 1:]

game_can_run = True # stavova hodnota hry, zmeni se pokud je vyuzito max mnozstvi chyb

while game_can_run:
    letter = input('Zadej písmeno: ')
    if letter not in word: # vetev pokud pismenko neni v retezci
        if mistakes == len(hangmen_men.hangmen)-1: # pokud uz je udelano max moznych chyb
            game_can_run = False # stavova hodnota hry je False, smycka a hra konci
            result = False # vysledek hry, vyhodnoti se na konci programu
        else:
            print('Tohle písmenko není ve slově. Zbývá', len(hangmen_men.hangmen)-1 - mistakes,'pokusů.')
            print(string)
        mistakes = mistakes + 1
        print(hangmen_choice(mistakes)) # vypise se obesenec podle poctu chyb
    elif letter in word: # vetev pokud pismenko je v retezci
        if '-' in string: # pokud je v retexci volne misto
            position = word.index(letter)
            string = change_letter(string, letter, position) # nahrazeni - za spravne pismenko
            print(string)
            if '-' not in string: # pokud uz je retezec plny
                game_can_run = False # stavova hodnota hry je False, smycka a hra konci
                result = True # vysledek hry vyhodnoti se na konci programu

print('Vyhrála jsi!') if result == True else print('Je mi líto.') # vyhodnoceni hry
