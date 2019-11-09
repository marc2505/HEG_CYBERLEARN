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
chaine = input("Entrez avec une chaîne de caratère : (pas vide '') ")
x = input("Entrez avec un caratère ")

# rechercher pour le caractère dans la chaîne
for i in chaine:
    if i == x:
        trouve = True

# afficher le résultat
print("chaîne: %s, caractère: %s, réponse: %r" %(chaine, x, trouve))
