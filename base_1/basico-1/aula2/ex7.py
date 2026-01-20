#Solicite um nome de usuário e uma senha e use uma estrutura if else para verificar se o nome de usuário e a senha fornecidos correspondem aos valores esperados determinados por você.

nome = 'gm'
senha = 'milkmilk9'

input_nome=input('Digite o seu nome: ')
input_senha=input('Digite sua senha: ')

if input_nome == nome and input_senha == senha:
    print('Você tem acesso ao sistema!')
else:
    print('Nome ou senha erradas')
    
