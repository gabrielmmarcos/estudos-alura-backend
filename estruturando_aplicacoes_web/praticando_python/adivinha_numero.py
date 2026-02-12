# Maria está criando um jogo para seus alunos praticarem lógica e pensamento rápido. Ela quer um programa onde o computador escolhe um número aleatório entre 1 e 100, e o jogador tem que adivinhar qual é.

# Além de garantir a jogabilidade, Maria deseja que o programa trate erros de entrada, impedindo que o usuário forneça valores inválidos, como letras ou números fora do intervalo permitido.

# Sua tarefa é criar um programa que gere um número aleatório entre 1 e 100 e permita que o usuário tente adivinhar o número. O programa deve informar se o palpite é maior ou menor que o número correto, até que o usuário acerte. Se o usuário digitar um valor inválido ou um número fora do intervalo, uma exceção ValueError deve ser lançada .

import random
import os

tentativas = []
numero = random.randrange(1, 100)

while True:
    escolha = int(input('Tente adivinhar o número (1-100): '))
    os.system('clear')
    try:
        if escolha > 100 or escolha < 1:
            print('Escolha um número entre 1 e 100')
            input('Digite enter para tentar novamente...')
            os.system('clear')
            pass
        elif escolha == numero:
            print('Parabéns você ganhou! O número escolhido era: ', numero)
            print('Total de tentativas: ', len(tentativas)+1)
            print('Números chutados: ', tentativas)
            break
        elif escolha > numero:
            print('Muito alto, tente novamente ')
            input('Digite enter para tentar novamente...')
            tentativas.append(escolha)
            os.system('clear')
            pass
        elif escolha < numero:
            print('Muito baixo, tente novamte')
            input('Digite enter para tentar novamente...')
            tentativas.append(escolha)
            os.system('clear')
            pass
    except:
        print('Entrada Inválida, Digite um número!')
        input('Digite enter para tentar novamente...')
        os.system('clear')
        pass
    


