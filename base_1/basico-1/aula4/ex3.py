# 3 - Crie um dicionário que relacione os números de 1 a 5 aos seus respectivos quadrados.

numero_e_quadrado ={'numero':1, 'quadrado':1}

for i in range(1,6):
    quadrado = i*i
    numero_e_quadrado.update({
            'numero':i, 'quadrado':quadrado
         }
        )
    print(numero_e_quadrado)
    


