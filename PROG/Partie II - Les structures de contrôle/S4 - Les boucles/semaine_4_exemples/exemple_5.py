""" algo: factorielle
données: n: int
résultat: la valeur de la factorielle
"""

### décl. et init. des variables
resultat: int = 1
n: int = None

### séquence d'opérations
n = int(input("Quel factoriel ?"))

for i in range(1, n + 1):
    resultat = resultat * i

print("resultat:", resultat)
