"""O F-strings, ou seja, o 'f' antes das aspas, serve para formatar a estrutura dentro do print,
 o mesmo serve para o ':.2f', que serve para reduzir o número de casas após a vírgula"""
nome = 'Afrânio'
idade = 21
altura = 1.70
peso = 97
imc = (peso/(altura**2))

print(f'{nome} tem {idade} anos de idade e seu IMC é: {imc:.2f}')