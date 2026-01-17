# Lucas está desenvolvendo um sistema para gerar relatórios financeiros e precisa filtrar apenas os valores pares de uma lista de números informada pelo usuário.

# Crie um programa que receba uma lista de números e exiba apenas os pares usando a função filter().

# Exemplo de entrada:


# Digite os números separados por espaço: 1 2 3 4 5 6 


numeros = input("Digite os números separados por espaço: ")

def converte_numeros(numeros):
    numeros_lista = numeros.split(" ")   
    numeros_convertidos = []
    for numero in numeros_lista:
        numeros_convertidos.append(int(numero))
    return numeros_convertidos

def pares(numero):
    if numero % 2 == 0:
        return numero
    
lista_numeros = converte_numeros(numeros)

numeros_corretos = filter(pares, lista_numeros)
print('Numeros pares:')
for numero in numeros_corretos:
    print( numero, end=' ')