# Lucas quer criar um jogo de pedra, papel e tesoura para jogar contra o computador. Ele precisa de um programa que permita ao usuário escolher uma opção e depois exiba o resultado da partida.

# Crie um programa que permita ao usuário escolher entre pedra, papel ou tesoura. O computador escolherá aleatoriamente uma opção. O programa deve exibir quem venceu a partida. Lembrando que:

# Pedra ganha de Tesoura (Pedra quebra Tesoura);
# Tesoura ganha de Papel (Tesoura corta Papel);
# Papel ganha de Pedra (Papel cobre Pedra);
# Se ambos escolherem a mesma opção, é um empate.
# Exemplo de entrada:

# Escolha: pedra, papel ou tesoura? papel  
# Copiar código
# Saída esperada:

# Computador escolheu: pedra
# Você venceu!  
# Copiar código
# Caso o computador vença:

# Computador escolheu: tesoura  
# Você perdeu!  
# Copiar código
# Caso o computador escolha a mesma opção que você:

# Computador escolheu: papel 
# Empate!

import random 
import os

def jogada():
    jogada = input('Digite sua jogada (pedra, papel, tesoura): ').strip().lower()
    return jogada


def titulo():
    print('-'*10)
    print('JOKEPON!')
    print('-'*10)

def pedra(jogada_computador):
    print('O computador jogou:', jogada_computador)
    if jogada_computador == 'pedra':
        print('Empate')
    elif jogada_computador == 'tesoura':
        print('Você Ganhou')
    else:
        print('Você Perdeu')

def tesoura(jogada_computador):
    print('O computador jogou:', jogada_computador)
    if jogada_computador == 'pedra':
        print('Você Perdeu')
    elif jogada_computador == 'tesoura':
        print('Empate')
    else:
        print('Você Ganhou')

def papel(jogada_computador):
    print('O computador jogou:', jogada_computador)
    if jogada_computador == 'pedra':
        print('Você Ganhou')
    elif jogada_computador == 'tesoura':
        print('Você Perdeu')
    else:
        print('Empate')


def verifica_jogada(jogada):
    jogada_computador = random.choice(['pedra', 'papel', 'tesoura'])
    if jogada == 'pedra':
        pedra(jogada_computador)
    elif jogada == 'papel':
        papel(jogada_computador)
    elif jogada == 'tesoura':
        tesoura(jogada_computador)
    else:
        print('Digite apenas PEDRA, PAPEL ou TESOURA\n\n\n\n\n')
        input('Digite enter para continuar')


def main():
    titulo()
    jogada_user = jogada()
    os.system('clear')
    verifica_jogada(jogada_user)
    
if __name__ == '__main__':
    main()
    