# Beatriz está desenvolvendo um sistema de atendimento para um site de serviços. Ela deseja criar um programa que exiba uma saudação personalizada dependendo da hora do dia que o usuário acessa a plataforma. O sistema deverá ter a seguinte regra:

# Se for antes das 12h, exibir "Bom dia";

# Entre 12h e 18h, exibir "Boa tarde";

# Após 18h, exibir "Boa noite".

# Exemplo de entrada:


# Digite a hora atual (0-23): 15 
# Copiar código
# Saída esperada:


# Boa tarde! 
# Copiar código

def saudacao(horario):
    if horario < 12:
        print('Bom Dia!')
    elif horario <= 18:
        print('Boa Tarde')
    else:
        print('Boa Noite')
        
horas = int(input('Digite as horas(0 - 23): '))

saudacao(horas)