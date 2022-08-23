"""A função len, conta a quantidade de caracteres em um string, mas serve apenas
para strings"""
nome = input('Digite o seu nome: ')
qtd_caracter= len(nome)

if(qtd_caracter<6):
    print(f'O nome de usuário {nome}, possui {qtd_caracter} caracteres, você precisa de no mínimo 6.')
else:
    print(f'O nome de usuário {nome}, possui {qtd_caracter} caracteres, logo, foi aceito.')
