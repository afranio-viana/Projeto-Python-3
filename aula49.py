from itertools import combinations,permutations,product

pessoas=['Afrânio', 'Esquerdo', 'Viana']

print(f'\t###Combinations###')

"""Serve para fazer combinações em uma lista,
mas a ordem importa e valores não se repetem"""
for grupo in combinations(pessoas, 2):
    print(f'\t{grupo}')

print(f'\n\t###Permutations###')
"""Serve para fazer combinações em uma lista, a ordem não importa,
mas os valores não se repetem"""
for grupo in permutations(pessoas,2):
    print(f'\t{grupo}')

print(f'\n\t###Product###')
"""Serve para fazer combinações em uma lista,
a ordem não importa e os valores podem se repetir!!!"""
for grupo in product(pessoas,repeat=2):
    print(f'\t{grupo}')