user_list = []

number_of_elements = int(input("Entrez le nombre d'entiers : "))

for count in range(number_of_elements):
    try:
        element = int(input("Entrez un element :"))
    except ValueError:
        print("Ce n'est pas un nombre entier. Essayez encore.")
        continue
    user_list.append(element)

print("La liste creé :", user_list)











user_list = []

number_of_elements = int(input("Entrez le nombre d'entiers : "))

for count in range(number_of_elements):
    element = input("Entrez un element :")
    element_type = type(element)
    if element_type != 'int':
        continue
    if_int = element.isdigit
    except ValueError:
        print("Ce n'est pas un nombre entier. Essayez encore.")
        continue
    user_list.append(element)

print("La liste creé :", user_list)