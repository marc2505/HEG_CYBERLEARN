"""algo: passage param
données: nb_char -> int: taille ligne
résultat: affiche une ligne de taille nb_char des étoiles
"""


def affiche_ligne(n: int):
    """
    affiche ligne avec n étoiles
    :param n: nombre de caratères
    :return:
    """
    for i in range(1, n + 1):
        print("*", end="")


# données
nb_char: int = 10
affiche_ligne(nb_char)
