teste = [ 
    {
        'Enunciado': 'Quem descobriu o Brasi?', 'Opcões': ['Cabral', 'Colombo', 'Pedro I', 'Pedro II'], 'resposta': '0'
    },
    {
        'Enunciado': 'Qual destes estados não pertence à região NE?',
        'Opcões': ['PI', 'MA', 'CE', 'SP'],
        'resposta': '3',
    },
    {
        'Enunciado': 'Qual a língua oficial do Brasil?',
        'Opcões': ['Inglês', 'Português', 'Francês', 'Espanhol'],
        'resposta': '1',
    }
]                
            
acerto = 0
erro = 0

for questao in teste:
    print('\n', questao['Enunciado'], '\n')
    
    for indice, alternativa in enumerate(questao['Opcões']):
        print(f'{indice}) {alternativa}')

    chute = input('\nEscolha apenas uma das alternativas: ')

    if chute == questao['resposta']:
        print('\nResposta CERTA!')
        acerto += 1
    else:
        print('\nResposta ERRADA!')
        erro += 1

print(
    f'\nVocê acertou {acerto} questão(ões)\n'
    f'Você errou {erro} questão(ões)'
    )
