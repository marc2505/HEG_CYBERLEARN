""" algo: calcule puissance
données: n -> int, x -> float
résultat: puissance x^n -> float
"""


def puissance(x: float, n: int) -> float:
    resultat: float = 1
    for cpt in range(1, n + 1):
        resultat = resultat * x
    return resultat


def print_res(x: float, n: int, y: float):
    print("puissance de %.2f ^ %d est %.2f" % (x, n, y))


x: float = float(input("x: "))
n: int = int(input("n: "))

resultat: float = puissance(x, n)
print_res(x, n, resultat)
