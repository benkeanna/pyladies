#The credit card number we want to validate. This program works with *most* credit card numbers.

#card_number = str(input("Enter credit card number you want to check: "))
#card_number = '4012888888881881'

card_number = input('Zadej číslo karty: ')

# Reverse the credit card number and take the digits in the odd positions and then the digits in the even positions
reversed_card_number = card_number[::-1]
print(reversed_card_number)

# Add up all the digits in the odd positions into a total.
odd_numbers = reversed_card_number[1::2]
print(odd_numbers)

total = 0
for odd_number in odd_numbers:
    odd_number = int(odd_number)
    total += odd_number
print(total)
# Multiply every even-positioned digit by two;
# if the product is greater than 9 (e.g. 8 * 2 = 16),
# then subtract 9 and add the result to the total.
# Otherwise add the multiplication product to the total.
even_numbers = reversed_card_number[::2]
for even_number in even_numbers:
    even_number = int(even_number)
    even_number_2 = even_number * 2
    if even_number_2 > 9:
        even_number_2 = even_number_2 - 9
        total += even_number_2
    else:
        total += even_number_2
print(total)

# If the total is divisible by 10 (the remainder after division by 10 is equal to 0 or the number ends in a zero);
#   then the credit card number is valid.
check = total % 10
print(check)
if check == 0:
    print('Karta je validní.')
else:
    print('Karta není validní.')
