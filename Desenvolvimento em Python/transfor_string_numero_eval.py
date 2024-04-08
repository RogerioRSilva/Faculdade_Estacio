# Utilizamos uma função do python chamada eval().
# Essa função recebe uma string e a transforma em valor numérico.

# EXEMPLO:

s = '10'
print(f'Variável: {s} - Tipo string: {type(s)}')

print(f'Tranformando em numero: {eval(s)} - Tipo Numérico: {type(eval(s))}')

