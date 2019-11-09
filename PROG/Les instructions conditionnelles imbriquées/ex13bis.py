''' Jeu pierre, papier, ciseaux'''
import random

# Constantes
PIERRE: int = 1
PAPIER: int = 2
CISEAUX: int = 3

# Variables
nb_joueur: int
nb_ordi: int
signe_joueur: str
signe_ordi: str

# Demande son choix au joueur
nb_joueur = int(input("Quel est votre choix ? :\n1 (Pierre)\n2 (Papier)\n3 (Ciseaux)\n"))

# Si le choix du joueur n'est pas valable
if nb_joueur < 1 and nb_joueur > 3:
    print("Ce choix n'est pas valable, vous ne pouvez pas jouer")
else:
    # Affiche le choix du joueur
    if nb_joueur == PIERRE:
        signe_joueur = "Pierre"
    elif nb_joueur == PAPIER:
        signe_joueur = "Papier"
    else:
        signe_joueur = "Ciseaux"
    print("Vous avez choisi :",signe_joueur)

    # Choix de l'ordinateur
    nb_ordi = random.randint(PIERRE,CISEAUX)
    # Affiche le choix de l'ordinateur
    if nb_ordi == PIERRE:
        signe_ordi = "Pierre"
    elif nb_ordi == PAPIER:
        signe_ordi = "Papier"
    else:
        signe_ordi = "Ciseaux"
    print("L'ordinateur a choisi :",signe_ordi)

    # Calcul du gagnant
    if nb_joueur == nb_ordi:
        print("Egalité")
    elif (nb_joueur == PIERRE and nb_ordi == CISEAUX) or \
            (nb_joueur == PAPIER and nb_ordi == PIERRE) or \
            (nb_joueur == CISEAUX and nb_ordi == PAPIER):
        print("Vous avez gagné")
    else:
        print("L'ordinateur a gagné")

