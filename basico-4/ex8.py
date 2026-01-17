# Joana está participando de um processo seletivo para uma vaga de desenvolvedora e recebeu um desafio técnico de criar uma calculadora para somar, subtrair, multiplicar e dividir dois números.

# Sua tarefa é criar um programa usando funções lambda que receba dois números e um operador matemático escolhido pelo usuário (+, -, * ou /) e exiba o resultado correspondente.

# Exemplo de entrada:


# Digite o primeiro número: 10   
# Digite o segundo número: 5   
# Escolha a operação (| + | - | * | / |): + 


soma = lambda a, b: a + b
subtracao = lambda a, b: a - b
multiplicacao = lambda a, b: a * b
divisao = lambda a, b: a / b

numero_1 = int(input('Digite o primeiro número: '))
numero_2 = int(input('Digite o segundo número: '))
operador = input('Escolha a operação (| + | - | * | / |): ')

if operador == '+':
    print(soma(numero_1, numero_2))
elif operador == '-':
    print(subtracao(numero_1, numero_2))
elif operador == '*':
    print(multiplicacao(numero_1, numero_2))
elif operador == '/':
    print(divisao(numero_1, numero_2))
else:
    print('Operador inválido')
