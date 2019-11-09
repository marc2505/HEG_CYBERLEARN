# Constantes
MASSE_CAMION = 5000
POIDS_CAISSE_GE_1 = 54.5
POIDS_CAISSE_GE_2 = 35
POIDS_CAISSE_LAUS = 5
POIDS_CAISSE_MONTR = 12.5

# Variables
masse_ge: float
masse_laus: float
masse_montr: float

# Demande à l'utilisateur le nombre de caisses pour chaque chargement
nb_caisse_ge_1: int = int(input("Combien de caisse de 54.5 Kg charge-t-on à Genève ? : "))
nb_caisse_ge_2: int = int(input("Combien de caisse de 35 Kg charge-t-on à Genève ? : "))
nb_caisse_laus: int = int(input("Combien de caisse de 5 Kg charge-t-on à Lausanne ? : "))
nb_caisse_montr: int = int(input("Combien de caisse de 12.5 Kg charge-t-on à Montreux ? : "))

# Calcule la masse restante dans le camion
masse_ge = MASSE_CAMION - (nb_caisse_ge_1 * POIDS_CAISSE_GE_1 + nb_caisse_ge_2 * POIDS_CAISSE_GE_2)
masse_laus = masse_ge - nb_caisse_laus * POIDS_CAISSE_LAUS
masse_montr = masse_laus - nb_caisse_montr * POIDS_CAISSE_MONTR

# Affiche le résultat
print("\nLors des différents chargements, les masses pouvant encore être ajoutées sont les suivantes :"
      "\n\t- Après le 1er chargement, on peut encore ajouter {} Kg dans le camion"
      "\n\t- Après le 2ème chargement, on peut encore ajouter {} Kg dans le camion"
      "\n\t- Après le 3ème chargement, on peut encore ajouter {} Kg dans le camion".format(masse_ge, masse_laus, masse_montr))

# Autre façon d'afficher le résultat
print("""Lors des différents chargements, les masses pouvant encore être ajoutées sont les suivantes :
      - Après le 1er chargement, on peut encore ajouter {} Kg dans le camion
      - Après le 2ème chargement, on peut encore ajouter {} Kg dans le camion
      - Après le 3ème chargement, on peut encore ajouter {} Kg dans le camion""".format(masse_ge, masse_laus, masse_montr))
