from itertools import zip_longest

cidades=["Manaus", "Belém", "Rio Branco", "Palmas"]
estados=["AM", "PA", "AC"]

"""Ao utilizar o zip para fazer a união, ela será feita até o tamanho da menor lista!!!"""
estados_cidades=zip(estados,cidades)
print(f'{list(estados_cidades)}')


"""Aou utilizar zip_longest para fazer a união de listas de tamanhos diferentes,
será completado com 'None' quando a menor lista for ultrapassada"""
estados_cidades2=zip_longest(estados,cidades)
print(f'{list(estados_cidades2)}')


"""fillvalue serve para falar o valor padrão
 que vai completar listas de tamanhos diferentes!!!"""
estados_cidades3=zip_longest(estados,cidades,fillvalue="TO")
print(f'{list(estados_cidades3)}')



