# Lístky na Polární expres je možné zakoupit elektronicky. Platnost lístku ověřují při nástupu podle následnujících podmínek, které musí splňovat číslo lístku:
# 1) Lístek je platný, pokud jeho číslo má sudý počet číslic a nesmí začínat nulou.
# 2) Číslo lístku musí být dělitelné 3 a 5.
# Vytvoř ve svém oblíbeném jazyce validátor, který určí, jestli je číslo lístku platné pro cestu Polárním expresem nebo není. (Vstupem je celé číslo a výstupem true/false.)

while True:
    ticket = input('Zadej číslo lístku na polární expres: ')
    try:
        ticket_number = int(ticket)
    except ValueError:
        print('To není číslo. ')
    else:
        break

ticket_number_array = list(ticket)

possible_mistakes = {'even': 'musí být sudé', 'zero':'nesmí začínat nulou', 'divide3':'musí být dělitelné třemi','divide5':'musí být dělitelné pěti'}
mistakes = []

if len(ticket_number_array) % 2 != 0: # cislo musi mit sudy pocet cislic
    mistakes.append('even')
if ticket_number_array[0] == '0': # cislo nesmi zscinat nulou
    mistakes.append('zero')
if ticket_number % 3 != 0: # cislo musi byt delitene tremi
    mistakes.append('divide3')
if ticket_number % 5 != 0: # cislo musi byt delitelne peti
    mistakes.append('divide5')

for mistake in mistakes:
    print('Lituji, číslo lístku', possible_mistakes[mistake])

if mistakes == []:
    print('Gratuluji, můžeš natoupit na polární expres!')
