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
########################################################################################################################
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

# print("hello11")
# print("hello4")
# print("hello5")
# print("hello6")
#
# print("hello99")


# def salom():
#     print("Salom!","men ")
# salom()

# t = str(input(" matni kiriting: "))
# a=t.replace(",", "").replace("." , "")
# b=a.split()
# print(sorted(b))
########################################################################################################################
# 1-topshiriqni 11-misoli
# t = " men ikki dona non oldim"
# b=sorted(t.split())
# q=str(b)
# w=q.replace("[","").replace("]",'').replace(","," ").replace("'","")
# print(w)
# #1-topshiriqni 22-misoli
# matn = input("Matn kiriting: ")
# sozlar = matn.split()
# polindromlar = []
# for soz in sozlar:
#     print(soz, "", soz[::-2])
#     if soz == soz[::-1]:
#         polindromlar.append(soz)

# if polindromlar:
#     print("ha mavjud , Polindrom sozlar topildi:")
#     for polindrom in polindromlar:
#         print(polindrom)
# else:
#     print("Polindrom sozlar topilmadi.")
########################################################################################################################

# satr = "Tursin Bugun Fizika fanidan oraliq topshirdi."
# sozlar = satr[:-1].split()
# sozlar = sorted(sozlar, key=str.lower)
# tartiblangan_satr = ' '.join(sozlar) + "."
# print(tartiblangan_satr)

########################################################################################################################
# class TALABA_GURUHI:
#     def __init__(self):
#         self.talabalar = []
#
#     def talaba_qoshish(self, familiya, ism, tugilgan_yili, telefon_nomeri):
#         talaba = {
#             'familiya': familiya,
#             'ism': ism,
#             'tugilgan_yili': tugilgan_yili,
#             'telefon_nomeri': telefon_nomeri
#         }
#         self.talabalar.append(talaba)
#         print(f"{familiya} {ism} guruhga qo'shildi.")
#
#     def talaba_izlash(self, key, value):
#         for talaba in self.talabalar:
#             if talaba[key] == value:
#                 return talaba
#         return None
#
#     def talaba_ochirish(self, familiya, ism):
#         for talaba in self.talabalar:
#             if talaba['familiya'] == familiya and talaba['ism'] == ism:
#                 self.talabalar.remove(talaba)
#                 print(f"{familiya} {ism} guruhdan o'chirildi.")
#                 return
#         print(f"{familiya} {ism} topilmadi.")
#
#     def talabalarni_tartiblash(self, key):
#         self.talabalar.sort(key=lambda a: a[key])
#         print(f"Talabalar {key} bo'yicha tartiblandi.")
#
#     def talabalarni_korsatish(self):
#         if not self.talabalar:
#             print("Guruhda hali hech qanday talaba yo'q.")
#         else:
#             for talaba in self.talabalar:
#                 print(talaba)
#
#
# # --- Asosiy dastur ---
#
# guruh = TALABA_GURUHI()
#
# print("Talaba Tizimi")
# while True:
#     print("Ish rejimini tanlang:")
#     print("1. Talabani qo'shish")
#     print("2. Talabani izlash")
#     print("3. Talabalar ro'yxatini tartiblash")
#     print("4. Chiqish (to'xtatish)")
#
#     tanlov = input("Rejimni tanlang (1, 2, 3, 4): ")
#
#     if tanlov == '1':
#         while True:
#             familiya = input("Familiyasini kiriting: ")
#             ism = input("Ismini kiriting: ")
#             tugilgan_yili = int(input("Tug‘ilgan yilini kiriting: "))
#             telefon_nomeri = input("Telefon raqamini kiriting: ")
#             guruh.talaba_qoshish(familiya, ism, tugilgan_yili, telefon_nomeri)
#
#             yana = input("Yana talaba qo‘shasizmi? (ha/yo'q): ").lower()
#             if yana != 'ha':
#                 break
#
#     elif tanlov == '2':
#         familiya = input("Izlamoqchi bo'lgan talabaning familiyasini kiriting: ")
#         ism = input("Ismini kiriting: ")
#         talaba = guruh.talaba_izlash('familiya', familiya)
#         if talaba and talaba['ism'] == ism:
#             print("Topildi:", talaba)
#             ochirish = input("Bu talabani o'chirmoqchimisiz? (ha/yo'q): ")
#             if ochirish.lower() == 'ha':
#                 guruh.talaba_ochirish(familiya, ism)
#         else:
#             print("Talaba topilmadi.")
#
#     elif tanlov == '3':
#         print("Talabalar ro'yxati tug'ilgan yil bo'yicha tartiblanmoqda...")
#         guruh.talabalarni_tartiblash('tugilgan_yili')
#         guruh.talabalarni_korsatish()
#
#     elif tanlov == '4':
#         print("Dastur to'xtatildi. Xayr!")
#         break
#
#     else:
#         print("Noto'g'ri tanlov! Iltimos, 1, 2, 3 yoki 4 ni tanlang.")
########################################################################################################################
# 17-topshiriq
# import pygame
# import sys
# import math
#
# # Pygame'ni boshlash
# pygame.init()
#
# # Oyna o'lchami
# kengligi, balandligi = 800, 600
# oyna = pygame.display.set_mode((kengligi, balandligi))
# pygame.display.set_caption("Dumalayotgan G'ildirak")
#
# # Ranglar
# WHITE = (255, 255, 255)
# BLACK = (0, 0, 0)
#
# # G'ildirak parametrlari
# radius = 50
# x = radius
# y = balandligi // 2
# tezlik =  2  # O'zgarmas tezlik
# burchak = 0  # Dastlabki burchak
#
# soat = pygame.time.Clock()
#
# # Asosiy tsikl
# while True:
#     for hodisa in pygame.event.get():
#         if hodisa.type == pygame.QUIT:
#             pygame.quit()
#             sys.exit()
#
#     # Ekranni tozalash
#     oyna.fill(WHITE)
#
#     # G'ildirak markazi koordinatasi
#     markaz = (int(x), int(y))
#
#     # G'ildirakni chizish  doira
#     pygame.draw.circle(oyna, BLACK, markaz, radius, 3)
#
#     # G'ildirak ustida chiziq (aylanayotganini ko‘rsatish uchun)
#     chiziq_uzunligi = radius
#     oxiri_x = x + chiziq_uzunligi * math.cos(burchak)
#     oxiri_y = y + chiziq_uzunligi * math.sin(burchak)
#     pygame.draw.line(oyna, BLACK, markaz, (oxiri_x, oxiri_y), 3)
#
#     # Harakat va burchakni yangilash
#     x += tezlik
#     burchak -= tezlik / radius  # Radiusga nisbatan dumalash
#
#     # Ekrandan chiqib ketmasligi uchun
#     if x - radius > kengligi:  # o‘ngdan chiqib ketsa
#         x = -radius
#
#     pygame.display.flip()
#     soat.tick(60)
########################################################################################################################
# def daraja(x, k, epsilon=0.0001):
#     y = 1
#     while True:
#         y_navbatagi = y + (x / (y ** (k - 1)) - y) / k
#         if abs(y_navbatagi - y) < epsilon:
#             break
#         y = y_navbatagi
#     return y_navbatagi
#
# a = float(input(" qiymatini kiriting: "))
# yuqori = daraja(a, 3) - daraja(a**2 + 1, 6)
# pastki = 1 + daraja(3 + a, 7)
#
# natija = yuqori / pastki
# print(f"Natija: {natija:.6f}")
########################################################################################################################
# class _CHIQARISH:
#     def __init__(self, son, uzunlik, kasr_raqamlar):
#         self.son = son
#         self.uzunlik = uzunlik
#         self.kasr_raqamlar = kasr_raqamlar
#
#     def formatla(self, satr):
#         if '.' not in satr:
#             satr += '.'
#
#         butun_qism, kasr_qism = satr.split('.')
#
#         kasr_qism = kasr_qism[:self.kasr_raqamlar]
#         while len(kasr_qism) < self.kasr_raqamlar:
#             kasr_qism += '0'
#
#         natija = butun_qism + '.' + kasr_qism
#
#         if len(natija) < self.uzunlik:
#             bosh_joy = self.uzunlik - len(natija)
#             natija = ' ' * bosh_joy + natija
#         else:
#             natija = natija[:self.uzunlik]
#
#         return natija
#
#     def chiqar(self):
#         satr = f"{self.son:.{self.kasr_raqamlar}f}"
#         formatlangan = self.formatla(satr)
#         print(formatlangan)
#
#
# class IKKILIK_CHIQARISH(_CHIQARISH):
#     def chiqar(self):
#         butun = int(self.son)
#         kasr = self.son - butun
#
#         butun_ikkilik = ''
#         if butun == 0:
#             butun_ikkilik = '0'
#         else:
#             while butun > 0:
#                 butun_ikkilik = str(butun % 2) + butun_ikkilik
#                 butun //= 2
#
#         kasr_ikkilik = ''
#         for _ in range(self.kasr_raqamlar):
#             kasr *= 2
#             raqam = int(kasr)
#             kasr_ikkilik += str(raqam)
#             kasr -= raqam
#
#         satr = butun_ikkilik + '.' + kasr_ikkilik
#         formatlangan = self.formatla(satr)
#         print(formatlangan)
#
#
# class SAKKIZLIK_CHIQARISH(_CHIQARISH):
#     def chiqar(self):
#         butun = int(self.son)
#         kasr = self.son - butun
#
#         butun_sakkizlik = ''
#         if butun == 0:
#             butun_sakkizlik = '0'
#         else:
#             while butun > 0:
#                 butun_sakkizlik = str(butun % 8) + butun_sakkizlik
#                 butun //= 8
#
#         kasr_sakkizlik = ''
#         for _ in range(self.kasr_raqamlar):
#             kasr *= 8
#             raqam = int(kasr)
#             kasr_sakkizlik += str(raqam)
#             kasr -= raqam
#
#         satr = butun_sakkizlik + '.' + kasr_sakkizlik
#         formatlangan = self.formatla(satr)
#         print(formatlangan)
#
# class ONOLTI_CHIQARISH(_CHIQARISH):
#     def chiqar(self):
#         butun = int(self.son)
#         kasr = self.son - butun
#
#         belgilar = "0123456789ABCDEF"
#         butun_onolti = ''
#         if butun == 0:
#             butun_onolti = '0'
#         else:
#             while butun > 0:
#                 qoldiq = butun % 16
#                 butun_onolti = belgilar[qoldiq] + butun_onolti
#                 butun //= 16
#
#         kasr_onolti = ''
#         for _ in range(self.kasr_raqamlar):
#             kasr *= 16
#             raqam = int(kasr)
#             kasr_onolti += belgilar[raqam]
#             kasr -= raqam
#
#         satr = butun_onolti + '.' + kasr_onolti
#         formatlangan = self.formatla(satr)
#         print(formatlangan)

# print("10lik:")
# _CHIQARISH(3.14, 15, 6).chiqar()
# print("2lik:")
# IKKILIK_CHIQARISH(3.14, 15, 6).chiqar()
# print("8lik:")
# SAKKIZLIK_CHIQARISH(3.14, 15, 6).chiqar()
# print("16lik:")
# ONOLTI_CHIQARISH(3.14, 15, 6).chiqar()
########################################################################################################################
# def matritsani_90_gradus_chapga_burish(matrix):
#       n = len(matrix)
#     burish = [[0] * n for _ in range(n)]
#     for i in range(n):
#         for j in range(n):
#             burish[j][n - i - 1]= matrix[i][j]
#     return burish

# def chiqarish_matrix(matrix):
#     for qator in matrix:
#         print(qator)
# n = int(input("Matritsa o'lchamini kiriting (n): "))
# matrix = []
# print("Matritsa elementlarini kiriting:")
# for i in range(n):
#     qator = list(map(int, input(f"{i+1}-qator elementlari: ").split()))
#     matrix.append(qator)

# print("Boshlangich matritsa:")
# chiqarish_matrix(matrix)
# aylantirilgan_matritsa = matritsani_90_gradus_chapga_burish(matrix)
# print("90 ga soat millariga teskari burilgan matritsa:")
# chiqarish_matrix(aylantirilgan_matritsa)

# QOSHIMCHA YANA QAYAQADUR BURISH KERE BOSA
#burish[i][j] = matrix[i][j] 360 chapka va onga burganda
# [n - j - 1][i] 90 chapka
# [j][n - i - 1] 90 onga
# [n - i - 1][n - j - 1] 180 chapka
# 270 giradus chapka burish 90onga teng
# 270 giradus onga burish 90chapiga teng
########################################################################################################################
# import tkinter as tk
# from tkinter import ttk
#
# class TalabaGuruhi:
#     def __init__(self):
#         self.talabalar = []
#
#     def talaba_qoshish(self, familiya, tugilgan_yil, telefon_raqami):
#         talaba = {
#             'familiya': familiya.strip(),
#             'tugilgan_yil': tugilgan_yil,
#             'telefon_raqami': telefon_raqami
#         }
#         self.talabalar.append(talaba)
#
#     def talaba_qidirish(self, kalit, qiymat):
#         qiymat = qiymat.lower()
#         return [t for t in self.talabalar if t[kalit].lower() == qiymat]
#
#     def talaba_ochirish(self, familiya):
#         familiya = familiya.lower()
#         yangi_royxat = []
#         ochirilganlar_soni = 0
#         for talaba in self.talabalar:
#             if talaba['familiya'].lower() == familiya:
#                 ochirilganlar_soni += 1
#             else:
#                 yangi_royxat.append(talaba)
#         self.talabalar = yangi_royxat
#         return ochirilganlar_soni
#
#     def talabalarni_tartiblash(self, kalit):
#         self.talabalar.sort(key=lambda t: t[kalit])
#
#     def barcha_talabalar(self):
#         return self.talabalar
#
#
# # Ob'ekt yaratamiz
# guruh = TalabaGuruhi()
#
#
# def yangilash_jadval():
#     for item in daraxt.get_children():
#         daraxt.delete(item)
#     for talaba in guruh.barcha_talabalar():    #barcha talabalar malumotini oladi
#         daraxt.insert("", tk.END, values=(talaba['familiya'], talaba['tugilgan_yil'], talaba['telefon_raqami']))
#
#
# def xabar_yoz(matn):
#     matn_oynasi.configure(state='normal')
#     matn_oynasi.delete(1.0, tk.END)
#     matn_oynasi.insert(tk.END, matn)
#     matn_oynasi.configure(state='disabled')
#
#
# def talaba_qoshish_gui():
#     familiya = kirish_familiya.get()
#     tugilgan_yil = kirish_yil.get()
#     telefon_raqami = kirish_telefon.get()
#
#     if familiya and tugilgan_yil and telefon_raqami:
#         try:
#             guruh.talaba_qoshish(familiya, int(tugilgan_yil), telefon_raqami)
#             kirish_familiya.delete(0, tk.END)
#             kirish_yil.delete(0, tk.END)
#             kirish_telefon.delete(0, tk.END)
#             yangilash_jadval()
#             xabar_yoz(f" {familiya} ismli talaba muvaffaqiyatli qo‘shildi.")
#         except ValueError:
#             xabar_yoz(" Tug‘ilgan yil raqamda bo‘lishi kerak.")
#     else:
#         xabar_yoz(" Iltimos, barcha maydonlarni to‘ldiring.")
#
#
# def talaba_qidirish_gui():
#     familiya = kirish_qidiruv.get()
#     if familiya:
#         natijalar = guruh.talaba_qidirish('familiya', familiya)
#         if natijalar:
#             matn = " Qidiruv natijasi:\n\n"
#             for t in natijalar:
#                 matn += (f" Familiya: {t['familiya']}\n"
#                          f" Tug‘ilgan yili: {t['tugilgan_yil']}\n"
#                          f" Telefon raqami: {t['telefon_raqami']}\n\n")
#             xabar_yoz(matn.strip())
#         else:
#             xabar_yoz(" Bunday familiyali talaba topilmadi.")
#     else:
#         xabar_yoz(" Familiyani kiriting.")
#
#
# def talaba_ochirish_gui():
#     familiya = kirish_ochirish.get()
#     if familiya:
#         ochgan_soni = guruh.talaba_ochirish(familiya)
#         if ochgan_soni > 0:
#             yangilash_jadval()
#             xabar_yoz(f" {familiya} familiyali {ochgan_soni} ta talaba muvaffaqiyatli o‘chirildi.")
#         else:
#             xabar_yoz(" Bunday familiyali talaba topilmadi.")
#     else:
#         xabar_yoz(" Familiyani kiriting.")
#
#
# def talabalarni_korsatish_gui():
#     guruh.talabalarni_tartiblash('tugilgan_yil')
#     yangilash_jadval()
#     xabar_yoz(" Talabalar tug‘ilgan yiliga qarab tartiblandi.")
#
#
# # Oyna yaratamiz
# oyna = tk.Tk()
# oyna.title("Talabalar Boshqaruvi")
# oyna.geometry("650x600")
# oyna.configure(bg="#f5f5f5")
#
# # Talaba qo‘shish qismi
# frame_qoshish = tk.Frame(oyna, bg="#f5f5f5")
# frame_qoshish.pack(pady=10)
#
# tk.Label(frame_qoshish, text=" Talaba qo‘shish", font=('Arial', 14, 'bold'), bg="#f5f5f5").grid(row=0, column=0, columnspan=2, pady=5)
# tk.Label(frame_qoshish, text="Familiya:", font=('Arial', 12), bg="#f5f5f5").grid(row=1, column=0, sticky="e")
# kirish_familiya = tk.Entry(frame_qoshish, font=('Arial', 12))
# kirish_familiya.grid(row=1, column=1, padx=5, pady=2)
#
# tk.Label(frame_qoshish, text="Tug‘ilgan yili:", font=('Arial', 12), bg="#f5f5f5").grid(row=2, column=0, sticky="e")
# kirish_yil = tk.Entry(frame_qoshish, font=('Arial', 12))
# kirish_yil.grid(row=2, column=1, padx=5, pady=2)
#
# tk.Label(frame_qoshish, text="Telefon raqami:", font=('Arial', 12), bg="#f5f5f5").grid(row=3, column=0, sticky="e")
# kirish_telefon = tk.Entry(frame_qoshish, font=('Arial', 12))
# kirish_telefon.grid(row=3, column=1, padx=5, pady=2)
#
# tk.Button(frame_qoshish, text=" Talaba qo‘shish", font=('Arial', 12), bg="#4CAF50", fg="white", command=talaba_qoshish_gui).grid(row=4, column=0, columnspan=2, pady=10)  ##4CAF50qizil rang
#
# # Operatsiyalar (Qidirish va O‘chirish)
# frame_operatsiya = tk.Frame(oyna, bg="#f5f5f5")
# frame_operatsiya.pack()
#
# tk.Label(frame_operatsiya, text=" Qidirish (familiya):", font=('Arial', 12), bg="#f5f5f5").grid(row=0, column=0, sticky="e")
# kirish_qidiruv = tk.Entry(frame_operatsiya, font=('Arial', 12))
# kirish_qidiruv.grid(row=0, column=1, padx=5, pady=2)
# tk.Button(frame_operatsiya, text="Qidirish", font=('Arial', 12), bg="#2196F3", fg="white", command=talaba_qidirish_gui).grid(row=0, column=2, padx=5)   ##2196F3kokrangorqafoni
#
# tk.Label(frame_operatsiya, text=" O‘chirish (familiya):", font=('Arial', 12), bg="#f5f5f5").grid(row=1, column=0, sticky="e")
# kirish_ochirish = tk.Entry(frame_operatsiya, font=('Arial', 12))
# kirish_ochirish.grid(row=1, column=1, padx=5, pady=2)
# tk.Button(frame_operatsiya, text="O‘chirish", font=('Arial', 12), bg="#f44336", fg="white", command=talaba_ochirish_gui).grid(row=1, column=2, padx=5)    ##f44336qizil rang
#
# tk.Button(frame_operatsiya, text=" Tartiblash va ko‘rsatish", font=('Arial', 12), bg="#FF9800", fg="white", command=talabalarni_korsatish_gui).grid(row=2, column=0, columnspan=3, pady=10)  #olovrang
#
# # Jadval (Treeview)
# frame_jadval = tk.Frame(oyna)
# frame_jadval.pack(fill=tk.BOTH, expand=True)
#
# ustunlar = ("familiya", "tugilgan_yil", "telefon")
# daraxt = ttk.Treeview(frame_jadval, columns=ustunlar, show="headings", height=8)
# daraxt.heading("familiya", text="Familiya")
# daraxt.heading("tugilgan_yil", text="Tug‘ilgan yili")
# daraxt.heading("telefon", text="Telefon raqami")
# daraxt.column("familiya", anchor="center", width=150)
# daraxt.column("tugilgan_yil", anchor="center", width=100)
# daraxt.column("telefon", anchor="center", width=150)
# daraxt.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
#
# scrollbar = ttk.Scrollbar(frame_jadval, orient=tk.VERTICAL, command=daraxt.yview)
# daraxt.configure(yscroll=scrollbar.set)
# scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
#
# # Pastki matnli oynacha
# frame_matn = tk.Frame(oyna)
# frame_matn.pack(fill=tk.BOTH, padx=10, pady=5)
#
# matn_oynasi = tk.Text(frame_matn, height=6, font=('Arial', 12), wrap=tk.WORD)
# matn_oynasi.pack(fill=tk.BOTH)
# matn_oynasi.configure(state='disabled')
#
# # Dasturni boshlash
# oyna.mainloop()
########################################################################################################################