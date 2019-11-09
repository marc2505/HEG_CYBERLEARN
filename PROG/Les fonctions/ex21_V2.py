'''
Cette correction de l'exercice 21, prend en compte le fait que les 2 valeurs
peuvent être égales (ce qui n'était pas demandé dans l'énoncé
'''

def compare(_valeur1: float, _valeur2: float) -> float:
    """
    Compare 2 valeurs et affiche la plus petite des 2 ou si elles sont égales
    :param _valeur1: float -> 1ère valeur à comparer
    :param _valeur2: float -> 2ème valeur à comparer
    :return: float -> la plus petite des 2 valeurs ou None si elles sont égales
    """
    if _valeur1 < _valeur2:
        return _valeur1
    elif _valeur2 < _valeur1:
        return _valeur2
    else:
        return None

### Programme principal
# Variables
nbr1:float
nbr2: float
plus_petit: float = None

# Invite à l'écran
nbr1 = float(input("Saisir un 1er nombre :"))
nbr2 = float(input("Saisir un 2ème nombre :"))

plus_petit = compare(nbr1, nbr2)

# Affiche le nombre le plus petit ou s'ils sont égaux
if plus_petit == None:
    print("Ces 2 nombres sont égaux")
else:
    print(plus_petit, "est le plus petit des 2 nombres")

# OU PAS BIEN : ne pas faire !!!!!!!!!!!!
if compare(nbr1, nbr2) == None:
    print("Ces 2 nombres sont égaux")
else:
    print(compare(nbr1, nbr2), "est le plus petit des 2 nombres")
