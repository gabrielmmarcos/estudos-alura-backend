# Camila está organizando um projeto e precisa calcular o tempo total necessário para concluir três atividades: A, B e C. No entanto, se alguma atividade tiver um número de dias negativo, o código deve avisar que os valores inseridos são inválidos e não calcular o total.

# Escreva um programa que receba o número de dias de três atividades e exiba o tempo total do projeto. Se algum valor for negativo, mostre uma mensagem informando o erro.
a = int(input('Digite o tempo para fazer na atividade A: '))
b = int(input('Digite o tempo para fazer na atividade B: '))
c = int(input('Digite o tempo para fazer na atividade C: '))

if a < 0 or b <0 or c < 0:
    print('Não pode ter número negativo')
else:
    print('O total de tempo foi: ', a+b+c)
