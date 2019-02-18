"""Exercice 1 / Page 1
Создание списка, показ элемента 4, заменить эл. 1 на 17 и эл. 3 суммой соседей (2 и 4), вывести 12 раз посл. эл.

"""
list = [8, 5, 6, 1, 17]
print(list[4])
list[1] = 17
list[3] = list[2] + list[4]
print(list)
for element in range (0, 12):
    print(list[len(list)-1])


"""Exercice 2 / Page 2
Обмен значениями между первым и последним элементом списка

"""
"""v1"""
list = [6, 12, 18, 5]
print("La liste avant permutation: ", list)
long = len(list)
aux = list[0]
list[0] = list[long-1]
list[long-1] = aux
print("La liste apres permutation: ", list)

"""v2"""
list = [6, 12, 18, 5]
print("La liste avant permutation: ", list)
# long = len(list)
aux = list[0]
list[0] = list[-1]
list[-1] = aux
print("La liste apres permutation: ", list)


"""Exercice 3 / Page 2
Манипуляции со списком

"""
# affiche en colonne
list = [8, 24, 48, 2, 16]
long = len(list)
for element in range (long):
    print("Element", element, ":", list[element])

# compte le nombre de multiples de 3 presents dans la liste
nb_entiers = int(input("Entrez le nombre d'entiers : "))
list = []
for number in range(nb_entiers):
    element = int(input("Entrez un element :"))
    list.append(element)
long = len(list)
print("Votre liste", list, "contient", long, "element(s)")

mult3 = int()
for element in range (long):
    if list[element] % 3 == 0:
        mult3 += 1

print("Nombre de multiples de 3 :", mult3)


"""Exercice 3 / Page 2
The same like previous but using functions

"""
def formation_d_une_liste():
    nb_entiers = int(input("Entrez le nombre d'entiers : "))

    if (nb_entiers == 0):
        return []

    number_list = []

    for number in range(nb_entiers):
        element = int(input("Entrez un element :"))
        number_list.append(element)
    long = len(number_list)
    print("Votre liste", number_list, "contient", long, "element(s)")

    return number_list

def exerсiсe_3_2():
    number_list = formation_d_une_liste()
    long = len(number_list)

    mult3 = int()
    for element in range (long):
        if number_list[element] % 3 == 0:
            mult3 += 1

    print("Nombre de multiples de 3 :", mult3)

exerсiсe_3_2()

