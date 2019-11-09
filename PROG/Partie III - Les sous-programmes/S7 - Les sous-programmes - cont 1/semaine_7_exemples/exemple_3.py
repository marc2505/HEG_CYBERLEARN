"""algo: passage param
données: nb_char -> int: taille ligne
résultat: affiche une ligne de taille nb_char
"""


def affiche_ligne(n: int, char: str = "*"):
    """
    affiche ligne avec n caractères
    :param n: nombre de caractères
    :return:
    """
    for i in range(1, n + 1):
        print(char, end="")


# données
nb_char: int = 10
affiche_ligne(nb_char, char = "#")

print()

affiche_ligne(nb_char)