# LISTA SEQUENCIAL

'''
Listas possuem posições (index) predefinidos que sempre começa em 0.
De form inversa temos as posições negativas onde ultimo item da lista
será o -1.
'''

lista = [101, 202, 303, 404, 505]

print(f'lista na posição [0] = {lista[0]}')
print(f'lista na posição [1] = {lista[1]}')
print(f'lista na posição [2] = {lista[2]}')
print(f'lista na posição [3] = {lista[3]}')
print(f'lista na posição [4] = {lista[4]}')
print(f'Lista completa: {lista}')

print('\n', 50*'#', '\n')
print('    DICIONÁRIO')
print(50*'#', '\n')

'''
Dicionários trabalham com chave valor geralmente separado por : 
ficaria assim:
nome_dicionario = { chave:[valor], chave2:[valor2]}
'''

dicionario = {'nome1':['Rogério'], 'nome2': ['Michele'], 'nome3':['Heloísa']}
print(dicionario)

# Exibição dos dados conforme chave passada
print(f'Mosta o nome1: {dicionario["nome1"]}')
print(f'Mosta o nome3: {dicionario["nome3"]}')
print(f'Mosta o nome2: {dicionario["nome2"]}')

a = ['u'] + ['RN']

print(len(a))

b = ['4'] * 4
print(len(b))