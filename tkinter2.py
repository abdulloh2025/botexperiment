import tkinter as tk
from tkinter import filedialog, messagebox
from collections import Counter
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# To'liq va to'g'ri tartiblangan O'zbek alifbosi
alphabet = [
    'a', 'b', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
    'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
    'v', 'x', 'y', 'z', 'sh', 'ch', 'ng'
]

aktiv_canvas = None  # Grafik uchun global o'zgaruvchi

def fayldan_matn_ol():
    fayl_nomi = filedialog.askopenfilename(filetypes=[("Matn fayllari", "*.txt")])
    if fayl_nomi:
        with open(fayl_nomi, "r", encoding="utf-8") as f:
            matn = f.read()
            yangilash_grafik(matn)

def harflarni_sana(matn):
    matn = matn.lower()
    harflar = []
    i = 0
    while i < len(matn):
        if matn[i:i+2] in ['sh', 'ch', 'ng']:
            harflar.append(matn[i:i+2])
            i += 2
        elif matn[i].isalpha():
            harflar.append(matn[i])
            i += 1
        else:
            i += 1
    return Counter(harflar)

def chiz_grafik(sana_counter):
    plt.clf()
    qiymatlar = [sana_counter.get(h, 0) for h in alphabet]

    fig = plt.figure(figsize=(14, 5))
    plt.bar(alphabet, qiymatlar, color='cornflowerblue')
    plt.title("Harf chastotalari")
    plt.xlabel("Harflar (O'zbek alifbosi)")
    plt.ylabel("Takrorlanish soni")
    return fig

def yangilash_grafik(matn):
    global aktiv_canvas
    harf_sanagich = harflarni_sana(matn)
    fig = chiz_grafik(harf_sanagich)

    if aktiv_canvas:
        aktiv_canvas.get_tk_widget().destroy()

    aktiv_canvas = FigureCanvasTkAgg(fig, master=oyna)
    aktiv_canvas.draw()
    aktiv_canvas.get_tk_widget().grid(row=1, column=0, columnspan=2, pady=10)

def saqlash_rasm():
    if aktiv_canvas:
        fayl_nomi = filedialog.asksaveasfilename(defaultextension=".png",
                                                 filetypes=[("PNG fayllari", "*.png")])
        if fayl_nomi:
            aktiv_canvas.figure.savefig(fayl_nomi)
            messagebox.showinfo("Saqlash", "Grafik muvaffaqiyatli saqlandi.")
    else:
        messagebox.showwarning("Xatolik", "Avval fayldan matn tanlang va grafik chizing.")

# GUI oynasi
oyna = tk.Tk()
oyna.title("Harf chastotasi gistogrammasi (fayldan)")

tk.Button(oyna, text="Matn faylini tanlash", command=fayldan_matn_ol, width=25).grid(row=0, column=0, padx=10, pady=10)
tk.Button(oyna, text="Grafikni rasmga saqlash", command=saqlash_rasm, width=25).grid(row=0, column=1, padx=10, pady=10)

oyna.mainloop()
