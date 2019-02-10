#!/usr/bin/env python3.7

# L = [6, 12, 10, 6]
# print("La liste avant permutation : ", L)
# l = len(L)
# aux = L[0]
# L[0] = L[l-1]
# L[l+1] = aux
# print("-----------------")
# print("La liste apres permutation :", L)

# L = [8, 24, 48, 2, 16]
# long = len(L)
# for i in range (long):
#     print("Element", i, ":", L[i])

# -----------------------------------------------------------------
nb = int(input("Entrez le nombre d'entiers : "))
L = []
for i in range (nb):
    element = int(input("Entrez le premier element : "))
    L.append(element)
print(L)
long = len(L)
print(long)
# somp = 0
# for i in range(long):
#     if L[i] %3 == 0:
#         mult
# не окончено

max = L[0]
min = L[0]
for i in range (long):
    if L[i] > max:
        max = L[i]
    elif:
        L[i] < min:
        min



#!/usr/bin/env python3.7

# L = [6, 12, 10, 6]
# print("La liste avant permutation : ", L)
# l = len(L)
# aux = L[0]
# L[0] = L[l-1]
# L[l+1] = aux
# print("-----------------")
# print("La liste apres permutation :", L)

# L = [8, 24, 48, 2, 16]
# long = len(L)
# for i in range (long):
#     print("Element", i, ":", L[i])

# -----------------------------------------------------------------
nb = int(input("Entrez le nombre d'entiers : "))
L = []
for i in range (nb):
    element = int(input("Entrez le premier element : "))
    L.append(element)
print(L)
long = len(L)
print(long)
# somp = 0
# for i in range(long):
#     if L[i] %3 == 0:
#         mult
# не окончено

max = L[0]
min = L[0]
for i in range (long):
    if L[i] > max:
        max = L[i]
    elif:
        L[i] < min:
        min


def carre(n):
    return (n * n)

def premiers_carres(k):
    for i in range(k):
        print(carre(i))

a = int(input("Enter le nombre : "))
premiers_carres(a)
