from time import sleep

tarefas = list()
tarefas_excluidas = list()

print(' AGENDA DIÁRIA '.center(50, '='))
print('Lista de Comandos:\n'
      'Listar - [L]\n'
      'Desfazer - [D]\n'
      'Refazer - [R]\n'
      'Sair - [S]')

def listar(comando):
    for compromisso in tarefas:
        print(f'-> {compromisso}')
    if len(tarefas) == 0:
        print('NÃO AÇÃO PARA LISTAR')

def desfazer(comando):
    if not tarefas:
        print(f'NÃO HÁ TAREFAS PARA DESFAZER')
        return
    
    excluido = tarefas.pop()
    for compromisso in tarefas:
        print(f'-> {compromisso}')
    tarefas_excluidas.append(excluido)

def refazer(tarefas_excluidas):
    if not tarefas_excluidas:
        print(f'NÃO HÁ TAREFAS PARA REFAZER')
        return
    
    reinserir = tarefas_excluidas.pop()
    tarefas.append(reinserir)
    for compromisso in tarefas:
        print(f'-> {compromisso}')

        
while True:
    acao = input(str(('\nDigite uma tarefa ou comando: ')))
    if acao in'Ss':
        print(f'Concluindo agenda...') 
        sleep(1.0)
        print(f'Até logo!')
        break
    if acao in 'Ll':
        listar(acao)
    elif acao in 'Dd':
        desfazer(acao)
    elif acao in 'Rr':
        refazer(tarefas_excluidas)
    elif len(acao) > 2:
        tarefas.append(acao)
