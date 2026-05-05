# Ana está organizando uma festa de aniversário e precisa de uma lista de convidados que não tenha repetições , pois algumas pessoas foram convidadas mais de uma vez por engano. Ela gostaria que o programa solicitasse o nome dos convidados e, ao final, exibisse a lista organizada sem repetições.

# Escreva um programa que receba os nomes dos convidados até que o usuário digite 'sair', e ao final mostre a lista de convidados sem repetições.

# Exemplo de entrada:


# Digite o nome do convidado: Ana 

# Digite o nome do convidado: João 

# Digite o nome do convidado: Ana 

# Digite o nome do convidado: Carla 

# Digite o nome do convidado: sair 
# Copiar código
# Saída esperada:


# Convidados confirmados: Ana, João, Carla 

candidatos = {1:'gabriel'}
nomes = []

key = 0

while True:

    candidato = input('Digite o nome do canditado ou sair para encerrar: ')
    if candidato == "sair":
        break
    
    nomes.append(candidato)

    for nome in nomes:
        print(nome)
        if candidato == nome:
            continue
        key += 1
        candidatos[key] = candidato

print('Convidados confirmados: ')
for key, value in candidatos.items():
    print(key, value, end=', ')