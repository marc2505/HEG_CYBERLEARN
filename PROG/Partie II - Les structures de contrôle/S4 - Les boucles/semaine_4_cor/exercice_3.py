"""
En mathématiques, la suite de Fibonacci est une suite d'entiers dans laquelle
chaque terme est la somme des deux termes qui le précèdent.

Elle commence par les termes 0 et 1 ; ses premiers termes sont : 0, 1, 1, 2, 3, 5, 8, 13, 21, etc.

Exemple:
fibonacci de 2 -> 1 + 0
fibonacci de 3 -> 1 + 1
fibonacci de 4 -> 2 + 1
fibonacci de 5 -> 3 + 2
fibonacci de 6 -> 5 + 3

Écrire un algorithme pour calculer le Fibonacci d'un nombre n donner par l'utilisateur
"""

""" algo: fibonacci
données: n: int
résultat: le Fibonacci de n
"""
### déclaration et initialisation
### des variables
fib_n_1: int = 1
fib_n_2: int = 0

n: int = None
res: int = 0
### séquence d'opérations

# saisie la valeur
while n is None or n < 0:
    n = int(input("Fibonacci de ? (n >=0) "))

# calcule le valeur de nombre de Fibonacci
if n == 0:
    res = 0
elif n == 1:
    res = 1
else:
    for i in range(2, n+1):
        res = fib_n_1 + fib_n_2
        fib_n_2 = fib_n_1
        fib_n_1 = res

print("Fibonacci de %d: %d" % (n, res))
