"""Podemos construir dicionários com filhos dicionários!!!"""
clientes={
    'cliente1':{
        'nome': 'Afrânio',
        'sobrenome': 'Viana'    
    },
    'cliente2':{
        'nome': 'Oinarfa',
        'sobrenome': 'Anaiv'
    },
    True:{},
    '':{}    
}
"""O primeiro Loop percorre todo o dicionário e exibe a chave dele,
 o segundo loop, percorre o dicionário filho e exibe índice e chave dos itens!!!"""
for cliente_k, cliente_v in clientes.items():
    print(f'{cliente_k, } {len(cliente_k) if type(cliente_k)==str else ""} {type(cliente_k)}')
    for valor_k, valor_v in cliente_v.items():
        print(f'\t{valor_k} = {valor_v}')