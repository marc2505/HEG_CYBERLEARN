"""algo: passage param
données: n -> list
résultat: ajoute 10 à la liste
"""


def ajoute(n: list):
    """
    ajoute 10
    :param n: list
    :return:
    """
    n.append(10)
    print("n dans la fonction: %s" % n)


# données
n: list = [10]
print("n avant la fonction: %s" % n)
ajoute(n)
print("n après la fonction: %s" % n)
