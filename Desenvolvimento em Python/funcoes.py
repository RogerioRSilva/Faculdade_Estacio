# Criando uma função que recebe um parametro e lhe retorna um valor
def encontrar_menor_item(lista):
    minimo = lista[0]
    for item in lista:
        if(item < minimo):
            minimo = item

    return minimo


lista_teste = [2, 10, 3, 1, 4, 5]
menor = encontrar_menor_item(lista_teste)

print(f'O menor item encontrado na lista foi: {menor}')

#================================================================
print()
lista_numeros = [10, 23, 31, 40, 54]

def item_par(n):
    return (n % 2 == 0)

def soma_itens_lista(lista):
    soma = 0
    for item in lista:
        if(item_par(item)):
            soma += item
    return soma

print(f'Lista de Números: {lista_numeros}')
print(f'A soma dos itens da lista é: {soma_itens_lista(lista_numeros)}')