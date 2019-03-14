#!/usr/bin/env python3

"""Exercice / Page 109
Menu

Cree par Victor Medvedev

"""

    # Import des modules"

import subprocess
import sys, os


    # Fonctions

def quitter():
    print("Vous avez choisi 0 pour quitter...")
    input("Appuyez sur Enter pour quitter...")
    exit()


def installer():
    print("**********************************")
    print("Vous avez choisi d'installer HTTPD")
    print("**********************************")
    code = os.system('sudo yum install httpd -y')
    if code != 0:
        print('Install failure')
        restart = input("Wanna restart Y/n ?")
        if (restart == 'Y'):
            redemarrer()
    input("Appuyez sur Enter pour continuer...")
    os.system('clear')


def configurer():
    print("*************************************************")
    print("Vous avez choisi de configurer HTTPD (httpd.conf)")
    print("*************************************************")
    print("Voulez vous faire un backup de fichier de configuration 'httpd.conf' ?")
    backup=input("'Y' pour 'Oui' ou n'importe quelle touche pour 'Non' : ")
    if backup.upper() in 'Y':
        os.system('sudo cp -i /etc/httpd/conf/httpd.conf /etc/httpd/conf/httpd.conf.bak')
        print("**************************************")
        print("Le fichier 'httpd.conf.bak' était créé")
        print("**************************************")
        input("Appuyez sur Enter pour continuer...")
    os.system('sudo nano /etc/httpd/conf/httpd.conf')
    os.system('clear')


def redemarrer():
    print("************************************")
    print("Vous avez choisi de redemarrer HTTPD")
    print("************************************")
    os.system('sudo systemctl restart httpd')
    input("Appuyez sur Enter pour continuer...")
    os.system('clear')


def demarrer():
    print("**********************************")
    print("Vous avez choisi de demarrer HTTPD")
    print("**********************************")
    os.system('sudo systemctl start httpd')
    input("Appuyez sur Enter pour continuer...")
    os.system('clear')


def status_service():
    print("***********************")
    print("Statut de service HTTPD")
    print("***********************")
    os.system('systemctl status httpd')
    input("Appuyez sur Enter pour continuer...")
    os.system('clear')


def status_port():
    print("***********************")
    print("Statut de port d'ecoute")
    print("***********************")
    os.system('netstat -na | grep :80')
    input("Appuyez sur Enter pour continuer...")
    os.system('clear')


def tester_connection():
    print("***************************************************")
    print("Vous avez choisi de tester la connection avec HTTPD")
    print("***************************************************")
    os.system('wget http://localhost')
    input("Appuyez sur Enter pour continuer...")
    os.system('clear')


def arreter():
    print("********************************")
    print("Vous avez choisi d'arreter HTTPD")
    print("********************************")
    os.system('sudo systemctl stop httpd')
    input("Appuyez sur Enter pour continuer...")
    os.system('clear')


def desinstaller():
    print("**************************************")
    print("Vous avez choisi de desinstaller HTTPD")
    print("**************************************")
    os.system('sudo yum remove httpd -y')
    input("Appuyez sur Enter pour continuer...")
    os.system('clear')


def choix():
    print("*********************************************************")
    print("Choisissez un nombre de 1 à 8 (ou 0 (zero) pour terminer)")
    print("*********************************************************")
    print("1. Installer le service HTTPD")
    print("2. Modifier fichier de configuration 'httpd.conf' (avec un backup)")
    print("3. Demarrer le service HTTPD")
    print("4. Verifier le status du service")
    print("5. Verifier le status du port d'ecoute")
    print("6. Tester la connection avec HTTPD")
    print("7. Arreter le service HTTPD")
    print("8. Desinstaller le service HTTPD")
    print("0. Quitter")

    choix = int(input("Veuillez entrer votre choix S.V.P. : "))

    return choix


    # Dictionnaire ou le script va chercher la fonction à executer après qu'user rentre son choix (0-8)

options = {
    0: quitter,
    1: installer,
    2: configurer,
    3: demarrer,
    4: status_service,
    5: status_port,
    6: tester_connection,
    7: arreter,
    8: desinstaller
}

os.system('clear')
user_choix = choix()

while user_choix != 0:
    os.system('clear')
    if user_choix in options.keys():
        options[user_choix]()

    else:
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print("Wrong choix. Essayez encore une fois.")
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print("")

    user_choix = choix()

"""Une boucle alternative

"""
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
