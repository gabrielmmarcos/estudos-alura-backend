# 7 - Construa um código que calcule a média dos valores em uma lista. Utilize um bloco try-except para lidar com a divisão por zero, caso a lista esteja vazia.


notas = [10, 50, 10, 10]

soma_notas = 0
contador = 0

for nota in notas:
    contador += 1
    soma_notas += nota
    
try:
    total = contador
    media = soma_notas / total
    print(media)
except ZeroDivisionError:
    print('A lista esta vazia')
    



