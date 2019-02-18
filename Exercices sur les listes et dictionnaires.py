#!/usr/bin/env python3.6

"""Exercice sur les listes"""
"""Ajouter la valeur 1 à chacun de ses éléments"""
print("-----------------------------")
liste = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print("La liste avant", liste)
print("On ajoute 1 à chacun des éléments...")
longueur = len(liste)

for element in range(longueur):
    liste[element] += 1

print("La liste après", liste)


"""Ajouter la valeur 11 à la fin de la liste"""
print("-----------------------------")
print("La liste avant", liste)
print("On ajoute 11 à la fin...")
liste.append(11)
print("La liste après", liste)


"""Ajouter les valeurs 12 et 13 à la fin de la liste"""
print("-----------------------------")
print("La liste avant", liste)
print("On ajoute 12 et 13 à la fin...")
liste.extend([12, 13])
print("La liste après", liste)


"""Afficher le premier el., les deux prem., le dernier, led deux dern."""
print("-----------------------------")
print("La liste", liste)
print("On affiche le premier el., les deux prem., le dernier, led deux dern. ...")
print(liste[0], ",", liste[0:2], ",", liste[-1], ",", liste[-2:])


"""Construire la liste 'paires' et la liste 'impaires'"""
print("-----------------------------")
# liste = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
print("La liste", liste)
print('On cree deux listes "paires" et "impaires"...')
paires = []
impaires = []
for element in range(len(liste)):
    if element % 2 != 0:
        paires.append(liste[element])
    else:
        impaires.append(liste[element])
print("Paires", paires)
print("Impaires", impaires)


"""Insérer 3.5 entre 3 et 4, var1"""
print("-----------------------------")
print("La liste avant", liste)
print("On ajoute 3.5 entre 3 et 4...")

for element in range(len(liste)):
    if liste[element] == 3:
        found_position = element
        break

liste.insert(found_position + 1, 3.5)
print("La liste après", liste)


# """Insérer 3.5 entre 3 et 4, var2"""
# print("-----------------------------")
# print("La liste avant", liste)
# print("On ajoute 3.5 entre 3 et 4...")
#
# if 3 in liste:
#     found_position = liste.index(3)
#
# liste.insert(found_position + 1, 3.5)
# print("La liste après", liste)


"""Supprimer la valeur 3.5"""
print("-----------------------------")
print("La liste avant", liste)
print("On supprime 3.5...")

liste.remove(3.5)
print("La liste après", liste)


"""Inverser l'ordre des el."""
print("-----------------------------")
print("La liste avant", liste)
print("On inverse l'ordre des éléments...")

liste.reverse()
print("La liste après", liste)



"""Demander à utilisateur de fournir un nombre au hasard et dire si ce nombre est present"""
print("-----------------------------")
user_input = int(input("Entrez un nombre :"))
if user_input in liste:
    print("Le nombre existe dans la liste")
else:
    print("Le nombre n'existe pas dans la liste")

