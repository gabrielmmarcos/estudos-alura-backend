# Sara está participando de um concurso de escrita, e uma das regras exige que cada palavra de seu texto tenha um limite máximo de caracteres.

# Ajude Sara criando uma função que receba uma palavra e exiba a quantidade de caracteres.

# Exemplo de entrada:


# Digite uma palavra: tecnologia 
# Copiar código
# Saída esperada:


# Essa palavra tem 10 caracteres. 

def caracteres(palavra):
    contador = 0
    for i in palavra:
        contador += 1
    return contador

palavra = input('Digite uma palavra: ')

print(f'Essa palavra tem {caracteres(palavra)} caracteres')