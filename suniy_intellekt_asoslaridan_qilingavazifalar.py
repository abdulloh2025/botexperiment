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


#
# import random
# import tkinter as tk
# from tkinter import messagebox
#
#
# def wolfram_dunyoni_yarat(qator_uzunligi, qator_soni, qoida_raqami):
#     qoida_bin = format(qoida_raqami, '08b')
#     print(f"Qoida {qoida_raqami} ikkilikda: {qoida_bin}")
#
#     dunyo = [[0] * qator_uzunligi for i in range(qator_soni)]
#     dunyo[0] = [random.randint(0, 1) for i in range(qator_uzunligi)]
#
#     for i in range(qator_soni - 1):
#         for j in range(qator_uzunligi):
#             chap = dunyo[i][j - 1]
#             markaz = dunyo[i][j]
#             ong = dunyo[i][(j + 1) % qator_uzunligi]
#
#             holat = f"{chap}{markaz}{ong}"
#             indeks = 7 - int(holat, 2)
#             dunyo[i + 1][j] = int(qoida_bin[indeks])
#     return dunyo
#
#
#
# def hayot_oyini_qadam(hozirgi_dunyo):
#     yangi_dunyo = [qator[:] for qator in hozirgi_dunyo]
#     n_qator = len(hozirgi_dunyo)
#     m_ustun = len(hozirgi_dunyo[0])
#
#     for i in range(1, n_qator - 1):
#         for j in range(1, m_ustun - 1):
#             qoshnilar_yigindisi = (
#                     hozirgi_dunyo[i - 1][j - 1] + hozirgi_dunyo[i - 1][j] + hozirgi_dunyo[i - 1][j + 1] +
#                     hozirgi_dunyo[i][j - 1] + hozirgi_dunyo[i][j + 1] +
#                     hozirgi_dunyo[i + 1][j - 1] + hozirgi_dunyo[i + 1][j] + hozirgi_dunyo[i + 1][j + 1]
#             )
#
#             if hozirgi_dunyo[i][j] == 1:
#
#                 yangi_dunyo[i][j] = 1 if qoshnilar_yigindisi in [2, 3] else 0
#             else:
#                 yangi_dunyo[i][j] = 1 if qoshnilar_yigindisi == 3 else 0
#     return yangi_dunyo
#
#
# class SimulyatsiyaDasturi:
#     def __init__(self, asosiy_oyna, tarix):
#         self.oyna = asosiy_oyna
#         self.tarix = tarix
#         self.qadam_indeksi = 0
#         self.katak_ulchami = 15
#
#
#         self.kvars = tk.Canvas(asosiy_oyna, width=len(tarix[0][0]) * self.katak_ulchami,
#                                height=len(tarix[0]) * self.katak_ulchami, bg="white")
#         self.kvars.pack(pady=10)
#
#
#         boshqaruv = tk.Frame(asosiy_oyna)
#         boshqaruv.pack(pady=5)
#         tk.Button(boshqaruv, text="<< Oldingi", command=self.oldingi, width=10).pack(side=tk.LEFT, padx=5)
#         tk.Button(boshqaruv, text="Keyingi >>", command=self.keyingi, width=10).pack(side=tk.LEFT, padx=5)
#
#         self.holat_label = tk.Label(asosiy_oyna, text="")
#         self.holat_label.pack()
#
#         self.chizish()
#
#     def chizish(self):
#         self.kvars.delete("all")
#         matritsa = self.tarix[self.qadam_indeksi]
#         for i, qator in enumerate(matritsa):
#             for j, qiymat in enumerate(qator):
#                 if qiymat == 1:
#                     x1, y1 = j * self.katak_ulchami, i * self.katak_ulchami
#                     self.kvars.create_rectangle(x1, y1, x1 + self.katak_ulchami, y1 + self.katak_ulchami,
#                                                 fill="black", outline="gray")
#         self.holat_label.config(text=f"Hozirgi qadam: {self.qadam_indeksi} / {len(self.tarix) - 1}")
#
#     def keyingi(self):
#         if self.qadam_indeksi < len(self.tarix) - 1:
#             self.qadam_indeksi += 1
#             self.chizish()
#         else:
#             messagebox.showinfo("Tugadi", "Bu oxirgi iteratsiya.")
#
#     def oldingi(self):
#         if self.qadam_indeksi > 0:
#             self.qadam_indeksi -= 1
#             self.chizish()
#
#
# if __name__ == "__main__":
#     n = int(input("n (ustunlar soni)="))
#     m = int(input("m (qatorlar soni)="))
#     qoida = int(input("Qoida raqami (0-255): "))
#
#     dastlabki_dunyo = wolfram_dunyoni_yarat(n, m, qoida)
#
#     print("\nHosil bo'lgan boshlang'ich matritsa:")
#     for qator in dastlabki_dunyo:
#         print(qator)
#     print("-" * 30)
#
#     tarix_ruyxati = [dastlabki_dunyo]
#     for k in range(100):
#         keyingi_holat = hayot_oyini_qadam(tarix_ruyxati[-1])
#         if keyingi_holat == tarix_ruyxati[-1]:
#             break
#         tarix_ruyxati.append(keyingi_holat)
#
#
#     root = tk.Tk()
#     root.title("Sun'iy Hayot: Wolfram + Conway")
#     app = SimulyatsiyaDasturi(root, tarix_ruyxati)
#     root.mainloop()
#
