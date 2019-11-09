""" Indique si une personne est en surpoids ou en sous poids
 en fonction de son IMC. """

# Déclaration
IMC_MAX:float = 25
IMC_MIN:float = 18.5
imc: float
poids_min: float
poids_max: float
poids_saisi: int
taille_saisie: float

# Demande le poids et la taille à l'utilisateur
poids_saisi: float = float(input("Quel est votre poids (KG) ? : "))
taille_saisie: float = float(input("Quel est votre taille (m) ? : "))

# Calcul de l'IMC de l'utilisateur et l'arrondi à 2 décimales
imc = round(poids_saisi / (taille_saisie ** 2), 2)

# Si l'IMC est supérieur à 25, la personne est en surpoids
if imc > IMC_MAX:
    poids_min = 18.5 * (taille_saisie ** 2) # Calcule le poids idéal minimum de la personne
    poids_max = 25 * (taille_saisie ** 2) # Calcule le poids idéal maximum de la personne
    print("Attention vous êtes en surpoids"
          "\nVotre poids idéal se situe entre {:.2f} et {:.2f}". format(poids_min, poids_max)) # Arrondi à 2 décimales

# Affiche l'IMC de la personne et la salue
print("Votre IMC est de : " + str(imc) +
      "\nMerci de votre visite")
