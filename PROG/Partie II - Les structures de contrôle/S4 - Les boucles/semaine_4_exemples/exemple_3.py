""" algo: table_multiplication
données: table: int
résultat: affiche une table de multi.
"""

### décl. et init. des variables
cpt: int = 1
table: int = None

### séquence d'opérations
table = int(input("Quelle table ?"))

while cpt <= 10:
    res: int = table * cpt
    print("%d x %d = %d" % (table, cpt, res))
    cpt += 1
