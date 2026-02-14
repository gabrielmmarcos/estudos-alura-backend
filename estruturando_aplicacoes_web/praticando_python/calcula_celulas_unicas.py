# Um banco está desenvolvendo um sistema para caixas eletrônicos e precisa de um programa que simule o saque de dinheiro. O caixa deve entregar o valor solicitado pelo usuário usando a menor quantidade possível de cédulas. As cédulas disponíveis são: R$ 100, R$ 50, R$ 20, R$ 10, R$ 5 e R$ 2.

# Crie um programa que solicite ao usuário o valor do saque e calcule quantas cédulas de cada tipo serão necessárias para entregar o valor. O programa deve garantir que o valor solicitado seja válido (múltiplo de 2, já que não há cédulas de R$ 1) e tratar erros de entrada caso não seja digitado um valor numérico válido.

import os

notas_disponiveis = {'100' : 0, '50' : 0, '20' : 0, '10' : 0, '5' : 0, '2' : 0 }

valor_saque = int(input('Digite o valor do saque: R$ '))

if valor_saque % 2 != 0:
    print('Digite um múltiplo de 2, pois não temos cédulas de R$ 1 no momento')
elif valor_saque == 0:
    print('Não foi possível fazer o saque! Digite um número maior que 0')
else:    
    while valor_saque > 0:
        if valor_saque / 100 >= 1 :
            notas_disponiveis['100'] += 1
            valor_saque -= 100
            pass
        elif valor_saque / 50 >= 1:
            notas_disponiveis['50'] += 1
            valor_saque -= 50
            pass
        elif valor_saque / 20 >= 1:
            notas_disponiveis['20'] += 1
            valor_saque -= 20
            pass
        elif valor_saque / 10 >= 1:
            notas_disponiveis['10'] += 1
            valor_saque -= 10
            pass
        elif valor_saque / 5 >= 1:
            notas_disponiveis['5'] += 1
            valor_saque -= 5
            pass
        elif valor_saque / 2 >= 1:
            notas_disponiveis['2'] += 1
            valor_saque -= 2
            pass

    os.system('clear')

    print('Cédulas entregues:\n')

    for nota, quantidade in notas_disponiveis.items():
        if quantidade > 0:
            print(f'{quantidade} de R$ {nota}')
        