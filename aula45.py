import sys
cart=[]
total=0


cart.append(('Produto 1', 300))
cart.append(('Produto 2', 20))
cart.append(('Produto 3', 500))


"""Utilizei list comprehension e geradores para ter acesso a tupla cart e 
somei a partir da função sum!!!"""
prod=sum((product[1] for product in cart))

print(f'Total = {prod}')
print(f'{sys.getsizeof(prod)}')
print(f'{type(prod)}')