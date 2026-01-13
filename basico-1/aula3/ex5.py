# 5 - Solicite ao usuário um número e, em seguida, utilize um loop for para imprimir a tabuada desse número, indo de 1 a 10.

import os

def titulo():
    print('TABUADA PRONTA!\n')

def numero_da_tabuada():
    numero = int(input('Digite o número da tabuada: '))
    return numero

def tabuada(numero):
    os.system('clear')
    for i in range(0, 11):
        print(f'{i} x {numero} = {i*numero}')

def main():
    os.system('clear')
    titulo()
    numero = numero_da_tabuada()
    tabuada(numero)

if __name__ == '__main__':
    main()