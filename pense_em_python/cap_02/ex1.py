# Pratique o uso do interpretador do Python como uma calculadora:

# O volume de uma esfera com raio r é Fórmula – Volume de uma esfera.. Qual é o volume de uma esfera com raio 5?
pi = 3.14
raio = 5
volume_esfera = 4/3 * pi * raio**3
print(volume_esfera)

# Suponha que o preço de capa de um livro seja R$ 24,95, mas as livrarias recebem um desconto de 40%. O transporte custa R$ 3,00 para o primeiro exemplar e 75 centavos para cada exemplar adicional. Qual é o custo total de atacado para 60 cópias?

custo = 24.95
desconto_livraria = custo - (custo * 40 / 100)
transporte_primeiro = 3
trasnporte_resto = 0.75
pedido = 60

total = desconto_livraria * 60 + transporte_primeiro + trasnporte_resto*59
print(total)

# Se eu sair da minha casa às 6:52 e correr 1 quilômetro a um certo passo (8min15s por quilômetro), então 3 quilômetros a um passo mais rápido (7min12s por quilômetro) e 1 quilômetro no mesmo passo usado em primeiro lugar, que horas chego em casa para o café da manhã?

hora_saida_segundos  = 6 * 3600 + 52 * 60

quilometros_corridos_lento = 2
quilometros_corridos_rapido = 3

passo_lento = 8*60 +15 #segundos
passo_rapido =  7*60 + 12 #segundos


tempo_gasto_passo_lento_segundos = quilometros_corridos_lento * passo_lento
tempo_gasto_passo_rapido_segundos = quilometros_corridos_rapido * passo_rapido

tempo_gasto_total_segundos = tempo_gasto_passo_lento_segundos + tempo_gasto_passo_rapido_segundos

hora_chegada = hora_saida_segundos + tempo_gasto_total_segundos

hora = hora_chegada // 3600
minutos = (hora_chegada % 3600) // 60
print(f'Hora prevista para chegar {hora} : {minutos}')

#hora_chegada = hora_saida + tempo_gasto_minuto resposta final seria 7.29, mas como chegar nesse resultado?




