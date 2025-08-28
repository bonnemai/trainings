# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

# Écrire un autre programme qui demande deux lettres à l'utilisateur et :
#
# si les deux lettres sont différentes, il affiche la phrase "le nombre de contacts entre ... et ... est de ..."
# si c'est la même lettre ou qu'au moins une lettre n'est pas dans le graphe un message d'erreur approprié
# Le faire pour le graphe suivant à partir du tableau ami (le tableau avec les 0 et les 1) :
from typing import List

amis_matrix = [[0, 1, 0, 0, 0, 1, 0, 0, 0],
               [1, 0, 1, 1, 1, 1, 1, 0, 0],
               [0, 1, 0, 1, 0, 0, 0, 0, 0],
               [0, 1, 1, 0, 0, 0, 0, 0, 0],
               [0, 1, 0, 0, 0, 0, 1, 1, 0],
               [1, 1, 0, 0, 0, 0, 0, 0, 1],
               [0, 1, 0, 0, 1, 0, 0, 1, 0],
               [0, 0, 0, 0, 1, 0, 1, 0, 1],
               [0, 0, 0, 0, 0, 1, 0, 1, 0]]

is_ami = lambda idx1, idx2: amis_matrix[idx1][idx2] == 1
get_amis = lambda idx: [i for i in range(len(amis_matrix)) if i != idx and is_ami(idx, i)]


def get_amis_damis(amis_l0: List[int]) -> List[int]:
    results: List[int] = []
    for l0 in amis_l0:
        amis_l1 = get_amis(l0)
        for l1 in amis_l1:
            if l1 not in results and l1 not in amis_l0:
                results.append(l1)
    return results


def distance_amis(idx1, idx2):
    if idx1 == idx2: return 0
    if idx1 > len(amis_matrix) or idx2 > len(amis_matrix): return -1
    amis_damis = get_amis(idx1)
    for level in range(1, len(amis_matrix)):
        if idx2 in amis_damis: return level
        amis_damis = get_amis_damis(amis_damis)


if __name__ == '__main__':
    print(f'isAmi: {is_ami(1, 0)}')
    print(f'getAmi: {get_amis(1)}')
    print(f'amis_damis: {get_amis_damis([1])}')
    print(f'distance_amis: {distance_amis(1, 0)}')
    print(f'distance_amis: {distance_amis(4, 0)}')
    print(f'distance_amis: {distance_amis(7, 0)}')
    print(f'distance_amis: {distance_amis(27, 0)}')
