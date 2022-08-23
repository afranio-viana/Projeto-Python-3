cpf1='16899535009'
cpf2=''
if len(cpf1)<=11:
    cpf2=cpf1[:-2]
    cont=10
    acum=0
    for digito in cpf2:
        acum+=(cont*int(digito))
        cont-=1
    digifim=(11-(acum%11))
    if digifim>9:
        cpf2+='0'
    else:
        cpf2+=str(digifim)
    cont=11
    acum=0
    for digito in cpf2:
        acum+=(cont*int(digito))
        cont-=1
    digifim=(11-(acum%11))
    if digifim>9:
        cpf2+='0'
    else:
        cpf2+=str(digifim)    
    
    if cpf2==cpf1:
        print('Válido')
    else:
        print('Inválido')