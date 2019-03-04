"""Exercice / Page 109
Menu

"""
import subprocess
import sys, os
os.system('clear')

def quitter():
    print("Vous avez choisi 0 pour quitter...")
    input("Appuyez sur une touche pour continuer...")
    exit()

def installer():
    print("Vous avez choisi d'installer HTTPD :")
    os.system('yum install httpd -y')




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

print("Choisissez un nombre de 1 a 4 (ou 0 (zero) pour terminer :")
print("**********************************************************")
print("1. Installer le service HTTPD")
print("2. Demarrer le service HTTPD")
print("3. Verifier son status et le port d'ecoute")
print("4. Tester une connection avec HTTPD")
print("0. Pour quitter")

choix = int(input("Veuillez entrer votre choix S.V.P. :"))



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
