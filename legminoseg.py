meresek = [42, 55, -1, 61, 48, -1, 70, 66]
db = 0
ossz = 0

for meres in meresek:
    if meres != -1:
        db = db + 1
        ossz = ossz + meres
atlag = ossz / db              
print(f"2. feladat: Érvényes mérések: {db}, átlag: {atlag}")

szoveg = []
for ora in range(len(meresek) // 2):
    ora_ossz = 0
    for index in (2 * ora, 2 * ora + 1):
        if meresek[index] != -1:   
            ora_ossz = ora_ossz + meresek[index]
    szoveg.append(f"{8 + ora} órától {ora_ossz}")
print("3. feladat: " + ", ".join(szoveg))

nagy = meresek[0]
nagy = 0
for i in range(1, len(meresek)):
    if meresek[i] > nagy:      
        nagy = meresek[i]
        nagy_index = i
percek = nagy_index * 30
ora = 8 + percek // 60
perc = percek % 60
print(f"4. feladat: A legnagyobb érték: {nagy}, időpontja: {ora}:{perc:02d}")
