
# shifrlangan_matn = "ZGJGK"
# kalit = 24
# alifbo = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# natija = ""
#
# for harf in shifrlangan_matn:
#     tartib_raqami = alifbo.find(harf)
#     yangi_tartib = (tartib_raqami - kalit) % 26
#
#     natija += alifbo[yangi_tartib]
#
# print("Natija :", natija)












# shifr = "SFINZG"
# alifbo = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# teskari_alifbo = "ZYXWVUTSRQPONMLKJIHGFEDCBA"
# natija = ""
#
# for harf in shifr:
#     index = alifbo.find(harf)
#     yangi_harf = teskari_alifbo[index]
#
#     natija = natija + yangi_harf
#
# print("Natija:", natija)
#
# kalit = "KLIENT"
# shifr = "RKFIXX"
# alifbo_tartibida_kalit = "EIKLNT"
# natija = ""
#
# for harf in kalit:
#     index = 0
#     for i in range(len(alifbo_tartibida_kalit)):
#         if alifbo_tartibida_kalit[i] == harf:
#             index = i
#             break
#
#     natija = natija + shifr[index]
#
# print("Javob:", natija)




#
# ochiq_matn = "ALGORITHM"
# kalit = "SIGMA"
# alifbo = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# natija = ""
#
# for i in range(len(ochiq_matn)):
#
#     p_raqam = alifbo.find(ochiq_matn[i])
#     k_raqam = alifbo.find(kalit[i % len(kalit)])
#
#
#     shifr_raqam = (p_raqam + k_raqam) % 26
#     natija += alifbo[shifr_raqam]
#
# print("Daftardagi bilan bir xil natija:", natija)


# shifr = "PSJMFBY"
# kalit = "NEWTON"
# alifbo = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# natija = ""
#
# for i in range(len(shifr)):
#     c_raqam = alifbo.find(shifr[i])
#     k_raqam = alifbo.find(kalit[i % len(kalit)])
#
#     o_raqam = (c_raqam - k_raqam) % 26
#
#     # Natijani yig'amiz
#     natija += alifbo[o_raqam]
#
# print("Asl so'z:", natija)








# # 1  Diffi
# p = int(input("son kiriting: "))
# g = int(input("son kiriting: "))
# a = int(input("son kiriting: "))
# b = int(input("son kiriting: "))
# A = (g**a)%p
# B = (g**b)%p
# Ka = (B**a)%p
# Kb = (A**b)%p
# print("A =",A,"B =",B,"K =",Ka)
#
# p = int(input("son kiriting: "))
# q = int(input("son kiriting: "))
# n = p * q
# f = (p - 1)*(q - 1)
# e = int(input("son kiriting: "))
# fn_fn = int(f * (1 - 1/2)* (1 - 1/3)* (1 - 1/11))
# d = (e**(fn_fn - 1))%f
# print("n =",n,"fe =",f,"e =",e,"d =",d)
#
# # 3 Shifrlash
# n = int(input("son kiriting: "))
# e = int(input("son kiriting: "))
# M = int(input("son kiriting: "))
# C = (M**e)%n
# print("C =",C)
#
# # 4 Deshifrlash
# n = int(input("son kiriting: "))
# d = int(input("son kiriting: "))
# C = int(input("son kiriting: "))
# M = (C ** d)%n
# print("D =",M)






#
# import tkinter as tk
# from tkinter import messagebox
#
# #1. DIFFIE-HELLMAN OYNASI
# def ochish_diffie():
#     dh_oyna = tk.Toplevel()
#     dh_oyna.title("Diffie-Hellman Protokoli")
#     dh_oyna.geometry("400x450")
#     dh_oyna.configure(bg="#e3f2fd") # Och ko'k fon
#
#     tk.Label(dh_oyna, text="Diffie-Hellman", font=("Arial", 16, "bold"), bg="#e3f2fd", fg="#1565c0").pack(pady=10)
#
#
#     def qator(txt):
#         f = tk.Frame(dh_oyna, bg="#e3f2fd")
#         f.pack(fill="x", padx=30, pady=5)
#         tk.Label(f, text=txt, bg="#e3f2fd", font=("Arial", 10)).pack(side="left")
#         e = tk.Entry(f, font=("Arial", 12))
#         e.pack(side="right", expand=True, fill="x")
#         return e
#
#     p_in = qator("p (tub son):")
#     g_in = qator("g (generator):")
#     a_in = qator("a (maxfiy A):")
#     b_in = qator("b (maxfiy B):")
#
#     def hisobla():
#         try:
#             p, g, a, b = int(p_in.get()), int(g_in.get()), int(a_in.get()), int(b_in.get())
#             A = pow(g, a, p)
#             B = pow(g, b, p)
#             K = pow(B, a, p)
#             messagebox.showinfo("Natija", f"A ochiq: {A}\nB ochiq: {B}\nUmumiy kalit (K): {K}")
#         except: messagebox.showerror("Xato", "Faqat son kiriting!")
#
#     tk.Button(dh_oyna, text="HISOBLASH", command=hisobla, bg="#1565c0", fg="white", font=("Arial", 12, "bold")).pack(pady=20)
#
# # --- 2. RSA KALIT YARATISH OYNASI ---
# def ochish_rsa_kalit():
#     rk_oyna = tk.Toplevel()
#     rk_oyna.title("RSA Kalit Generatsiyasi")
#     rk_oyna.geometry("400x400")
#     rk_oyna.configure(bg="#f3e5f5") # Siyohrang fon
#
#     tk.Label(rk_oyna, text="RSA Kalit Yaratish", font=("Arial", 16, "bold"), bg="#f3e5f5", fg="#7b1fa2").pack(pady=10)
#
#     def qator(txt):
#         f = tk.Frame(rk_oyna, bg="#f3e5f5")
#         f.pack(fill="x", padx=30, pady=5)
#         tk.Label(f, text=txt, bg="#f3e5f5").pack(side="left")
#         e = tk.Entry(f, font=("Arial", 12))
#         e.pack(side="right", expand=True, fill="x")
#         return e
#
#     p_in = qator("p soni:")
#     q_in = qator("q soni:")
#     e_in = qator("e (ochiq):")
#
#     def yarat():
#         try:
#             p, q, e = int(p_in.get()), int(q_in.get()), int(e_in.get())
#             n, f = p * q, (p-1)*(q-1)
#             d = pow(e, -1, f)
#             messagebox.showinfo("Natija", f"Modul (n): {n}\nEyler (φ): {f}\nMaxfiy (d): {d}")
#         except: messagebox.showerror("Xato", "Noto'g'ri ma'lumot!")
#
#     tk.Button(rk_oyna, text="YARATISH", command=yarat, bg="#7b1fa2", fg="white", font=("Arial", 12, "bold")).pack(pady=20)
#
# # --- 3. RSA SHIFRLASH OYNASI ---
# def ochish_shifrlash():
#     sh_oyna = tk.Toplevel()
#     sh_oyna.title("RSA Shifrlash")
#     sh_oyna.geometry("400x350")
#     sh_oyna.configure(bg="#e8f5e9") # Yashil fon
#
#     tk.Label(sh_oyna, text="RSA Shifrlash", font=("Arial", 16, "bold"), bg="#e8f5e9", fg="#2e7d32").pack(pady=10)
#
#     def qator(txt):
#         f = tk.Frame(sh_oyna, bg="#e8f5e9")
#         f.pack(fill="x", padx=30, pady=5)
#         tk.Label(f, text=txt, bg="#e8f5e9").pack(side="left")
#         e = tk.Entry(f, font=("Arial", 12))
#         e.pack(side="right", expand=True, fill="x")
#         return e
#
#     n_in = qator("n (modul):")
#     e_in = qator("e (ochiq):")
#     m_in = qator("M (matn):")
#
#     def shifrlash():
#         try:
#             n, e, m = int(n_in.get()), int(e_in.get()), int(m_in.get())
#             c = pow(m, e, n)
#             messagebox.showinfo("Natija", f"Shifrlangan matn (C): {c}")
#         except: messagebox.showerror("Xato", "Faqat son!")
#
#     tk.Button(sh_oyna, text="SHIFRLASH", command=shifrlash, bg="#2e7d32", fg="white", font=("Arial", 12, "bold")).pack(pady=20)
#
# # 4. RSA DESHIFRLASH OYNASI
# def ochish_deshifrlash():
#     dsh_oyna = tk.Toplevel()
#     dsh_oyna.title("RSA Deshifrlash")
#     dsh_oyna.geometry("400x350")
#     dsh_oyna.configure(bg="#fff3e0") # To'q sariq fon
#
#     tk.Label(dsh_oyna, text="RSA Deshifrlash", font=("Arial", 16, "bold"), bg="#fff3e0", fg="#ef6c00").pack(pady=10)
#
#     def qator(txt):
#         f = tk.Frame(dsh_oyna, bg="#fff3e0")
#         f.pack(fill="x", padx=30, pady=5)
#         tk.Label(f, text=txt, bg="#fff3e0").pack(side="left")
#         e = tk.Entry(f, font=("Arial", 12))
#         e.pack(side="right", expand=True, fill="x")
#         return e
#
#     n_in = qator("n (modul):")
#     d_in = qator("d (maxfiy):")
#     c_in = qator("C (shifr):")
#
#     def deshifrlash():
#         try:
#             n, d, c = int(n_in.get()), int(d_in.get()), int(c_in.get())
#             m = pow(c, d, n)
#             messagebox.showinfo("Natija", f"Asl matn (M): {m}")
#         except: messagebox.showerror("Xato", "Faqat son!")
#
#     tk.Button(dsh_oyna, text="DESHIFRLASH", command=deshifrlash, bg="#ef6c00", fg="white", font=("Arial", 12, "bold")).pack(pady=20)
#
#
# # --- ASOSIY BOSHQARUV OYNASI ---
# root = tk.Tk()
# root.title("Kriptografiya Portali")
# root.geometry("450x500")
# root.configure(bg="#263238") # To'q kulrang fon
#
# tk.Label(root, text="ALGORITMNI TANLANG", font=("Arial", 18, "bold"), bg="#263238", fg="#eceff1").pack(pady=30)
#
# # Tugmalar stili
# btn_params = {"font": ("Arial", 12, "bold"), "width": 25, "pady": 10, "cursor": "hand2"}
#
# tk.Button(root, text="1. Diffie-Hellman", bg="#1565c0", fg="white", command=ochish_diffie, **btn_params).pack(pady=10)
# tk.Button(root, text="2. RSA Kalit Yaratish", bg="#7b1fa2", fg="white", command=ochish_rsa_kalit, **btn_params).pack(pady=10)
# tk.Button(root, text="3. RSA Shifrlash", bg="#2e7d32", fg="white", command=ochish_shifrlash, **btn_params).pack(pady=10)
# tk.Button(root, text="4. RSA Deshifrlash", bg="#ef6c00", fg="white", command=ochish_deshifrlash, **btn_params).pack(pady=10)
#
# tk.Label(root, text="Dastur 2026", bg="#263238", fg="#546e7a").pack(side="bottom", pady=10)
#
# root.mainloop()
#
#




