lista_a=[11,2,3,40,5,6,7]
lista_b=[1,2,3,4]

"""Caminho mais longo:
    Foi feito usando append e interadores"""
lista_c=zip(lista_a,lista_b)
lista_soma=[]
for valor1,valor2 in lista_c:
    lista_soma.append(valor1+valor2)

print(f'{lista_soma}')


"""Caminho mais curto:
    Foi feito usando listcomprehension!!!"""
lista_soma2=[x+y for x,y in zip(lista_a,lista_b)]
print(f'{lista_soma2}')