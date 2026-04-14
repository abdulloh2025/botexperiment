# 7-topshiriq gradyan tushish
# import random
# import matplotlib.pyplot as plt
#
# x_qiymatlari = []
# y_qiymatlari = []
#
# random.seed(42)
# for i in range(100):
#     tasodifiy_x = random.random()
#     shovqin = random.uniform(-0.1, 0.1)
#     tasodifiy_y = 2 * tasodifiy_x + 1 + shovqin
#
#     x_qiymatlari.append(tasodifiy_x)
#     y_qiymatlari.append(tasodifiy_y)
#
#
# w = 0.0
# b = 0.0
# organish_tezligi = 0.01
# iteratsiya_soni = 5000
# n = len(x_qiymatlari)
# mse_tarixi = []
#
# for qadam in range(iteratsiya_soni):
#     mse_yigindisi = 0
#     grad_w = 0
#     grad_b = 0
#
#     for i in range(n):
#         x = x_qiymatlari[i]
#         y = y_qiymatlari[i]
#
#         y_bashorat = w * x + b
#         xatolik = y - y_bashorat
#         mse_yigindisi += xatolik ** 2
#
#         grad_w += -2 * x * xatolik
#         grad_b += -2 * xatolik
#
#     mse = mse_yigindisi / n
#     grad_w /= n
#     grad_b /= n
#
#     w = w - organish_tezligi * grad_w
#     b = b - organish_tezligi * grad_b
#
#     mse_tarixi.append(mse)
#
#     if qadam % 100 == 0:
#         print(f"Qadam {qadam:4}: w={w:.4f}, b={b:.4f}, mse={mse:.4f}")
#
#
# plt.figure(figsize=(10, 5))
#
#
# plt.subplot(1, 2, 1)
# plt.scatter(x_qiymatlari, y_qiymatlari, color='blue', alpha=0.5, label='Ma\'lumotlar')
#
#
# x_chiziq = [0, 1]
# y_chiziq = [w * 0 + b, w * 1 + b]
# plt.plot(x_chiziq, y_chiziq, color='red', linewidth=3, label='Model chizig\'i')
#
# plt.title("Chiziqli Regressiya Natijasi")
# plt.xlabel("X")
# plt.ylabel("Y")
# plt.legend()
# plt.grid(True)
#
#
# plt.subplot(1, 2, 2)
# plt.plot(mse_tarixi, color='green')
# plt.title("MSE xatolikning kamayishi")
# plt.xlabel("Iteratsiyalar")
# plt.ylabel("MSE qiymati")
# plt.grid(True)
#
# plt.tight_layout()
# plt.show()
#
# print(f"\nYakuniy natija: y = {w:.4f}x + {b:.4f}")