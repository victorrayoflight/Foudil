n = int(input("Entrez un entier structement positif :"))
while n < 1:
    n = int(input("Entrez un entier STRUCTEMENT POSITIF, s.v.p. :"))

if n%2 == 0:
    print(n, "est pair !")
else:
    print(n, "est impair !")


