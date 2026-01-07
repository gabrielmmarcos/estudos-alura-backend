# 3 - Utilize um loop for para calcular a soma dos números ímpares de 1 a 10.

soma_impares = 0

for i in range(0, 11):
    if i % 2 != 0:
        soma_impares = i + soma_impares
        
    
print(soma_impares)
