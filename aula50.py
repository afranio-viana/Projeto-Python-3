from itertools import groupby, tee

alunos=[
    {'nome': 'Afrânio','nota':'A'},
    {'nome': 'Esquerdo','nota':'B'},
    {'nome':'Viana','nota':'C'},
    {'nome': 'Afrânio','nota':'A'},
    {'nome': 'Esquerdo','nota':'B'},
    {'nome':'Viana','nota':'C'},
    {'nome': 'Afrânio','nota':'A'},
    {'nome': 'Esquerdo','nota':'B'},
    {'nome':'Viana','nota':'C'},
    {'nome': 'Afrânio','nota':'A'},
    {'nome': 'Esquerdo','nota':'B'},
    {'nome':'Viana','nota':'C'}
]

"""Ordena os alunos por nota!!!"""
ordena=lambda item: item['nota']
alunos.sort(key=ordena)

"""Agrupa os alunos a partir da ordenação"""
alunos_agrupados=groupby(alunos,ordena)

for agrupamento, valores_agrupados in alunos_agrupados:
    va1,va2=tee(valores_agrupados)
    print(f'Agrupamento: {agrupamento}')
    for aluno in va1:
        print(f'\t{aluno}')
    quantidade=len(list(va2))
    print(f'\t{quantidade} alunos tiraram nota {agrupamento}')
    print()