""" algo: table_multiplication
données: nombre maximum pour calculer la multiplication
résultat: tables de multiplication
"""
### déclaration et initialisation
### des variables
TABLE_MAX: int = 10

### séquence d'opérations
for table1 in range(1, TABLE_MAX + 1):  # traite la boucle extérieur
    print("### table de", table1, "###")

    for table2 in range(1, TABLE_MAX + 1):  # traite la boucle intérieur
        resultat: int = table1 * table2
        print("%d x %d = %d" % (table1, table2, resultat))
