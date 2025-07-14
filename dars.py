# # # # test
# import numpy as np
#
# # Ildizlar ro'yxati (o'zingizning qiymatlaringizni kiriting)
# a = list(range(15, -1, -1))  # 15 dan 0 gacha sonlar
#
# # Ko'phadning koeffisiyentlarini hisoblash
# coefficients = np.poly(a)
#
# print("Ko'phadning koeffisiyentlari:", coefficients)
# # ######################################################################################################################33
# # # Parametrlarni o'rnatamiz
# # # def solve_n_queens():
# # #     yechimlar= []  # Yechimlar ro'yxati
# # #     board = [-1] * 8  # 8 ta satr uchun boshlang'ich taxta
# # #
# # #     def place_queen(row):
# # #         if row == 8:  # Agar barcha 8 ta farzin joylashtirilsa
# # #             yechimlar.append(board[:])  # Yechimni saqlash
# # #             return
# # #         for col in range(8):  # Har bir ustunni tekshirish
# # #             # Farzinni joylashtirish mumkinligini tekshirish
# # #             if all(board[i] != col and abs(board[i] - col) != abs(i - row) for i in range(row)):
# # #                 board[row] = col  # Farzinni joylashtirish
# # #                 place_queen(row + 1)  # Keyingi satrga o‘tish
# # #                 board[row] = -1  # Backtracking
# # #
# # #     place_queen(0)  # Boshlang'ich satrni chaqiramiz
# # #
# # #     # Yechimlarni chiqarish
# # #     print(f"Jami yechimlar soni: {len(yechimlar)}")
# # #     for solution in yechimlar:
# # #         for row in yechimlar:
# # #             print("." * row + "Q" + "." * (7 - row))  # Farzinni ('Q') chiqarish
# # #         print()  # Yechimlar orasiga bo'sh satr qo'yish
# # #
# # # # Dastur ishga tushurish
# # # solve_n_queens()
# # # def burish_90_chap(matritsa):
# # #     return [[matritsa[j][i] for j in range(len(matritsa))] for i in range(len(matritsa[0]) - 1, -1, -1)]
# # # matritsa = [
# # #     [1, 2, 3],
# # #     [4, 5, 6],
# # #     [7, 8, 9]
# # # ]
# # # a_matritsa = burish_90_chap(matritsa)
# # # for qator in a_matritsa:
# # #     print(qator)
# #
# #
import math
from os.path import split

#
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
# haqiqiy_a = int(input("son kiriting:"))
#
# # Hisoblash
# javob = kattalik_hisobla(haqiqiy_a)
# print(f"Kattalik: {javob:.6f}")
# # ###############################################################################################################33#######
# # # def r_matrix_90_chapka(matrix):
# # #     return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix)-1, -1,-1 )]
# # #
# # # n = int(input("Matritsa o'lchamini kiriting (n): "))
# # # matrix = [list(map(int, input(f"{i + 1}-qator: ").split())) for i in range(n)]
# # # print("\n90° ga soat millariga teskari yo'nalishda burilgan matritsa:")
# # # rotated_matrix = r_matrix_90_chapka(matrix)
# # # for row in rotated_matrix:
# # #     print(*row)
# # ########################################################################################################################
# # # *row orqali har bir qatorni ajratib chiqaramiz
# #
# # # def r_matrix_90chapka(matrix):
# # #       #matiritsani olchamini topadi
# # #     n = len(matrix)
# # #     a = []
# # #    # n = len(matrix)#Yangi burilgan matritsani saqlash uchun bosh royxat yaratadi.
# # #     for i in range(n):           #har bir ustun uchun yangi qator yaratiladi
# # #         yengi_royhat = []          #yangi qatorni saqlash uchun bosh royhat
# # #         for j in range(n):           #har bir elementni tanlaydi
# # #             yengi_royhat.append(matrix[j][n - 1 - i])   #ustun indeks orqadan oldinga qarab tanlaydi
# # #         a.append(yengi_royhat)                             #hosil bolgan yangi qatorni natijaviy matiritsaga qoshamz
# # #     return a                        #yangi burilgan matiritsani qaytaradi
# # #
# # # n = int(input("Matritsa o'lchamini kiriting (n): "))
# # # matrix = []                      #bosh matiritsa yaratamiz
# # # for i in range(n):                    #n marta sikl orqali har bir qatorni kiritamiz
# # #     row = list(map(int, input(f"{i + 1}-qatorni kiriting: ").split()))
# # #     matrix.append(row)                          #kiritilgan qatorni matiritsaga qoshamz
# # # print(matrix)
# # # print("\n90° ga soat millariga teskari yo'nalishda burilgan matritsa:")
# # # r_matrix = r_matrix_90chapka(matrix)
# # # for row in r_matrix:             # burilgan matiritsani har bir qatorini olamz
# # #    print(*row)              ## Har bir qatorni ekranga chiqarish (elementlar orasida bo'sh joy bilan)
# # ########################################################################################################################
# # # def r_matrix_90chapka(matrix):
# # #     n = len(matrix)  # Matritsaning o'lchami (qatormiz ustunlar soni)
# # #     a = []  # Burilgan matritsani saqlash uchun bo'sh ro'yxat yaratamiz
# # #     for i in range(n):  # Har bir qatorni burish uchun sikl
# # #         new_row = []  # Yangi qatorni saqlash uchun bo'sh ro'yxat yaratamiz
# # #         for j in range(n):  # Har bir ustunni burish uchun sikl
# # #             new_row.append(matrix[j][n - 1 - i])  # Burilgan qatorni yaratamiz
# # #         a.append(new_row)  # Yangi qatorni burilgan matritsaga qo'shamiz
# # #     return a  # Burilgan matritsani qaytaramiz
# # #
# # # # Foydalanuvchidan matritsa o'lchamini olish
# # # n = int(input("Matritsa o'lchamini kiriting (n): "))
# # #
# # # matrix = []  # Matritsani saqlash uchun bo'sh ro'yxat
# # #
# # # # Foydalanuvchidan matritsa qatorlarini olish
# # # for i in range(n):
# # #     row = list(map(int, input(f"{i + 1}-qatorni kiriting: ").split()))  # Qatorni kiritish va butun sonlar ro'yxatiga aylantirish
# # #     matrix.append(row)  # Qatorni matritsaga qo'shish
# # #
# # # # Burilgan matritsani chiqarishdan oldin matnli xabar chiqaramiz
# # # print("\n90° ga soat millariga teskari yo'nalishda burilgan matritsa:")
# # #
# # # # Matritsani 90° ga chapga burib, natijani saqlaymiz
# # # r_matrix = r_matrix_90chapka(matrix)
# # #
# # # # Burilgan matritsani ekranga chiqarish
# # # for row in r_matrix:
# # #     print(*row)  # Har bir qatorni ekranga chiqarish (elementlar orasida bo'sh joy bilan)
# # ########################################################################################################################
# 10-topshiriq dasturlash
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
# # # 1. Poezd nomerlarini o'sish tartibida chiqarish
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

# #
# #
# # # ism = "gulom"
# # # yosh = 18
# # # boyi = 17,0
# # # dasturchi = True
# # #
# # # print("mening ismim:",ism)
# # # print("mening yoshim:", yosh)
# # # print("mening boyim:",boyi)
# # # print("men dastuchi", dasturchi)
# # #
# # # a = 22
# # # b = 44
# # # s = a+b
# # # print("javob:", s)
# # #
# #
# # # yosh = 13
# # #
# # # if yosh <18:
# # #     print("san hali kickinasan")
# # # elif yosh == 18:
# # #     print("san kottasann")
# # # else:
# # #     print("san kottasan")
# # #
# #
# # # Son toqmi yoki juft?
# # # son = 8893856646464644554545454545455566566
# # # if son%2 == 0:
# # #     print("bu juft son:")
# # # else:
# # #     print("bu toq son:")
# #
# # #temperatura
# # # temperatura = -1
# # #
# # # if temperatura <0:
# # #     print("issiq havo")
# # # if temperatura >0:
# # #     print("havo zor")
# # #
# # # temperatura = -1
# # #
# # # if temperatura < 0:
# # #     print("Sovuq havo")
# # # elif temperatura > 0:
# # #     print("Havo zo'r")
# # # else:
# # #     print("Temperatura 0 daraja")
# #
# # #ball baholash
# # # ball = 100
# # # if ball >= 90:
# # #     print("boho yahshi", ball)
# # # elif ball > 50:
# # #     print("ortacha baho", ball)
# # # else :
# # #     print("baho yomon")
# #
# #
# # # raqam = 1
# # # while raqam <= 9999999999999999999999999999 :
# # #      print(raqam)
# # #      raqam +=1
# #
# # # isimlar = ["ali ,gulom,salim, abor, izzat, napi, qwer, bori, jonibek "]
# # # for ism in isimlar:
# # #     print("salo", ism)
# # # raqam = 2
# # # while raqam <=2:
# # #     raqam += 1
# # #     print("Raqam:", raqam)
# #
# #
# # # raqamlar = [12, 13, 14, 15, 16, 34, 344,45]
# # # a = 124+9988 * (9)
# # # b = 432/3 + 45 - 65
# # # print("Natija:" , a + b)
# # # def salom_ber():
# # #    print("salom , dasturchi")
# # # salom_ber()
# # # def salom_ber(ism):
# # #    print(f" salom, {ism}")
# # # salom_ber("abdulloh")
# # # salom_ber("izzat")
# # # salom_ber("baror")
# # # def kavadrat_son(son):
# # #     return son**2
# # # natija = kavadrat_son(5)
# # # print(natija)
# # # def bolinma(son):
# # #     return son%2
# # # natija = bolinma(7)
# # # print(f"natija", natija)
# # # def yigindi(son):
# # #     return son
# # # a = int(input("a ga son kiriting:"))
# # # f = int(input("f ga son kiriting:"))
# # # natija = (a + f)
# # # print(f"natija", natija)
# # # def kub_ildiz_hisoblash(son):
# # #     return son**3
# # # natija = kub_ildiz_hisoblash(5)
# # # print("natiaja:", natija)
# # # def kub_ildiz(son):
# # #     return son**3
# # # natija = kub_ildiz(int(input("son kiriting: ")))
# # # print(natija)
# # # def ayirma(son):
# # #      return son
# # # a = float(input("a ga qiymat kiriitng:"))
# # # b = float(input("b ga son kiriting:"))
# # # natija = a - b
# # # print("javob", natija)
# # # def kopaytma(x):
# # #     return x
# # # c = float(input("c ga qiymat kiriitng:"))
# # # h = float(input("h ga son kiriting:"))
# # # natija = c * h
# # # print("Javob:", natija)
# # #
# # #
# # # sonlar = [1, 2, 3, 4, 5]
# # # print(sonlar[0])  # 1-qiymatni chiqaradi
# # # sonlar.append(6)  # Ro'yxatga yangi qiymat qo'shadi
# # # print(sonlar)
# # #
# # # isimlar = ["ali, murod, zerzod, eldor, dilshod" ]
# # # print(isimlar[0])
# # # isimlar.append("gulom")
# # # print(isimlar)
# #
# # # print("hello11")
# # # print("hello4")
# # # print("hello5")
# # # print("hello6")
# # #
# # # print("hello99")
# #
# #
# # # def salom():
# # #     print("Salom!","men ")
# # # salom()
# #
# #
# # # t = str(input(" matni kiriting: "))
# # # a=t.replace(",", "").replace("." , "")
# # # b=a.split()
# # # print(sorted(b))
# # #
#
# #
# # class Node:
# #     def __init__(self, data):
# #         self.data = data
# #         self.next = None
# #
# # class LinkedList:
# #     def __init__(self):
# #         self.head = None
# #
# #     def append(self, data):
# #         if not self.head:
# #             self.head = Node(data)
# #             return
# #         cur = self.head
# #         while cur.next:
# #             cur = cur.next
# #         cur.next = Node(data)
# #
# #     def print_list(self):
# #         cur = self.head
# #         while cur:
# #             print(cur.data, end=", ")
# #             cur = cur.next
# #         print()
# #
# #     def append_birinchi(self, value):
# #         cur = self.head
# #         while cur:
# #             if cur.data > value:
# #                 new_node = Node(cur.data)
# #                 new_node.next = cur.next
# #                 cur.next = new_node
# #                 return
# #             cur = cur.next
# #         print(f"{value} dan katta element topilmadi.")
# # # Misol
# # l = LinkedList()
# # for num in [10, 20, 30, 40, 50]:
# #     l.append(num)
# # print("Original ro'yxat:")
# # l.print_list()
# # l.append_birinchi(15)
# # print("dan katta birinchi element qoshilgan royxat:")
# # l.print_list()
#
#
#
#
#
# # 1-topshiriqni 11-misoli
# # t = " men ikki dona non oldim"
# # b=sorted(t.split())
# # q=str(b)
# # w=q.replace("[","").replace("]",'').replace(","," ").replace("'","")
# # print(w)
# # #1-topshiriqni 22-misoli
# # matn = input("Matn kiriting: ")
# # sozlar = matn.split()
# # polindromlar = []
# # for soz in sozlar:
# #     print(soz, "", soz[::-2])
# #     if soz == soz[::-1]:
# #         polindromlar.append(soz)
#
# # if polindromlar:
# #     print("ha mavjud , Polindrom sozlar topildi:")
# #     for polindrom in polindromlar:
# #         print(polindrom)
# # else:
# #     print("Polindrom sozlar topilmadi.")
#
#
# # class Node:
# #     def __init__(self, data):
# #         self.data = data
# #         self.prev = None
# #         self.next = None
# #
# #
# # class DoublyLinkedList:
# #     def __init__(self):
# #         self.head = None
# #         self.tail = None
# #
# #     def append(self, data):
# #         new_node = Node(data)
# #         if not self.head:
# #             self.head = new_node
# #             self.tail = new_node
# #         else:
# #             new_node.prev = self.tail
# #             self.tail.next = new_node
# #             self.tail = new_node
# #
# #     def ohirgi_elementni_royhati_boshiga_otkazish(self):
# #         if not self.head or self.head == self.tail:
# #             return
# #
# #         last = self.tail
# #         self.tail = last.prev
# #         self.tail.next = None
# #
# #         last.prev = None
# #         last.next = self.head
# #         self.head.prev = last
# #         self.head = last
# #
# #     def musbat_qiymatli_elementlarni_olibtashlash(self):
# #         cur = self.head
# #         while cur:
# #             if cur.data > 0:
# #                 if cur.prev:
# #                     cur.prev.next = cur.next
# #                 else:
# #                     self.head = cur.next
# #
# #                 if cur.next:
# #                     cur.next.prev = cur.prev
# #                 else:
# #                     self.tail = cur.prev
# #
# #             cur = cur.next
# #
# #     def print_list(self):
# #         cur = self.head
# #         while cur:
# #             print(cur.data, end=" <-> ")
# #             cur = cur.next
# #         print("None")
# #
# #
# #
# # dl = DoublyLinkedList()
# # for num in [1, -2, 3, 4, 6, 9, -4, 5,]:
# #     dl.append(num)
# #
# # print("Original ro'yxat:")
# # dl.print_list()
# #
# # dl.ohirgi_elementni_royhati_boshiga_otkazish()
# # print("\nOxirgi element boshiga o'tkazilgan:")
# # dl.print_list()
# #
# # dl. musbat_qiymatli_elementlarni_olibtashlash()
# # print("\nMusbat sonlar o'chirilgan:")
# # dl.print_list()
#
#
#
# # class Node:
# #     def __init__(self, data):
# #         self.data = data
# #         self.prev = None
# #         self.next = None
# #
# #
# # class DoublyLinkedList:
# #     def __init__(self):
# #         self.head = None
# #         self.tail = None
# #
# #     def append(self, data):
# #         new_node = Node(data)
# #         if not self.head:
# #             self.head = new_node
# #             self.tail = new_node
# #         else:
# #             new_node.prev = self.tail
# #             self.tail.next = new_node
# #             self.tail = new_node
# #
# #     def ohirgi_elementni_royhati_boshiga_otkazish(self):
# #         if not self.head or self.head == self.tail:
# #             return
# #
# #         last = self.tail
# #         self.tail = last.prev
# #         self.tail.next = None
# #
# #         last.prev = None        #buyoda obtawidi
# #         last.next = self.head
# #         self.head.prev = last
# #         self.head = last    #royhat boshini ohrgisiga ozgart
# #
# #     def musbat_qiymatli_elementlarni_olibtashlash(self):
# #         cur = self.head
# #         while cur:
# #             next_node = cur.next          # Keyingi tugunni saqlab qolamiz, chunki cur o‘chiriladi
# #             if cur.data > 0:
# #                 if cur.prev:
# #                     cur.prev.next = cur.next      #a ni c ga ulaw uchn
# #                 else:                             #birinchi elem
# #                     self.head = cur.next
# #
# #                 if cur.next:                     #ortadini ochirib ohirgini boshiga ulaw
# #                     cur.next.prev = cur.prev
# #                 else:                             #ohirgi elemnt bolsa oldign ulw uc
# #                     self.tail = cur.prev
# #
# #             cur = next_node  # Keyingi elementga o‘tamiz
# #
# #     def print_list(self):
# #         cur = self.head
# #         while cur:
# #             print(cur.data, end=" <-> ")
# #             cur = cur.next
# #         print("None")
# #
# #     def print_teskari(self):  # Ro'yxatni teskari chiqarish
# #         cur = self.tail
# #         while cur:
# #             print(cur.data, end=" <-> ")
# #             cur = cur.prev          #oldingi elemntga otad
# #         print("None")
# #
# #
# # # Sinov uchun kod:
# # dl = DoublyLinkedList()
# # for num in [1, -2, 3, 4, 6, 9, -4, 5]:
# #     dl.append(num)
# #
# # print("Original ro'yxat:")
# # dl.print_list()
# # print("orginal ro'yxat teskarisi:")
# # dl.print_teskari()
# #
# # dl.ohirgi_elementni_royhati_boshiga_otkazish()
# # print("\nOxirgi element boshiga o'tkazilgan:")
# # dl.print_list()
# # dl.print_teskari()
# # dl.musbat_qiymatli_elementlarni_olibtashlash()
# # print("\nMusbat sonlar o'chirilgan:")
# # dl.print_list()
# #
# # print("\nRo'yxatni teskari chop etish:")
# # dl.print_teskari()

# #
# #
# # class TALABA_GURUHI:
# #     def __init__(self):
# #         self.talabalar = []
# #
# #     def talaba_qoshish(self, familiya, ism, tugilgan_yili, telefon_nomeri):
# #         talaba = {
# #             'familiya': familiya,
# #             'ism': ism,
# #             'tugilgan_yili': tugilgan_yili,
# #             'telefon_nomeri': telefon_nomeri
# #         }
# #         self.talabalar.append(talaba)
# #         print(f"{familiya} {ism} guruhga qo'shildi.")
# #
# #     def talaba_izlash(self, key, value):
# #         for talaba in self.talabalar:
# #             if talaba[key] == value:
# #                 return talaba
# #         return None
# #
# #     def talaba_ochirish(self, familiya, ism):
# #         for talaba in self.talabalar:
# #             if talaba['familiya'] == familiya and talaba['ism'] == ism:
# #                 self.talabalar.remove(talaba)
# #                 print(f"{familiya} {ism} guruhdan o'chirildi.")
# #                 return
# #         print(f"{familiya} {ism} topilmadi.")
# #
# #     def talabalarni_tartiblash(self, key):
# #         self.talabalar.sort(key=lambda a: a[key])
# #         print(f"Talabalar {key} bo'yicha tartiblandi.")
# #
# #     def talabalarni_korsatish(self):
# #         if not self.talabalar:
# #             print("Guruhda hali hech qanday talaba yo'q.")
# #         else:
# #             for talaba in self.talabalar:
# #                 print(talaba)
# #
# #
# # # --- Asosiy dastur ---
# #
# # guruh = TALABA_GURUHI()
# #
# # print("Talaba Tizimi")
# # while True:
# #     print("Ish rejimini tanlang:")
# #     print("1. Talabani qo'shish")
# #     print("2. Talabani izlash")
# #     print("3. Talabalar ro'yxatini tartiblash")
# #     print("4. Chiqish (to'xtatish)")
# #
# #     tanlov = input("Rejimni tanlang (1, 2, 3, 4): ")
# #
# #     if tanlov == '1':
# #         while True:
# #             familiya = input("Familiyasini kiriting: ")
# #             ism = input("Ismini kiriting: ")
# #             tugilgan_yili = int(input("Tug‘ilgan yilini kiriting: "))
# #             telefon_nomeri = input("Telefon raqamini kiriting: ")
# #             guruh.talaba_qoshish(familiya, ism, tugilgan_yili, telefon_nomeri)
# #
# #             yana = input("Yana talaba qo‘shasizmi? (ha/yo'q): ").lower()
# #             if yana != 'ha':
# #                 break
# #
# #     elif tanlov == '2':
# #         familiya = input("Izlamoqchi bo'lgan talabaning familiyasini kiriting: ")
# #         ism = input("Ismini kiriting: ")
# #         talaba = guruh.talaba_izlash('familiya', familiya)
# #         if talaba and talaba['ism'] == ism:
# #             print("Topildi:", talaba)
# #             ochirish = input("Bu talabani o'chirmoqchimisiz? (ha/yo'q): ")
# #             if ochirish.lower() == 'ha':
# #                 guruh.talaba_ochirish(familiya, ism)
# #         else:
# #             print("Talaba topilmadi.")
# #
# #     elif tanlov == '3':
# #         print("Talabalar ro'yxati tug'ilgan yil bo'yicha tartiblanmoqda...")
# #         guruh.talabalarni_tartiblash('tugilgan_yili')
# #         guruh.talabalarni_korsatish()
# #
# #     elif tanlov == '4':
# #         print("Dastur to'xtatildi. Xayr!")
# #         break
# #
# #     else:
# #         print("Noto'g'ri tanlov! Iltimos, 1, 2, 3 yoki 4 ni tanlang.")
#
#
#
# # son = 3
# #
# # print(son*1)
# # print(son*2)
# # print(son*3)
# # print(son*4)
# # print(son*5)
# # print(son*6)
# # print(son*7)
# # print(son*8)
# # print(son*9)
# # print(son*10)
# # print(son*11)
# # print(son*12)
# # # print(son*13)
# #
# #
# # b =4
# # a = 3
# # # b = 4
# # a = b
# #
# # print(a)
#
# # a = int(input())
# # print("siz kiritkan son: ",a)
# # a = 2
# # A = 6*a**2
# # print("kubninig yuzasi:" ,A)
# # a = 4
# # b = a**3
# # print("kubninig hajmi" , b)
# a = int(input("a ga qiymat kiriting"))
# b = int(input("b ga qiymat kiriting"))
# p = 2*(a + b)
# print(p)
# a,b,c=map(float,input("a,b,c ni kiritiing").split())
# print((a+b+c)/3)

#
# from collections import Counter, defaultdict
#
#
# class Talaba:
#     def __init__(self, familiya, ism, sharif, jinsi, yosh, bosqich):
#         self.familiya = familiya
#         self.ism = ism
#         self.sharif = sharif
#         self.jinsi = jinsi.upper()  # 'E' yoki 'A'
#         self.yosh = int(yosh)
#         self.bosqich = int(bosqich)
#
#
# def anketa_analiz(fayl_nomi):
#     with open(fayl_nomi, 'r', encoding='utf-8') as f:
#         talabalar = []
#         for qator in f:
#             qism = qator.strip().split(',')
#             if len(qism) < 6:
#                 continue
#             talaba = Talaba(*qism)
#             talabalar.append(talaba)
#
#     # a) erkaklar soni eng ko‘p bo‘lgan o‘quv bosqichi
#     bosqich_erkaklar = defaultdict(int)
#     for t in talabalar:
#         if t.jinsi == 'E':
#             bosqich_erkaklar[t.bosqich] += 1
#     eng_kop_erkak_bosqich = max(bosqich_erkaklar.items(), key=lambda x: x[1])[0]
#
#     # b) eng ko‘p tarqalgan erkak va ayollar ismlari
#     erkak_ism = Counter(t.ism for t in talabalar if t.jinsi == 'E')
#     ayol_ism = Counter(t.ism for t in talabalar if t.jinsi == 'A')
#     eng_kop_erkak_ism = erkak_ism.most_common(1)[0][0] if erkak_ism else None
#     eng_kop_ayol_ism = ayol_ism.most_common(1)[0][0] if ayol_ism else None
#
#     # d) yoshi va sharifi bir xil bo‘lgan eng ko‘p ayol talaba guruhidagi familiyalar
#     ayol_guruhlar = defaultdict(list)
#     for t in talabalar:
#         if t.jinsi == 'A':
#             kalit = (t.yosh, t.sharif)
#             ayol_guruhlar[kalit].append(t.familiya)
#
#     eng_kop_guruh = max(ayol_guruhlar.items(), key=lambda x: len(x[1]))[1]
#     eng_kop_guruh.sort()  # alfavit tartibida
#
#     return eng_kop_erkak_bosqich, eng_kop_erkak_ism, eng_kop_ayol_ism, eng_kop_guruh
#
#
# def main():
#     fayl_nomi = input("ANKETA fayl nomini kiriting: ")
#     try:
#         bosqich, erkak_ism, ayol_ism, familiyalar = anketa_analiz(fayl_nomi)
#
#         print(f"\nErkaklar soni eng ko‘p bo‘lgan o‘quv bosqichi: {bosqich}")
#         print(f"Eng ko‘p uchraydigan erkak ismi: {erkak_ism}")
#         print(f"Eng ko‘p uchraydigan ayol ismi: {ayol_ism}")
#         print("Eng ko‘p uchraydigan yoshi va sharifi bir xil ayol talabalarning familiyalari (alfavit tartibida):")
#         for fam in familiyalar:
#             print(f"  {fam}")
#
#     except FileNotFoundError:
#         print("Fayl topilmadi!")
#     except Exception as e:
#         print(f"Xatolik yuz berdi: {e}")
#
#
# if __name__ == "__main__":
#     main()

##################################################################
# 7751444752:AAEfmgzmAU8CEDxV5j5ALxx6RaqpjilORH8
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Telegram bot tokeningizni shu yerga kiriting
# BotFather orqali yangi bot yaratganingizda olasiz
TOKEN = "7751444752:AAEfmgzmAU8CEDxV5j5ALxx6RaqpjilORH8"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """/start buyrug'i kelganda ishga tushadi."""
    user = update.effective_user
    await update.message.reply_html(
        f"Hi! {user.mention_html()} 👋",
        # reply_markup=ForceReply(selective=True), # Agar foydalanuvchiga javob berishni so'ramoqchi bo'lsangiz
    )

def main() -> None:
    """Botni ishga tushirish uchun asosiy funksiya."""
    # Bot obyektini yaratish
    application = Application.builder().token(TOKEN).build()

    # /start buyrug'ini qabul qiluvchi handler qo'shish
    application.add_handler(CommandHandler("start", start))

    # Botni doimiy tinglash holatiga o'tkazish
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()


















