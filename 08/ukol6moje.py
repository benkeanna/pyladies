zvirata = ['pes', 'kočka', 'králík','had', 'andulka']

nova_zvirata = []
for zvire in zvirata:
    prvek = zvire[1:], zvire
    nova_zvirata.append(prvek)

print(nova_zvirata)
nova_zvirata.sort()
zvirata = []
for klic, zvire in nova_zvirata:
    zvirata.append(zvire)

print(zvirata)
