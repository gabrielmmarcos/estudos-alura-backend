palavra = input('Digite uma palavra: ')

verifica_palavra = ''

for i in range(len(palavra) -1, -1, -1):
    verifica_palavra += palavra[i]
    
if palavra.lower().strip() == verifica_palavra.lower().strip():
    print('É um palindromo')
else:
    print('Não é um plaindromo')