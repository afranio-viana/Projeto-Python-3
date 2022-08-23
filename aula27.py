"""O operador ternário possui uma estrutura bem semelhante ao if."""
idade=input('Qual sua idade? ')

if not idade.isnumeric():
    print('Digite um número!!!')
else:
    idade=int(idade)
    e_de_maior=(idade>=18)
    msg='Pode entrar!!!' if e_de_maior else 'Não pode entrar!!!'
    print(msg)