""" algo: boucle_x
données: ...
affiche: ...
"""
# séquence d'opérations
for x in range(3, 0, -1):
    res: int = 0
    for y in range(3, 0, -1):
        res += y
    res = res / x
    print(str(int(res)) + "-", end="")
