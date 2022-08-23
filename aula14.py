"""try serve para tentar um certo bloco de código,
e except serve para mostrar o que deve ser executado, caso apresente erro no try"""
try:
    n1 = int(input('Digite um número: '))
    n2 = int(input('Digite um outro número: '))
    print(f'{n1+n2}')
except:
    print('ERRO, não podemos prosseguir!!!')