"""
1. Dévelopez un algorithme pour calculer la surface et le périmètre d'un cercle
Le rayon du cercle et l'unité de mesure sont donnés par l'utilisateur

Exemple de fonctionnement :

Entrer le rayon du cercle ?
Entrer l'unité de mesure ? (ex., cm, m, km, etc.)
La surface est          <xx.xxx>    <unité>^2
Le périmètre est        <yy.yyy>    <unité>

2. Modifiez l'algorithme pour afficher la condition (ou affirmation) "La valeur du rayon est positive:"
suivie du résultat de l'évaluation de l'expression "rayon est positif"

Exemple de fonctionnement :

Entrer le rayon du cercle ?
La valeur du rayon est positive: True
...
"""

""" algo: calcul_cercle
données: rayon: float, unite: str
résultat: affiche la surface et le périmètre d'un cercle de rayon r
"""

### déclaration et initialisation des variables
PI: float = 3.14

surface: float = 0.0
perimetre: float = 0.0

rayon: float = None
unite: str = None

### séquence d'opérations
rayon = float(input("Entrer le rayon du cercle ?"))
print("La valeur du rayon est positive:", rayon > 0)

unite = input("Entrer l'unité de mesure ? (ex., cm, m, km, etc.)")

surface = PI * rayon ** 2
perimetre = 2 * PI * rayon

print("La surface est\t\t\t%.3f\t%s^2" %(surface, unite))
print("Le périmètre est\t\t%.3f\t%s" %(perimetre, unite))




