import math

fayl_nomi = "Volki_Sobaki.tbl"
malumotlar = {}

f = open(fayl_nomi, mode="r")
for qator in f:
    qismlar = qator.split()
    if not qismlar: continue

    sonlar = []
    for x in qismlar:
        sonlar.append(float(x))

    sinf = int(sonlar[0])
    alomatlar = sonlar[1:]

    if sinf not in malumotlar:
        malumotlar[sinf] = []
    malumotlar[sinf].append(alomatlar)
f.close()


def evklid(v1, v2):
    k = 0
    for i in range(len(v1)):
        k += (v1[i] - v2[i]) ** 2
    return math.sqrt(k)


def manhetten(nu1, nu2):
    s = 0
    for i in range(len(nu1)):
        s += abs(nu1[i] - nu2[i])
    return s


def chebyshev(nu1, nu2):
    farqlar = []
    for i in range(len(nu1)):
        farqlar.append(abs(nu1[i] - nu2[i]))
    return max(farqlar)


def kn_n(lugat, nuqta, func):
    p = []
    for key, values in lugat.items():
        for value in values:
            l_masofa = func(nuqta, value)
            p.append((key, l_masofa))

    saralangan = sorted(p, key=lambda x: x[1])

    k = int(input("k ni kiritng: "))
    yaqinlar = saralangan[:k]

    sinflar = []
    for i in yaqinlar:
        sinflar.append(i[0])

    natija = max(set(sinflar), key=sinflar.count)
    return natija

while True:
    print("""
            1.evklid
            2.manhetn
            3.chebyshev
            4.chqish
            """)
    l = int(input("tanlang qaysi algoritmda hsioblasin :"))

    if l == 4:
        break

    nuqta = list(map(float, input("alomatlarni kiritng; ").split()))

    if l == 1:
        print("eng yaqin qo'shni ", kn_n(malumotlar, nuqta, evklid))
    elif l == 2:
        print("eng yaqin qo'shni ", kn_n(malumotlar, nuqta, manhetten))
    elif l == 3:
        print("eng yaqin qo'shni ", kn_n(malumotlar, nuqta, chebyshev))
    else:
        print("Xato tanlov!")