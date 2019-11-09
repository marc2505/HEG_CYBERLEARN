""" algo: compteur
données: valeur initial
résultat: affiche compteur
"""

### décl. et init. des variables
compteur: int = 1

### séquence d'opérations
while compteur <= 10:
    print("compteur:", compteur)
    compteur = compteur + 1
