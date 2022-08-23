"""Assim como em outras linguagens, o return pode ser utilizado para
retornar valores em um função!!!"""
def soma(n1,n2):
    return n1+n2

valor1=input('Digite um número: ')
valor2=input('Digite outro número: ')

if  valor1.isnumeric() and valor2.isnumeric():
    print(soma(int(valor1), int(valor2)))
else:
    print('Algum dos valores digitados não é um número!!!')