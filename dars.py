# test
# import numpy as np
#
# # Ildizlar ro'yxati (o'zingizning qiymatlaringizni kiriting)
# a = list(range(15, -1, -1))  # 15 dan 0 gacha sonlar
#
# # Ko'phadning koeffisiyentlarini hisoblash
# coefficients = np.poly(a)
#
# print("Ko'phadning koeffisiyentlari:", coefficients)
######################################################################################################################33
# Parametrlarni o'rnatamiz
# def solve_n_queens():
#     yechimlar= []  # Yechimlar ro'yxati
#     board = [-1] * 8  # 8 ta satr uchun boshlang'ich taxta
#
#     def place_queen(row):
#         if row == 8:  # Agar barcha 8 ta farzin joylashtirilsa
#             yechimlar.append(board[:])  # Yechimni saqlash
#             return
#         for col in range(8):  # Har bir ustunni tekshirish
#             # Farzinni joylashtirish mumkinligini tekshirish
#             if all(board[i] != col and abs(board[i] - col) != abs(i - row) for i in range(row)):
#                 board[row] = col  # Farzinni joylashtirish
#                 place_queen(row + 1)  # Keyingi satrga o‘tish
#                 board[row] = -1  # Backtracking
#
#     place_queen(0)  # Boshlang'ich satrni chaqiramiz
#
#     # Yechimlarni chiqarish
#     print(f"Jami yechimlar soni: {len(yechimlar)}")
#     for solution in yechimlar:
#         for row in yechimlar:
#             print("." * row + "Q" + "." * (7 - row))  # Farzinni ('Q') chiqarish
#         print()  # Yechimlar orasiga bo'sh satr qo'yish
#
# # Dastur ishga tushurish
# solve_n_queens()
# def burish_90_chap(matritsa):
#     return [[matritsa[j][i] for j in range(len(matritsa))] for i in range(len(matritsa[0]) - 1, -1, -1)]
# matritsa = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# a_matritsa = burish_90_chap(matritsa)
# for qator in a_matritsa:
#     print(qator)


import math

# def ildiz_topish(a, epsilon=0.0001):
#     # Iterativ formulani amalga oshirish
#     y_n = a / 2  # Boshlang'ich qiymat
#     while True:
#         y_n1 = (y_n + a / y_n) / 2
#         if (y_n1 - y_n) < epsilon:
#             return y_n1
#         y_n = y_n1
#
# def kattalik_hisobla(a):
#     # Ildizni hisoblash
#     x = ildiz_topish(a)
#
#     # Kattalikni hisoblash
#     natija = (7 * x + 6) / (2 * x**3 + 3 * x - 1)
#     return natija
#
# # Berilgan a qiymati
# haqiqiy_a = 2
#
# # Hisoblash
# javob = kattalik_hisobla(haqiqiy_a)
# print(f"Kattalik: {javob:.6f}")
###############################################################################################################33#######
# def r_matrix_90_chapka(matrix):
#     return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix)-1, -1,-1 )]
#
# n = int(input("Matritsa o'lchamini kiriting (n): "))
# matrix = [list(map(int, input(f"{i + 1}-qator: ").split())) for i in range(n)]
# print("\n90° ga soat millariga teskari yo'nalishda burilgan matritsa:")
# rotated_matrix = r_matrix_90_chapka(matrix)
# for row in rotated_matrix:
#     print(*row)
########################################################################################################################
# *row orqali har bir qatorni ajratib chiqaramiz

# def r_matrix_90chapka(matrix):
#       #matiritsani olchamini topadi
#     n = len(matrix)
#     a = []
#    # n = len(matrix)#Yangi burilgan matritsani saqlash uchun bosh royxat yaratadi.
#     for i in range(n):           #har bir ustun uchun yangi qator yaratiladi
#         yengi_royhat = []          #yangi qatorni saqlash uchun bosh royhat
#         for j in range(n):           #har bir elementni tanlaydi
#             yengi_royhat.append(matrix[j][n - 1 - i])   #ustun indeks orqadan oldinga qarab tanlaydi
#         a.append(yengi_royhat)                             #hosil bolgan yangi qatorni natijaviy matiritsaga qoshamz
#     return a                        #yangi burilgan matiritsani qaytaradi
#
# n = int(input("Matritsa o'lchamini kiriting (n): "))
# matrix = []                      #bosh matiritsa yaratamiz
# for i in range(n):                    #n marta sikl orqali har bir qatorni kiritamiz
#     row = list(map(int, input(f"{i + 1}-qatorni kiriting: ").split()))
#     matrix.append(row)                          #kiritilgan qatorni matiritsaga qoshamz
# print(matrix)
# print("\n90° ga soat millariga teskari yo'nalishda burilgan matritsa:")
# r_matrix = r_matrix_90chapka(matrix)
# for row in r_matrix:             # burilgan matiritsani har bir qatorini olamz
#    print(*row)              ## Har bir qatorni ekranga chiqarish (elementlar orasida bo'sh joy bilan)
########################################################################################################################
# def r_matrix_90chapka(matrix):
#     n = len(matrix)  # Matritsaning o'lchami (qatormiz ustunlar soni)
#     a = []  # Burilgan matritsani saqlash uchun bo'sh ro'yxat yaratamiz
#     for i in range(n):  # Har bir qatorni burish uchun sikl
#         new_row = []  # Yangi qatorni saqlash uchun bo'sh ro'yxat yaratamiz
#         for j in range(n):  # Har bir ustunni burish uchun sikl
#             new_row.append(matrix[j][n - 1 - i])  # Burilgan qatorni yaratamiz
#         a.append(new_row)  # Yangi qatorni burilgan matritsaga qo'shamiz
#     return a  # Burilgan matritsani qaytaramiz
#
# # Foydalanuvchidan matritsa o'lchamini olish
# n = int(input("Matritsa o'lchamini kiriting (n): "))
#
# matrix = []  # Matritsani saqlash uchun bo'sh ro'yxat
#
# # Foydalanuvchidan matritsa qatorlarini olish
# for i in range(n):
#     row = list(map(int, input(f"{i + 1}-qatorni kiriting: ").split()))  # Qatorni kiritish va butun sonlar ro'yxatiga aylantirish
#     matrix.append(row)  # Qatorni matritsaga qo'shish
#
# # Burilgan matritsani chiqarishdan oldin matnli xabar chiqaramiz
# print("\n90° ga soat millariga teskari yo'nalishda burilgan matritsa:")
#
# # Matritsani 90° ga chapga burib, natijani saqlaymiz
# r_matrix = r_matrix_90chapka(matrix)
#
# # Burilgan matritsani ekranga chiqarish
# for row in r_matrix:
#     print(*row)  # Har bir qatorni ekranga chiqarish (elementlar orasida bo'sh joy bilan)
########################################################################################################################

# Poezdlar ma'lumotlari
# poezdlar = [
#     [42, "Namangan", 18.00],
#     [87, "Jizzah", 20.00],
#     [102, "Samarqand", 15.15],
#     [90, "Urganch", 18.00],
#     [77, "Buxoro", 11.00],
#     [88, "Sirdaryo", 10.00],
#     [54, "Andijon", 12.30],
#     [33, "Farg'ona", 14.00],
#     [60, "Qashqadaryo", 16.45],
#     [72, "Surxondaryo", 19.15],
#     [95, "Xorazm", 13.00],
#     [25, "Toshkent", 09.00]
# ]
#
# # 1. Poezd nomerlarini o'sish tartibida chiqarish
# print("1) Poezdlar nomerlarini o'sish tartibida saralash:")
# poezdlar.sort()  # Poezdlarni avtomatik tartiblab beradi (1-ustun bo'yicha)
# for poezd in poezdlar:
#     print(f"Poezd nomeri: {poezd[0]}, Manzil: {poezd[1]}, Vaqt: {poezd[2]}")
#
# # 2. Kiritilgan nomer bo'yicha poezdni topish
# nomer = int(input("\n2) Poezd nomerini kiriting: "))
# topildi = False
# for poezd in poezdlar:
#     if poezd[0] == nomer:  # Poezd raqami mos keladimi tekshiramiz
#         print(f"Poezd topildi: {poezd[0]} - {poezd[1]}, jo'nash vaqti: {poezd[2]}")
#         topildi = True
#         break
# if not topildi:
#     print("Bunday nomerli poezd topilmadi!")
#
# # 3. Kiritilgan manzil va vaqtdan keyin jo'naydigan poezdlarni topish
# manzil = input("\n3) Manzilni kiriting: ")
# vaqt = float(input("Jo'nash vaqtini kiriting : "))
# print("\nManzil va vaqtdan keyin jo'naydigan poezdlar:")
# topildi = False
# for poezd in poezdlar:
#     if poezd[1].lower() == manzil.lower() and poezd[2] > vaqt:  # Manzil va vaqtni tekshiramiz
#         print(f"{poezd[0]} - {poezd[1]}, Vaqt: {poezd[2]}")
#         topildi = True
# if not topildi:
#     print("Ko'rsatilgan shartga mos poyezd topilmadi.")
#










# ism = "gulom"
# yosh = 18
# boyi = 17,0
# dasturchi = True
#
# print("mening ismim:",ism)
# print("mening yoshim:", yosh)
# print("mening boyim:",boyi)
# print("men dastuchi", dasturchi)
#
# a = 22
# b = 44
# s = a+b
# print("javob:", s)
#

# yosh = 13
#
# if yosh <18:
#     print("san hali kickinasan")
# elif yosh == 18:
#     print("san kottasann")
# else:
#     print("san kottasan")
#

# Son toqmi yoki juft?
# son = 8893856646464644554545454545455566566
# if son%2 == 0:
#     print("bu juft son:")
# else:
#     print("bu toq son:")

#temperatura
# temperatura = -1
#
# if temperatura <0:
#     print("issiq havo")
# if temperatura >0:
#     print("havo zor")
#
# temperatura = -1
#
# if temperatura < 0:
#     print("Sovuq havo")
# elif temperatura > 0:
#     print("Havo zo'r")
# else:
#     print("Temperatura 0 daraja")

#ball baholash
# ball = 100
# if ball >= 90:
#     print("boho yahshi", ball)
# elif ball > 50:
#     print("ortacha baho", ball)
# else :
#     print("baho yomon")


# raqam = 1
# while raqam <= 9999999999999999999999999999 :
#      print(raqam)
#      raqam +=1

# isimlar = ["ali ,gulom,salim, abor, izzat, napi, qwer, bori, jonibek "]
# for ism in isimlar:
#     print("salo", ism)
# raqam = 2
# while raqam <=2:
#     raqam += 1
#     print("Raqam:", raqam)


# raqamlar = [12, 13, 14, 15, 16, 34, 344,45]
# a = 124+9988 * (9)
# b = 432/3 + 45 - 65
# print("Natija:" , a + b)
# def salom_ber():
#    print("salom , dasturchi")
# salom_ber()
# def salom_ber(ism):
#    print(f" salom, {ism}")
# salom_ber("abdulloh")
# salom_ber("izzat")
# salom_ber("baror")
# def kavadrat_son(son):
#     return son**2
# natija = kavadrat_son(5)
# print(natija)
# def bolinma(son):
#     return son%2
# natija = bolinma(7)
# print(f"natija", natija)
# def yigindi(son):
#     return son
# a = int(input("a ga son kiriting:"))
# f = int(input("f ga son kiriting:"))
# natija = (a + f)
# print(f"natija", natija)
# def kub_ildiz_hisoblash(son):
#     return son**3
# natija = kub_ildiz_hisoblash(5)
# print("natiaja:", natija)
# def kub_ildiz(son):
#     return son**3
# natija = kub_ildiz(int(input("son kiriting: ")))
# print(natija)
# def ayirma(son):
#      return son
# a = float(input("a ga qiymat kiriitng:"))
# b = float(input("b ga son kiriting:"))
# natija = a - b
# print("javob", natija)
# def kopaytma(x):
#     return x
# c = float(input("c ga qiymat kiriitng:"))
# h = float(input("h ga son kiriting:"))
# natija = c * h
# print("Javob:", natija)
#
#
# sonlar = [1, 2, 3, 4, 5]
# print(sonlar[0])  # 1-qiymatni chiqaradi
# sonlar.append(6)  # Ro'yxatga yangi qiymat qo'shadi
# print(sonlar)
#
# isimlar = ["ali, murod, zerzod, eldor, dilshod" ]
# print(isimlar[0])
# isimlar.append("gulom")
# print(isimlar)

print("hello11")
print("hello2")
