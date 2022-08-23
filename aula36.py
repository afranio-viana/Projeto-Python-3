lista= [
    ['P1',14],
    ['P2',3],
    ['P3',1],
    ['P4',33],
    ['P5',22]
]
"""As expressões lambda são utilizadas para substituir funções muito pequenas!!!
Nessa expressão, a lista[[0][1],[0][1],[0][1],[0][1],[0][1]]
 é recebida e ordena com a função sort, a partir do item i[1] 
 de um objeto iterável, no caso, a lista"""
print(sorted(lista,key=lambda i:i[0],reverse=True))