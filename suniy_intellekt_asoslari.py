import math

def fayldan_jadval_yasash(fayl_nomi):
    natija_jadval = []
    f = open(fayl_nomi, "r")
    qatorlar = f.readlines()

    for q in qatorlar:
        qism_sonlar = []
        for son in q.split():
            qism_sonlar.append(float(son))
        natija_jadval.append(qism_sonlar)

    f.close()
    return natija_jadval

jadval = fayldan_jadval_yasash("Volki_Sobaki.tbl")
n_qatorlar = len(jadval)
m_ustunlar = len(jadval[0])
print("Qatorlar soni:", n_qatorlar)
print("Ustunlar soni:", m_ustunlar)



def urta_qiymat(ustun_elementlari):
    yigindi = 0.0
    element = len(ustun_elementlari)
    if element == 0:
        return 0

    for qiymat in ustun_elementlari:
        yigindi = yigindi + qiymat
    return yigindi / element


def mediana_topish(ustun_elementlari):
    toza_sonlar = []
    for son in ustun_elementlari:
        if son != 0:
            toza_sonlar.append(son)
    toza_sonlar.sort()
    uzunlik = len(toza_sonlar)

    if uzunlik == 0:
        return 0

    oraliq_index = uzunlik // 2
    if uzunlik % 2 != 0:
        return toza_sonlar[oraliq_index]
    else:
        return (toza_sonlar[oraliq_index - 1] + toza_sonlar[oraliq_index]) / 2


def dispersiya_hisoblash(ustun_elementlari):
    m_qiymat = urta_qiymat(ustun_elementlari)
    summa = 0.0
    soni = len(ustun_elementlari)

    if soni == 0:
        return 0

    for son in ustun_elementlari:
        summa = summa + (son - m_qiymat) ** 2
    return summa / soni


def korrelyatsiya_k(x_ustun, y_ustun):
    urtacha_x = urta_qiymat(x_ustun)
    urtacha_y = urta_qiymat(y_ustun)

    surat = 0.0
    maxraj_x = 0.0
    maxraj_y = 0.0

    for index in range(len(x_ustun)):
        if x_ustun[index] != 0 and y_ustun[index] != 0:
            surat = surat + (x_ustun[index] - urtacha_x) * (y_ustun[index] - urtacha_y)
            maxraj_x = maxraj_x + (x_ustun[index] - urtacha_x) ** 2
            maxraj_y = maxraj_y + (y_ustun[index] - urtacha_y) ** 2

    if maxraj_x == 0 or maxraj_y == 0:
        return 0

    return surat / math.sqrt(maxraj_x * maxraj_y)


def z_score_aniqlash():
    print("\nOUTLIER (Z-score usuli)")
    for j in range(m_ustunlar):
        joriy_ustun = []
        for i in range(n_qatorlar):
            joriy_ustun.append(jadval[i][j])

        m = urta_qiymat(joriy_ustun)
        d = dispersiya_hisoblash(joriy_ustun)
        std = math.sqrt(d)

        if std == 0:
            continue

        for i in range(n_qatorlar):
            qiymat = jadval[i][j]
            if qiymat != 0:
                z = abs((qiymat - m) / std)
                if z > 3:
                    print("Qator:", i, " Ustun:", j, " Qiymat:", qiymat)


def iqr_usuli():
    print("\n IQR OUTLIER ")
    for j in range(m_ustunlar):
        tartiblangan = []
        for i in range(n_qatorlar):
            if jadval[i][j] != 0:
                tartiblangan.append(jadval[i][j])

        tartiblangan.sort()

        if len(tartiblangan) == 0:
            continue

        chorak_1 = tartiblangan[int(len(tartiblangan) * 0.25)]
        chorak_3 = tartiblangan[int(len(tartiblangan) * 0.75)]
        iqr_masofa = chorak_3 - chorak_1

        pastki_chegara = chorak_1 - 1.5 * iqr_masofa
        yuqori_chegara = chorak_3 + 1.5 * iqr_masofa

        for i in range(n_qatorlar):
            qiymat = jadval[i][j]
            if qiymat != 0:
                if qiymat < pastki_chegara or qiymat > yuqori_chegara:
                    print("Qator:", i, " Ustun:", j, " Qiymat:", qiymat)


def bosh_joyni_mean_bilan_toldir():
    yangi_jadval = []
    for qator in jadval:
        yangi_jadval.append(qator[:])

    for j in range(m_ustunlar):
        joriy_ustun = []
        for i in range(n_qatorlar):
            joriy_ustun.append(jadval[i][j])

        urtacha_m = urta_qiymat(joriy_ustun)

        for i in range(n_qatorlar):
            if yangi_jadval[i][j] == 0:
                yangi_jadval[i][j] = round(urtacha_m, 2)

    return yangi_jadval


def bosh_joyni_mediana_bilan_toldir():
    yangi_jadval = []
    for qator in jadval:
        yangi_jadval.append(qator[:])

    for j in range(m_ustunlar):
        joriy_ustun = []
        for i in range(n_qatorlar):
            joriy_ustun.append(jadval[i][j])

        med_qiymat = mediana_topish(joriy_ustun)

        for i in range(n_qatorlar):
            if yangi_jadval[i][j] == 0:
                yangi_jadval[i][j] = med_qiymat

    return yangi_jadval

while True:
    print("\n Tanlang qaysi usul bilan ")
    print("1 -> Korrelyatsiya hisoblash")
    print("2 -> Dispersiya hisoblash")
    print("3 -> Z-score outlier qidirish")
    print("4 -> IQR outlier qidirish")
    print("5 -> Nol o'rniga Mean qo'yish")
    print("6 -> Nol o'rniga Median qo'yish")
    print("7 -> Dasturdan chiqish")

    tanlash = input("Kerakli bo'limni tanlang: ")

    if tanlash == "1":
        for j in range(m_ustunlar - 1):
            x_ustun = []
            y_ustun = []

            for i in range(n_qatorlar):
                x_ustun.append(jadval[i][0])
                y_ustun.append(jadval[i][j + 1])

            natija = korrelyatsiya_k(x_ustun, y_ustun)
            print(f"0-ustun bilan {j + 1}-ustun o'rtasidagi Korrelyatsiya: {round(natija, 4)}")

    elif tanlash == "2":
        print("\nHar bir ustun uchun dispersiya:")
        for j in range(m_ustunlar):
            joriy = []
            for i in range(n_qatorlar):
                joriy.append(jadval[i][j])
            print("Ustun", j, ":", dispersiya_hisoblash(joriy))

    elif tanlash == "3":
        z_score_aniqlash()

    elif tanlash == "4":
        iqr_usuli()

    elif tanlash == "5":
        natija_mean = bosh_joyni_mean_bilan_toldir()
        print("\nO'rtacha qiymat bilan to'ldirilgan :")
        for r in natija_mean:
            print(r)

    elif tanlash == "6":
        natija_median = bosh_joyni_mediana_bilan_toldir()
        print("\nMediana bilan to'ldirilgan :")
        for r in natija_median:
            print(r)


    elif tanlash == "7":
        print("Dastur to'xtatildi.")
        break
    else:
        print("Xato tanlov, qaytadan urinib ko'ring!")