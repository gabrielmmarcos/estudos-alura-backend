# Camila adora receber amigos para jantares temáticos. Para o próximo encontro, ela quer garantir que a ordem de chegada seja respeitada, mas ainda precisa fazer ajustes na lista de convidados. Camila quer adicionar novos nomes e organizá-los em posições específicas.

# Como você criaria um programa que mostre a lista inicial, permita a inserção de um novo nome em uma posição escolhida e exiba a lista atualizada?

# Exemplo de Entrada:

# Lista atual de convidados: ['Ana', 'Pedro', 'Carlos']
# Digite o nome do novo convidado: João
# Digite a posição na qual deseja inserir o convidado: 2


convidados = ['Ana', 'Pedro', 'Carlos']
print('Lista de convidados: ',convidados)

while True:
    convidado = input('Digite o nome do novo convidado (ou sair para encerrar): ').strip()
    if convidado == 'sair':
        break
    posicao = int(input('Digite a posição na qual deseja inserir o convidado: ')) - 1
    convidados.insert(posicao, convidado)
    print('Lista atual: ', convidados)

