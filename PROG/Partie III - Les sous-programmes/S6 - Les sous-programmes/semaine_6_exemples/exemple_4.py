""" algo: puissance
données: n -> int, x -> float
résultat: puissance x^n -> float
"""


def puissance(x: float, n: int) -> float:
    """
    calcule la puissance de x ^ n
    :param x: la base
    :param n: l'exposant
    :return: la puissance x^n
    """
    resultat: float = 1
    signe: int = 1
    if n != 0:
        if n <= 0:
            n = -n
            signe = -1
        for cpt in range(1, n + 1):
            resultat = resultat * x
        if signe < 0:
            resultat = 1 / resultat
    return resultat


x: float = float(input("Entrez avec la valeur de x: "))
n: int = int(input("Entrez avec la valeur de n: "))

resultat: float = puissance(x, n)

print("x^n =", resultat)
