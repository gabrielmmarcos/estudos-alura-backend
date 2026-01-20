# Uma professora precisa de um programa que ajude a calcular a média final dos alunos e informe se foram aprovados, ficaram de recuperação ou reprovados. As regras são:

# Média >= 7: Aprovado
# 5 <= Média < 7: Recuperação
# Média < 5: Reprovado
# Escreva um programa que receba três notas como entrada e calcule a média final. Com base na média, exiba a situação do aluno.

nota_1 = float(input('Digite o valor da primeira nota: '))
nota_2 = float(input('Digite o valor da segunda nota: '))
nota_3 = float(input('Digite o valor da terceira nota: '))

media = (nota_1 + nota_2 + nota_3) /3

if media >= 7:
    print('Aprovado')
elif media >=5:
    print('Recuperação')
else:
    print('Reprovado')