"""
Olvasd be az f1.txt adatait, majd oldd meg az alábbi feladatokat!

1. Hány versenyző szerepel a fájlban?
2. Melyik versenyző nyerte a legtöbb futamot?
3. Ki teljesített a legtöbb futamot?
4. Átlagosan hány futamot teljesítettek a versenyzők?"

A megoldott feladatokat a kiirt_adatok nevű mappába hozd
létre statisztika.txt néven!
"""
f = open('./beolvasando_adatok/f1.txt', "r", encoding="utf-8")

f1 = []
with open('./beolvasando_adatok/f1.txt', 'r', encoding='utf-8') as forrasfajl:
    next(forrasfajl)
    for sor in forrasfajl:
        adatok = sor.strip().split(';')
        nev = str(adatok[0])
        csapat = str(adatok[1])
        gyozelmek = int(adatok[2])
        teljesitett_futamok = int(adatok[3])

        f1.append([nev, csapat, gyozelmek, teljesitett_futamok])

# 1. Hány versenyző szerepel a fájlban?

# 2. Melyik versenyző nyerte a legtöbb futamot?
legjobb_versenyzo = None
for versenyzo in f1:
    if legjobb_versenyzo is None or versenyzo[2] > legjobb_versenyzo[2]:
        legjobb_versenyzo = versenyzo

# 3. Ki teljesített a legtöbb futamot?
legtobb_futam = None
for versenyzo in f1:
    if legtobb_futam is None or versenyzo[3] > legtobb_futam[3]:
        legtobb_futam = versenyzo

# 4. Átlagosan hány futamot teljesítettek a versenyzők?
atlagos_futamszam = 0
for versenyzo in f1:
    atlagos_futamszam += versenyzo[3]

# A megoldott feladatokat a kiirt_adatok nevű mappába hozd 
# létre statisztika.txt néven!

with open('./kiirt_adatok/statisztika.txt', 'w', encoding='utf-8') as celfajl:
    print(f'A beolvasott fájlban összesen {len(f1)} versenyző szerepel.', file=celfajl)
    print(f'A legtöbb futamot nyert versenyző: {legjobb_versenyzo[0]}', file=celfajl)
    print(f'A legtöbb futamot teljesített versenyző: {legtobb_futam[0]}', file=celfajl)
    print(f'Az átlagos futamszám: {atlagos_futamszam / len(f1)}', file=celfajl)
