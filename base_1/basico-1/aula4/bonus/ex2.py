#dados
dados = [
  {"nome": "Ana", "idade": 22, "ativo": True},
  {"nome": "Bruno", "idade": 17, "ativo": False},
  {"nome": "Carlos", "idade": 30, "ativo": True},
  {"nome": "Daniela", "idade": 16, "ativo": True}
]

# Filtrar apenas os usuários ativos
print('User Ativos:\n')
for ativos in dados:
    verifica_ativo = ativos['ativo']
    if verifica_ativo == True:
        nome = ativos['nome']
        print(nome)
print('----------------------------\n')
# Considerar apenas usuários maiores de idade (≥ 18 anos)
print('Maiores de idades:\n')
for idade in dados:
    verifica_idade = idade['idade']
    if verifica_idade >= 18:
        nome = idade['nome']
        print(nome)
print('----------------------------\n')
# Retornar apenas os nomes, em ordem alfabética
print('Nomes em ordem alfabética: ')
nomes = []
for nome in dados:
    recebe_nome = nome['nome']
    nomes.append(recebe_nome)
nomes.sort()
print(nomes)
print('----------------------------\n')
# Retornar também a quantidade total de usuários válidos
print('Quantidade total de users:\n')
contador = 0
for quantidade in dados:
    contador +=1
print(contador)