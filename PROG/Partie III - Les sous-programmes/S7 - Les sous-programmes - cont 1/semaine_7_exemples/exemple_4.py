"""algo: passage param
données: n -> int
résultat: ajoute 10 à n
"""


def ajoute(n: int):
    """
    ajoute 10
    :param n: int
    :return: n + 10
    """
    n = n + 10
    print("n dans la fonction: %d" % n)


# données
n: int = 10
print("n avant la fonction: %d" % n)
ajoute(n)
print("n après la fonction: %d" % n)
