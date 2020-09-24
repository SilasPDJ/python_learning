"""
Combinations, Permutations e Product - itertools

combination - Ordem não importa, logo NÃO repetem combinações que somente a ordem muda
permutation - Ordem importa, logo repete todas as ordens possíveis, SEM valores únicos
Ambos não repetem valores únicos
product - Ordem importa e repete valores únicos
"""
# ######################################################### COMBINAÇÕES em ITERÁVEIS (list, tuple, dict, etc)
from itertools import combinations, permutations, product

pessoas = ['Silas', 'Dada', 'Karol', 'Carol', 'Andrei', 'Alef']
for grupo in combinations(pessoas, 2):
    # print(grupo)
    pass


for grupo in permutations(pessoas, 2):
    # print(grupo)
    pass

for grupo in product(pessoas, repeat=2):
    # o arg repeat seleciona a qtd de elementos
    print(grupo)

