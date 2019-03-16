#!/usr/bin/env python3

chaine = input("Veuillez entrer la chaine : ")
car = input("Veuillez entrer le caractere recherche : ")


if car.upper() in chaine.upper():
    print("Le caractere recherche dans la chaine est : ", car)
    print("Il est present dans la chaine : ", chaine)

