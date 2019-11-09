'''Stocker la phrase « je commence la heg cette année » dans une variable,
puis affichez ce texte de la façon suivante : « Je commence la HEG, cette année »'''

# Variables
partie_1: str
partie_2: str
partie_3: str
phrase: str = "Je commance la heg cette année"

# Découpe la phrase en 3 parties pour avoir le mot HEG, seul, dans une variable
# et pouvoir le mettre en majuscule
partie_1 = phrase[0:15]
partie_2 = phrase[15:19].upper()
partie_3 = phrase[19:]

# Affiche la phrase avec HEG en majsucule
print(partie_1 + partie_2 + partie_3)
