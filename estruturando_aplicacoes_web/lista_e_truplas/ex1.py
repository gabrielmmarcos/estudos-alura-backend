# Roberto está organizando sua despensa e quer verificar se determinados itens já estão armazenados antes de adicioná-los à lista de compras.

# Ajude Roberto a criar um programa que pergunte o item desejado e verifique se ele está na lista de itens disponíveis na despensa. Caso o item não esteja na lista, o programa deve informar que ele precisa ser comprado.

# Exemplo de Entrada:

# Digite o item que você quer verificar: açúcar
# Copiar código
# Saída esperada:

# O item açúcar precisa ser comprado.


despensa = ['arroz', 'feijão', 'açúcar', 'refrigerante', 'pastel']

item_selecionado = input('Digite o item que vc quer verificar: ')
def verifica_item(item_selecionado):
    for item in despensa:
        if item_selecionado == item:
            return False 
    return True


if not verifica_item(item_selecionado):
    print(f'Não precisa comprar, já temos {item_selecionado} na dispensa!')
else: 
    print(f'O {item_selecionado} precisa ser comprado!')

