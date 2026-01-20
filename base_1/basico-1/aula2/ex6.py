#2 - Pergunte ao usuário sua idade e, com base nisso, use uma estrutura if elif else para classificar a idade em categorias de acordo com as seguintes condições:

idade = int(input('Digite para mim sua idade: '))

if idade <= 0:
    print('Ta na barriga da sua mãe?')
elif idade <= 12:
    print('Cria22nça')
elif idade <= 18:
    print('Adolecente')
else:
    print('Adulto')
    