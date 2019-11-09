""" affiche parametres
données: p1 -> int, p2 -> int
résultat: somme p1 et p2
"""


def somme(p1: int, p2: int) -> int:
    """
    somme p1 et p2
    """
    print("somme:", p1, p2)
    r: int = p1 + p2
    return r


# programme principal
res: int = somme(10, 20)
print("retour somme: %d" % res)
