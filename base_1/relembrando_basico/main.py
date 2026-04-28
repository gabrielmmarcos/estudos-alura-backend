##1 verifica par
def verifica_par(number):
    if number % 2 == 0:
        return True
    else:
        return False
    
numero = int(input('Digite um número: '))

if verifica_par(numero):
    print('Par!')
else:
    print('Ímpar!')
