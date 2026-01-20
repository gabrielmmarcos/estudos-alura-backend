import os

# Dicionário
dados = {
    'nome': 'Gabriel',
    'idade': 21,
    'cidade': 'SP'
}
def titulo():
    print('Te Conhecendo melhor\n\n\n')

def exibir_opcoes():
    print(
        '1- Ver meus dados\n'
        '2- Adicionar Profissão\n'
        '3- Remover item\n'
        '4- Alterar valores\n\n\n'
    )

def ver_dados():
    os.system('clear')
    
    for chave, valor in dados.items():
        print(f'{chave.capitalize()}: {valor}')
    
    print('\n')
    input('Digite enter para voltar para o menu...')
    main()

def adicionar_profissao():
    os.system('clear')
    
    profissao = input('Digite a Profissão: ')
    dados['profissao'] = profissao
    
    print('\nProfissão adicionada com sucesso!\n')
    input('Digite enter para voltar para o menu...')
    main()

def remover_item():
    os.system('clear')
    
    print('Selecione um dado que você quer apagar:\n')
    
    lista_chaves = list(dados.keys())
    
    for i, chave in enumerate(lista_chaves, start=1):
        print(f'{i} - {chave}')
    
    opcao = int(input('\nDigite o número do item: '))
    
    chave_remover = lista_chaves[opcao - 1]
    del dados[chave_remover]
    
    print('\nDado deletado com sucesso!\n')
    input('Digite enter para voltar para o menu...')
    main()

def atualizar_dados():
    os.system('clear')
    
    print('Selecione um dado que você quer atualizar:\n')
    
    lista_chaves = list(dados.keys())
    
    for i, chave in enumerate(lista_chaves, start=1):
        print(f'{i} - {chave}')
    
    opcao = int(input('\nDigite o número do item: '))
    chave_atualizar = lista_chaves[opcao - 1]
    
    novo_valor = input(f'Digite o novo valor para {chave_atualizar}: ')
    
    # Se for idade, converte para int
    if chave_atualizar == 'idade':
        novo_valor = int(novo_valor)
    
    dados[chave_atualizar] = novo_valor
    
    print('\nDado atualizado com sucesso!\n')
    input('Digite enter para voltar para o menu...')
    main()

def opcao_escolhida():
    try:
        opcao = int(input('Digite uma opção: '))
        
        if opcao == 1:
            ver_dados()
        elif opcao == 2:
            adicionar_profissao()
        elif opcao == 3:
            remover_item()
        elif opcao == 4:
            atualizar_dados()
        else:
            print('\nOpção inválida!\n')
            input('Pressione enter para continuar...')
            main()
            
    except ValueError:
        print('\nEntrada inválida! Digite apenas números.\n')
        input('Pressione enter para continuar...')
        main()

def main():
    os.system('clear')
    titulo()
    exibir_opcoes()
    opcao_escolhida()

if __name__ == '__main__':
    main()
