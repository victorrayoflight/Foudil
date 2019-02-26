#!/usr/bin/env python3.6

if 'c' in "Victor":
    print('Letter "c" exist in word "Victor"')

fic = open('Names.txt', 'r') # open a file for reading
content = fic.read()
print(content)

def affiche():
    print("Salut")
affiche()

print("Bonjour " * 4)

"""Shows type of variable and its conversion."""
age = input("SVP entrer votre age : ")
print(type(age))
age = int(age)
print(age + 5)

n = 0
while n < 5:
    print("Victor")
    n=n+1

n = 0
while n < 5:
    print("Victor", end=" ")
    n = n + 1

print('My name is {} and family name is {}'.format('Victor', 'Medvedev'))
print('My name is {1} and family name is {0}'.format('Medvedev', 'Victor'))

# page 25
"""Print IP address using . separator"""
print (192, 168, 20, 3,sep=".")

# page 25
print("Mon nom est {}, et ma taille est {}".format('Halitim', '1.82 m'))

# page 26
for i in range(1, 11):
    print("{:2d} {:3d} {:4d}".format(i, i*i, i*i*i))
for i in range(1, 11):
    print(i, i*i, i*i*i)

# page 26
from math import pi
rayon = float(input('Rayon dy cone (m) :'))
hauteur = float(input('Hauteur du cone (m) :'))
volume = (pi*rayon*rayon*hauteur)/3.0
print("Volume du cone = {:.2f}".format(volume), "m3")

# page 32
"""User enters the price, program counts price+taxes."""
prix = float(input('Entrez le prix :'))
prixPlusTaxes = prix * 1.15
print('Prix avec les taxes est {:.2f}'.format(prixPlusTaxes))

# page 84 CoursPython_new
"""Number of vowels in the phrase."""
"""Nombre de voyelles dans une phrase."""
def nb_voyelles(a):
    count = 0
    phrase_len = len(a)
    phrase_len = phrase_len - 1
    while phrase_len >= 0:
        if a[phrase_len] in ('aeiou'):
            count += 1
        phrase_len -= 1
    return count
a=input("Entrer le mot ou la chaine : ")
print("Le nombre de voyelles est", nb_voyelles(a))

"""Number of words in the phrase."""
"""Nombre de mots dans une phrase."""
machine = input("Entrez la phrase : ")
if len(machine) == 0:
    print("0 mots")
nm = 1
for c in machine:
    if c == " ":
        nm = nm +1
print("Votre phrase contient", nm, 'mot(s)')

"""Prints pyramide of letters using entered word, "while" variant."""
ma_chaine = "VIK"
count = 0
while count < len(ma_chaine):
    count = count + 1
    print (ma_chaine[0:count])
while count > 1:
    count = count - 1
    print (ma_chaine[0:count])

"""Prints pyramide of letters using entered word, "for" variant."""
ma_chaine = "PYTHON"
count = 0
for letter in ma_chaine:
    count = count + 1
    print (ma_chaine[0:count])
for letter in ma_chaine:
    count = count - 1
    print (ma_chaine[0:count])

"""Prints matrix of * using user's number of repeats."""
"""Find errors!"""
nb = int(input("Entrez un nombre : "))
star = ""
columns = 0
rows = 0
while rows < nb:
    while columns < nb:
        star += "*"
        columns += 1
    print(star)
    rows += 1
print(star)

"""Prints user's number of *."""
nb = int(input("Entrez un nombre : "))
star = ""
count = 0
while count < nb:
    star += "*"
    count += 1
print(star)

# page 43
"""Enter the coordinats x and y and find what is the quarter."""
"""Entrer les coordonnees d'un point et afficher dans quel cadran elles se trouvent."""
x = int(input("Entrez x : "))
y = int(input("Entrez y : "))
if x > 0:
    if y > 0:
        print("Q1")
    else:
        print("Q4")
else:
    if y > 0:
        print("Q2")
    else:
        print("Q3")



"""Exercice / Page 102 2019-02-15
Affiche si les objets sont des dossiers ou des fichiers

"""
import os.path
import sys
DOSSIER_SOURCE = "/home/vik"
dirs = os.listdir(DOSSIER_SOURCE)
for file in dirs:
    complet = DOSSIER_SOURCE + os.sep + file
    if os.path.isdir(complet):
        print("Dossier :", file)
    if os.path.isfile(complet):
        print("Fichier :", file)



"""Exercice sys.ergv / Page 104 2019-02-15"""
import os, sys

path = '.'
program_name = sys.argv[0]
print(program_name)

# option = sys.argv[1]
# print(option)

if len(sys.argv) == 2:
    path = sys.argv[1]

files = os.listdir(path)
for name in files:
    print(name)



"""Exercice / Page 150 2019-02-15
Verifie si un fichier existe

"""
import sys
import os
if os.path.exists("/home/vik"):
    print("Le fishier/dossier existe")
else:
    print("Absent")



"""Exercice preparatoire au prochain
Creation du hach d'un MDP

"""
import hashlib
user_password = input("Enter your pwd:")
user_hash = hashlib.md5(user_password.encode('utf-8')).hexdigest()
print("Your hash is", user_hash)


"""Exercice / Page 107 2019-02-15
hachlib

"""
import hashlib
import time
counter = 1

md5_hash = input("Entrer le hash du MDP :")
md5_dict = input("Entrer le chemin du dictionnaire :")

try:
    md5_dict = open(md5_dict, 'r')
except:
    print("\n Fichier introuvable")
    quit()

for password in md5_dict:
    # str = password.strip().encode('utf-8')
    # md5_hash = hashlib.md5(str)
    # hash = md5_hash.hexdigest()

    hash_obj = hashlib.md5(password.strip().encode('utf-8')).hexdigest()
    start = time.time()
    print("Trying password %d -----> %s" % (counter, password.strip()))
    counter += 1
    end = time.time()
    t_time = end - start

    if hash_obj == md5_hash:
        print("Password found! Password is %s" % password)
        print("Total running time is %d sec." % t_time)
        time.sleep(10)
        break
    else:
        print("Password not found.")


"""Exercice / Page 109
Menu

"""
import subprocess
import sys, os
os.system('clear')

print("Choisissez un nombre de 1 a 4 (ou 0 (zero) pour terminer :")
print("**********************************************************")
print("1. Installer le service HTTPD")
print("2. Demarrer le service HTTPD")
print("3. Verifier son status et le port d'ecoute")
print("4. Tester une connection avec HTTPD")
print("0. Pour quitter")

choix = int(input("Veuillez entrer votre choix S.V.P. :"))

while a != 0:
    if choix == 1:
        print("Vous avez choisi d'installer HTTPD :")
        os.system('yum install httpd -y')
        os.system('python menuaffichage.py')
    elif choix == 2:
        print("Vous avez choisi de demarrer HTTPD: ")
        os.system('systemctl stop httpd')
        os.system('systemctl start httpd')
        input("Appuyez sur une touche pour continuer...")
        os.system('python menuaffichage.py')
    elif choix == 3:
        print("Vous avez choisi de verifier le status et le port d'ecoute :")
        input("Verifions son status... Appuyez sur une touche...")
        os.system('systemctl status httpd')
        print("Verifions port d'ecoute...")
        os.system('netstat - na | grep :80')
        input("Appuyez sur une touche pour continuer...")
        os.system('python menuaffichage.py')
    elif choix == 4:
        print("Vous allez tester la connection avec HTTPD :")
        os.system('wget http://www.bdeb.qc.ca')
        input("Appuyez sur une touche pour continuer...")
        os.system('python menuaffichage.py')
    else:
        print("Vous avez choisi 0 pour quitter :")
        input("Appuyez sur une touche pour continuer...")
    exit()
print("Vous avez entre zero :")
print("L'exercice est termine.")
