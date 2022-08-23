"""O for in pode ser utilizado com a função range,
 que por padrão é range(start=0, stop, step=1)"""
for n in range(0,100,8):
    print(n)

palavra = 'afranio'
nova_palavra = ''
print(palavra)


"""O for in também pode ser utilizado para iterar sobre strings"""
for letra in palavra:
    if(letra=='i'):
        nova_palavra += letra.upper()
    else:
        nova_palavra += letra

print(nova_palavra)

