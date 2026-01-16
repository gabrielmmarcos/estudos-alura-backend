# Julia é professora e precisa de um programa para ajudar seus alunos a calcularem suas idades com base no ano de nascimento. Sua tarefa é criar uma função que receba o ano de nascimento e o ano atual e retorne à idade correspondente.

# Exemplo de entrada:


# Digite o ano de nascimento: 2005  

# Digite o ano atual: 2025 
# Copiar código
# Saída esperada:


# A idade é 20 anos. 

def calcula_idade(nascimento, atual):
    idade = atual - nascimento
    return idade

ano_nascimento = int(input('Digite o ano que você nasceu: '))
ano_atual = int(input('Digite o ano atual: '))

print(f'Sua idade é : {calcula_idade(ano_nascimento, ano_atual)}')