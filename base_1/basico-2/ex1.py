# Bruno gerencia um pequeno comércio e quer saber qual produto teve o melhor desempenho de vendas no mês passado. Ele registrou a quantidade vendida de dois produtos: maçãs e bananas. Agora, ele precisa escrever um programa que identifique e exiba qual deles teve maior venda.

# Crie um programa que receba o número de vendas dos dois produtos e exiba uma mensagem indicando qual deles vendeu mais. Se as quantidades forem iguais, exiba uma mensagem dizendo que houve empate.

maca = int(input('Digite a quantidade de maçâs vendidas: '))
banana = int(input('Digite a quantidade de bananas vendidas: '))
diferenca = maca - banana
print()

if maca > banana:    
    print('Maçã vendeu mais!')
    print(f'Vendendo {diferenca} unidades a mais que a banana')
if banana > maca:
    print('Banana vendeu mais!')
    print(f'Vendendo {abs(diferenca)} unidades a mais que a maçã')
if maca == banana:
    print('Ambas venderam igualemente')
    