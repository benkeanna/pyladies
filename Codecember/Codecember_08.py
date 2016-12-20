# A co myslíte, že dělá Mikuláš, když už má letos po práci?
# Rozhodl se, že bude trochu hubnout, protože se už pomalu nevejde do svého červeného kožichu.
# Napiš mu appku, do které bude moci zadat, kolik procent tuků má v jídle, kolik sacharidů (cukrů) a kolik bílkovin (proteinů).
# Dále bude moci zadat hmotnost porce, kterou sní, a appka mu spočítá, kolik je to energie.
# Mikuláš ví, že 100 gramů tuku má 900 kcal, 100 gramů sacharidů má 400 kcal a 100 gramů bílkovin má 420 kcal.
# Nakonec mu ještě appka vypíše, jak dlouho by musel běžet za sáněmi (místo toho, aby se vezl), aby spálil rovnocenné množství energie.
# Mikuláš ví, že za hodinu mírného běhu spálí 600 kcal. Například když si Mikuláš dá svůj oblíbený Pribináček, zadá (podle obalu) 16,1 % tuků, 15,8 % sacharidů a 7,4 % bílkovin.
# Pribináček má hmotnost 80 gramů, tedy asi 190 kcal energie a zhruba 19 minut běhání.
import math

total_weight = int(input('Enter weight of your food. ')) # vstupní hodnoty váhy jídla a procent jednotlivých komponent
fat_perc = int(input('Enter percent of fat in your food. '))
carbohydrate_perc = int(input('Enter percent of carbohydrate in your food. '))
protein_perc = int(input('Enter percent of protein in your food. '))

food_perc = [fat_perc, carbohydrate_perc, protein_perc] # seznam procentuálních hodnot podílu tuku, sacharidů a tuků
kcal_in_food = [9.0, 4.0, 4.2] # seznam kalorií v 1g jednotlivých komponent

def get_weight_of_component(component_perc): # funkce na výpočet váhy jednotlivých komponent z procentuálního podílu na jídle
    weight_of_component = (total_weight * component_perc)/100
    return weight_of_component

def get_calories(component_weight, kcal): # funkce na výpočet kalorií jednotlivých komponent s využitím seznamu kalorických hodnot komponent
    calories = component_weight * kcal
    return calories

def get_time_of_running(total_calories): # funkce na výpočet času, jak dlouho musí běhat vzhledem k přijatým kaloriím
    running_time = (60 * total_calories) / 600
    return running_time

food_weight = []
for item_perc in food_perc: # plnění nového seznamu váhy komponent vycházející z procentuálního podílu na váze jídla
    food_weight.append(get_weight_of_component(item_perc))

food_calories = []
i = 0
for item_weight in food_weight: # plnění nového seznamu kalorií komponent z jejich váhy
    food_calories.append(get_calories(item_weight,kcal_in_food[i]))
    i += 1 # index kvůli použití hodnoty kalorií na komponentu ze seznamu na řádku 17

total_calories = sum(food_calories) # celkové mmožství přijatých kalorií
total_running_time = get_time_of_running(total_calories) # počet minut, kdy by měl běhat by spálil kalorie
hour_total_running_time = math.floor(total_running_time / 60) # počet hodin běhání
minute_total_running_time = total_running_time % 60 # počet zbývajících minut běhání

print('You will have to run', hour_total_running_time, 'hours and',minute_total_running_time,'minutes.')
