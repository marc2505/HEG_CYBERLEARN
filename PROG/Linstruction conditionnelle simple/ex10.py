""" Indique si une personne est en surpoids
 en fonction de son IMC """

# Déclaration
IMC_MAX: int = 25
imc: float

# Demande le poids et la taille à l'utilisateur
poids: float = float(input("Quel est votre poids (KG) ? : "))
taille: float = float(input("Quel est votre taille (m) ? : "))

# Calcul de l'IMC de l'utilisateur
imc = poids / (taille ** 2)
# Si l'IMC est supérieur à 25 la personne est en surpoids
if imc > IMC_MAX:
    print("Attention vous êtes en surpoids")

