# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#
# class LinkedList:
#     def __init__(self):
#         self.head = None
#
#     def append(self, data):
#         if not self.head:
#             self.head = Node(data)
#             return
#         cur = self.head
#         while cur.next:
#             cur = cur.next
#         cur.next = Node(data)
#
#     def print_list(self):
#         cur = self.head
#         while cur:
#             print(cur.data, end=", ")
#             cur = cur.next
#         print()
#
#     def append_birinchi(self, value):
#         cur = self.head
#         while cur:
#             if cur.data > value:
#                 new_node = Node(cur.data)
#                 new_node.next = cur.next
#                 cur.next = new_node
#                 return
#             cur = cur.next
#         print(f"{value} dan katta element topilmadi.")
# # Misol
# l = LinkedList()
# for num in [10, 20, 30, 40, 50]:
#     l.append(num)
# print("Original ro'yxat:")
# l.print_list()
# l.append_birinchi(15)
# print("dan katta birinchi element qoshilgan royxat:")
# l.print_list()
########################################################################################################################
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.prev = None
#         self.next = None
#
#
# class DoublyLinkedList:
#     def __init__(self):
#         self.head = None
#         self.tail = None
#
#     def append(self, data):
#         new_node = Node(data)
#         if not self.head:
#             self.head = new_node
#             self.tail = new_node
#         else:
#             new_node.prev = self.tail
#             self.tail.next = new_node
#             self.tail = new_node
#
#     def ohirgi_elementni_royhati_boshiga_otkazish(self):
#         if not self.head or self.head == self.tail:
#             return
#
#         last = self.tail
#         self.tail = last.prev
#         self.tail.next = None
#
#         last.prev = None
#         last.next = self.head
#         self.head.prev = last
#         self.head = last
#
#     def musbat_qiymatli_elementlarni_olibtashlash(self):
#         cur = self.head
#         while cur:
#             if cur.data > 0:
#                 if cur.prev:
#                     cur.prev.next = cur.next
#                 else:
#                     self.head = cur.next
#
#                 if cur.next:
#                     cur.next.prev = cur.prev
#                 else:
#                     self.tail = cur.prev
#
#             cur = cur.next
#
#     def print_list(self):
#         cur = self.head
#         while cur:
#             print(cur.data, end=" <-> ")
#             cur = cur.next
#         print("None")
#
#
#
# dl = DoublyLinkedList()
# for num in [1, -2, 3, 4, 6, 9, -4, 5,]:
#     dl.append(num)
#
# print("Original ro'yxat:")
# dl.print_list()
#
# dl.ohirgi_elementni_royhati_boshiga_otkazish()
# print("\nOxirgi element boshiga o'tkazilgan:")
# dl.print_list()
#
# dl. musbat_qiymatli_elementlarni_olibtashlash()
# print("\nMusbat sonlar o'chirilgan:")
# dl.print_list()
########################################################################################################################
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.prev = None
#         self.next = None
#
#
# class DoublyLinkedList:
#     def __init__(self):
#         self.head = None
#         self.tail = None
#
#     def append(self, data):
#         new_node = Node(data)
#         if not self.head:
#             self.head = new_node
#             self.tail = new_node
#         else:
#             new_node.prev = self.tail
#             self.tail.next = new_node
#             self.tail = new_node
#
#     def ohirgi_elementni_royhati_boshiga_otkazish(self):
#         if not self.head or self.head == self.tail:
#             return
#
#         last = self.tail
#         self.tail = last.prev
#         self.tail.next = None
#
#         last.prev = None        #buyoda obtawidi
#         last.next = self.head
#         self.head.prev = last
#         self.head = last    #royhat boshini ohrgisiga ozgart
#
#     def musbat_qiymatli_elementlarni_olibtashlash(self):
#         cur = self.head
#         while cur:
#             next_node = cur.next          # Keyingi tugunni saqlab qolamiz, chunki cur o‘chiriladi
#             if cur.data > 0:
#                 if cur.prev:
#                     cur.prev.next = cur.next      #a ni c ga ulaw uchn
#                 else:                             #birinchi elem
#                     self.head = cur.next
#
#                 if cur.next:                     #ortadini ochirib ohirgini boshiga ulaw
#                     cur.next.prev = cur.prev
#                 else:                             #ohirgi elemnt bolsa oldign ulw uc
#                     self.tail = cur.prev
#
#             cur = next_node  # Keyingi elementga o‘tamiz
#
#     def print_list(self):
#         cur = self.head
#         while cur:
#             print(cur.data, end=" <-> ")
#             cur = cur.next
#         print("None")
#
#     def print_teskari(self):  # Ro'yxatni teskari chiqarish
#         cur = self.tail
#         while cur:
#             print(cur.data, end=" <-> ")
#             cur = cur.prev          #oldingi elemntga otad
#         print("None")
#
#
# # Sinov uchun kod:
# dl = DoublyLinkedList()
# for num in [1, -2, 3, 4, 6, 9, -4, 5]:
#     dl.append(num)
#
# print("Original ro'yxat:")
# dl.print_list()
# print("orginal ro'yxat teskarisi:")
# dl.print_teskari()
#
# dl.ohirgi_elementni_royhati_boshiga_otkazish()
# print("\nOxirgi element boshiga o'tkazilgan:")
# dl.print_list()
# dl.print_teskari()
# dl.musbat_qiymatli_elementlarni_olibtashlash()
# print("\nMusbat sonlar o'chirilgan:")
# dl.print_list()
#
# print("\nRo'yxatni teskari chop etish:")
# dl.print_teskari()
########################################################################################################################
#1-topshirigni 3-misoli
# class Node:
#      def __init__(self, data):
#          self.data = data
#          self.next = None
#
# class LinkedList:
#     def __init__(self):
#         self.head = None
#
#     def append(self, data):
#         cur = self.head
#         node = Node(data)
#         if not self.head:
#             self.head = node
#             return
#         while cur.next:
#             cur = cur.next
#         cur.next = node
#
#
#
#     def remove_oldin_value(self, value):
#         cur = self.head
#         prev = None
#         if not cur or cur.data == value:
#             print("Birinchi elementdan oldin element yo'q.")
#         while cur.next and cur.next.data != value:
#             prev = cur
#             cur = cur.next
#
#         if not cur.next:
#             print(f"{value} qiymatli element topilmadi.")
#
#         if prev and prev.data != value:
#             prev.next = cur.next
#         else:
#             print("Oldingi element qiymati berilgan qiymatga teng yoki yo'q.")
#     def print(self):
#         cur = self.head
#         while cur:
#             print(cur.data, end=" , ")
#             cur = cur.next
#         print()
#
#
# ll = LinkedList()
# for num in [4, 5, 3, 4, 4, 7, 4, 3, 3, 4]:
#     ll.append(num)
#
# print("Original ro'yxat:")
# ll.print()
#
# ll.remove_oldin_value(4)
# print("4 dan oldingi element olib tashlangan royxat:")
# ll.print()
########################################################################################################################
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#
# class LinkedList:
#     def __init__(self):
#         self.head = None
#
#     def append(self, data):
#         if not self.head:
#             self.head = Node(data)
#             return
#         cur = self.head
#         while cur.next:
#             cur = cur.next
#         cur.next = Node(data)
#
#     def print_list(self):
#         cur = self.head
#         while cur:
#             print(cur.data, end=", ")
#             cur = cur.next
#         print()
#
#     def toq_manfiy_kopaytma(self):
#         kopaytma = 1
#         prev = None                                                      #royhatan oldingi boshlangich
#         cur = self.head
#
#
#         while cur:
#             if cur.data < 0:
#                 kopaytma *= cur.data
#             if cur.data % 2 != 0:
#                 if prev:
#                     prev.next = cur.next
#                 else:
#                  self.head = cur.next
#                 cur = cur.next
#             else:
#                 prev = cur
#                 cur = cur.next
#
#         return kopaytma
#
# # Misol uchun ro'yxat yaratamiz
# l = LinkedList()
# l.append(1)
# l.append(-2)
# l.append(3)
# l.append(-4)
# l.append(5)
# l.append(-6)
# l.append(7)
# l.append(13)
# print("Original ro'yxat:")
# l.print_list()
#
# n_kopaytma = l.toq_manfiy_kopaytma()
# print("Toq qiymatli elementlar olib tashlangan ro'yxat:")
# l.print_list()
# print(f"Manfiy qiymatli elementlar ko'paytmasi: {n_kopaytma}")
########################################################################################################################
#3-topshiriq 1-misol
# class Node:
#     def __init__(self, data):
#         self.Data = data
#         self.Next = None
#
# class Stek:
#     def __init__(self):
#         self.head = None
#         self.count = 0
#
#     def push(self, data):  # Yangi elementni stekka qo'shish
#         node = Node(data)
#         node.Next = self.head
#         self.head = node
#         self.count += 1
#
#     def is_empty(self):  # Stek bo'shligini tekshirish
#         return self.head is None
#
#     def pop(self):  # Stekdan eng yuqori elementni olib tashlash
#         if self.is_empty():
#             return "stek bo'sh"
#         cur = self.head
#         self.head = self.head.Next
#         self.count -= 1
#         return cur.Data
#
#     def peek(self):  # Stekning eng yuqori elementini ko'rish
#         if self.is_empty():
#             return "stek bo'sh"
#         return self.head.Data
#
#     def print(self):  # Stekdagi barcha elementlarni chiqarish
#         if self.is_empty():
#             return "stek bo'sh"
#         cur = self.head
#         while cur is not None:
#             print(cur.Data, end=" -> ")
#             cur = cur.Next
#         print("None")
#
#
# # Stek yaratish va elementlar qo'shish
# stek = Stek()
# stek.push(8848)
# stek.push(8611)
# stek.push(5895)
# stek.push(4807)
# stek.push(5642)
#
# # Stek elementlarini chiqarish
# print("Stek elementlari:")
# stek.print()
#
# # Juft sonlarni topish va ularning o'rtacha arifmetigini hisoblash
# temp = Stek()
# juft_sonlar_yigindi = 0
# juft_sonlar_sonni = 0
#
# while not stek.is_empty():
#     num = stek.pop()
#     temp.push(num)
#     if num % 2 == 0:
#         juft_sonlar_yigindi += num
#         juft_sonlar_sonni += 1
#
# # Elementlarni asl holatiga qaytarish
# while not temp.is_empty():
#     stek.push(temp.pop())
#
# # Natijalarni chiqarish
# if juft_sonlar_sonni > 0:
#     average = juft_sonlar_yigindi / juft_sonlar_sonni
#     print(f"Juft sonlar o'rtacha arifmetigi: {average}")
# else:
#     print("Stekda juft sonlar mavjud emas")
########################################################################################################################
#3-topshiriq 2-misol
#
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#
#
# class Navbat:
#     def __init__(self):
#         self.head = None
#         self.tail = None
#         self.count = 0
#
#     def navbat_ohiriga_elementqoshish(self, data):  # Navbatning oxiriga element qo'shish
#         node = Node(data)
#         if self.head is None:
#             self.head = self.tail = node
#         else:
#             self.tail.next = node
#             self.tail = node
#         self.count += 1
#
#     def navbat_boshidan_olibtashlash(self):  # Navbatning boshidan elementni olib tashlash
#         if self.head is None:
#             return "Navbat bo'sh!"
#         else:
#             cur = self.head.data   #navbat boshidagi elementni saqlimiz
#             self.head = self.head.next
#             self.count -= 1
#             return cur
#
#     def navbatagi_elementlarni_chqarsh(self):  # Navbatdagi elementlarni chiqarish
#         if self.head is None:
#             print("Navbat bosh")
#             return
#         cur = self.head
#         while cur is not None:
#             print(cur.data, end=" -> ")
#             cur = cur.next
#         print("None")
#
#     def birdan_kichik_yigindi(self):  # Moduli 1.0 dan kichik sonlar yig'indisi
#         Jami = 0.0
#         cur = self.head
#         while cur is not None:
#             if abs(cur.data) < 1.0:
#                 Jami += cur.data
#             cur = cur.next
#         return Jami
#
#
#
# navbat = Navbat()
#
# #
# print("Navbatga elementlar qo'shilyapti: 3.2, 2.2, 2.4, -3.2, 0.5")
# navbat.navbat_ohiriga_elementqoshish(3.2)
# navbat.navbat_ohiriga_elementqoshish(2.2)
# navbat.navbat_ohiriga_elementqoshish(2.4)
# navbat.navbat_ohiriga_elementqoshish(-3.2)
# navbat.navbat_ohiriga_elementqoshish(0.5)
#
# # Navbat tarkibini chop etamiz
# print("Navbat tarkibi:")
# navbat.navbatagi_elementlarni_chqarsh()
#
#
# # sum_less = navbat.birdan_kichik_yigindi()
# # print(f"Moduli 1.0 dan kichik sonlar yig'indisi: {sum_less:.2f}")
#
# dequeued = navbat.navbat_boshidan_olibtashlash()
# print(f"Navbatdan olib tashlangan element: {dequeued}")
# print("Navbatga 0.04 qo'shilyapti")
# navbat.navbat_ohiriga_elementqoshish(0.04)
# print("Yangi navbat tarkibi:")
# navbat.navbatagi_elementlarni_chqarsh()
# # Moduli 1.0 dan kichik bo'lgan sonlar yig'indisini hisoblaymiz
# sum_less = navbat.birdan_kichik_yigindi()
# print(f"Moduli 1.0 dan kichik sonlar yig'indisi: {sum_less:.2f}")
########################################################################################################################
#3topwiriq 3misol
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#
# class Navbat:
#     def __init__(self):
#         self.head = None
#         self.tail = None
#
#     def navbatga_qoshish(self, data):
#         node = Node(data)
#         if self.head is None:
#             self.head = self.tail = node
#         else:
#             self.tail.next = node
#             self.tail = node
#
#     def navbatdan_olib_tashlash(self):
#         if self.head is None:
#             return None
#         data = self.head.data
#         self.head = self.head.next
#         if self.head is None:
#             self.tail = None
#         return data
#
#     def Print(self):
#         if self.head is None:
#             print("Navbat bo'sh!")
#             return
#         cur = self.head
#         while cur:
#             print(cur.data, end=" -> ")
#             cur = cur.next
#         print("None")
#
# # Navbat yaratish va elementlar qo'shish
# navbat = Navbat()
# navbat.navbatga_qoshish(3)
# navbat.navbatga_qoshish(1.3)
# navbat.navbatga_qoshish(-1.34)
# navbat.navbatga_qoshish(6)
# navbat.navbatga_qoshish(4)
#
# print("Boshlang'ich navbat:")
# navbat.Print()
#
# # Juft son topilguncha elementlarni chiqarish
# print("Chiqarilgan elementlar:")
# while navbat.head and navbat.head.data % 2 != 0:
#     print(navbat.navbatdan_olib_tashlash(), end=", ")
#
# # Natijaviy navbat va korsatkichlar
# print("\nNatijaviy navbat:")
# navbat.Print()
#
# natija = navbat.head
# natija1 = navbat.tail
#
# print("Boshi manzili:", natija.data)
# print("Oxiri manzili:", natija1.data)
########################################################################################################################
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#
# class Navbat:
#     def __init__(self):
#         self.head = None
#         self.tail = None
#
#     def navbatga_qoshish(self, data):
#         node = Node(data)
#         if self.head is None:
#             self.head = self.tail = node
#         else:
#             self.tail.next = node
#             self.tail = node
#
#     def navbatdan_olib_tashlash(self):
#         if self.head is None:
#             return None
#         data = self.head.data
#         old_node = self.head                                       #eski head tugunini saqlab
#         self.head = self.head.next
#         if self.head is None:
#             self.tail = None
#         del old_node  # xotirani bo'shatish
#         return data
#
#     def Print(self):
#         if self.head is None:
#             print("Navbat bo'sh!")
#             return
#         cur = self.head
#         while cur:
#             print(cur.data, end=" -> ")
#             cur = cur.next
#         print("None")
#
# # Navbat yaratish va elementlar qo'shish
# navbat = Navbat()
# navbat.navbatga_qoshish(3)
# navbat.navbatga_qoshish(7)
# navbat.navbatga_qoshish(5)
# navbat.navbatga_qoshish(4)
# navbat.navbatga_qoshish(8)
#
# print("Boshlang'ich navbat:")
# navbat.Print()
#
# #  Boshlang'ich P1 va P2 ko'rsatkichlari
# if navbat.head:
#     print("Boshlang'ich P1 (Bosh) manzili:", navbat.head.data)
# else:
#     print("Boshlang'ich P1 (Bosh) manzili: None")
#
# if navbat.tail:
#     print("Boshlang'ich P2 (Oxir) manzili:", navbat.tail.data)
# else:
#     print("Boshlang'ich P2 (Oxir) manzili: None")
#
# # Juft butun son topilguncha elementlarni chiqarish
# print("\nChiqarilgan elementlar:")
# juft_topildi = False
# while navbat.head:
#     data = navbat.head.data
#     if isinstance(data, int) and data % 2 == 0:
#         juft_topildi = True
#         break
#     print(navbat.navbatdan_olib_tashlash(), end=", ")
#
# # Agar butun juft son topilmagan bo‘lsa, qolganlarini ham chiqaramiz
# if not juft_topildi:
#     while navbat.head:
#         print(navbat.navbatdan_olib_tashlash(), end=", ")
# print("\n\nNatijaviy navbat:")
# navbat.Print()
########################################################################################################################










