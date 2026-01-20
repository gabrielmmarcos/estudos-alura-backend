# Você está recebendo uma lista de valores representando os produtos de sua loja virtual e gostaria de calcular a soma total desses produtos para entender o desempenho financeiro semanal.

# valores = [10, 20, 30, 40, 50]
# Copiar código
# Crie um programa para implementar a soma.

valores = [10, 20, 30, 40, 50]

soma_total = 0

for valor in valores:
    soma_total += valor
    
print(f'Soma total: {soma_total}')