# Compare 2 valeurs et retourne la plus petites des 2
def compare(_valeur1: float, _valeur2: float) -> float:
    if _valeur1 < _valeur2:
        return _valeur1
    else:  # OU elif _valeur2 < _valeur1:
        return _valeur2

### Programme principal
# Variables
nbr1:float
nbr2: float
plus_petit: float = None

# Invite à l'écran
nbr1 = float(input("Saisir un 1er nombre :"))
nbr2 = float(input("Saisir un 2ème nombre :"))

plus_petit = compare(nbr1, nbr2)
print(plus_petit, "est le plus petit des 2 nombres")

# OU
print(compare(nbr1, nbr2), "est le plus petit des 2 nombres")
