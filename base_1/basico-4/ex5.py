# Carlos trabalha em um comércio e precisa saber o valor total de vendas realizadas no dia. As vendas são informadas em uma única linha separadas por espaços.

# Sua tarefa é criar um programa que receba essa linha, converta os valores para números e exiba o total.

# Exemplo de entrada:


# Digite os valores das vendas: 100 250 300 

vendas = input('Digite os valores das vendas: ')

def converte_soma(vendas):
    lista = vendas.split(" ")
    convertido_int = []
    for valor in lista:
        convertido_int.append(int(valor))
    
    total = 0
    
    for valor in convertido_int:
        total +=valor
    return total

print(f'O total de vendas foi: {converte_soma(vendas)}')

