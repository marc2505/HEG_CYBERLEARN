""" algo: puissance
données: n -> int, x -> float
résultat: puissance x^n -> float
"""
resultat: float = 1
signe: int = 1
x: float = float(input("Entrez avec la valeur de x: "))
n: int = int(input("Entrez avec la valeur de n: "))

if n != 0:
    if n <= 0:
        n = -n
        signe = -1
    for cpt in range(1, n + 1):
        resultat = resultat * x
    if signe < 0:
        resultat = 1 / resultat
print("x^n =", resultat)
