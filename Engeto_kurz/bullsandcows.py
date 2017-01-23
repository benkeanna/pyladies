"""
Game bulls and cows in Python 3.
Program generate 4-digit secret number, where digits must be all different.
Player tries to guess the secret number and program gives the number of matches.
If the matching digits are in their right positions, they are "bulls",
if in different positions, they are "cows".
"""

import random

puzzle_size = 4
puzzle = random.sample(range(0, 10), puzzle_size)
number_of_user_guesses = 0

class InputValidator:
    def __init__(self, user_input):
        self.input = user_input

    def validate(self):
        """Returns True if following checks passes.  """
        return (self.check_input_digits_count()
            and self.check_if_input_is_int()
            and self.check_if_input_digits_are_unique())

    def check_if_input_is_int(self):
        """Returns True if user input type is integer, otherwise returns False.  """
        try:
            int(self.input)
        except ValueError:
            return False
        else:
            return True

    def check_input_digits_count(self):
        """Returns True if user input length is 4, otherwise returns False.  """
        check =  len(str(self.input)) == 4
        return check

    def check_if_input_digits_are_unique(self):
        """Returns True if every digit is in user input only once.

        For each element append how many times is that element in user input.
        The goal is that every element is in user input only once, so the sum of number of their occurence is the same as length od the puzzle.
        """
        number_of_occurrence = []
        for element in self.input:
            count_of_element_in_input = self.input.count(element)
            number_of_occurrence.append(count_of_element_in_input)
        if sum(number_of_occurrence) == len(str(self.input)):
            return True
        else:
            return False


class MatchGuessAndPuzzle:
    def __init__(self, puzzle, guess):
        self.puzzle = puzzle
        self.guess = guess

    def get_number_of_bulls(self):
        """Return number of "bulls" in current user input. """
        list_of_bulls = [i for i, j in zip(self.puzzle, self.guess) if i == j]
        bulls = len(list_of_bulls)
        return bulls

    def get_number_of_cows(self):
        """Returns number of "cows" in current user input.
        This metod includes "bulls", they have to be subtracted from count of "cows".
        """
        bulls = self.get_number_of_bulls()
        list_of_cows = set(self.puzzle) & set(self.guess)
        cows = (len(list_of_cows) - bulls)
        return cows


def convert_str_input_into_list_of_int(guess_input):
    """Returns user input in required form - list of integers.  """
    guess = list(guess_input)
    guess = [int(x) for x in guess]
    return guess

def evaluate_success_rate(number_of_user_guesses):
    """Returns success_rate according to number of guesses.  """
    if number_of_user_guesses < 10:
        success_rate = 'Awesome'
    elif number_of_user_guesses >= 10 and number_of_user_guesses < 20:
        success_rate = 'Good'
    elif number_of_user_guesses >= 20 and number_of_user_guesses < 30:
        success_rate = 'I quess it is good'
    elif number_of_user_guesses >= 30:
        success_rate = 'Not so good'
    return success_rate

print('Welcome in game bulls and cows.')
print('I\'ve generated four different digits for you, try to guess them.')
print('If the matching digits are in their right positions, they are "bulls", if in different positions, they are "cows"')
while True:
    while True:
        user_input = input('Enter four different digits ')
        guess_input_validator = InputValidator(user_input)
        if guess_input_validator.validate():
            break
        else:
            print('These are not four different digits')

    guess = convert_str_input_into_list_of_int(user_input)
    game = MatchGuessAndPuzzle(puzzle, guess)
    bulls = game.get_number_of_bulls()
    cows = game.get_number_of_cows()
    print(bulls,'bulls')
    print(cows,'cows')
    number_of_user_guesses += 1

    if bulls == len(puzzle):
        break

success_rate = evaluate_success_rate(number_of_user_guesses)
print('Congratulation, you made it with',number_of_user_guesses,'guesses.',end=' ')
print(success_rate,'job.')
