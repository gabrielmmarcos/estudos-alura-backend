# 4 - Crie um dicionário e verifique se uma chave específica existe dentro desse dicionário.

dados = {'pessoa': 'gabriel', 'idade':212,'cargo':'vagabundo'}

verifica = input('Digite um valor para ver se tem alguma chave com o mesmo nome:')

lista_chaves = list(dados.keys())

ativador = False

for i in lista_chaves:
    if verifica == i:
        ativador = True
        
if ativador:
    print('A Chave existe!')
else:
    print('Essa chave não existe')
# for i, chave in enumerate(lista_chaves, start=1):
#     print(f'{i} - {chave}')

# opcao = int(input())
# chave_escolhida = lista_chaves[opcao - 1]

# print(chave_escolhida)


