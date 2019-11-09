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

mutation = MUTATION1

# rechercher l'indice de la sous-chaîne
fin: int = len(SEQ_ADN) - len(mutation)     # fin de la recherche
for i in range(fin+1):
    debut_recherche: int = i                # position initiale
    fin_recherche: int = debut_recherche + len(mutation)    # position finale
    if SEQ_ADN[debut_recherche:fin_recherche] == mutation:
        indice = i

# afficher la position
print("mutation dans la position: %d" %indice)
