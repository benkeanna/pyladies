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

if len(ticket_number_array) % 2 != 0 or ticket_number_array[0] == '0' or ticket_number % 3 != 0 or ticket_number % 5 != 0:
    print('Lituji, tvůj lístek do polárního expresu neplatí.')
else:
    print('Gratuluji, můžeš nastoupit do polárního expresu.')
