# Ježíšek na svém obstarožním počítači nemůže otevřít seznam lidí, kteří byli celý rok hodní.
# Pokusem a omylem Ježíšek zjistil, že jeho systém neumí písmena ď, ť, ň a ě.
# Pomoz mu napsat funkci,´která převede pole řetězců jmen a příjmení do bezpečné podoby tak, aby mohl seznam konečně otevřít. :)
# Vstup: ["Petr Vopršal", "Dan Ťok", "Kateřina Pěkná", "Pavel Ďolík", "Bětka Ňoková"]

list_of_behaves = ["Petr Vopršal", "Dan Ťok", "Kateřina Pěkná", "Pavel Ďolík", "Bětka Ňoková"]
list_of_letters = {'ď':'d', 'Ď':'D', 'ť':'t', 'Ť':'T', 'ň':'n', 'Ň':'N', 'ě':'e'}
new_list_of_behaves = []

for name in list_of_behaves:
    name_list = []
    for letter in name:
        name_list.append(list_of_letters[letter]) if letter in list_of_letters.keys() else name_list.append(letter)
    new_name = ''.join(name_list)
    new_list_of_behaves.append(new_name)

print(new_list_of_behaves)
