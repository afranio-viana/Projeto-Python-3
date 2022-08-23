from itertools import count

"""O contador é infinito, seus parâmetros são 'start' para inicio
e 'step' para passo!!!"""
contador= count(start=4,step=5)

lista=['Afrânio', 'Esquerdo', 'Viana']
lista=zip(contador,lista)

print(f'{list(lista)}')