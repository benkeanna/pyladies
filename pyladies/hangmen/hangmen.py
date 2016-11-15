import random
import hangmen_men

words =  ['vločka','sníh','kopec']
word = random.choice(words)
string = '-' * len(word)

mistakes = 0

def hangmen_choice(mistakes):
    index = mistakes - 1
    return hangmen_men.hangmen[index]

def change_letter(string, letter, position):
    return string[:position] + letter + string[position + 1:]

game_can_run = True

while game_can_run:
    letter = input('Zadej písmeno: ')
    if letter not in word:
        if mistakes == 9:
            game_can_run = False
            result = False
        else:
            print('Tohle písmenko není ve slově. Zbývá', 9 - mistakes,'pokusů.')
            print(string)
        mistakes = mistakes + 1
        print(hangmen_choice(mistakes))
    elif letter in word:
        if '-' in string:
            position = word.index(letter)
            string = change_letter(string, letter, position)
            print(string)
            if '-' not in string:
                game_can_run = False
                result = True

print('Vyhrála jsi!') if result == True else print('Je mi líto.')
