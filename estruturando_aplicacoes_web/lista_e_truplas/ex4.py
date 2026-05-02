# Armano trabalha com a gestão de dois estoques de mercadorias que são representados como tuplas. Agora, ele precisa criar um relatório unificado com os produtos dos dois estoques juntos.

# Para ajudá-lo, como você criaria um programa que ler as informações dos estoques e gera um relatório com todos os produtos juntos?

# Exemplo de Entrada:

# Produtos do estoque 1 (separados por vírgula): Arroz, Feijão, Macarrão
# Produtos do estoque 2 (separados por vírgula): Óleo, Sal, Açúcar
# Copiar código
# Saída esperada:

# Estoque combinado:
# ('Arroz', 'Feijão', 'Macarrão', 'Óleo', 'Sal', 'Açúcar')

# listas dos estoques
first_stock = []
second_stock = []

# funcao para adicionar item na lista
def add_item_in_stock(items, stock):
    add_stock = ''
    for i in items:
        add_stock += i 
        if i == ',':
            add_stock = add_stock.replace(',', '')
            if stock == 1:
                first_stock.append(add_stock)
                add_stock = ''
                continue
            else: 
                second_stock.append(add_stock)
                add_stock = ''
                continue

    if not len(add_stock) == 0:
        add_stock = add_stock.replace(',', '')
        if stock == 1:
            first_stock.append(add_stock)
        else: 
            second_stock.append(add_stock)

    

# input para pegar os items
first = input('Produtos do estoque 1 (separados por vírgula): ').strip().replace(' ', '')
# chama funcao 
add_item_in_stock(first, 1)
# segundo input
second = input('Produtos do estoque 2 (separados por vírgula): ').strip().replace(' ', '')
# chama a funcao novamente
add_item_in_stock(second, 2)
# converte para tuplas
first_stock_tuple = tuple(first_stock)
second_stock_tuple = tuple(second_stock)
# concatena as tuplas
stock_together = first_stock_tuple + second_stock_tuple
# printa
print('Estoque Combinado: \n', stock_together)