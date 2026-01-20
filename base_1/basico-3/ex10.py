# João está desenvolvendo um sistema de cadastro para um site de leitura. Ele precisa garantir que os usuários insiram um nome de usuário e uma senha válidos. As regras são as seguintes:

# O nome de usuário deve ter pelo menos 5 caracteres.
# A senha deve ter pelo menos 8 caracteres.
# João quer que o sistema continue solicitando as informações até que ambas as condições sejam atendidas. Quando o usuário insere dados válidos, o programa deve exibir a mensagem: "Cadastro realizado com sucesso!".

# Crie um programa que implemente essa lógica usando um laço while.

import os

verifica_nome = True
verifica_senha = True

while verifica_nome or verifica_senha:
    os.system('clear')
    nome = input('Digite o seu nome: ')
    senha = input('Digite a sua senha: ')
    
    contador = 0
    
    for caracteres in nome:
        contador += 1

    if contador < 5:
        os.system('clear')
        print('O nome precisa ter 5 caracteres')
        input('Aperte enter para tentar novamente... ')
        verifica_nome = True
        continue
    else:  
        verifica_nome = False
        
    contador_senha = 0
    
    for caracteres in senha:
        contador_senha+=1
    
    if contador_senha < 8:
        os.system('clear')
        print('A senha precisa ter pelo menos 8 caracteres!')
        input('Aperte enter para tentar novamente... ')
        verifica_senha = True
        continue
    else:
        verifica_senha = False
    
print('Acesso Liberado!')
    