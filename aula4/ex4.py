# 4 - Crie um dicionário e verifique se uma chave específica existe dentro desse dicionário.

dados = {'pessoa': 'gabriel', 'idade':212,'cargo':'vagabundo'}

lista_chaves = list(dados.keys())

for i, chave in enumerate(lista_chaves, start=1):
    print(f'{i} - {chave}')

opcao = int(input())
chave_escolhida = lista_chaves[opcao - 1]

print(chave_escolhida)


