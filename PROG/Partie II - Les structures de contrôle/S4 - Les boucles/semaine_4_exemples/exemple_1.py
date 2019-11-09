""" algo: precedence
données: les variables var1, var2 et var3
résultat: affiche True ou False
"""

### déclaration et initialisation
### des variables
var_1: int = 0
var_2: int = 1
var_3: int = 1

### séquence d'opérations
if var_1 * var_2 + var_3:
    print("True")
else:
    print("False")

if var_1 * (var_2 + var_3):
    print("True")
else:
    print("False")
