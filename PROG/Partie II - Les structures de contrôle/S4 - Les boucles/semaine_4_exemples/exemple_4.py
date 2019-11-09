""" algo: boucle_x
données: i: int
résultat: la valeur x
"""

### décl. et init. des variables
x: int = 1
i: int = 5

### séquence d'opérations
while i > 0:
  x = x * i
  i = i - 1

print("resultat:", x)