# import random
# sonlar=[1,1,2,2,3,3,4,4,5,5]
# # for i in range(10):
# #     sonlar.append(random.randint(1,10))
# # print(sonlar)
#
# def orta_qiymat(sonlar):
#     return sum(sonlar)/len(sonlar)
#
# def mediana(sonlar):
#     sonlar.sort()
#     print(sonlar)
#     if len(sonlar)%2==0:
#         return (sonlar[len(sonlar)//2]+sonlar[len(sonlar)//2-1])/2
#     else:
#         return sonlar[len(sonlar)//2]
# def moda(sonlar):
#     k=0
#     g=[]
#     p=set(sorted(sonlar))
#     for i in p:
#
#         j=sonlar.count(i)
#         if j>=k:
#             k=j
#         g.append(j)
#     if len(set(g))==1:
#         return "modasi yuq!"
#     o=[]
#     for i in p:
#         if sonlar.count(i)==k:
#             o.append(i)
#     return o
#
#
# def dispirsiya(sonlar):
#     ortacha=sum(sonlar)/len(sonlar)
#     k=0
#     for i in sonlar:
#         k+=(i-ortacha)**2
#     return k/len(sonlar)
#
# print(orta_qiymat(sonlar))
# print(mediana(sonlar))
# print(moda(sonlar))
# print(dispirsiya(sonlar))


# import matplotlib.pyplot as plt
#
# x = [1, 3, 5, 8]
# y = [2, 4, 3, 9]
#
# data = []
# for i in range(len(x)):
#     data += [x[i]] * y[i]
#
# plt.hist(data, bins=12, edgecolor='red')
# plt.title("Gistogramma")
# plt.xlabel("Interval")
# plt.ylabel("Chastota")
# plt.show()
#
# plt.plot(x, y, marker='o')
# plt.title("Chastotalar poligoni")
# plt.xlabel("Interval markazi")
# plt.ylabel("Chastota")
# plt.grid(True)
# plt.show()
