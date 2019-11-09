"""
Un palindrome est une chaîne de caractères qui se lit de la même façon dans les deux sens
Exemple :
    "elle"
    "radar"
    "laval"

Ecrire un algorithme qui vérifie si un mot est un palindrome

L'algorithme doit afficher 1 si le mot est un palindrome et 0 sinon
"""
"""
algo: palindrome
données: un mot
résultat: affiche 1 si le mot est palindrome et 0 sinon
"""
### déclaration et initiation des variables
mot: str = None
palindrome: int = 1

### séquence d'opérations

# saisir l'information
mot = input("Entrez avec le mot : ")

# verifier si le mot est un palindrome
debut: int = 0
fin: int = len(mot)
while palindrome == 1 and debut < fin:
    if mot[debut] != mot[fin - 1]:
        palindrome = 0
    debut += 1
    fin -= 1

# afficher le résultat
print("palindrome:", palindrome)