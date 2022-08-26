from dados import produtos,pessoas,lista

"""Utilizando list comprehension para multiplicar 
todos os valores de uma lista por 2!!!!"""
nova_lista=[x*2 for x in lista]

"""Mesma coisa, mas com map!!!"""
nova_lista2=map(lambda x:x*2, lista)

print(f'{lista}')
print(f'{nova_lista}')
print(f'{list(nova_lista2)}')


def aumenta_preco(p):
    p['preco']=round(p['preco']*0.5,2)
    return p

"""Utilizando map para lidar com dicionários!!!"""
novos_produtos=map(aumenta_preco,produtos)

for produto in produtos:
    print(f'{produto}')
print()
for produto in novos_produtos:
    print(f'{produto}')