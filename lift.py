utasok=[72, 85, 64, 91, 58, 103, 77, 69, 88, 95, 60, 81]
maxsully = int(input("2. feladat: A lift teherbírása (kg): "))
ossz = 0
for tomeg in utasok:
    ossz = ossz + tomeg
if ossz <= teherbiras:
    print(f"3. feladat: Az összes tömeg {ossz} kg. Mindenki elfér.")
else:
    print(f"3. feladat: Az összes tömeg {ossz} kg. Nem fér el mindenki.")

talalt_i = -1                    
i = 0
while i < len(utasok) and talalt_i == -1:
    if utasok[i] > 100:
        talalt_i = i             
    i = i + 1
if talalt_i != -1:
    print(f"4. feladat: Az első 100 kg feletti utas: {talalt_i + 1}. ({utasok[talalt_i]} kg)")
else:
    print("4. feladat: Nincs 100 kg feletti utas.")




