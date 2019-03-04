"""Les dicts sont dans le meme dossier :
wordlist_1-4_0123456789.txt (1-4 characters, juste les chiffres 0-9) ;
wordlist_6_xyz123.txt (6 characters, lettre x, y, z et chiffres 1-3)

"""


"""Exercice / Page 107
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
