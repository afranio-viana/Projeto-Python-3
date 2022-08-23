"""O *sequido de uma variável pode ser usado para fazer o desempacotamento de uma lista!!!"""
lista1=list(range(0,16,3))
lista1.append('Afrânio')
lista1.append('a')
print(lista1)
n1,n2,*outros,n3,n5=lista1
print(n1,n2,n3,n5,outros)