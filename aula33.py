def cumprimento(saudacao, nome):
    print(f'{saudacao} {nome}!!!')

def soma(n1,n2,n3):
    print(f'{int(n1+n2+n3)}')

def perc(n1,percentual):
    return(n1+((percentual*n1)/100))

def divisivel(n1):
    if (n1%5==0 and n1%3==0):
        return 'FizzBuzz'
    if (n1%5==0):
        return 'buzz'
    if (n1%3==0):
        return 'fizz'
    return n1

cumprimento('Olá', 'Afrânio')
soma(4,2,3)
print(perc(100, 50))
print(divisivel(15))


