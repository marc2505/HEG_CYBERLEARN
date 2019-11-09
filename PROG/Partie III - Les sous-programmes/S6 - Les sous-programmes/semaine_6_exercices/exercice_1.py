"""
Créer un algorithme pour tester si une chaîne de caractére contient un caractère

Toujours utiliser uniquement les structures et les méthodes vues dans le cours.

Exemple:
chaîne: "algo I", caractère: "a", réponse: True
chaîne: "algo I", caractère: "i", réponse: True
chaîne: "algo I", caractère: "u", réponse: False
"""
""" algo : recherche
données: chaîne de caractères -> str, clé -> str
résultat: affiche True si le caractère est dans la chaîne
"""

# données
chaine: str = None
cle : str = None
contient: bool = False

# saisir les informations
while chaine is None or len(chaine) == 0:
    chaine = input("entrez avec la chaîne: (pas vide) ")

while cle is None or len(cle) != 1:
    cle = input("entrez avec le caractère: (unique) ")

# faire la recherche
for i in chaine.lower():
    if i == cle.lower():
        contient = True
        break

# afficher le résultat
print("chaîne: \"%s\", caractère: \"%s\", réponse: %r" % (chaine, cle, contient))