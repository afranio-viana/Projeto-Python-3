"""Range pode ser utilizado para inserir valores na lista"""
lista= list(range(0,100,8))
print(lista)

"""Uma lista consegue receber vários tipos de valores!!!
O append serve para adicionar valores no final da lista"""
lista.append('Ralph')
print(lista)

"""A função insert serve para inserir valores em qualquer parte da lista,
 desde que você coloque o índice"""
lista.insert(3, True)
print(lista)

"""A função pop elimina o último valor da lista"""
lista.append(78)
print(lista)
lista.pop()
print(lista)

"""A função del elimina qualquer valor de uma lista, desde que tenhamos o índice!!!"""
del(lista[9])
print(lista)

"""A função extende serve para juntar duas listas ou inserir um valor no final de uma lista"""
lista2=list(range(0,11,2))
print(lista2)
lista2.extend(lista)
print(lista2)

for valor in lista:
    print(f'O elemento{valor} é {type(valor)}')