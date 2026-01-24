# Carlos trabalha em um cartório e precisa validar se um CPF informado pelo cliente tem o formato correto antes de prosseguir com o atendimento. O CPF deve conter exatamente 11 dígitos numéricos. Se a entrada contiver letras ou qualquer outro caractere que não seja um número, o programa deve exibir uma mensagem de erro.

# Crie um programa que peça ao usuário um número de CPF e verifique se ele tem 11 dígitos e contém apenas números.

# Exemplo de entrada:

# Digite seu CPF: 12345678901


cpf = input('Digite o seu CPF (apenas números): ')

count= 0

letter = False

for i in cpf:
    if i != '1' or i != '2' or i != '3' or i != '4' or i != '5' or i != '6' or i != '7' or i != '8' or i != '9' or i != '0':
        letter = True
        break
    count += 1

if letter == True:
    print('Digite apenas números!')
elif count < 11 or count > 11:
    print('O cpf deve ter 11 dígitos!')
else:
    print('Cpf cadastrado!')