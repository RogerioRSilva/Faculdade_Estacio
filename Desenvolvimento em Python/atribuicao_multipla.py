# Atribuição Multipla de Variáveis

a, b = 1, 2
print('Antes da Troca')
print(f'O valor das variáveis: a={a}, b={b}')

# primeira forma de efetuar a troca
temp = a
a = b
b = temp
print('Primeira Troca')
print(f'O valor das variáveis: a={a}, b={b}')

# Segunda forma de efetuar a troca
a, b = b, a
print('Segunda Troca')
print(f'O valor das variáveis: a={a}, b={b}')