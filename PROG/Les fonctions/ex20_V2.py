# Compare 2 valeurs et affiche la plus petites des 2 ou si elles sont égales
def compare(_valeur1: float, _valeur2: float):
    if _valeur1 < _valeur2:
        print(_valeur1, "est le plus petit des 2 nombres")
    elif _valeur2 < _valeur1:
        print(_valeur2, "est le plus petit des 2 nombres")
    else:
        print("Ces 2 nombres sont égaux")

# Invite à l'écran
def demande_nb() -> None:
    nbr1 = float(input("Saisir un 1er nombre :"))
    nbr2 = input("Saisir un 2ème nombre :")
    return nbr1, nbr2

### Programme principal
# Variables
nbr1: float = None
nbr2: float = None

nbr1, nbr2 = demande_nb()
print(type(nbr1), type(nbr2))
compare(nbr1, float(nbr2))
