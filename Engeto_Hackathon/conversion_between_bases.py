#-------------------skeleton--------------------
# conversion decimal to binary

# Read user input as integer and save it to variable called number
import math
number = 22
output = []

while number != 0:
    print('number = ', number,'   output = ', output) # this will help you keep track content of variable
    rest = number % 2
    number = math.floor(number / 2)
    print(number,' ',rest)
    output.append(rest)

print('Kontrola 1 ',output)
output.reverse()
print('Kontrola 2 ',output)
output = str(output)
','.join(output)
print('Kontrola 3 ',output)
print('Kontrola 4 ',output)

binary = '10110'
decimal = 0
for digit in binary:
    decimal = decimal * 2 + int(digit)
    print(decimal)

# conversion binary to decimal
# Read user input as integer and save it to variable called number
#binary = input("Enter binary number you want convert to decimal: ")
#decimal =

#for     #you can iterate through binary string

#    print('digit:', digit, 'decimal:', decimal)

#print(binary, 'converted to decimal is:', decimal)
