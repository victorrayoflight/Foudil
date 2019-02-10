#!/usr/bin/env python3.6

"""Cahier d'exercices en Python / 2019-01-28"""

"""Quiz 1 / Page 1"""
a=7
b=12
if a>5:
    b=b-4
if b>10:
    b=b+1
print(b)

a=3
b=6
if a>5 or b!=3:
    b=4
else:
    b=2
print(b)

a=2
b=5
if a>8:
    b=10
elif a>6:
    b=3
print(b)

a=2
b=0
if a<0:
    b=1
elif a>0 and a<5:
    b=2
else:
    b=3
print(b)

a=10
if a<5: a=20
elif a<100: a=500
elif a<1000: a=1
else: a=0
print(a)

"""Exercice 1 / Page 3"""
"""Affiche la table de multiplication d'un nombre donne par l'utilisateur"""
nombre = input("SVP entrez le nombre : ")
if nombre.isdigit():
    for chiffre in range (1, 10):
        print(chiffre, "*", nombre, "=", chiffre*int(nombre))
else:
    print("Ce n'est pas un nombre.")

"""Quiz 2 / Page 3"""
n=0
while n<15: n=n+2
print(n)

n=10
while n>=11: n=n+2
print(n)

n=0
for i in range(5): n=n+1
print(n)

n=0
for i in range(5): n=n+1
print(i)

resultat=""
for c in "Bonsoir": resultat=resultat+c
print(resultat)

"""Exercice 3 / Page 7"""
"""Verifie si une chaine donne par l'utilisateur est une chaine ADN"""
DNAString = input("Entrez une chaine de caracteres : ")
DNAString = DNAString.upper()
if all(letters in 'ACGT' for letters in DNAString):
    print("Correct,", DNAString, "c'est un brin ADN.")
    print()
else:
    print("Incorrect,", DNAString, "ce n'est pas un brin ADN.")
    print()
