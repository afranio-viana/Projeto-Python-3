frase='Python é bom S2!!!'

"""A função split serve para fatiar um string e transformá-la em uma lista,
 de acordo com um separador pré-estabelecido!!!"""
lista1=frase.split(' ')
print(lista1)

"""A função join une os elementos de uma lista, de acordo com um separador!!!"""
lista2='%'.join(lista1)
print(lista2)

"""A função enumerate enumera os valores de uma lista"""
for indice,valor in enumerate(lista1,8):
    print(f'Lista[{indice}] = {valor}')