"""List Comprehension, podem ser utilizadas para passar
 valores de uma lista para outra!!!"""
l1=[1,3,5,1,2,3,8,9]
exe1=[v for v in l1]
print(f'{exe1}')

"""Os valores podem ser manipulados na área antes do for!!!"""
exe2=[v*8 for v in l1]
print(f'{exe2}')

"""Os if e else podem ser utilizados para especificar 
o que fazer com tipos específicos de valores!!!"""
exe3=[v if v%2==0 else 'não é' for v in l1]
print(exe3)

"""Ou podem ser utilizados para filtrar os valores que irão para a outra lista!!!"""
exe4=[v for v in l1 if v%2==0]
print(exe4)

string='01234567890123456789012345678901234567890123456789012345678901234567890123456789'
"""O i caminha de 10 em 10, a string é fatida de i até i+10,
 por cada i, indo até o final da string"""
list1=[string[i:i+10] for i in range(0,len(string),10)]
print(list1)

"""Usa a função join para transformar a lista em string"""
resultado=".".join(list1)
print(resultado)

a=int(1)

b=f'Valor {a}'
a=2
print(b)
b = f'Valor {a}'
print(b)