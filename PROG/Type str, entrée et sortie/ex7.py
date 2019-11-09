'''Demande à l’utilisateur un mot de 3 lettres et qui décale
ces lettres de 3 rangs dans l’alphabet'''

# Constante
ALPHABET:str = "abcdefijklmnopqrstuvwxyz"
# Variables
pos_lettre_1:str
pos_lettre_2:str
pos_lettre_3:str
code_lettre_1:str
code_lettre_2:str
code_lettre_3:str

# Demande un mot de 3 lettres
mot:str = input("Saisir un mot de 3 lettres : ")

# Recherche la position dans l'alphabet, des lettres du mot
pos_lettre_1 = ALPHABET.find(mot[0])
pos_lettre_2 = ALPHABET.find(mot[1])
pos_lettre_3 = ALPHABET.find(mot[2])

# Récupère la lettre 3 positions plus loin, dans l'alphabet
code_lettre_1 = ALPHABET[pos_lettre_1 + 3]
code_lettre_2 = ALPHABET[pos_lettre_2 + 3]
code_lettre_3 = ALPHABET[pos_lettre_3 + 3]

# Affiche le mot codé
print("Le mot codé est : " + code_lettre_1 + code_lettre_2 + code_lettre_3)



