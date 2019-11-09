"""
Modifier l'algorithme ci-dessous pour qu'il utilise une fonction somme_n pour calculer la somme de n premiers entiers
    a. l'exécuter pas à pas en utilisant le mode débogage
    b. vérifier quelles variables sont valides dans le programme principal et dans la fonction somme_n
    c. modifier les noms des variables pour voir ce qui se passe
"""
"""algo: somme_n
données: n -> int
résultat: somme de n premiers entiers
"""

# données
n: int = 5
resultat: int = 0

# calcule la somme de n 
for i in range(1, n + 1):
    resultat = resultat + i

# affiche le résultat
print("La somme de %d premiers enties est %d" % (n, resultat))
