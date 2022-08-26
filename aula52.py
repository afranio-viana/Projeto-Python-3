from dados import produtos,pessoas,lista

"""A função filter serve para realizar a filtragem!!!"""

"""Filtragem sendo realizada com list comprehension!!!"""
nova_lista2=[x for x in lista if x>8]
print(f'{nova_lista2}')


"""Filtragem sendo realizada com filter!!!"""
nova_lista= filter(lambda x: x>5, lista)
print(f'{list(nova_lista)}')

"""Utilizando a função filter para filtrar um dicionário!!!"""
filtro_produtos=filter(lambda p: p['preco']<=10 , produtos)
for produto in filtro_produtos:
    print(f'{produto}')

