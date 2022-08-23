"""A troca de valores de variáveis no Python é semelhante ao desempacotamento de listas!!!"""
x=10
y='Afrânio'
z=True
print(f'X= {x}\nY= {y}\nZ= {z}\n\n\n')

x,y,z=y,z,x
print(f'X= {x}\nY= {y}\nZ= {z}\n\n\n')

idade=int("""40""")
print(type(idade))