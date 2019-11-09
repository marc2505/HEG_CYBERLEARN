### Exercice 6 - 1ère partie - Traite une phrase et une lettre
# Déclaration
nb_lettres: int
pos_lettre: int

phrase = input("Saisir une phrase : ")
lettre = input("Saisir une lettre : ")

# Affiche le nombre de fois que la lettre est présente dans la phrase
nb_lettres = phrase.count(lettre)
print("La lettre", lettre.upper(), "apparait", nb_lettres, "fois dans la phrase \"" + phrase + "\"")

# Affiche la 1ère position (index) où se trouve la lettre dans la phrase
pos_lettre = phrase.find(lettre)
print("La lettre", lettre.upper(), "se trouve à la position", pos_lettre, "dans la phrase \"" + phrase + "\"")

# Affiche le nombre de caractères dans la phrase
print("La phrase compte", len(phrase), "caractères")

### Exercice 6 - 2ème partie - •	Demander à l’utilisateur sa date de naissance (format jj.mm.aaaa).
### Puis afficher : « Vous êtes né en aaaa »
date_naiss = str(input("Quelle est votre date de naissance (jj.mm.aaaa) ? : "))
print("Vous êtes né en", date_naiss[6:11])




