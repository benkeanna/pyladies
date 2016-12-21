# Ježíšek se chystá na nákup a počítá finance. Chce dnes koupit ponožky, svetry, angličáky, panenky a flešky.
# Napiš funkci, která na vstupu dostane potřebné množství, ceny produktů a peníze v peněžence a vrátí informaci, zda Ježíškovi stačí peníze, které má, nebo si musí dojít k bankomatu.
# Vstup:
# Ceny: ponožka 5 ₱, svetr 42 ₱, angličák 17 ₱, panenka 23 ₱, fleška 33 ₱
# Potřebuje: 427 párů ponožek, 392 svetrů, 917 angličáků, 736 panenek a 1428 flešek
# V peněžence: 100 000 ₱

vallet = 100000 # peníze v peněžence
item_prices = {'sock': '5', # slovník cen jednotlivých položek
            'sweater': '42',
            'toycar': '17',
            'doll': '23',
            'flashdisc': '33'
            }

sock = int(input('Enter number of socks. ')) # input počtu položek v nákupu
sweater = int(input('Enter number of sweaters. '))
toycar = int(input('Enter number of toycars. '))
doll = int(input('Enter number of dolls. '))
flashdisc = int(input('Enter number of flashdisc. '))
shopping_list = {'sock': sock, 'sweater': sweater, 'toycar': toycar, 'doll': doll, 'flashdisc': flashdisc} # slovník nákupního listu s položkou a jejím počtem

def go_to_cashmachine(item_prices, shopping_list, vallet): # funkce, která vezme nákupní list, ceny položek a peníze v peněžence a vrtáí celkovou cenu nákupu
    final_price_list = []                                   # a jestli je nižší než peníze v peněžence
    for item in shopping_list: # procházení nákupního seznamu položku po položce
        number_of_items = int((shopping_list[item])) # číslo počtu kusů položky
        item_price = int((item_prices[item])) # číslo ceny položky
        final_price = number_of_items * item_price # celková cena za položku podle počtu kusů
        final_price_list.append(final_price) # naplněný seznamu ceny za jednotlivé položky
        final_price = sum(final_price_list) # celková cena daná součtem cen jednotlivých položek
    if final_price <= vallet:
        return [True, final_price] # pokud je cena nižší než peníze v pěněžence
    else:
        return [False, final_price] # pokud je cena vyšší než peníze v pěněžence

result = (go_to_cashmachine(item_prices, shopping_list, vallet)) # výsledek funkce go_to_cashmachine
print('Final price is',result[1],', it\'s ok, you don\'t need to go to cashmachine.') if result[0] else print('Final price is',result[1],', you don\'t have enough cash, go to the cashmachine.')
