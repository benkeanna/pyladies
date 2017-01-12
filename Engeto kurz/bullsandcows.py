# game bulls and cows in python 3

import random
field_size = 4 # pocet cislic, ktere hrac hada
puzzle = random.sample(range(1, 10), field_size) # nahodne generovane cislice, ktere hrac hada
number_of_guesses = 0 # pocet pokusu, ktery se bude zvetsovat po kazdem tahu hrace

class CheckInput: # kontrola, jestli je vstup 4-mistne cislo s ruznymi cislicemi
    def __init__(self, user_input):
        self.input = user_input

    def check_if_input_is_int(self): # kontrola, ze vstup jsou cislice
        try:
            int(self.input)
        except ValueError:
            return False
        else:
            return True

    def check_digits_count(self): # kontrola 4-mistneho vstupu
        return True if len(str(self.input)) == 4 else False

    def check_if_digits_are_different(self): # kontrola, ze vstup obsahuje 4 ruzne cislice
        number_of_occur = []
        for number in self.input:
            number_of_occur.append(self.input.count(number)) # pocet vyskytu jednotlivych cislic ve vstupu
        return True if sum(number_of_occur) == len(str(self.input)) else False # suma vyskytu jednotlivých cislic ma byt stejna jako delka vstupu - kazda polozka je v nem jenom jednou


print('Welcome in game cows and bulls. In this game you will have to quess the puzzle made of four different digits.')
while True:
    while True: # vstup a overeni jeho validity
        user_input = input('Enter four different digits ')
        guess_input = CheckInput(user_input)
        if guess_input.check_digits_count() and guess_input.check_if_input_is_int() and guess_input.check_if_digits_are_different(): # overeni, jestli je vstup 4-mistne cislo s ruznymi cislicemi
            break
        else:
            print('These are not four different digits')
            pass

    guess = list(guess_input.input) # vytvoreni seznamu z inputu pro porovnani s puzzle
    guess = [ int(x) for x in guess ] # pretypovani elementu v seznamu na cislice

    list_of_bulls = [i for i, j in zip(puzzle, guess) if i == j] # zjisteni vsech bulls
    bulls = len(list_of_bulls) # zjisteni pocet bulls
    print(bulls,'bulls')

    list_of_cows = set(puzzle) & set(guess) # zjiteni vsech cows
    cows = (len(list_of_cows) - bulls) # zjisteni poctu cows
    print(cows,'cows')
    number_of_guesses += 1

    if bulls == len(puzzle): # vyhodnoceni hry (uzivatel spravne uhadnul)
        break
    else:
        pass

if number_of_guesses < 6: # vyhodnoceni uspesnosti
    success_rate = 'Awesome'
elif number_of_guesses >= 6 and number_of_guesses < 10:
    success_rate = 'Good'
elif number_of_guesses >= 10 and number_of_guesses < 20:
    success_rate = 'I quess it is good'
elif number_of_guesses >= 20:
    success_rate = 'Not so good'

print('Congratulation, you made it with',number_of_guesses,'guesses.',success_rate,'job.')
