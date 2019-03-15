#!/usr/bin/env python3

list1 = []

num = int(input("Enter number of elements in list: "))

for i in range(1, num + 1):
    ele = int(input("Enter elements :"))
    list1.append(ele)

print("La moyenne est :", max(list1))
