# Crie um dicionário chamado usuario com:

# nome

# idade

# email

# Requisitos:

# Mostre todos os dados usando for + .items()

# Pergunte ao usuário qual campo ele quer alterar

# Atualize o valor escolhido

# Mostre o dicionário atualizad
import os
import time

usuario = {'nome':'Gabriel', 'idade':21, 'email':'gabrielmmarcos7@gmail.com'}

def titulo():
    print('ALTERAR DADOS\n\n')

def listar_dados():
    print('DADOS: \n')
    contador = 0
    for chave, valor in usuario.items():
        contador += 1
        print(f'{contador} - {chave}: {valor}')

def alterar_nome():
    novo_nome = input('Digite um novo nome: ')
    usuario['nome'] = novo_nome
    dados_atualizados()
    
def alterar_idade():
    novo_idade = int(input('Digite uma nova idade: '))
    usuario['idade'] = novo_idade
    dados_atualizados()
    
def alterar_email():
    novo_email = input('Digite um novo email: ')
    usuario['email'] = novo_email
    dados_atualizados()
    
def dados_atualizados():
    print('Dado Atualizado com Sucesso!\nProcessando aguarde...')
    time.sleep(3)
    
    os.system('clear')
    for chave, valor in usuario.items():
        print(f' {chave}: {valor}')
    input('\n\n\nPrecione enter para fechar...')
    
def opcao_escolhida():
    try:
        opcao = int(input('\n\nDigite o número do que você quer alterar: '))
        if opcao == 1:
            os.system('clear')
            alterar_nome()
        elif opcao == 2:
            os.system('clear')
            alterar_idade()
        elif opcao == 3:
            os.system('clear')
            alterar_email()
            
        else:
            os.system('clear')
            print('Erro! Tente novamente em alguns segundos.\nDigite um número de 1 a 3!')
            time.sleep(5)
            main()
    except ValueError:
        os.system('clear')
        print('Erro! Tente novamente em alguns segundos.\nDigite um número de 1 a 3!')
        time.sleep(5)
        main()

def main():
    os.system('clear')
    titulo()
    listar_dados()
    opcao_escolhida()

if __name__ == '__main__':
    main()
    