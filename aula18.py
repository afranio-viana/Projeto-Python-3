"""No caso de strings, os : podem servir para auxiliar no processo de fatiamento """

palavra = 'Python_S2'
qtd=len(palavra)
print(palavra)
print(palavra[0:6])#Um intervalo com início fechado e final aberto

print(palavra[0::2])#Um intervalo fechado que começa em zer e salteia de 2 em 2.
