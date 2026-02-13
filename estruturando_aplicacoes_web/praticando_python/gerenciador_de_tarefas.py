# Ana precisa de um programa simples para gerenciar suas tarefas diárias. Ela quer poder adicionar, visualizar e remover tarefas de uma lista.

# Crie um programa com um menu interativo que permita ao usuário adicionar, visualizar e remover tarefas. Use uma lista para armazenar as tarefas.

# Exemplo de entrada:

# 1. Adicionar tarefa 
# 2. Visualizar tarefas 
# 3. Remover tarefa 
# 4. Sair
# Escolha uma opção: 1
# Copiar código
# Saída esperada:

# Digite a tarefa: Estudar Python
# Tarefa adicionada!
# Copiar código
# Caso selecione a opção 2 ao adicionar uma tarefa:

# Tarefas:
# 1. Estudar Python
# Copiar código
# Caso selecione a opção 3 com uma tarefa adicionada:

# Digite o número da tarefa a ser removida: 1
# Tarefa 'Estudar Python' removida!
# Copiar código
# Caso selecione a opção 3 sem uma tarefa adicionada:

# Digite o número da tarefa a ser removida: Estudar Python
# Erro: Nenhuma tarefa para remover.
# Copiar código
# Caso selecione a opção 3 com uma opção inválida:

# Escolha uma opção: 3
# Digite o número da tarefa a ser removida: ABC
# Erro: Entrada inválida! Digite um número.
# Copiar código
# Caso selecione nenhuma das opções listadas:

# Escolha uma opção: 5
# Erro: Opção inválida! Escolha uma opção entre 1 e 4.
# Copiar código
# Caso selecione a opção 4:

# Escolha uma opção: 4 
# Saindo do gerenciador de tarefas. Até mais!

import os
import time

tarefas = []

def titulo():
    print('='*25)
    print('Gerenciador de Tarefas!')
    print('='*25)
    print()
    
def opcoes():
    print('1. Adicionar tarefa\n2. Visualizar tarefas\n3. Remover tarefa\n4. Sair')

def volta_main():
    input('\n\n\nDigite enter para voltar')   
    time.sleep(3)
    os.system('clear')
    main()
    
def adiciona_tarefa():
    tarefa = input('Digite a tarefa: ')
    tarefas.append(tarefa)
    print('\n\n\nTarefa Adicionada com Sucesso!')
    volta_main()
    
    
def visualizar_tarefa():
    count = 1
    for i in tarefas:
        print (f'{count}. {i}')
        count += 1
    volta_main()
    
def remover_tarefa():
    visualizar_tarefa()
    deletar = int(input('\n\n\nDigite o número da tarefa que você quer remover: '))
    
    if deletar > len(tarefas) or deletar < 1:
        print('Erro ao deletar a tarefa') 
        input('\n\n\nDigite enter para tentar novamente...')   
        
    tarefas.pop(deletar - 1)
    print('Tarefa Deletada com sucesso!')
    volta_main()
    
def sair():
    print('Saindo do gerenciador de tarefas. Até mais!')
    time.sleep(3)
    
    
def verifica_escolha():
    try:
        opcao = int(input('\n\n\nEscolha uma opção: '))
        
        if opcao < 1 or opcao > 4:
            print('Digite uma opção entre 1 a 4!!!')
            input('\n\n\nDigite enter para tentar novamente...')
        
        if opcao == 1:
            os.system('clear')
            adiciona_tarefa()
        elif opcao == 2:
            os.system('clear')
            visualizar_tarefa()
        elif opcao == 3:
            os.system('clear')
            remover_tarefa()
        else:
            os.system('clear')
            sair_programa()
    
    except ValueError:
        print('Erro', ValueError)
        
def main():
    titulo()
    opcoes()
    verifica_escolha()

if __name__ == '__main__':
    main()
        
