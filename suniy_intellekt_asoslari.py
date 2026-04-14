import random
import matplotlib.pyplot as plt

def suniy_hayot_avtomati(qoida_raqami, qadamlar_soni, kenglik):
    qoida_ikkilik = format(qoida_raqami, '08b')


    qoidalar = {
        (1, 1, 1): int(qoida_ikkilik[0]),
        (1, 1, 0): int(qoida_ikkilik[1]),
        (1, 0, 1): int(qoida_ikkilik[2]),
        (1, 0, 0): int(qoida_ikkilik[3]),
        (0, 1, 1): int(qoida_ikkilik[4]),
        (0, 1, 0): int(qoida_ikkilik[5]),
        (0, 0, 1): int(qoida_ikkilik[6]),
        (0, 0, 0): int(qoida_ikkilik[7])
    }


    hozirgi_qator = [random.randint(0, 1) for i in range(kenglik)]

    matritsa = [hozirgi_qator]

    for i in range(qadamlar_soni - 1):
        keyingi_qator = []
        for i in range(kenglik):
            # Qo'shnilar: chap, markaz va o'ng katak
            chap = hozirgi_qator[(i - 1) % kenglik]
            markaz = hozirgi_qator[i]
            ong = hozirgi_qator[(i + 1) % kenglik]

            # Yangi holatni jadvaldan aniqlash
            yangi_holat = qoidalar[(chap, markaz, ong)]
            keyingi_qator.append(yangi_holat)

        hozirgi_qator = keyingi_qator
        matritsa.append(hozirgi_qator)

    return matritsa

QOIDA = 98
QADAMLAR = 32
KENGLIK = 32

natija_matritsasi = suniy_hayot_avtomati(QOIDA, QADAMLAR, KENGLIK)

plt.figure(figsize=(10, 10))

plt.imshow(natija_matritsasi, cmap='binary', interpolation='nearest')

plt.title(f"Sun'iy hayot: {QOIDA}-qoida bo'yicha elementar avtomat", fontsize=14)
plt.axis('off')

plt.show()
# matritsada 32 qadam tashagandan kegin ohiriga borgandan kegin yana nechi marta qadam tashidi