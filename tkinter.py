import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
from collections import Counter
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

alphabet = "abdefghijklmnopqrstuvxyzshchng"

def chiz_grafik(matn):
    matn = matn.lower()
    harf_sanagich = Counter(filter(str.isalpha, matn))

    qiymatlar = [harf_sanagich.get(harf, 0) for harf in alphabet]

    plt.clf()  # Eski grafikni tozalash
    fig = plt.figure(figsize=(12, 5))
    plt.bar(alphabet, qiymatlar, color='skyblue')
    plt.title("Harf chastotalari")
    plt.xlabel("Harflar")
    plt.ylabel("Takrorlanish soni")

    return fig

def yangilash_grafik():
    matn = matn_kiritish.get("1.0", tk.END)
    fig = chiz_grafik(matn)

    canvas = FigureCanvasTkAgg(fig, master=oyna)
    canvas.draw()
    canvas.get_tk_widget().grid(row=2, column=0, columnspan=2, pady=10)
    global aktiv_canvas
    aktiv_canvas = canvas

def saqlash_rasm():
    if aktiv_canvas:
        fayl_nomi = filedialog.asksaveasfilename(defaultextension=".png",
                                                 filetypes=[("PNG fayllari", "*.png")])
        if fayl_nomi:
            aktiv_canvas.figure.savefig(fayl_nomi)
            messagebox.showinfo("Saqlash", "Grafik saqlandi.")
    else:
        messagebox.showwarning("Xatolik", "Avval grafikni chizing.")

# Dastur oynasi
oyna = tk.Tk()
oyna.title("Matndagi harflar gistogrammasi")

tk.Label(oyna, text="Matnni kiriting:").grid(row=0, column=0, sticky="w", padx=10, pady=5)
matn_kiritish = tk.Text(oyna, height=5, width=60)
matn_kiritish.grid(row=1, column=0, columnspan=2, padx=10)

tk.Button(oyna, text="Grafikni chiqarish", command=yangilash_grafik).grid(row=3, column=0, pady=10)
tk.Button(oyna, text="Grafikni rasmga saqlash", command=saqlash_rasm).grid(row=3, column=1, pady=10)

aktiv_canvas = None  # Grafik obyekti uchun global o‘zgaruvchi

oyna.mainloop()