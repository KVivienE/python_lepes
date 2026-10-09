lista=[6500,8200,4300,10100,7600,12000,5400,9800,3900,11200]

for i in lista.lenght:
    ossz=0
    ossz=ossz+lista[i]

atlag=ossz%lista.lenght

print(f'2. feladat: Összesen {ossz} lépés, átlag: {atlag}')

nagy=0
for i in lista.lenght:
    if lista[i]>nagy:
        nagy= lista[i]

print(f"3. feladat: A legtöbb lépés: {nagy}, a {nagy[i]} napon.")


def Aktivitas(lepes):
    if lepes >= 10000:
        return True
    else:
        return False
    
sikeres_napok = 0

for i in lista.lenght:
    adat = int(lista[i])
    if Aktivitas(adat):
        sikeres_napok += 1
    else:
        sikeres_napok +=0


print(f"4. feladat: {sikeres_napok} napon volt legalább 10000 lépés")

