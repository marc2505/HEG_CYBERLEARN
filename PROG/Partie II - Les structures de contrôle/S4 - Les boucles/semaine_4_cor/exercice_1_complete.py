"""
Une personne peut économiser un montant fixe d'argent chaque mois.
Elle a trouvé un bon investissement qui lui rapporte en moyenne 0,5 % d'intérêt par mois.
Elle veut acheter un certain produit et aimerait savoir combien de mois elle doit économiser.

Écrire un algorithme pour calculer le nombre de mois qu'il lui faut épargner pour acheter le produit.


Exemple de déroulement 1:

...

Prix du produit: 		x.xx CHF
Montant d'argent initial: 	y.yy CHF

mois 1:
    vous avez 		    y.yy CHF
	il vous manque		x.xx CHF

mois 2:
    vous avez 		    y.yy CHF
	il vous manque		x.xx CHF

mois 3:
    vous avez		    y.yy CHF

Vous pouvez acheter votre ... en n mois
Il vous reste encore		z.zz CHF




Exemple de déroulement 2:

...

Prix du produit: 		x.xx CHF
Montant d'argent initial: 	y.yy CHF

Vous pouvez acheter votre ... en n mois
Il vous reste encore		z.zz CHF
"""

""" algo: epargne
données: 
    produit:    str
    prix:       float
    montant:    float
    epargne:    float    
    interet:    float
résultat: calcule le nombre de mois necessaires pour acheter un produit
"""
### déclaration et initialisation de variables
produit: str = None
prix: float = None
montant: float = None
epargne: float = None
interet: float = None

mois: int = 0
### séquence d'opérations

# saisie les valeurs
while prix is None or prix <= 0:
    prix = float(input("Quel est le prix du produit ?"))

while montant is None or montant < 0:
    montant = float(input("Quel est votre montant initial ?"))

while epargne is None or epargne < 0:
    epargne = float(input("Quelle est votre épargne mensuelle ?"))

while interet is None or interet < 0:
    interet = float(input("Quel est l'intérêt de votre investissement ?"))

while produit is None or len(produit) == 0:
    produit = input("Quel produit voulez-vous acheter ?")


print("Prix du produit :\t\t\t\t%.2f CHF" %(prix))
print("Montant d'argent initial :\t\t%.2f CHF" %(montant))

# test si il est possible d'arriver au prix du produit
if interet == 0 and epargne == 0 and montant < prix:
    print("Vous ne pouvez pas acheter ce(tte) %s" %produit)
else:
    # calcule la quantité necessaire de mois pour arriver
    # à la valeur du produit avec un intérêt par mois appliqué
    # au montant
    while montant < prix:
        mois += 1
        montant = montant + montant*interet + epargne

        print("mois %d:" %(mois))
        print("\tvous avez\t\t\t%.2f CHF" % (montant))

        # if montant < prix:
        print("\til vous manque\t\t%.2f CHF" %(prix - montant))

    print()
    print("Vous pouvez acheter votre %s en %d mois" %(produit, mois))
    rest: float = montant - prix
    print("Il vous reste encore\t%.2f CHF" %(rest))
