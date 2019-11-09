"""
Étant donné une séquence d'ADN et une mutation,
on demande de créer un algorithme pour tester si la séquence d'ADN contient la mutation
    a. si oui, l'algorithme doit afficher la position de la mutation dans la séquence
    b. si non, l'algorithme affiche l'indice -1


Tester votre algorithme avec les mutations 1, 2, 3, 4 et 5

"""
""" algo: recherche_mutation
données: séquence d'ADN, mutation
résultat: affiche la position de la mutation
"""

### déclaration et initialisation des variables
SEQ_ADN: str = "ctggtctcacgaccctcgggggaagcttccgctgatttaacctcttggcggggcaaccgccgacaatcagtgtcatagattcaaagtcgagtaagacgtagacttcgcttttcgctatttcaaaactccaatagtaatttagggacgacctgtcattatcaccgtccagtcaaagtgcttgggtatcaaatagtgaatttgaagatttcatcgtgtggaaaagtgaaatccccggaaccacggaatcgccggccggtatgccgatcttgagtcttcagggacgcaacttgtacaactccatataatgtagtagcttggtttgaacgcccacttatcaactcgtccccaatcagaatcgaaaacacctgttgccgatgctcctcgctgcttggattgatagttttcgggcgagacaacacatcacttccccgaaggtgcccgccccaaatattttcgtgccggtaggattaccagctatgagatcttattcacctgttcggccaccggaccatatttattttgccatatggatgcttctcttaatcaaacgtgtagtgaatacgggtggttcgaatattcagtcattagataactgaggcagacggctcgaagttctcgacaaactatcagcacagcgggacccgtctgctaactcttccagctctgtaggaggaggagcagacagaatttccttcggtcctagcggaacacagatagaggggaggctacgttgatacccagtcgttaagcgagtggtgattaattgtctacgacttgaagtttgatccgttgacagacttgcgtttcctactctgtgccacgcattggattatagatcacatcggacgattaaagtgtatggtcggtcgatatgttaaaggggtccgtgctgaagaaccgcaaaatccgactgcgggatcggagtcctccatcataaaagtatcggagtagggttaatagaccttttttcctggttcgttacgatttatctaaggaccgc"

MUTATION1: str = "ctggtctc"
MUTATION2: str = "tggtctca"
MUTATION3: str = "tcgaatat"
MUTATION4: str = "ccaaatcg"
MUTATION5: str = "aggaccgc"

indice: int = -1

mutation: str = None
### séquence d'opérations

# saisir la mutation à tester
while mutation is None:
    mut_number: int = int(input("Entrez avec le numéro de la mutation à tester : (1 <= n <= 5 ) "))
    if mut_number == 1:
        mutation = MUTATION1
    elif mut_number == 2:
        mutation = MUTATION2
    elif mut_number == 3:
        mutation = MUTATION3
    elif mut_number == 4:
        mutation = MUTATION4
    elif mut_number == 5:
        mutation = MUTATION5


# rechercher l'indice de la sous-chaîne
fin: int = len(SEQ_ADN) - len(mutation)
i: int = 0
while indice < 0 and i <= fin:
    debut_recherche: int = i                # position initiale
    fin_recherche: int = debut_recherche + len(mutation)    # position finale
    if SEQ_ADN[debut_recherche:fin_recherche] == mutation:
        indice = i
    i += 1

# afficher la position
print("mutation dans la position: %d" %indice)
