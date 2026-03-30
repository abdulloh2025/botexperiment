#5x5 matrixni transponerlash

# print("5x5 matritsani kiriting:")
# A = []
# for i in range(5):
#     qator= list(map(int, input(f"{i+1}-qatorni kiriting (5 ta son): ").split()))
#     A.append(qator)
#
#
# T = []
# for j in range(5):
#     yangi_qator = []
#     for i in range(5):
#         yangi_qator.append(A[i][j])
#     T.append(yangi_qator)
#
# print("Transponirlangan matritsa:")
# for qator in T:
#     print(qator)


#
#
# def determinant_gauss(mat):
#     n = len(mat)
#     A = [qator[:] for qator in mat]
#     det = 1
#     ishora = 1
#
#     for i in range(n):
#         if A[i][i] == 0:
#             topildi = False
#             for k in range(i + 1, n):
#                 if A[k][i] != 0:
#                     A[i], A[k] = A[k], A[i]
#                     ishora *= -1
#                     topildi = True
#                     break
#             if not topildi:
#                 return 0
#
#
#         for k in range(i + 1, n):
#             koeffitsient = A[k][i] / A[i][i]
#             for j in range(i, n):
#                 A[k][j] = A[k][j] - koeffitsient * A[i][j]
#
#     for i in range(n):
#         det *= A[i][i]
#     return det * ishora
#
# n = int(input("Matritsa o'lchamini kiriting: "))
# M = []
# for i in range(n):
#     M.append(list(map(float, input(f"{i+1}-qator: ").split())))
#
# natija = determinant_gauss(M)
# print(f"Determinant (diagonal ko'paytma) = {round(natija, 2)}")




# n = int(input("\nMatritsalar o'lchamini kiriting (n): "))
# A, B = [], []
#
# print("A matritsa elementlarini kiriting:")
# for i in range(n):
#     A.append(list(map(int, input().split())))
#
# print("B matritsa elementlarini kiriting:")
# for i in range(n):
#     B.append(list(map(int, input().split())))
#
# yigindi = []
# for i in range(n):
#     qator = []
#     for j in range(n):
#         qator.append(A[i][j] + B[i][j])
#     yigindi.append(qator)
#
# kopaytma = []
# for i in range(n):
#     qator = []
#     for j in range(n):
#         summa = 0
#         for k in range(n):
#             summa += A[i][k] * B[k][j]
#         qator.append(summa)
#     kopaytma.append(qator)
#
# print("A + B natijasi:", yigindi)
# for qator in yigindi:
#     print(*qator)
# print("A * B natijasi:", kopaytma)
# for qator in kopaytma:
#     print(*qator)
#

#
# print("\2x2 matritsaning teskarisini topish:")
# a11, a12 = map(int, input("1-qatorni kiriting: ").split())
# a21, a22 = map(int, input("2-qatorni kiriting: ").split())
# det = a11 * a22 - a12 * a21
# if det == 0:
#     print("Determinant 0, teskari matritsa yo'q.")
# else:
#     t11 = a22 / det
#     t12 = -a12 / det
#     t21 = -a21 / det
#     t22 = a11 / det
#
#     print(f"Teskari matritsa: \n[{t11}, {t12}]\n[{t21}, {t22}]")