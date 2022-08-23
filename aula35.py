def func2():
    valor = 'afânio'
    return valor

def func1(args):
    return args

print(func1(func2()).upper())

"""Uma das principais funções dos *args e **kwargs, é justamente repassar valores de funções,
podendo servir para fazer uma função executar outra!!!"""

def func3(func, *args, **kwargs):
    return func(*args,**kwargs)

def oi(nome):
    return f'Oi {nome}!'

def saudacao(nome,saudacao):
    return f'{saudacao} {nome}!!!'

print(func3(oi,'afânio').title())

print(func3(saudacao,'afrânio','hi').title())