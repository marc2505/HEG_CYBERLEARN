"""
Une personne peut économiser un montant fixe d'argent chaque mois.
Elle a trouvé un bon investissement qui lui rapporte en moyenne 0,5 % d'intérêt par mois.
Elle veut acheter un certain produit et aimerait savoir combien de mois elle doit économiser.

Écrire un algorithme pour calculer le nombre de mois qu'il lui faut épargner pour acheter le produit.


Exemple de déroulement 1:

...

Prix du produit: 		    x.xx CHF
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
produit = input("Quel produit voulez-vous acheter ?")
prix = float(input("Quel est le prix du produit ?"))
montant = float(input("Quel est votre montant initial ?"))
epargne = float(input("Quelle est votre épargne mensuelle ?"))
interet = float(input("Quel est l'intérêt de votre investissement ?"))


print("Prix du produit :\t\t\t\t%.2f CHF" %(prix))
print("Montant d'argent initial :\t\t%.2f CHF" %(montant))

# calcule la quantité necessaire de mois pour arriver
# à la valeur du produit avec un intérêt par mois appliqué
# au montant
while montant < prix:
    montant = montant + montant*interet + epargne

    print("mois %d:" %(mois))
    print("\tvous avez\t\t\t%.2f CHF" % (montant))

print("Vous pouvez acheter votre %s en %d mois" %(produit, mois))
print("Il vous reste encore\t%.2f CHF" %(montant - prix))



