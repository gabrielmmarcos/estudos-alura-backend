import os
#Calculadora basica
def erro():
    input('Houve um erro, digite enter para tentar novamente!')
    main()

def operador():
    valid_operations = ['+', '-', '*', "/"]
    choice = input('Escolha uma operação: ("+", "-", "*", "/"): ')

    if len(choice) > 1:
        erro()

    if choice in valid_operations:
        return choice
    else:
        erro()

def calculadora (number1, number2, operation):
    if operation == '+':
        return number1 + number2
    elif operation == '-':
        return number1 - number2
    elif operation == '*':
        return number1 * number2
    elif operation == '/':
        if number2 == 0:
            erro()
        return number1 / number2
    
def get_number():
    number = int(input('Digite um número: '))
    return number

def main():
    print('Calculadora')
    print('\n')
    #pega numero 
    number_1 = get_number()
    os.system('cls')
    #pega operacao
    operacao = operador()
    os.system('cls')
    #pega numero
    number_2 = get_number()
    os.system('cls')

    result = calculadora(number_1, number_2, operacao)

    print('Resultado: ', result)

if __name__ == '__main__':
    main()