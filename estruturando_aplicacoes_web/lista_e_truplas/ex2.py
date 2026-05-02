# Uma escola realizou um concurso de redação, e o próximo passo é organizar as notas dos participantes para definir a ordem de premiação. Para garantir transparência, as notas precisam ser classificadas em ordem crescente, do menor para o maior valor.

# Com base nisso, desenvolva um programa que receba como entrada uma lista contendo as notas de todos os participantes e exiba, ao final, essa lista ordenada em ordem crescente.

# Exemplo de Entrada:

# Notas: [85, 70, 90, 60, 75]

# Saída esperada:

# Notas ordenadas: [60, 70, 75, 85, 90]


notas = [85, 70, 90, 60, 75]

notas_ordenadas = sorted(notas)

print(notas_ordenadas)

#fazendo essa porra na mao

notas_ordenadas_mao = []

for i in range(0, len(notas) - 1):
    if notas[i]< notas[i + 1]:
        notas_ordenadas.insert(notas[i], notas[i + 1])
        continue
    notas_ordenadas_mao.append(notas[i])
print(notas_ordenadas_mao)