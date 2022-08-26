from dados import produtos,pessoas,lista
from functools import reduce

"""O reduce funciona como um acumulador, primeiro você passa a função,
depois passa o que ele deve fazer com os itens,
 em seguida você passa a lista e por último diz com quanto ele inicia!!!"""
soma_lista=reduce(lambda ac, i:i+ac, lista, 0)
print(f'{soma_lista}')

soma_idade=reduce(lambda ac,idade: idade['idade']+ac,pessoas,0)
print(f'{soma_idade/len(pessoas)}')