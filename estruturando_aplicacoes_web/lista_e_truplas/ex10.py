# Uma escola está organizando os dados dos alunos para criar um relatório resumido. Cada aluno tem seus dados registrados em uma única entrada, incluindo nome, idade e nota final no semestre. Esses dados devem ser exibidos separadamente para cada aluno no formato abaixo:

# Aluno: Nome
# Idade: Idade
# Nota: Nota
# Copiar código
# Ajude a escola a desenvolver um programa que registre as informações dos alunos, organize os dados e exiba um relatório detalhado com as informações separadamente.

# Exemplo de Entrada:

# Digite os dados do aluno no formato Nome, Idade, Nota separados por vírgula: João, 16, 8.5, Maria, 17, 9.2, Pedro, 15, 7.8
# Copiar código
# Saída esperada:

# Aluno: João
# Idade: 16
# Nota: 8.5

# Aluno: Maria
# Idade: 17
# Nota: 9.2

# Aluno: Pedro
# Idade: 15
# Nota: 7.8
# Copiar código


dados_alunos = input('Digite os dados do aluno no formato Nome, Idade, Nota separados por vírgula: ')

alunos = [dado.strip() for dado in dados_alunos.split(',')]

count = 0
for i in range(len(alunos)):
    print(f'Aluno: {alunos[count]}')
    count += 1
    print(f'Idade: {alunos[count]}')
    count += 1
    print(f'Nota: {alunos[count]}')
    count += 1
    if count == len(alunos):
        break