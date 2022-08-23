"""Acha o primeiro valor duplicado e o retorna, se não ocorrer, retorna -1"""
def duplicados(lista2):
    numero_duplicado=-1
    conjunto=set()
    for numero in lista2:
        if(numero in conjunto):
            numero_duplicado=numero
            break
        else:
            conjunto.add(numero)
    return numero_duplicado

lista=[1,2,3,4,5,6,7,8,9,10]

print(f'{duplicados(lista)}')