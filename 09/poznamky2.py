seznam = [5,1,2,3,4]
seznam.append(seznam)

print(seznam)

assert seznam[0] == 5
assert seznam[5][0] == 5
assert seznam[5][5][0] == 5
assert seznam[5][5][5][5][5][5][5][5][5][5][5][0] == 5
