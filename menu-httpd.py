#!/usr/bin/env python3.6

"""Exercice / Page 109
Menu

"""
import subprocess
import sys, os
os.system('clear')

def quitter():
    print("Vous avez choisi 0 pour quitter...")
    input("Appuyez sur Enter pour quitter...")
    exit()

def installer():
    print("Vous avez choisi d'installer HTTPD :")
    code = os.system('sudo yum install httpd -y')
    if code != 0:
        print('Install failure')
        restart = input("Wanna restart Y/n ?")
        if (restart == 'Y'):
            demarrer()

def demarrer():
    os.system('systemctl restart httpd')

def status_service():
    os.system('systemctl status httpd')

def status_port():
    os.system('netstat - na | grep :80')

def tester_connection():
    os.system('wget http://localhost')

def arreter():
    os.system('systemctl stop httpd')

def desinstaller():
    os.system('sudo yum remove httpd -y')

def choix():
    print("Choisissez un nombre de 1 a 7 (ou 0 (zero) pour terminer) :")
    print("**********************************************************")
    print("1. Installer le service HTTPD")
    print("2. Demarrer le service HTTPD")
    print("3. Verifier le status du service")
    print("4. Verifier le status du port d'ecoute")
    print("5. Tester la connection avec HTTPD")
    print("6. Arreter le service HTTPD")
    print("7. Desinstaller le service HTTPD")
    print("0. Quitter")

    choix = int(input("Veuillez entrer votre choix S.V.P. :"))

    return choix

options = {
    0 : quitter,
    1 : installer,
    2 : demarrer,
    3 : status_service,
    4 : status_port,
    5 : tester_connection,
    6 : arreter,
    7 : desinstaller
}

# while True:
#     user_choix = choix()
#
#     if user_choix in options.keys():
#         options[user_choix]()
#
#         if user_choix == 0:
#             break
#     else:
#         print("Wrong choix. Essayez encore une fois :")

user_choix = choix()

while user_choix != 0:

    if user_choix in options.keys():
        options[user_choix]()

    else:
        print("Wrong choix. Essayez encore une fois :")

    user_choix = choix()

#