# A co myslíte, že dělá Mikuláš, když už má letos po práci?
# Rozhodl se, že bude trochu hubnout, protože se už pomalu nevejde do svého červeného kožichu.
# Napiš mu appku, do které bude moci zadat, kolik procent tuků má v jídle, kolik sacharidů (cukrů) a kolik bílkovin (proteinů).
# Dále bude moci zadat hmotnost porce, kterou sní, a appka mu spočítá, kolik je to energie.
# Mikuláš ví, že 100 gramů tuku má 900 kcal, 100 gramů sacharidů má 400 kcal a 100 gramů bílkovin má 420 kcal.
# Nakonec mu ještě appka vypíše, jak dlouho by musel běžet za sáněmi (místo toho, aby se vezl), aby spálil rovnocenné množství energie.
# Mikuláš ví, že za hodinu mírného běhu spálí 600 kcal. Například když si Mikuláš dá svůj oblíbený Pribináček, zadá (podle obalu) 16,1 % tuků, 15,8 % sacharidů a 7,4 % bílkovin.
# Pribináček má hmotnost 80 gramů, tedy asi 190 kcal energie a zhruba 19 minut běhání.

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

def get_time_of_running(total_calories):
    running_time = (60 * total_calories) / 600
    return running_time

food_weight = []
for item_perc in food_perc:
    food_weight.append(get_weight_of_component(item_perc))

food_calories = []
i = 0
for item_weight in food_weight:
    food_calories.append(get_calories(item_weight,kcal_in_food[i]))
    i += 1

total_calories = sum(food_calories)
total_running_time = get_time_of_running(total_calories)

print('You will have to run', total_running_time, 'minut.')
