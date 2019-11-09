"""algo: factorielle_5
données: n -> int
résultat: factorielle de n -> int
"""
### decl. et init. des variables
n: int = 5
resultat: int = 1
### séquence d'opérations
for i in range(1, n + 1):
    resultat = i * resultat

print("resultat =", resultat)
