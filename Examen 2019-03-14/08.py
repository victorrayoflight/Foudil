#!/usr/bin/env python3

t1 = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
t2 = ['Janvier', 'Fevrier', 'Mars', 'Avril', 'Mai', 'Juin', 'Juillet', 'Aout', 'Septembre', 'Octobre', 'Novembre', 'Decembre']

t12 = []

for i in range(len(t1)):
  t12.append(t2[i])
  t12.append(t1[i])

print(t12)
