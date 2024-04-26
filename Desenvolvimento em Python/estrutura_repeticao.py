# Laço for com uma string

nome = input("Digite um nome: ")

# O "for" considera a string como uma lista e a fragmenta em letras.
for letra in nome:
    print(letra)


# Um laço usando qualqer sequencia
nomes = ['Laura', 'Lis', 'Guilherme', 'Enzo', 'Arthur']
for nome in nomes:
    print(nome)


# Usando a instrução "continue" com o for.
for num in range(1, 11):
    if num == 5: # O if faz com que o numero 5 seja pulado
        continue
    else:
        print(num)
print('Laço encerrado')


# Usando a instrução "pass": (Imprimindo todos os numeros impares)
for num in range(1, 11):
    if num % 2 == 0:
        pass # O pass pula para a instrução "else" mesmo a "if" sendo verdadeira.
    else:
        print(num)
print('Laço encerrado')


print(50*"=")
print()

#Utilizando o laço "While"
palavra = input('Entre com uma palavra: \n ')

while palavra != 'sair':
    palavra = input('Digite sair para encerrar o laço: \n')

print('Você digitou sair e agora está fora do laço')


# Utilizando o "break"
while True:
    palavra = input('Entre com uma palavra: \n')
    if palavra == 'sair':
        break
print('Você digitou sair e agora está fora do laço')


# Utilizando laços aninhados
while True:
    print('Você está no primeiro laço.')

    opcao1 = input('Deseja sair dele? Digite SIM para isso. \n')

    if opcao1 == 'SIM':
        break  # este break é do primeiro laço
    else:
        while True:
            print('Você está no segundo laço.')

            opcao2 = input('Deseja sair dele? Digite SIM para isso. \n')
            if opcao2 == 'SIM':
                break  # este break é do segundo laço

        print('Você saiu do segundo laço.')

print('Você saiu do primeiro laço')