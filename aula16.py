try:
    numero = int(input('Digite um número inteiro:'))
    if(numero%2==0):
        print(f'O número é par!')
    else:
        print(f'O número é ímpar!')
except:
    print(f'O "número" digitado não é inteiro!')

try: 
    hora= int(input('Digite o horário: '))
    if(hora>=0 and hora<=11):
        print(f'Bom dia!')
    elif(hora>=12 and hora<=17):
        print(f'Boa tarde!')
    elif(hora>=18 and hora<=23):
        printf(f'Boa noite!')
    else: 
        print(f'Número fora do escopo!')
except:
    print(f'O "número" digitado não é inteiro!')

nome = input('Digite seu nome: ')
qtd_caracter = len(nome)
if(qtd_caracter<=4):
    print(f'O seu nome é curto!')
elif(qtd_caracter>=5 and qtd_caracter<=6):
    print(f'O seu nome é normal!')
else:
    print(f'O seu nome é muito grande!')
