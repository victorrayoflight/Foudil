#!/usr/bin/env python3

import os

print("Le nom d'hote est : ")
os.system('hostname')
print("")
input("Appuyez sur Enter pour continuer...")

print("")
print("L'adresse IP d'hote est : ")
os.system('ifconfig ens33 | grep broadcast')

print("")
input("Appuyez sur Enter pour quitter...")
