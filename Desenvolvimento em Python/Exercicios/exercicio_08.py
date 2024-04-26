# Somando os pares de uma lista

lista = [10, 2, 5, 7, 6, 3]
soma = 0

print(f'Lista de numeros: {lista}')

for c in range(len(lista)):
    if (lista[c] % 2 == 0):
        soma += lista[c]
        print(f'O numero {lista[c]} é par!')

print(f'A soma dos numeros da lista é: {soma}')

print(50*'=')
print()

# Outra forma de resolver esse problema
soma2 = 0
for num in lista:
    if (num % 2 == 0):
        soma2 += num
        print(f'O numero {num} é par!')

print(f'Usando outra forma de soma dos numeros da lista: {soma2}')