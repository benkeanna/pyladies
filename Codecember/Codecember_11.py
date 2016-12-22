# Ježíšek při balení dárků řeší, kolik bude potřebovat balicího papíru.
# Má rozměry krabičky (vždycky délku, šířku a výšku) a potřebuje vědět, kolik metrů balicího papíru spotřebuje.
# Balicí papír je vždycky široký 100 cm a je na dlouhé, téměř nekonečné roli.
# Pomoz mu a napiš aplikaci, která spočítá potřebnou délku této role na jednu krabičku.
# Krabička jde zabalit na délku nebo na šířku a podél kratší strany nebo podél delší strany.
# Tedy čtyřmi způsoby. Obrázek napoví. Ale pozor, ne vždy se krabička všemi způsoby vejde na balící papír.
# Dokonce se může stát, že se nevejde vůbec.
# Cílem je napsat aplikaci, která po zadání délky, šířky a výšky krabičky rozhodne nejkratší délku balicího papíru, který bude potřeba.
# Případně, pokud se krabička kvůli rozměrům zabalit nedá, aplikace by to měla správně poznat.

width_of_wrap = 100 # šířka role balícího papíru
length = int(input('Enter lenght of package: ')) # délka balíčku
width = int(input('Enter width of package: ')) # šířka balíčku
height = int(input('Enter height of package: '))# výška balíčku

#def pack_present(length, width, height):
package_size_length = [(width * 2 ) + (height * 2), length + (height * 2)]
print(package_size_length)
package_size_width = [(length * 2 ) + (height * 2), width + (height * 2)]
print(package_size_width)

if package_size_length[0] < width_of_wrap or package_size_length[1] < width_of_wrap:
    print('a')
elif package_size_width[0] < width_of_wrap or package_size_width[1] < width_of_wrap:
    print('b')
else:
    print('c')
#    if package_length > width_of_wrap or package_width > width_of_wrap:
#        return False
#    else:
#        return True

#result = pack_present(length, width, height)

#print('Present will fit into wrapping paper.') if result else print('Present is too big..')
