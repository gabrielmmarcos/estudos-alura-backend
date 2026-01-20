# João trabalha como garçom em um restaurante e precisa calcular a gorjeta que os clientes deixam ao pagar a conta. O restaurante sugere uma gorjeta de 10%, mas alguns clientes podem escolher dar mais ou menos.

# Para agilizar o processo, João quer um programa que receba o valor total da conta e a porcentagem de gorjeta desejada e exiba o valor final que o cliente deverá pagar.

# Crie um programa que peça ao usuário o valor da conta e a porcentagem de gorjeta. O programa deve calcular e exibir o valor da gorjeta e o total a ser pago.

def titudo():
    print('-------------------------')
    print('PROGRAMA CALCULA GORJETA!')
    print('-------------------------')
    
def input_conta():
    valor_conta = float(input('Digite o valor da conta: '))
    return valor_conta

def input_gorjeta():
    gorjeta_porcentagem = float(input('Digite a porcentagem da gorjeta: '))
    return gorjeta_porcentagem

def calcula_gorjeta(valor_conta, gorjeta_porcentagem):
    gorjeta_valor = (valor_conta * gorjeta_porcentagem) / 100
    return gorjeta_valor

def total_conta(valor_conta, valor_gorjeta):
    total = valor_conta + valor+gorjeta
    return total

def dados_finais(gorjeta_valor, total):
    print(f'Valor da Gorjeta: R${gorjeta_valor}')
    print(f'Total a pagar: R${total}')

def main():
    titulo()
    conta = input_conta()
    gorjeta = input_gorjeta()
    calcula_gorjeta = calcula_gorjeta(conta, gorjeta)
    total = total_conta (conta, calcula_gorjeta)
    dados_finais(calcula_gorjeta, total)
    
if __name__ == '__main__':
    main()
    
    
    



