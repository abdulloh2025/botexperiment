# def tozalash(matn):
#     return " ".join(matn.strip().lower().split())
#
#
# def indeks_topish(matn, lugat):
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
#     print("(Eslatma: Sozlarni jadvaldaka yozing)")
#
#     while True:
#
#         a_input1 = input("\nAtribut kirit = ")
#         q_input1 = input("Qiymat kirit = ")
#         a_input2 = input("Atribut kirit = ")
#         q_input2 = input("Qiymat kirit = ")
#
#         a1 = indeks_topish(a_input1, atribut_dict)
#         q1 = indeks_topish(q_input1, qiymat_dict)
#         a2 = indeks_topish(a_input2, atribut_dict)
#         q2 = indeks_topish(q_input2, qiymat_dict)
#
#         if None in (a1, q1, a2, q2):
#             print("\nXATO: So'zlarni yozishda xato qildingiz.")
#             print("Tog'ri variantlar: 'Sharoit / Vaqt', 'Oraliq xulosa', 'Piyoda (yayov)' va h.k.")
#             continue
#
#         shart1, shart2 = (a1, q1), (a2, q2)
#         topildi = False
#
#         for i, qoida in enumerate(qoidalar):
#             q_sh1, q_sh2, natija = qoida[0], qoida[1], qoida[2]
#
#             if (shart1 == q_sh1 and shart2 == q_sh2) or (shart1 == q_sh2 and shart2 == q_sh1):
#                 print(f"\nP{i + 1} QOIDASI ISHLADI:")
#                 print(f"JAVOB: {natijalar_matni[natija[1]]}")
#                 topildi = True
#                 break
#
#         if not topildi:
#             print("\nJAVOB: Bunday shartlar kombinatsiyasi mavjud emas.")
#
#         savol = input("\ndavom etish (ha/yo'q) = ").strip().lower()
#         if savol not in ['ha', 'h']: break
#
#
#
# main()

#
# malumot = [
#     ("Ha", "Ha", 30),
#     ("Ha", "Yo‘q", 10),
#     ("Yo‘q", "Ha", 20),
#     ("Yo‘q", "Yo‘q", 40)
# ]
#
#
# gripp = {}
# isitma = {}
# birgalikda = {}
#
# for g_korinishi, i_korinishi, soni in malumot:
#     if g_korinishi not in gripp:
#         gripp[g_korinishi] = 0
#     gripp[g_korinishi] += soni
#
#
#     if i_korinishi not in isitma:
#         isitma[i_korinishi] = 0
#     isitma[i_korinishi] += soni
#
#     birgalikda[(g_korinishi, i_korinishi)] = soni
#
#
# print("P(Isitma | Gripp)")
# for qiymat in birgalikda:
#     g_qiymat, i_qiymat = qiymat
#     natija = birgalikda[qiymat] / gripp[g_qiymat]
#     print(f"P(Isitma={i_qiymat} | Gripp={g_qiymat}) = {natija}")
#
# print("\nP(Gripp | Isitma)")
# for qiymat in birgalikda:
#     g_qiymat, i_qiymat = qiymat
#     natija = birgalikda[qiymat] / isitma[i_qiymat]
#     print(f"P(Gripp={g_qiymat} | Isitma={i_qiymat}) = {natija}")
#
# #
# import random
# import matplotlib.pyplot as plt
#
# tajribalar_soni = 10000
# statistika = []
# gerb_soni = 0
# raqam_soni = 0
#
# for qadam in range(1, tajribalar_soni + 1):
#     tanga = random.randint(0, 1)
#
#     if tanga == 1:
#         gerb_soni += 1
#     else:
#         raqam_soni += 1
#
#     statistika.append((gerb_soni / qadam, raqam_soni / qadam))
#
# print(f"Oxirgi natija (Gerb/Raqam ulushi): {statistika[-1]}")
#
# # Grafik qismi
# x_axis = list(range(1, tajribalar_soni + 1))
# gerb_ulushi = [s[0] for s in statistika]
# raqam_ulushi = [s[1] for s in statistika]
#
# plt.figure(figsize=(11, 5))
# plt.plot(x_axis, gerb_ulushi, label="Gerb ulushi", color="blue", linewidth=1)
# plt.plot(x_axis, raqam_ulushi, label="Raqam ulushi", color="orange", linewidth=1)
# plt.axhline(0.5, color='black', linestyle=':', label="Ideal (0.5)")
#
# plt.title("Katta sonlar qonuni: Ulushlarning 0.5 ga yaqinlashishi")
# plt.xlabel("Tashlashlar soni")
# plt.ylabel("Ehtimollik ulushi")
# plt.legend()
# plt.grid(alpha=0.3)
# plt.show()