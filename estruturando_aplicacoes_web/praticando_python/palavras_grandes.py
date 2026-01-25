# Sofia é revisora de textos e precisa identificar palavras muito longas em um parágrafo. Textos mais fáceis de ler costumam ter palavras curtas, então ela quer um programa que encontre palavras que tenham mais de 10 letras e as exiba em destaque.

# Crie um programa que receba um texto e exiba todas as palavras que possuem mais de 10 letras. Caso nenhuma palavra longa seja encontrada, o programa deve avisar o usuário.

texto = input('Digite um texto: ')

palavras = []

palavra_atual = []

for letra in texto:
    palavra_atual.append(letra)
    if letra == ' ':
        if len(palavra_atual) > 10:
            print(palavra_atual)
            palavras.append(palavra_atual)
            palavra_atual.pop()

print(palavra_atual)
print(palavras)