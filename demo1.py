# # print("demo 1")
# # print("demo 11")
# #   from operator import index
# #from fontTools.misc.cython import returns
#
# #1-topshirigni 3-misoli
# # class Node:
# #      def __init__(self, data):
# #          self.data = data
# #          self.next = None
# #
# # class LinkedList:
# #     def __init__(self):
# #         self.head = None
# #
# #     def append(self, data):
# #         cur = self.head
# #         node = Node(data)
# #         if not self.head:
# #             self.head = node
# #             return
# #         while cur.next:
# #             cur = cur.next
# #         cur.next = node
# #
# #
# #
# #     def remove_oldin_value(self, value):
# #         cur = self.head
# #         prev = None
# #         if not cur or cur.data == value:
# #             print("Birinchi elementdan oldin element yo'q.")
# #         while cur.next and cur.next.data != value:
# #             prev = cur
# #             cur = cur.next
# #
# #         if not cur.next:
# #             print(f"{value} qiymatli element topilmadi.")
# #
# #         if prev and prev.data != value:
# #             prev.next = cur.next
# #         else:
# #             print("Oldingi element qiymati berilgan qiymatga teng yoki yo'q.")
# #     def print(self):
# #         cur = self.head
# #         while cur:
# #             print(cur.data, end=" , ")
# #             cur = cur.next
# #         print()
# #
# #
# # ll = LinkedList()
# # for num in [4, 5, 3, 4, 4, 7, 4, 3, 3, 4]:
# #     ll.append(num)
# #
# # print("Original ro'yxat:")
# # ll.print()
# #
# # ll.remove_oldin_value(4)
# # print("4 dan oldingi element olib tashlangan royxat:")
# # ll.print()
#
# # satr = "Tursin Bugun Fizika fanidan oraliq topshirdi."
# # sozlar = satr[:-1].split()
# # sozlar = sorted(sozlar, key=str.lower)
# # tartiblangan_satr = ' '.join(sozlar) + "."
# # print(tartiblangan_satr)
#
#
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
# #     def toq_manfiy_kopaytma(self):
# #         kopaytma = 1
# #         prev = None                                                      #royhatan oldingi boshlangich
# #         cur = self.head
# #
# #
# #         while cur:
# #             if cur.data < 0:
# #                 kopaytma *= cur.data
# #             if cur.data % 2 != 0:
# #                 if prev:
# #                     prev.next = cur.next
# #                 else:
# #                  self.head = cur.next
# #                 cur = cur.next
# #             else:
# #                 prev = cur
# #                 cur = cur.next
# #
# #         return kopaytma
# #
# # # Misol uchun ro'yxat yaratamiz
# # l = LinkedList()
# # l.append(1)
# # l.append(-2)
# # l.append(3)
# # l.append(-4)
# # l.append(5)
# # l.append(-6)
# # l.append(7)
# # l.append(13)
# # print("Original ro'yxat:")
# # l.print_list()
# #
# # n_kopaytma = l.toq_manfiy_kopaytma()
# # print("Toq qiymatli elementlar olib tashlangan ro'yxat:")
# # l.print_list()
# # print(f"Manfiy qiymatli elementlar ko'paytmasi: {n_kopaytma}")
#
#

#
# #3-topshiriq 1-misol
#
#
# #
# # #
# # class Node:
# #     def __init__(self, data):
# #         self.Data = data
# #         self.Next = None
# #
# # class Stek:
# #     def __init__(self):
# #         self.head = None
# #         self.count = 0
# #
# #     def push(self, data):  # Yangi elementni stekka qo'shish
# #         node = Node(data)
# #         node.Next = self.head
# #         self.head = node
# #         self.count += 1
# #
# #     def is_empty(self):  # Stek bo'shligini tekshirish
# #         return self.head is None
# #
# #     def pop(self):  # Stekdan eng yuqori elementni olib tashlash
# #         if self.is_empty():
# #             return "stek bo'sh"
# #         cur = self.head
# #         self.head = self.head.Next
# #         self.count -= 1
# #         return cur.Data
# #
# #     def peek(self):  # Stekning eng yuqori elementini ko'rish
# #         if self.is_empty():
# #             return "stek bo'sh"
# #         return self.head.Data
# #
# #     def print(self):  # Stekdagi barcha elementlarni chiqarish
# #         if self.is_empty():
# #             return "stek bo'sh"
# #         cur = self.head
# #         while cur is not None:
# #             print(cur.Data, end=" -> ")
# #             cur = cur.Next
# #         print("None")
# #
# #
# # # Stek yaratish va elementlar qo'shish
# # stek = Stek()
# # stek.push(8848)
# # stek.push(8611)
# # stek.push(5895)
# # stek.push(4807)
# # stek.push(5642)
# #
# # # Stek elementlarini chiqarish
# # print("Stek elementlari:")
# # stek.print()
# #
# # # Juft sonlarni topish va ularning o'rtacha arifmetigini hisoblash
# # temp = Stek()
# # juft_sonlar_yigindi = 0
# # juft_sonlar_sonni = 0
# #
# # while not stek.is_empty():
# #     num = stek.pop()
# #     temp.push(num)
# #     if num % 2 == 0:
# #         juft_sonlar_yigindi += num
# #         juft_sonlar_sonni += 1
# #
# # # Elementlarni asl holatiga qaytarish
# # while not temp.is_empty():
# #     stek.push(temp.pop())
# #
# # # Natijalarni chiqarish
# # if juft_sonlar_sonni > 0:
# #     average = juft_sonlar_yigindi / juft_sonlar_sonni
# #     print(f"Juft sonlar o'rtacha arifmetigi: {average}")
# # else:
# #     print("Stekda juft sonlar mavjud emas")
#
#
# #3-topshiriq 2-misol
# #
# # class Node:
# #     def __init__(self, data):
# #         self.data = data
# #         self.next = None
# #
# #
# # class Navbat:
# #     def __init__(self):
# #         self.head = None
# #         self.tail = None
# #         self.count = 0
# #
# #     def navbat_ohiriga_elementqoshish(self, data):  # Navbatning oxiriga element qo'shish
# #         node = Node(data)
# #         if self.head is None:
# #             self.head = self.tail = node
# #         else:
# #             self.tail.next = node
# #             self.tail = node
# #         self.count += 1
# #
# #     def navbat_boshidan_olibtashlash(self):  # Navbatning boshidan elementni olib tashlash
# #         if self.head is None:
# #             return "Navbat bo'sh!"
# #         else:
# #             cur = self.head.data   #navbat boshidagi elementni saqlimiz
# #             self.head = self.head.next
# #             self.count -= 1
# #             return cur
# #
# #     def navbatagi_elementlarni_chqarsh(self):  # Navbatdagi elementlarni chiqarish
# #         if self.head is None:
# #             print("Navbat bosh")
# #             return
# #         cur = self.head
# #         while cur is not None:
# #             print(cur.data, end=" -> ")
# #             cur = cur.next
# #         print("None")
# #
# #     def birdan_kichik_yigindi(self):  # Moduli 1.0 dan kichik sonlar yig'indisi
# #         Jami = 0.0
# #         cur = self.head
# #         while cur is not None:
# #             if abs(cur.data) < 1.0:
# #                 Jami += cur.data
# #             cur = cur.next
# #         return Jami
# #
# #
# #
# # navbat = Navbat()
# #
# # #
# # print("Navbatga elementlar qo'shilyapti: 3.2, 2.2, 2.4, -3.2, 0.5")
# # navbat.navbat_ohiriga_elementqoshish(3.2)
# # navbat.navbat_ohiriga_elementqoshish(2.2)
# # navbat.navbat_ohiriga_elementqoshish(2.4)
# # navbat.navbat_ohiriga_elementqoshish(-3.2)
# # navbat.navbat_ohiriga_elementqoshish(0.5)
# #
# # # Navbat tarkibini chop etamiz
# # print("Navbat tarkibi:")
# # navbat.navbatagi_elementlarni_chqarsh()
# #
# #
# # # sum_less = navbat.birdan_kichik_yigindi()
# # # print(f"Moduli 1.0 dan kichik sonlar yig'indisi: {sum_less:.2f}")
# #
# # dequeued = navbat.navbat_boshidan_olibtashlash()
# # print(f"Navbatdan olib tashlangan element: {dequeued}")
# #
# #
# # print("Navbatga 0.04 qo'shilyapti")
# # navbat.navbat_ohiriga_elementqoshish(0.04)
# #
# #
# # print("Yangi navbat tarkibi:")
# # navbat.navbatagi_elementlarni_chqarsh()
# #
# # # Moduli 1.0 dan kichik bo'lgan sonlar yig'indisini hisoblaymiz
# # sum_less = navbat.birdan_kichik_yigindi()
# # print(f"Moduli 1.0 dan kichik sonlar yig'indisi: {sum_less:.2f}")

########################################################################################################################
########################################################################################################################
#
# #3topwiriq 3misol
#
# # class Node:
# #     def __init__(self, data):
# #         self.data = data
# #         self.next = None
# #
# # class Navbat:
# #     def __init__(self):
# #         self.head = None
# #         self.tail = None
# #
# #     def navbatga_qoshish(self, data):
# #         node = Node(data)
# #         if self.head is None:
# #             self.head = self.tail = node
# #         else:
# #             self.tail.next = node
# #             self.tail = node
# #
# #     def navbatdan_olib_tashlash(self):
# #         if self.head is None:
# #             return None
# #         data = self.head.data
# #         self.head = self.head.next
# #         if self.head is None:
# #             self.tail = None
# #         return data
# #
# #     def Print(self):
# #         if self.head is None:
# #             print("Navbat bo'sh!")
# #             return
# #         cur = self.head
# #         while cur:
# #             print(cur.data, end=" -> ")
# #             cur = cur.next
# #         print("None")
# #
# # # Navbat yaratish va elementlar qo'shish
# # navbat = Navbat()
# # navbat.navbatga_qoshish(3)
# # navbat.navbatga_qoshish(1.3)
# # navbat.navbatga_qoshish(-1.34)
# # navbat.navbatga_qoshish(6)
# # navbat.navbatga_qoshish(4)
# #
# # print("Boshlang'ich navbat:")
# # navbat.Print()
# #
# # # Juft son topilguncha elementlarni chiqarish
# # print("Chiqarilgan elementlar:")
# # while navbat.head and navbat.head.data % 2 != 0:
# #     print(navbat.navbatdan_olib_tashlash(), end=", ")
# #
# # # Natijaviy navbat va korsatkichlar
# # print("\nNatijaviy navbat:")
# # navbat.Print()
# #
# # natija = navbat.head
# # natija1 = navbat.tail
# #
# # print("Boshi manzili:", natija.data)
# # print("Oxiri manzili:", natija1.data)
# #
########################################################################################################################
########################################################################################################################
# # class Node:
# #     def __init__(self, data):
# #         self.data = data
# #         self.next = None
# #
# # class Navbat:
# #     def __init__(self):
# #         self.head = None
# #         self.tail = None
# #
# #     def navbatga_qoshish(self, data):
# #         node = Node(data)
# #         if self.head is None:
# #             self.head = self.tail = node
# #         else:
# #             self.tail.next = node
# #             self.tail = node
# #
# #     def navbatdan_olib_tashlash(self):
# #         if self.head is None:
# #             return None
# #         data = self.head.data
# #         old_node = self.head                                       #eski head tugunini saqlab
# #         self.head = self.head.next
# #         if self.head is None:
# #             self.tail = None
# #         del old_node  # xotirani bo'shatish
# #         return data
# #
# #     def Print(self):
# #         if self.head is None:
# #             print("Navbat bo'sh!")
# #             return
# #         cur = self.head
# #         while cur:
# #             print(cur.data, end=" -> ")
# #             cur = cur.next
# #         print("None")
# #
# # # Navbat yaratish va elementlar qo'shish
# # navbat = Navbat()
# # navbat.navbatga_qoshish(3)
# # navbat.navbatga_qoshish(7)
# # navbat.navbatga_qoshish(5)
# # navbat.navbatga_qoshish(4)
# # navbat.navbatga_qoshish(8)
# #
# # print("Boshlang'ich navbat:")
# # navbat.Print()
# #
# # #  Boshlang'ich P1 va P2 ko'rsatkichlari
# # if navbat.head:
# #     print("Boshlang'ich P1 (Bosh) manzili:", navbat.head.data)
# # else:
# #     print("Boshlang'ich P1 (Bosh) manzili: None")
# #
# # if navbat.tail:
# #     print("Boshlang'ich P2 (Oxir) manzili:", navbat.tail.data)
# # else:
# #     print("Boshlang'ich P2 (Oxir) manzili: None")
# #
# # # Juft butun son topilguncha elementlarni chiqarish
# # print("\nChiqarilgan elementlar:")
# # juft_topildi = False
# # while navbat.head:
# #     data = navbat.head.data
# #     if isinstance(data, int) and data % 2 == 0:
# #         juft_topildi = True
# #         break
# #     print(navbat.navbatdan_olib_tashlash(), end=", ")
# #
# # # Agar butun juft son topilmagan bo‘lsa, qolganlarini ham chiqaramiz
# # if not juft_topildi:
# #     while navbat.head:
# #         print(navbat.navbatdan_olib_tashlash(), end=", ")
# # print("\n\nNatijaviy navbat:")
# # navbat.Print()
# #
#
#
########################################################################################################################
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
# #
# n = int(input("Fibonacci ketma-ketligining nechanchi o‘rnini kiritasiz? "))
#



















