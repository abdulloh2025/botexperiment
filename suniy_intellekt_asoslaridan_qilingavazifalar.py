#1-topshiriq
# import math
# fayl = open('Volki_Sobaki.tbl', 'r')
# matritsa = []
# for qator in fayl:
#     qator_royxati = qator.split()
#     if len(qator_royxati) > 0:
#         yangi_qator = []
#         for son in qator_royxati:
#             if '.' in son:
#                 yangi_qator.append(float(son))
#             else:
#                 yangi_qator.append(int(son))
#
#
#         matritsa.append(yangi_qator)
#
# fayl.close()
#
# for q in matritsa:
#     print(q)
########################################################################################################################
#2-topshiriq
# import math
# fayl = open('Volki_Sobaki.tbl', 'r')
# matritsa = []
# for qator in fayl:
#     qator_royxati = qator.split()
#     if len(qator_royxati) > 0:
#         yangi_qator = []
#         for son in qator_royxati:
#             yangi_qator.append(float(son))
#         matritsa.append(yangi_qator)
# fayl.close()
#
# ustunlar_soni = len(matritsa[0])
# qatorlar_soni = len(matritsa)
#
# norm_matritsa = [q[:] for q in matritsa]
#
# for j in range(1, ustunlar_soni):
#
#     ustun_elementlari = []
#     for i in range(qatorlar_soni):
#         ustun_elementlari.append(matritsa[i][j])
#
#     x_min = min(ustun_elementlari)
#     x_max = max(ustun_elementlari)
#
#
#     for i in range(qatorlar_soni):
#         if x_max - x_min != 0:
#             norm_matritsa[i][j] = (matritsa[i][j] - x_min) / (x_max - x_min)
#
#
# print("Normallashtirilgan matritsa (Min-Max):")
# for i in range(qatorlar_soni):
#     print([round(x, 3) for x in norm_matritsa[i]])
#OB-Havo
########################################################################################################################

#
# def tozalash(matn):
#     return " ".join(matn.strip().lower().split())
#
#
# def id_topish(matn, lugat):
#     matn = tozalash(matn)
#     for k, v in lugat.items():
#         if tozalash(k) == matn:
#             return v
#     return None
#
#
# def main():
#     atribut_dict = {
#         "harorat": 0, "yog'ingarchilik": 1, "shamol": 2,
#         "sharoit / vaqt": 3, "oraliq xulosa": 4, "yakuniy tavsiya": 5
#     }
#
#     qiymat_dict = {
#         "0 dan past": 0, "0-20 oraliqda": 1, "30 dan yuqori": 2,
#         "qor": 3, "yomg'ir": 4, "yo'q (ochiq)": 5, "kuchli": 6,
#         "piyoda (yayov)": 7, "12:00-17:00": 8, "ko'chada bo'lish": 9,
#         "ko'rinish yomon": 10, "yo'l muzlagan": 11, "yo'l ho'l": 12,
#         "jazirama": 13, "chang-to'zon": 14, "bo'ron": 15,
#         "etik kiyish": 16, "kurtka kiyish": 17, "konditsionerli bino": 18,
#         "niqob taqish": 19, "uyda qolish": 20
#     }
#
#     natijalar_matni = {
#         11: "Yo'l holati = Muzlagan", 12: "Yo'l holati = Ho'l",
#         13: "Havo = Jazirama", 14: "Havo = Chang-to'zon", 15: "Havo = Bo'ron",
#         16: "TAVSIYA: Etik kiyish", 17: "TAVSIYA: Kurtka kiyish",
#         18: "TAVSIYA: Konditsionerli bino", 19: "TAVSIYA: Niqob taqing",
#         20: "TAVSIYA: Uyda qoling"
#     }
#
#     qoidalar = [
#         [(0, 0), (1, 3), (4, 11)], [(4, 11), (3, 7), (5, 16)], [(0, 1), (1, 4), (4, 12)],
#         [(4, 12), (2, 6), (5, 17)], [(0, 2), (1, 5), (4, 13)], [(4, 13), (3, 8), (5, 18)],
#         [(2, 6), (1, 5), (4, 14)], [(4, 14), (3, 9), (5, 19)], [(0, 0), (2, 6), (4, 15)],
#         [(4, 15), (3, 10), (5, 20)]
#     ]
#
#     print("OB-HAVO EKSPERT TIZIMI")
#     print("(Eslatma: So'zlarni jadvaldagi kabi yozing)\n")
#
#     while True:
#         malumotlar = []
#
#
#         while True:
#             a_input = input("Atribut kirit = ")
#             q_input = input("Qiymat kirit = ")
#
#             a_id = id_topish(a_input, atribut_dict)
#             q_id = id_topish(q_input, qiymat_dict)
#
#             if a_id is None or q_id is None:
#                 print("Xato: Kiritilgan soz topilmadi. Qaytadan kiriting.")
#                 continue
#
#             malumotlar.append((a_id, q_id))
#
#             davom = input("Yana ma'lumot kiritasizmi? (ha/yoq) = ").strip().lower()
#             if davom not in ['ha', 'h']:
#                 break
#
#
#         print("\nNATIJALAR:")
#         topildi = False
#         ishlatilgan_qoidalar = set()
#
#         while True:
#             yangi_malumot_qoshildi = False
#
#             for i, qoida in enumerate(qoidalar):
#                 if i in ishlatilgan_qoidalar:
#                     continue
#
#                 shart1, shart2, natija = qoida[0], qoida[1], qoida[2]
#
#
#                 if (shart1 in malumotlar) and (shart2 in malumotlar):
#                     print(f"P{i + 1} QOIDASI ISHLADI:")
#                     print(f"JAVOB: {natijalar_matni[natija[1]]}\n")
#
#                     malumotlar.append(natija)
#                     ishlatilgan_qoidalar.add(i)
#                     yangi_malumot_qoshildi = True
#                     topildi = True
#
#             if not yangi_malumot_qoshildi:
#                 break
#
#         if not topildi:
#             print("JAVOB: Bunday shartlar kombinatsiyasi mavjud emas.")
#
#         davom_dastur = input("\nDasturni boshidan davom ettirasizmi? (ha/yo'q) = ").strip().lower()
#         if davom_dastur not in ['ha', 'h']:
#             break
#
#
# main()


# import math
#
# fayl_nomi = "Volki_Sobaki.tbl"
# malumotlar = {}
#
# f = open(fayl_nomi, mode="r")
# for qator in f:
#     qismlar = qator.split()
#     if not qismlar: continue
#
#     sonlar = []
#     for x in qismlar:
#         sonlar.append(float(x))
#
#     sinf = int(sonlar[0])
#     alomatlar = sonlar[1:]
#
#     if sinf not in malumotlar:
#         malumotlar[sinf] = []
#     malumotlar[sinf].append(alomatlar)
# f.close()
#
#
# def evklid(v1, v2):
#     k = 0
#     for i in range(len(v1)):
#         k += (v1[i] - v2[i]) ** 2
#     return math.sqrt(k)
#
#
# def manhetten(v1, v2):
#     s = 0
#     for i in range(len(v1)):
#         s += abs(v1[i] - v2[i])
#     return s
#
# def chebyshev(v1, v2):
#     farqlar = []
#     for i in range(len(v1)):
#         farqlar.append(abs(v1[i]-v2[i]))
#     return max(farqlar)
#
# def kn_n(lugat, nuqta, f):
#     p = []
#     for key, values in lugat.items():
#         for value in values:
#             l_masofa = f(nuqta, value)
#             p.append((key, l_masofa))
#
#     saralangan = sorted(p, key=lambda x: x[1])
#
#     k = int(input("k ni kiritng: "))
#     yaqinlar = saralangan[:k]
#
#     sinflar = []
#     for i in yaqinlar:
#         sinflar.append(i[0])
#
#     natija = max(set(sinflar), key=sinflar.count)
#     return natija
#
# while True:
#     print("""
#             1.evklid
#             2.manhetn
#             3.chebyshev
#             4.chqish
#             """)
#     tanlang = int(input("tanlang qaysi algoritmda hsioblasin :"))
#
#     if tanlang == 4:
#         break
#
#     nuqta = list(map(float, input("alomatlarni kiritng; ").split()))
#
#     if tanlang == 1:
#         print("eng yaqin qo'shni ", kn_n(malumotlar, nuqta, evklid))
#     elif tanlang== 2:
#         print("eng yaqin qo'shni ", kn_n(malumotlar, nuqta, manhetten))
#     elif tanlang == 3:
#         print("eng yaqin qo'shni ", kn_n(malumotlar, nuqta, chebyshev))
#     else:
#         print("Xato tanlov!")

#k ning eng max chegarasi
# javob : 2x -1 eng kam sinifni 2 ga kopaytirib kegin 1ni ayiramiz