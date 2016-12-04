# Při plánování Ježíškovy rozvážky dárků se jeho pomocníci baví tím,
# že v adresách a jménech budoucích obdarovaných hledají palindromy.
# Palindrom je slovo, či sousloví, které se čte zepředu i zezadu stejně (ignoruje mezery a velká/malá písmena).
# Příkladem takového palindromu je: „dar hotelu Letohrad”.
# Pomoz jim hledání takových textů automatizovat.

import re

def string_contains_numbers(string):
    return bool(re.search(r'\d', string))

while True:
    palindrom = input('Zadej slovo pro palindrom. ')
    test = string_contains_numbers(palindrom)
    if test:
        print('To není slovo.')
    else:
        break

def palindrom_validator(palindrom):
    palindrom = palindrom.replace(' ', '').lower()
    palindrom_array = list(palindrom)
    palindrom_array_reverse = list(palindrom_array)
    palindrom_array_reverse.reverse()
    return bool(palindrom_array == palindrom_array_reverse)

print('Tvoje slovo je palindrom.') if palindrom_validator(palindrom) == True else print('Toto není palindrom.')
