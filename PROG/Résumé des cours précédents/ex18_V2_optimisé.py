'''
Optimisation du code
'''

# Constantes
PAYS: str = 'Suisse'
CAPITALE: str = 'BERN'
NB_HABITANTS: int = 133115

# Variables
superficie_saisie: float = 0.0 #-MOI- j'aime bien mettre "saisi" à la fin pour bien distiquer les var
nb_habitants_saisi: int  = 0
capitale_saisie: str

# Invites à l'écran
capitale_saisie = input("Quel est le nom de la capitale du pays {} ? : ".format(PAYS))
nb_habitants_saisi = int(input("Quel est le nombre d'habitants de cette capitale ? :"))
superficie_saisie = float(input("Quel est la superficie de cette capitale ? : "))

# Teste si la capitale saisie est correcte --MOI--mettre le code dans l'ordre de la demande
# de l'utilisateur sinon les message s'affiche dans le mauvais ordre et c'est moche
if capitale_saisie.upper() == CAPITALE: #--MOI-- en majuscule comme ça on a pas de problème ave la saisie
    print("C'est la bonne capitale")
else:
    print("Ce n'est la bonne capitale")

# Teste si la le nombre d'habitant saisi est correct
if nb_habitants_saisi != NB_HABITANTS:
    print("Ce n'est pas le bon nombre d'habitants")

