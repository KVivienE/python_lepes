eredmeny = input("1. feladat: Eredménysor: ")
gyoz = 0
dontetlen = 0
vereseg = 0


for betu in eredmeny:             
    if betu == "G":
        gyoz = gyoz + 1
    elif betu == "D":
        dontetlen = dontetlen + 1
    elif betu == "V":
        vereseg = vereseg + 1
print(f"2. feladat: Győzelem: {gyoz}, döntetlen: {dontetlen}, vereség: {vereseg}")

pont = gyoz * 3 + dontetlen * 1
print(f"3. feladat: A csapat {pont} pontot szerzett.")
if vereseg == 0:
    print("4. feladat: Veretlen maradt.")
else:
    print("4. feladat: Volt vereség.")
