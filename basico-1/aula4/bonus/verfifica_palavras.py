frase = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.'
blank = ' '
contador = 1

for letra in frase:
    if letra == blank:
        contador+=1
        
print(f'A frase tem {contador} palavras ')

