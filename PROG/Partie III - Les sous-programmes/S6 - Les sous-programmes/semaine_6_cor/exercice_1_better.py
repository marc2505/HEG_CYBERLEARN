"""
Créer un algorithme pour tester si une chaîne de caractére contient un caractère

Toujours utiliser uniquement les structures et les méthodes vues dans le cours.

Exemple:
chaîne: "algo I", caractère: "a", réponse: True
chaîne: "algo I", caractère: "i", réponse: True
chaîne: "algo I", caractère: "u", réponse: False
"""

""" algo: recherche_caractere
données: chaine: str, x: str
résultat: True si x est dans chaine
"""
### déclaration et initialisation des variables
chaine: str = None
x: str = None

trouve: bool = False

### séquence d'opérations

# saisir les valeurs
while chaine is None or len(chaine) <= 0:
    chaine = input("Entrez avec une chaîne de caratère : (pas vide '') ")

while x is None or len(x) == 0:
    x = input("Entrez avec un caratère ")

# rechercher pour le caractère dans la chaîne
i: int = 0
while not trouve and i < len(chaine):
    if chaine[i] == x:
        trouve = True
    i += 1

# afficher le résultat
print("chaîne: %s, caractère: %s, réponse: %r" %(chaine, x, trouve))
