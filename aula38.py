"""Os dicionários são muito parecidos com as listas, mas devemos informar o valor e o índice, 
o índice pode ser apenas valores imutáveis, como strings, números e tuplas!!!"""
d1={
    'key1': 9,
    7: 8,
    (1,2,3): 'afr'
}

print(f'{type(d1),d1}')

k= float(input('Digite a chave: '))
v= input('Digite o valor: ')

"""Esse trecho de código verifica se o índice k está cotido no dicionário,
 se sim, exibe o valor, se não, insere o valor v no objeto d1[k]"""
if k not in d1:
    d1[k]= v
    print(f'{d1}')
else:
    print(f'{d1[k]}')