# Comentários:

# Podemos utilizar a # para comentar uma linha

'''Podemos utilzar 3 aspas simples poara poder comentar
em várias linhas ao mesmo tempo.
O Comentário não faz parte da execução do código sendo ignorado na compilação.
'''


# Principais execuções:

# Exibição
print(50*'#')
print('Exibição no Terminal')
print(50*'#')
print()

print("Olá Mundo!!!")

print('Usnado numeros diretamente no print: ', 123456789)

'''
As váriaves em python não precisão ser declaradas, 
pois são declaradas em tempo de execução
'''

texto = "Texto da variável"
numero = 1234
numero_fluatuante = 0.74
boleano = True

print('Texto: ', texto, " Números: ", numero, " Números Flutuantes: ", numero_fluatuante,
      " Boleano (True ou False): ", boleano)

# Print Formatado
print(f'Print formatado => Texto: {texto} - Números: {numero} - Números Flutuantes: {numero_fluatuante} - Boleano (True ou False): {boleano}')

print()
print(50*'#')
print('Processamento Aritimético')
print(50*'#','\n')

# Processamento Aritimético
numero1 = 10
numero2 = 20

print("Numeros de entrada - 1º Número:", numero1, " 2º Número: ", numero2)

soma = numero1 + numero2
print("Resultado da soma: ", soma)

subtracao = numero1 - numero2
print("Resultado da Subitração: ", subtracao)

multiplicacao = numero1 * numero2
print("Resultado da Multiplicação: ", multiplicacao)

divisao = numero2 / 2
print("Resultado da Divisão: ", divisao)

resto = 3 % 2
print("Resultado de uma divisão pegando o resto: ", resto)

# Entrada de dados utilizando um input
print()
print(50*'#')
print('Entrada de dados utilizando um input')
print(50*'#','\n')

# Entrada padrão do input é sempre em String (Texto)
nome = input("Digite seu nome: ")
print("O nome digitado foi: ", nome)

# Nesse caso estamos convertendo a entrada para inteiro
numero = int(input("Digite um numero: "))
print(f"O numero digitado foi: {numero}")

# Nesse caso estamos convertendo a entrada para flutuante
valor = float(input('Digite o valor em reais (R$): '))
print(f'O Valor digitado foi: R${valor}')