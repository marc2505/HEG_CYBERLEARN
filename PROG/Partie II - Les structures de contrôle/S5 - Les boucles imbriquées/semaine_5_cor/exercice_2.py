"""
Créez un algorithme qui imprime la table de division des n premiers entiers comme dans l'exemple ci-dessous.

L'étoile indique que le nombre indiqué dans la colonne est divisé par le nombre indiqué dans la ligne
ou que le nombre indiqué dans la ligne est divisé par le nombre indiqué dans la colonne.


Exemple de déroulement:

Entrez avec la valeur n: (n >= 1) 10
	1	2	3	4	5	6	7	8	9	10
1	*	*	*	*	*	*	*	*	*	*
2	*	*		*		*		*		*
3	*		*			*			*
4	*	*		*				*
5	*				*					*
6	*	*	*			*
7	*						*
8	*	*		*				*
9	*		*						*
10	*	*			*					*

"""

""" algo: table_division
données: n -> taille de table
résultat: affiche la table de division de n premiers entiers
"""

### déclaration et initiation des variables
n: int = None

### séquence d'opérations

# while n is None or n < 1:
n = int(input("Entrez avec la valeur n: (n >= 1) "))

# afficher l'en-tête de colonne

for i in range(1, n + 1):
    print("\t"+str(i), end="")
print()

# processer les tables de division ligne par ligne, colonne par colonne
for i in range(1, n + 1):
    # affiche le numéro de la ligne
    print(str(i) + "\t", end="")
    for j in range(1, n + 1):
        # si la colonne n'est pas divisible par la ligne
        # ou la ligne n'est pas divisible par le colonne
        # affiche un tab
        if j % i == 0 or i % j == 0:
            print("*\t", end="")
        else:
            print("\t", end="")
    print()
