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

""" algo: triangle
donées: n: int -> hauteur du triangle
résultat: affiche un triangle de hauter n à l'écran
"""

### déclaration et initialisation des variables
n: int = None

### séquence d'opérations

# saisir la hauter du triangle
n = int(input("Hauter du triangle ? (>= 2) "))

# afficher le triangle
for i in range(1, n+1):			# traite les lignes
    print("*" * i)