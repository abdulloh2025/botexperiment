import random
import tkinter as tk
from tkinter import messagebox

# 1. Wolfram avtomati asosida dunyoni yaratish (Wolfram Elementary CA)
def wolfram_dunyoni_yarat(qator_uzunligi, qator_soni, qoida_raqami):
    # Qoidani 8-bitli ikkilik tizimga o'tkazish
    qoida_bin = format(qoida_raqami, '08b')
    print(f"Qoida {qoida_raqami} ikkilikda: {qoida_bin}")

    # Boshlang'ich holat (0-qator tasodifiy to'ldiriladi)
    # Bu yerda i ishlatildi
    dunya = [[0] * qator_uzunligi for i in range(qator_soni)]
    dunya[0] = [random.randint(0, 1) for i in range(qator_uzunligi)]

    # Wolfram qoidalarini qatorlar bo'yicha qo'llash
    for i in range(qator_soni - 1):
        for j in range(qator_uzunligi):
            # Qo'shnilarni aniqlash (chap, markaz, ong)
            chap = dunya[i][j - 1]
            markaz = dunya[i][j]
            ong = dunya[i][(j + 1) % qator_uzunligi]

            holat = f"{chap}{markaz}{ong}"
            # Ikkilikdan o'nlikka o'tkazib qoida indeksini topish
            indeks = 7 - int(holat, 2)
            dunya[i + 1][j] = int(qoida_bin[indeks])
    return dunya


# 2. Conway "Hayot o'yini" qoidalari
def hayot_oyini_qadam(hozirgi_dunya):
    yangi_dunya = [qator[:] for qator in hozirgi_dunya]
    n_qator = len(hozirgi_dunya)
    m_ustun = len(hozirgi_dunya[0])

    for i in range(1, n_qator - 1):
        for j in range(1, m_ustun - 1):
            # 8 ta qo'shnini yig'indisini hisoblash
            qoshnilar_yigindisi = (
                    hozirgi_dunya[i - 1][j - 1] + hozirgi_dunya[i - 1][j] + hozirgi_dunya[i - 1][j + 1] +
                    hozirgi_dunya[i][j - 1] + hozirgi_dunya[i][j + 1] +
                    hozirgi_dunya[i + 1][j - 1] + hozirgi_dunya[i + 1][j] + hozirgi_dunya[i + 1][j + 1]
            )

            # Tirik yoki o'lik holatini aniqlash
            if hozirgi_dunya[i][j] == 1:
                # Tirik hujayra: 2 yoki 3 qo'shni bo'lsa yashaydi
                yangi_dunya[i][j] = 1 if qoshnilar_yigindisi in [2, 3] else 0
            else:
                # O'lik hujayra: 3 ta qo'shni bo'lsa tiriladi
                yangi_dunya[i][j] = 1 if qoshnilar_yigindisi == 3 else 0
    return yangi_dunya


# 3. Interfeys klassi (Tkinter orqali vizualizatsiya)
class SimulyatsiyaDasturi:
    def __init__(self, asosiy_oyna, tarix):
        self.oyna = asosiy_oyna
        self.tarix = tarix
        self.qadam_indeksi = 0
        self.katak_ulchami = 15

        # Chizma maydoni (Canvas)
        self.kvars = tk.Canvas(asosiy_oyna, width=len(tarix[0][0]) * self.katak_ulchami,
                               height=len(tarix[0]) * self.katak_ulchami, bg="white")
        self.kvars.pack(pady=10)

        # Boshqaruv tugmalari
        boshqaruv = tk.Frame(asosiy_oyna)
        boshqaruv.pack(pady=5)
        tk.Button(boshqaruv, text="<< Oldingi", command=self.oldingi, width=10).pack(side=tk.LEFT, padx=5)
        tk.Button(boshqaruv, text="Keyingi >>", command=self.keyingi, width=10).pack(side=tk.LEFT, padx=5)

        self.holat_label = tk.Label(asosiy_oyna, text="")
        self.holat_label.pack()

        self.chizish()

    def chizish(self):
        self.kvars.delete("all")
        matritsa = self.tarix[self.qadam_indeksi]
        # Bu yerda enumerate ishlatilgan, i va j o'zgaruvchilari tayyor
        for i, qator in enumerate(matritsa):
            for j, qiymat in enumerate(qator):
                if qiymat == 1:
                    x1, y1 = j * self.katak_ulchami, i * self.katak_ulchami
                    self.kvars.create_rectangle(x1, y1, x1 + self.katak_ulchami, y1 + self.katak_ulchami,
                                                fill="black", outline="gray")
        self.holat_label.config(text=f"Hozirgi qadam: {self.qadam_indeksi} / {len(self.tarix) - 1}")

    def keyingi(self):
        if self.qadam_indeksi < len(self.tarix) - 1:
            self.qadam_indeksi += 1
            self.chizish()
        else:
            messagebox.showinfo("Tugadi", "Bu oxirgi iteratsiya.")

    def oldingi(self):
        if self.qadam_indeksi > 0:
            self.qadam_indeksi -= 1
            self.chizish()


# Dasturni ishga tushirish qismi
if __name__ == "__main__":
    n = int(input("n (ustunlar soni)="))
    m = int(input("m (qatorlar soni)="))
    qoida = int(input("Qoida raqami (0-255): "))

    # 1-qadam: Wolfram orqali matritsa yaratish
    dastlabki_dunya = wolfram_dunyoni_yarat(n, m, qoida)

    # Terminalda matritsani chiqarish
    print("\nHosil bo'lgan boshlang'ich matritsa:")
    for qator in dastlabki_dunya:
        print(qator)
    print("-" * 30)

    # 2-qadam: Hayot o'yini tarixi (10 qadamgacha)
    tarix_ruyxati = [dastlabki_dunya]
    # Bu yerda _ o'rniga k qo'yildi (i bilan aralashib ketmasligi uchun)
    for k in range(100):
        keyingi_holat = hayot_oyini_qadam(tarix_ruyxati[-1])
        if keyingi_holat == tarix_ruyxati[-1]:
            break
        tarix_ruyxati.append(keyingi_holat)

    # 3-qadam: Oynani ochish
    root = tk.Tk()
    root.title("Sun'iy Hayot: Wolfram + Conway")
    app = SimulyatsiyaDasturi(root, tarix_ruyxati)
    root.mainloop()