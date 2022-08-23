"""O else pode ser usado para executar algo no final do while"""
a=int(1)
b=int(1)
cont=1
print(a)
print(b)
while(cont<8):
    acum=a+b
    print(acum)
    cont+=1
    a=b
    b=acum
else:
    print('Fim')