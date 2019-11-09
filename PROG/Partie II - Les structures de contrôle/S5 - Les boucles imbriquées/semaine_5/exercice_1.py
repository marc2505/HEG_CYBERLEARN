"""
Créez un algorithme pour afficher un triangle à l'écran comme indiqué ci-dessous.
La hauteur du triangle est donnée par l'utilisateur.

*
**
***
****
*****
******
*******
********
*********
**********
"""
"""algo: triangle
données: n -> hauter du triangle
résultat: affichage d'un triangle
"""

### déclaration et initialisation des variables
n: int = 0 # hauter du triangle

### séquence d'opérations

# saisir la hauter du triangle
while n is None or n < 2:
    n = int(input("quel hauter? (n >=2) "))

# afficher le triangle
for i in range(1, n+1):         # traiter les lignes
    for j in range(1, i+1):     # traiter les colonnes
        print("*", end="")
    print()






