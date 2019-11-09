"""
Créez un algorithme qui imprime la table de division des n premiers entiers comme dans
l'exemple ci-dessous.

L'étoile indique que le nombre indiqué dans la colonne est divisé par le nombre indiqué
dans la ligne ou que le nombre indiqué dans la ligne est divisé par le nombre indiqué
dans la colonne.


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

"""algo: table de division
données: n -> la valeur maximum de la table
résultat: affiche la table de division
"""

### déclaration et initialisation de variables
n: int = None   # table de division

### séquence d'opérations

while n is None or n < 1:
    n = int(input("Entrez avec la valeur n: (n >= 1) "))

#	1	2	3	4	5	6	7	8	9	10
for i in range(1, n+1):
    print("\t"+str(i), end="")

print()

for i in range(1, n+1):                 # traiter les lignes
    print(str(i)+"\t", end="")
    for j in range(1, n+1):             # traiter les colonnes
        if i % j == 0 or j % i == 0:    # si la ligne est divisable par la colonne
                                        # ou si la colonne est divisable par ligne
                                        # on affiche une etoile
            print("*\t", end="")
        else:
            print("\t", end="")         # sinon, affiche un vide
    print()











