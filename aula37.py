"""As tuplas parecem as listas, mas usam parênteses e não podem ter seus valores alterados,
uma alternativa para isso, é converter a tupla em lista e modificar o valor!!!"""

t1=(1,2,3,'Afrânio',4,5)
print(type(t1),t1)

t1=list(t1)
t1[1]='fhaja'
print(type(t1),t1)

t1=tuple(t1)
print(type(t1),t1)
