""" algo: carre
donées: n: int -> côté du carré
résultat: affiche un carré de taille n x n à l'écran
"""

### déclaration et initialisation
### des variables
n: int = None

# saisie la valeur
n = int(input("Côté du carré ?"))

### séquence d'opérations
i: int = 1
while i <= n:  # traite les lignes
    j: int = 1
    while j <= n:  # traite les colonnes
        print("*", end="")
        j += 1
    print()
    i += 1
