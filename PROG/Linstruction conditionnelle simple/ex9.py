"""Ce programme indique si un joueur peut jouer ou non
selon son age"""

# Déclaration
AGE_LIMITE: int = 16

# Demande son age à l'utilisateur
age: int = int(input("Quel est votre age ? : "))

# Teste si l'age limite est atteint
if age < AGE_LIMITE:
    print("Ce jeux est déconseillé aux moins de 16 ans")
else:
    print("Début de la partie")
