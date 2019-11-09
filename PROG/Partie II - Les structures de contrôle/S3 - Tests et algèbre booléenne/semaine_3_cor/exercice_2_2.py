"""
2.2  Ecrire un algorithme qui affiche si un contribuable d’un pays imaginaire est imposable ou non sachant que :
- les hommes de plus de 18 ans paient l’impôt
- les femmes paient l’impôt si elles ont entre 18 et 35 ans
- les autres ne paient pas d’impôt

ex.: 1
... <saisir les données> ...
"Vous êtes imposable !"


ex.: 2
... <saisir les données> ...
"Vous n'êtes pas imposable !"

"""
""" algo: impots
données: sexe et age d'un contribuable
résultat: affiche si contribuable est imposable ou non
"""
### déclaration et initialisation des variables
GENRE_FEMME: str = "femme"
GENRE_HOMME: str = "homme"

AGE_LIMITE_1: int = 18
AGE_LIMITE_2: int = 35

sexe: str = None
age: int = None
est_imposable: bool = False

### séquence d'opérations
sexe = input("Entrez votre sexe: (%s ou %s)" % (GENRE_FEMME, GENRE_HOMME))
if sexe != GENRE_FEMME and sexe != GENRE_HOMME:
    print("Les valeurs possibles pour sexe sont: %s et %s" % (GENRE_FEMME, GENRE_HOMME))
    exit()

age = int(input("Entrez votre âge:"))
if age <= 0:
    print("L'âge doit être plus grand que zero")
    exit()

if sexe == GENRE_HOMME and age >= AGE_LIMITE_1:
    est_imposable = True
elif sexe == GENRE_FEMME and age >= AGE_LIMITE_1 and age <= AGE_LIMITE_2:
    est_imposable = True

if est_imposable:
    print("Vous êtes imposable !")
else:
    print("Vous n'êtes pas imposable !")
