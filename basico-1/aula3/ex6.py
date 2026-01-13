# 6 - Crie uma lista de números e utilize um loop for para calcular a soma de todos os elementos. Utilize um bloco try-except para lidar com possíveis exceções.

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'i']

soma_elementos = 0
for numero in numeros:
    try:
        soma_elementos+=numero
    except TypeError:
        print(f'valor errado igonaro {numero}')

print(f'Total: {soma_elementos}')