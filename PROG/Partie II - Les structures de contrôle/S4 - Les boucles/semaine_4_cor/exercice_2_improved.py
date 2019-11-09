"""
Écrire un algorithme que calcule et affiche la puissance de 2 pour les n premiers entiers

Exemple de déroulement:

...

puissance   résultat
0           1
1           2
2           4
3           8
4           16
5           32
"""

""" algo: puissance de 2
données: n: int
résultat: affiche la puissance de 2 pour les n premiers entiers
"""
### decl. et init. des variables
n: int = None
power: int = 1
### séq. d'opérations

# saisie la valuer
while n is None or n < 0:
    n = int(input("Puissance ? (>= 0) "))

print()
print("puissance\trésultat")
# calcule et affiche
for i in range(0, n+1):
    print("%d\t\t\t%d" %(i, power))
    power = 2 * power
