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

mutation_cle: str = None
### à coder ###
