# Pedro está criando um sistema de cadastro de produtos para sua loja e percebeu que todos os números de telefone dos clientes estão armazenados como strings. No entanto, para facilitar buscas e validações, ele precisa que esses números sejam tratados como inteiros.

# Dado o seguinte código com uma lista de números de telefone armazenados incorretamente como str, faça duas funções, uma que converte os tipos para inteiro e outra que verifica se a conversão foi feita corretamente e todos os números de telefone são inteiros:

# Exemplo de entrada:


# telefones = ["11987654321", "21912345678", "31987654321", "11911223344"] 
# Copiar código
# Saida esperada:


# Todos os números foram convertidos corretamente! 
# Copiar código
#  Discutir no Fórum



telefones = ["11987654321", "21912345678", "31987654321", "11911223344"] 

def converter_inteiro(tel):
    telefones_interios = []
    for telefone in tel:
        telefones_interios.append(int(telefone))
    return telefones_interios

def verifica_conversao(tel)    :
    for telefone in tel:
        if type(telefone) != int:
            return print('Não foi convertido corretamente')
            
    return print('Foi convertido corretamente!')
    
lista_inteira = converter_inteiro(telefones)
verifica_conversao(lista_inteira)
    