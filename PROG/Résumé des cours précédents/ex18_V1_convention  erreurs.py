'''
Correction des erreurs de syntaxe et de convention
'''

# Constantes
PAYS: str = 'Suisse'

# Variables
superficie_saisie: float = 0.0 #-MOI- j'aime bien mettre "sais" à la fin pour bien distiquer les var
nb_habitants_saisi: int  = 0
capitale_saisie: str
erreur: bool = True

# Invites à l'écran
capitale_saisie = input("Quel est le nom de la capitale du pays {} ? : ".format(PAYS))
nb_habitants_saisi = int(input("Quel est le nombre d'habitants de cette capitale ? :"))
superficie_saisie = float(input("Quel est la superficie de cette capitale ? : "))

# Teste si la le nombre d'habitant saisi est correct
if nb_habitants_saisi != 133115:
    erreur = True
if nb_habitants_saisi == 133115:
    erreur = False
if erreur == True:
 print("Ce n'est pas le bon nombre d'habitants")

# Teste si la capitale saisie est correcte
if capitale_saisie == 'Bern':
    print("C'est la bonne capitale")
else:
    print("Ce n'est la bonne capitale")
