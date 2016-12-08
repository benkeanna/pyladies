# Ježíškovi pomocníci v centrálních skladech dárků mají vymyšlený systém třídění dárků podle jejich barvy a tvaru tak, aby je dokázali snadno vybírat pro doručení.
# Dárky potom ukládají do řady za sebe tak, že první jsou červené dárky, pak dárky modré a nakonec zelené.
# V jednotlivých barevných oddílech jsou potom nejdříve dárky tvaru krychle, následují kvádry a potom dárky kulového tvaru.
# Dárek je reprezentovaný jako seznam jeho parametrů a vstupem je seznam dárků. Výstupem je seznam dárků seřazený podle pravidel Ježíškových centrálních skladů.
# [“KR”, “cer”] je KRychle CERvena, [“KV”, “zel”] je KVadr ZELeny a [“KO”, “mod”] je KOule MODra.

# Vytvořte funkci, která přijme seznam dárků ve tvaru [["KV", "zel"], ["KO", "zel"], ["KV", "mod"], ["KR", "mod"], ["KV", "cer"]] (seznam seznamů)
# a vrátí tentýž seznam, ale seřazený podle pravidel pomocníků.

# Testovací vstup: [[“KV”, “zel”], [“KO”, “zel”], [“KV”, “mod”], [“KR”, “mod”], [“KV”, “cer”]]

import operator
list_of_gifts = [['KVÁDR', 'zelený'], ['KOULE', 'zelená'], ['KVÁDR', 'modrý'], ['KRYCHLE', 'modrá'], ['KVÁDR', 'cervený']]
print(list_of_gifts)

sorted_list_oif_gifts = sorted(list_of_gifts, key = operator.itemgetter(0,1))
print(sorted_list_oif_gifts)
