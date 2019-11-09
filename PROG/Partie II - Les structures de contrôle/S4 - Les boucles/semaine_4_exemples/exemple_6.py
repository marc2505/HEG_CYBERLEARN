""" algo: boucle_x
données: i: int
résultat: la valeur x
"""

### décl. et init. des variables
x: int = 0
n: int = 5

### séquence d'opérations
for i in range(1, n + 1):
    x = x + i

print("resultat:", x)
