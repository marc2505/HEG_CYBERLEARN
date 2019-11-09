""" algo: table_multiplication
données: nombre maximum pour calculer la multiplication
résultat: tables de multiplication
"""
### déclaration et initialisation
### des variables
TABLE_MAX: int = 10

### séquence d'opérations
table1: int = 1
while table1 <= TABLE_MAX:  # traite la boucle extérieur
    print("### table de", table1, "###")

    table2: int = 1
    while table2 <= TABLE_MAX:  # traite la boucle intérieur
        resultat: int = table1 * table2
        print("%d x %d = %d" % (table1, table2, resultat))
        table2 += 1

    table1 += 1
