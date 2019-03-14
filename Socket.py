import socket
import sys, os
from datetime import datetime

print("")
remote_server = input("Entrez le nom d'hôte ou l'adresse IP à scanner :")
"""On peut utiliser le fichier hosts pour la résolution des noms"""
# remote_server_ip = socket.gethostbyname(remote_server)

print("")
print("Scan en cours", remote_server, "...")
print("")

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

time_start = datetime.now()

for port_number in range (101, 1001): # max 65535
    result = sock.connect_ex((remote_server, port_number))
    if result == 0:
        print("Port", port_number, ": Open")
    else:
        print("Port", port_number, ": Closed")
    result += 1

time_end = datetime.now()
time_scan = time_end - time_start
print("")
print("Le temps utilisé pour effectuer le scan :", time_scan)
