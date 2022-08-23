"""A diferença de um set para um dicionário, é que o set não precisa da chave, apenas o valor!
Além disso, sets geralmente não respeitam oredem dos elementos do conjunto,
 fora isso, também não aceita itens duplicados!!!"""
conjunto={'a'}

"""Função de atualizar!!!"""
conjunto.update('b')

"""Função para adicionar!!!"""
conjunto.add(4)

conjunto2={5,4,"b"}
print(f'{conjunto}\n{conjunto2}')

"""| realiza a união"""
conjunto3=conjunto2|conjunto
print(f'{conjunto3}')

"""O - pega apenas os elementos que estão presentes somente no set da esquerda"""
conjunto3=conjunto2-conjunto
print(f'{conjunto3}')

"""O & pega a interseção dos conjuntos"""
conjunto3=conjunto2&conjunto
print(f'{conjunto3}')

"""Pega os elementos que estão nos dois sets, mas não em ambos!"""
conjunto3=conjunto2^conjunto
print(f'{conjunto3}')