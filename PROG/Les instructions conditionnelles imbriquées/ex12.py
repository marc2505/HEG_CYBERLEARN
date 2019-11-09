'''Demande l'année de l'escalade et indique si c'est la bonne à 5 ans pret'''

# Déclaration
ANNEE_ESCALADE: int = 1602
annee_saisie: int

# Demande à l'utilisateur la date
annee_saisie = int(input("En quelle date s'est déroulée l'escalade ? : "))

# Indique si la date est correcte
if annee_saisie == ANNEE_ESCALADE:
    print("C'est la bonne réponse")
# Indique si la date est proche à 5 ans prêt
elif annee_saisie >= ANNEE_ESCALADE - 5 and annee_saisie <= ANNEE_ESCALADE + 5:
    print("C'est presque ça")
# la date est fausse
else:
    print("C'est faux")
