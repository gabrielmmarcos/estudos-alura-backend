# Exercício 3.3
# Nota: Este exercício deve ser feito usando-se apenas as instruções e os outros recursos que aprendemos até agora.

# Escreva uma função que desenhe uma grade como a seguinte:

#         + - - - - + - - - - +
#         |         |         |
#         |         |         |
#         |         |         |
#         |         |         |
#         + - - - - + - - - - +
#         |         |         |
#         |         |         |
#         |         |         |
#         |         |         |
#         + - - - - + - - - - +
# Dica: para exibir mais de um valor em uma linha, podemos usar uma sequência de valores separados por vírgula:


# print('+', '-')
# Por padrão, print avança para a linha seguinte, mas podemos ignorar esse comportamento e inserir um espaço no fim, desta forma:


# print('+', end=' ')
#  print('-')
# A saída dessas instruções é + -. Uma instrução print sem argumento termina a linha atual e vai para a próxima linha.


def aresta():
    print('+', end=' ')

def linha():
    print('- '*4, end='')
    
def coluna():
    print('|' + ' '*9  + '|' + ' '*9  +'|')
    
def coluna_completa(arg):
    arg()
    arg()
    arg()
    arg()

def linha_completa():
    aresta()
    linha()
    aresta()
    linha()
    aresta()
    print()
    

def grid():
    linha_completa()
    coluna_completa(coluna)
    linha_completa()
    coluna_completa(coluna)
    linha_completa()

grid()

# Escreva uma função que desenhe uma grade semelhante com quatro linhas e quatro colunas.
print('\n'*5)

def linha_2():
    print('- '*4, end='')
    
def coluna_2():
    print('|' + ' '*9  + '|' + ' '*9  +'|' + ' '*9  +'|' + ' '*9  +'|')
    
def coluna_completa_2(arg):
    arg()
    arg()
    arg()
    arg()

def linha_completa_2():
    aresta()
    linha_2()
    aresta()
    linha_2()
    aresta()
    linha_2()
    aresta()
    linha_2()
    aresta()
    print()
    

def grid_2():
    linha_completa_2()
    coluna_completa_2(coluna_2)
    linha_completa_2()
    coluna_completa_2(coluna_2)
    linha_completa_2()
    coluna_completa_2(coluna_2)
    linha_completa_2()
    coluna_completa_2(coluna_2)
    linha_completa_2()

grid_2()