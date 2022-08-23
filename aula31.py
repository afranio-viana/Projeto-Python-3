"""A definição de funções em Python é bem semelhante a em outras linguagens."""
def saudacao(msg='Olá', nome='Usuário'):
    print(f'{msg} {nome.title()}')

"""É possível determinar valores padrões caso não seja enviado nada para a função."""
saudacao()

"""Valores podem ser enviados de forma normal"""
saudacao('Hi', 'Afrânio')

"""Valores 'parciais' podem ser enviados"""
saudacao(nome='Tulipa')
saudacao('Hi')
nome=input('Digite seu nome:')
saudacao(nome=nome)