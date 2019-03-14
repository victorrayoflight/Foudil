#!/usr/bin/env python3

""" Exercice / Page 107 2019-02-15
    Creation du hach d'un MDP

    Cree par Victor Medvedev
    Documentation : Digest access authentication
    https://en.wikipedia.org/wiki/Digest_access_authentication

"""

import hashlib
from itertools import product

""" Takes HTTP method and Authorization header from .pcap file.

    Authorization: Digest username="webadmin", realm="Pentester-Academy",
    nonce="X95LDujmBAA=9c8ec8a0aeee0ddf7f24a5a75c57d0f90245d0f5", uri="/", algorithm=MD5,
    response="0fd7c603fdf61e89bfc9c95fb73e343a", qop=auth, nc=00000001, cnonce="89b024ea3adb54ec"
    
    # HA1 = MD5(username:realm:password)
    # HA2 = MD5(method:digestURI)
    # response = MD5(HA1:nonce:nonceCount:cnonce:qop:HA2)

"""

method='GET'
digestURI='/'

username='webadmin'
realm='Pentester-Academy'
nonce='X95LDujmBAA=9c8ec8a0aeee0ddf7f24a5a75c57d0f90245d0f5'
qop='auth'
nonce_count='00000001'
cnonce='89b024ea3adb54ec'

response = '0fd7c603fdf61e89bfc9c95fb73e343a'

    # Calculer MD5 pour un string

def md5(value):
    return hashlib.md5(value.encode('utf-8')).hexdigest()

    # Formation d'un string pour l'utiliser dans md5()

def calc_ha1(username, realm, password):
    args=[username, realm, password]
    str=':'.join(args)
    hash=md5(str)

    return hash

    # Formation d'un string l'utiliser dans md5()

def calc_ha2(method, digestURI):
    return md5(':'.join([method, digestURI]))

    # Formation d'un string l'utiliser dans md5()

def calc_response(ha1, nonce, nonce_count, cnonce, qop, ha2):
    return md5(':'.join([ha1, nonce, nonce_count, cnonce, qop, ha2]))



def find_password():
    ha2 = calc_ha2(method, digestURI)

    password_chars=['x','y','z','1','2','3']
    password_length=6

    """ Pour ne pas utiliser un dictionnaire car on a pas beaucoup de caractères et
        la longueur de MDP n'est pas longe,
        on utilise la fonction 'product' qui génère les strings en toutes les combinaisons possibles
        
    """

    for subset in product(password_chars, repeat = password_length):
        password=''.join(subset)
        ha1 = calc_ha1(username, realm, password)

        if (calc_response(ha1, nonce, nonce_count, cnonce, qop, ha2) == response):
            print("Found password for username", "'", username, "' :", "'", password, "'")
            break

find_password()
