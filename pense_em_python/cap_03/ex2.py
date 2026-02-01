# Exercício 3.2
# Um objeto de função é um valor que pode ser atribuído a uma variável ou passado como argumento. Por exemplo, do_twice é uma função que toma um objeto de função como argumento e o chama duas vezes:


# def do_twice(f):
#     f()
#     f()
# Aqui está um exemplo que usa do_twice para chamar uma função chamada print_spam duas vezes:


# def print_spam():
#     print('spam')
# do_twice(print_spam)
# Digite este exemplo em um script e teste-o.

def do_twice(f):
    f()
    f()
    
def print_spam():
    print('spam')

do_twice(print_spam)

# Altere do_twice para que receba dois argumentos, um objeto de função e um valor, e chame a função duas vezes, passando o valor como um argumento.

def do_twice_2(f, V):
    f(V)
    f(V)
    
def print_spam_2(a):
    print(a)

do_twice_2(print_spam_2, 'a')

# Copie a definição de print_twice que aparece anteriormente neste capítulo no seu script.

def print_twice(bruce):
    print(bruce)
    print(bruce)


# Use a versão alterada de do_twice para chamar print_twice duas vezes, passando 'spam' como um argumento.
do_twice_2(print_twice, 'spam')
# Defina uma função nova chamada do_four que receba um objeto de função e um valor e chame a função quatro vezes, passando o valor como um parâmetro. Deve haver só duas afirmações no corpo desta função, não quatro.

def do_four(objeto, valor):
    do_twice_2(objeto, valor)
    do_twice_2(objeto, valor)
    
    
def print_do_four(text):
    print(text)

do_four(print_do_four, 'text')