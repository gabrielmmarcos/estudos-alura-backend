# O clube de atletismo Alura Runners organizou uma corrida e divulgou a lista com a classificação final dos participantes. Mas, um erro foi identificado: um dos nomes está incorreto. O organizador precisa de um programa que permita localizar o nome errado e substituí-lo pelo correto.

# Como você escreveria um programa que solicite o nome errado, o nome correto e atualize a lista exibindo a nova classificação ao final?

# Exemplo de Entrada:

# Digite o nome incorreto: Carlos
# Digite o nome correto: João


ordem_de_chegada =  ['Ana', 'João', 'Pedro']

print('Lista Atual: ', ordem_de_chegada)

while True:
    nome_errado = input('Digite o nome incorreto: ')

    if not nome_errado in ordem_de_chegada:
        print('Esse nome não está na lista!')
    else:
        break

nome_correto = input('Digite o nome correto: ')

count = 0
for nome in ordem_de_chegada:
    if nome == nome_errado:
        ordem_de_chegada.insert(count, nome_correto)
        ordem_de_chegada.remove(nome_errado)
        break
    count += 1

print(f'O nome {nome_errado} for substituído por {nome_correto}')

print(f'Lista atualizada: {ordem_de_chegada}')