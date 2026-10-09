koltseg = [1200, 800, 1500, 700, 900, 1100, 400]
egyenleg = 5000
maradt = 0                        
elsomaradt = 0                   
napi_egyenlegek = []                


for i in range(len(koltseg)):
    if koltseg[i] <= egyenleg:
        egyenleg = egyenleg - koltseg[i]   
    else:
        maradt = maradt + 1          
        if elsomaradt == 0:
            elsomaradt = i + 1         
    napi_egyenlegek.append(str(egyenleg))
print("2. feladat: " + " ".join(napi_egyenlegek))

if maradt > 0:
    print(f"3. feladat: {maradt} napon maradt el a vásárlás, először az {elsomaradt}. napon.")
else:
    print("3. feladat: Minden nap sikerült vásárolni.")

if egyenleg >= 500:
    print("4. feladat: Maradt tartalék.")
else:
    print("4. feladat: Elfogyott a tartalék.")
