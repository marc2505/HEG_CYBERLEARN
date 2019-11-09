''' LA LETTRE EST-ELLE DANS LA PHRASE ?
Demandez à l’utilisateur de saisir une phrase, puis une lettre en minuscule.
Si la lettre est présente dans la phrase, affichez à l’écran le message suivant : La lettre ? (en majuscule)
apparait ? fois dans la phrase "???" (Exemple : La lettre N apparait 2 fois dans la phrase "Bonjour, comment ça va ?").
Si la lettre est présente plus d’une fois, afficheZ la 1ère position (index) où se trouve cette lettre dans la phrase
ainsi que la partie de la phrase jusqu’à cette lettre. Exemple : La 1ère occurrence de la lettre U se trouve à la position 5 (BONJOU).
Si la lettre n’est pas présente, vous devez afficher le message : la lettre ? (en majuscule) n’est pas présente dans la phrase "???".
'''

# Variables
nb_lettres: int
pos_lettre: int

# Demande à l'utilisateur de saisir une phrase et une lettre
phrase = input("Saisir une phrase : ")
lettre = input("Saisir une lettre : ")

# Détermine le nombre de fois que la lettre est présente dans le texte
nb_lettres = phrase.count(lettre)

# Si la lettre est présente dans la phrase : affiche le nombre de fois qu'elle est présente
if nb_lettres > 0:
    print("La lettre", lettre.upper(), "apparait", nb_lettres, "fois dans la phrase \"" + phrase + "\"")
    # Si la lettre est présent plus d'une fois
    if nb_lettres > 1:
            pos_lettre = phrase.find(lettre)
            # Affiche la 1ère position (index) où se trouve la lettre dans la phrase ainsi que la partie de la phrase jusqu’à cette lettre
            print("La 1ère occurrence de la lettre", lettre.upper(), "se trouve à la position",
                  pos_lettre, "(" + phrase[0:pos_lettre + 1].upper() + ")")
# La lettre n'est pas présente dans la phrase
else:
    print("La lettre", lettre.upper(), "n'est pas présente dans la phrase \"" + phrase + "\"")
