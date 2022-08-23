"""Os operadores lógico and, or, not são iguais aos do c, mas os operadores in e not in,
são diferentes, o in identifica se há uma certa letra em uma senteça, e o not in faz o inverso"""
n1 = 1
n2 = 3
nome = 'Afranio'

if n1>2 or n1==1:
    print('Aqui')
else:
    print('Aqui2')

if 'a' in nome:
    print(f'Existe a em {nome}')
elif 'A' in nome:
    print(f'Existe A em {nome}')
else:
    print('Não existe')