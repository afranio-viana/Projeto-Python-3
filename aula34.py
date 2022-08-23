"""*args é usado para a criação de tuplas,
**kwargs são usados para a criação de tuplas com argumentos estabelecidos"""

def funcao(*args,**kwargs):
    print(args)
    nome=kwargs.get('nome')
    if nome is not None:
        print(f'{nome.title()}')



funcao(4,4,5,11,'af',nome='afrânio')