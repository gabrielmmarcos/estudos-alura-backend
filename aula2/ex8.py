#4 - Solicite ao usuário as coordenadas (x, y) de um ponto qualquer e utilize uma estrutura if elif else para determinar em qual quadrante do plano cartesiano o ponto se encontra de acordo com as seguintes condições:

x = float(input('Digite o valor do eixo x: '))
y = float(input('Digite o valor do eixo y: '))

if x > 0 and y > 0:
    print('Esse eixo esta no PRIMEIRO quadrante')
elif x < 0 and y > 0:
    print('Esse eixo esta no SEGUNDO quadrante')
elif x > 0 and y < 0:
    print('Esse eixo esta no TERCEIRO quadrante')
elif x < 0 and y < 0:
    print('Esse eixo esta no QUARTO quadrante')
else:
    print('O ponto está localizado no eixo de origem')
