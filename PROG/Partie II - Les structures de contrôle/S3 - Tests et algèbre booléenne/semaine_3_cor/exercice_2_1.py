"""
2.1 Ecrire un algorithme qui affiche le prix de n photocopies sachant que le reprographe facture
CHF -.10 les dix premières photocopies,
CHF -.09 les vingt suivantes et
CHF -.08 au-delà

Exemple de fonctionnement :

Entrer le nombre de photocopies ?
Le prix est : CHF xxx.xx
"""
""" algo: prix photocopies
données: n nombre de photocopies, prix unitaire des photocopies
résultat: affiche le prix de n photocopies
"""

### déclaration et initialisaiton des variables
PRIX1: float = 0.10
PRIX2: float = 0.09
PRIX3: float = 0.08

LOT1: int = 10
LOT2: int = 20

nombre_photocopie: int = None
prix: float = 0

### séquence d'opérations
nombre_photocopie = int(input("Entrer le nombre de photocopies ?"))

if nombre_photocopie <= 0:
    print("Le nombre de photocopies doit être un entier positif")
    exit()

if nombre_photocopie > LOT1:
    prix = LOT1 * PRIX1
    nombre_photocopie = nombre_photocopie - LOT1
    if nombre_photocopie > LOT2:
        prix += LOT2 * PRIX2
        nombre_photocopie = nombre_photocopie - LOT2
        prix += nombre_photocopie * PRIX3
    else:
        prix += nombre_photocopie * PRIX2
else:
    prix = nombre_photocopie * PRIX1

print("Le prix est : CHF %2.2f" % prix)
