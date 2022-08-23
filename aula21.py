"""O while pode ser usado para iterar strings!"""

frase = 'O rato roeu a roupa do rei de roma'
cont = int(0)
nova_frase=''
while cont<len(frase):
    nova_frase+=frase[cont]
    print(nova_frase)
    cont+=1