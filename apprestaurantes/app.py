import os
import time

restaurantes = [{'nome':'Gabriel', 'comida':'marcos', 'ativo':False},
                {'nome':'Italiana', 'comida':'Pizza', 'ativo':False}]

def exibir_nome_programa():
    print('SABOR EXPRESS\n')

def exibir_opcoes():
    print('1- Cadastrar restaurante')
    print('2- Exibir restaurantes')
    print('3- Ativar/Desativar restaurante')
    print('4- Fechar programa\n')

def sair_sistema():
    print('Finalizando app...')

def opcao_errada():
    input('Opção invalida\nDigite qualquer tecla para voltara para o menu ')
    main()
    
def cadastra_restaurante():
    nome_restaurante = input('Digite o nome do restaurante: ')
    comida = input('Digite a especialidade: ')

    restaurantes.append({
        'nome': nome_restaurante,
        'comida': comida,
        'ativo': False
    })

    print('Restaurante cadastrado com sucesso!')
    input('Pressione ENTER para voltar ao menu ')
    main()

   
def exibir_restaurantes():
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        especialidade = restaurante['comida']
        aberto = restaurante['ativo']

        if aberto:
            status = 'SIM'
        else:
            status = 'NÃO'

        print(f'''
Nome: {nome_restaurante}
Especialidade: {especialidade}
Aberto: {status}
-----------------------
''')

    input('Pressione ENTER para voltar ao menu ')
    main()

def ativar_restaurante():
    # restaurantes_fechados = []
    # for restaurante in restaurantes:
    #     restaurante_abriu = restaurante['ativo']
        
    #     if restaurante_abriu == False:
    #         print(f'{restaurante+1} - {restaurante['nome']}')
    
    # # for i in restaurantes_fechados:
    # #     print(f'1 - {i}')
        
    # restaurante_aberto = int(input('Digite o número do restaurante para abrir ele: '))
    # print('Restaurante aberto com sucesso!')
    # time.sleep(3)
    restaurante_nome = input('Digite o nome do restaurante: ')
    restaurante_encontrado = False
    
    for restaurante in restaurantes:
        if restaurante_nome == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = 'Restaurante aberto com sucesso' if restaurante['ativo'] else 'Restaurante Fechado com Sucesso'
            print(mensagem)
            
    if not restaurante_encontrado:
        print('Restaurante não está cadastrado\n\nTente novamente.')
      
    input('\n\n\nPrecione ENTER para continuar')
    main()

    

def opcao_escolhida():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))

        if opcao_escolhida == 1:
            os.system('clear')
            cadastra_restaurante()
        elif opcao_escolhida == 2:
            os.system('clear')
            exibir_restaurantes()
        elif opcao_escolhida == 3:
            os.system('clear')
            ativar_restaurante()
        elif opcao_escolhida == 4:
            os.system('clear')
            sair_sistema()
        else:
            
            opcao_errada()   
    except:
        opcao_errada()

    
def main():
    os.system('clear')
    exibir_nome_programa()
    exibir_opcoes()
    opcao_escolhida()

if __name__ == '__main__':
    main()