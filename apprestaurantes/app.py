import os
import time
restaurantes = []

def exibir_nome_programa():
    print('SABOR EXPRESS')

def exibir_opcoes():
    print('1- Cadastrar restaurante')
    print('2- Exibir restaurantes')
    print('3- Ativar restaurante')
    print('4- Fechar programa\n')

def sair_sistema():
    print('Finalizando app...')

def opcao_errada():
    input('Opção invalidade\nDigite qualquer tecla para voltara para o menu ')
    main()
    
def cadastra_restaurante():
    nome_restaurante = input('Digite o nome do restaurante: ')
    restaurantes.append(nome_restaurante)
    print('Restaurante Cadastrado com sucesso!')
    time.sleep(3)
    main()
    
def exibir_restaurantes():
    for i in restaurantes:
        print('Nome: ', i)
    input('\n\n\nPressione enter para sair')
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
            print('Escolheu 3')
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