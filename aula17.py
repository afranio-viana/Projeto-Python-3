"""O sinais ^,<,>; podem ser usados para formatar strings e números"""
numero = 4
print(f'{numero:u^26}')# o ^ serve para obrigar o objeto a ter um certo número de caracteres e centraliza o número
print(f'{numero:u>26}')#Idem, mas colocar o número a direita
print(f'{numero:u<26}')#Idem, mas colocar o número a esquerda

nome = 'afrânio viana'

print(nome.lower())#transforma a string em minúsculo
print(nome.upper())#transforma a string em maiúsculo
print(nome.title())#transforma a as primeiras letras de cada sub-string em maiúscula