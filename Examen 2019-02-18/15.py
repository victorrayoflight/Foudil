phrase = input("Enter la phrase :")

position = 0
trouve = False
for c in phrase:
    position = position + 1
    if 'A' <= c <= 'Z':
        print("La premiere MAJ est :", c)
        print("La position de la MAJ est :", position)
        trouve = True
        break

if trouve == False:
    print("Il n'y a pas de MAJ")


Fo