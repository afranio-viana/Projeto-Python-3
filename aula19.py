"""No python, o while funciona como na linguagem c"""
while True:
    n1 = input('Digite um número: ')
    n2 = input('Digite outro número: ')
    if((not n1.isnumeric()) or not (n2.isnumeric())):
        print('Não é um número!!!')
        continue #para o laço aqui e passa para o próximo
    if((n1=='0') and (n2=='0')):
        print('Tchau!!!')
        break #para o laço e sai dele