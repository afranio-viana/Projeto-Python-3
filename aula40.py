perguntas={
    'Pergunta 1':{
        'pergunta': 'Quanto é 5/2?',
        'Opções':{
            '[a]':'4','[b]':'2.5','[c]':'1.5',
        },
        'resposta_certa': 'b',
    },
    'Pergunta 2':{
        'pergunta': 'Quanto é 5*2?',
        'Opções':{
            '[a]':'10','[b]':'9','[c]':'11',
        },
        'resposta_certa':'a',
    },
    'Pergunta 3':{
        'pergunta':'Quanto é 4*4?',
        'Opções':{
            '[a]':'24','[b]':'26','[c]':'16',
        },
        'resposta_certa':'c',
    },
}

respostas_certas=0

for pergunta_k, pergunta_v in perguntas.items():
    print(f'{pergunta_k}\n\t{pergunta_v["pergunta"]}')

    for opcoes_k, opcoes_v in pergunta_v["Opções"].items():
        print(f'\t\t{opcoes_k}:{opcoes_v}')
    
    resposta_user=input('Escolha uma opção:')
    
    if (resposta_user==pergunta_v["resposta_certa"]):
        print("Parabéns, você acertou!!!!")
        respostas_certas+=1
    else:
        print("Você errou!")

print(f'Repostas certas: {(respostas_certas*100)/len(perguntas):.1f}%')