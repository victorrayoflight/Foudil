#!/usr/bin/env python3.6

"""Cahier d'exercices en Python / 2019-01-28"""

"""Exercice 1 / Page 1"""
"""La note entre 0 et 100"""
moyenne = 80
note = int(input("Entrez votre note :"))
if note >= 0 and note <= 100:
    if note < moyenne:
        print("C'est en dessous de la moyenne.")
        if note == 0:
            print("Lamentable !")
    elif note > moyenne:
        print("Plus que la moyenne.")
        if note == 100:
            print("C'est meme excellent !")
    else:
        print("C'est la moyenne.")
else:
    print("Note invalide !")
    print("Fin du programme.")



"""Quiz 1 / Page 1"""
a = 7
b = 12
if a > 5:
    b = b - 4
if b > 10:
    b = b + 1
print(b)

a = 3
b = 6
if a > 5 or b != 3:
    b = 4
else:
    b = 2
print(b)

a = 2
b = 5
if a > 8:
    b = 10
elif a > 6:
    b = 3
print(b)

a = 2
b = 0
if a < 0:
    b = 1
elif a > 0 and a < 5:
    b = 2
else:
    b = 3
print(b)

a = 10
if a < 5:
    a=20
elif a < 100:
    a = 500
elif a < 1000:
    a = 1
else: a = 0
print(a)



"""Exercice 1 / Page 3
Affiche la table de multiplication d'un nombre donne par l'utilisateur
Version 1

"""
nombre = input("SVP entrez le nombre : ")
if nombre.isdigit():
    for chiffre in range (1, 10):
        print(chiffre, "*", nombre, "=", chiffre*int(nombre))
else:
    print("Ce n'est pas un nombre.")



"""Exercice 1 / Page 3
Affiche la table de multiplication d'un nombre donne par l'utilisateur
Version 2

"""
print(("La table de multiplication de 1 a 9").upper())
for block_number in range(1, 10):
    print("---------------------")
    print("Multiplication de :", block_number)
    for number in range(1, 10):
        print(number, '*', block_number, '=', number * block_number)
print("---------------------")



"""Quiz 2 / Page 3"""
n = 0
while n < 15:
    n = n + 2
print(n)

n = 10
while n >= 11:
    n = n + 2
print(n)

n = 0
for i in range(5):
    n = n + 1
print(n)

n = 0
for i in range(5):
    n = n + 1
print(i)

resultat = ""
for c in "Bonsoir":
    resultat = resultat + c
print(resultat)

"""The same."""
resultat = ""
for letter in "Bonsoir":
    resultat = resultat + letter
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



'''Exercice 2 / Page 6'''
'''Codage et decodage de texte avec le "Chiffre de Cesar"'''
alphabet = ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
            "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
            "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
            "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z")
alphabet_count = len(alphabet)

string_input = input("Enter your phrase:")
string_output = ""

for letter in string_input:
    if letter == " ":
        string_output += " "
        continue
    index = alphabet.index(letter)
    index_output = index + 26
    if index_output >= alphabet_count:
        index_output -= alphabet_count
    string_output += alphabet[index_output]
print(string_output)



"""Exercice 4 / Page 8"""
"""Creation des noms avec un suffixe fixe"""
prefixes = "JKLMNOP"
suffixe = "ack"
for letter in prefixes:
    print(letter + suffixe)



"""Exercice 5 / Page 8"""
"""Split the phrase letters in two lines 
(using odd and even letter position 

"""
def exercice_5():
    phrase = input("Enter your phrase:").upper()
    line1 = ""
    line2 = ""
    for index in range(len(phrase)):
        if index % 2 == 0:
            line1 += phrase[index]
        else:
            line2 += phrase[index]
    print(line1)
    print(line2)

exercice_5()


"""Exercice 7 / Page 9"""
"""Vérification de MDP"""
import uuid
import hashlib
import getpass

def hash_password(password):
    # uuid is used to generate a random number
    salt = uuid.uuid4().hex
    hash = hashlib.sha256(salt.encode() + password.encode()).hexdigest() + ':' + salt

    return hash

def check_password(hashed_valid_password, verifying_user_password):
    hashed_password, salt = hashed_valid_password.split(':')
    verifying_user_hashed_password = hashlib.sha256(salt.encode() + verifying_user_password.encode()).hexdigest()

    return hashed_password == verifying_user_hashed_password

PASSWORD = 'azerty'
hash = hash_password(PASSWORD)

def verify_password(password_input):
    if not check_password(hash, password_input):
        print('Error: I am sorry but the password does not match. Try again.')
    else:
        print('Succès: Mot de passe accepté')

def ask_user_input_v1():
    return input('Please enter a password: ')

def ask_get_pass_2():
    print('Welcome ' + getpass.getuser())
    return getpass.getpass(prompt='Please enter a password: ')

password_input = ask_user_input_v1()
verify_password(password_input)




