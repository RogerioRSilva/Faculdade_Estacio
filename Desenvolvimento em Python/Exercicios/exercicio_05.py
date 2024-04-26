# Implemente uma solução em python que verifique se um numero é par ou impar.

numero = int(input("Digite um numero: "))

if(numero % 2 == 0):
    print(f'O numero {numero} é par!')
else:
    print(f'O numero {numero} é impar!')


# Outra forma usando um ternário
resultado = f'{numero} é par' if (numero % 2 == 0) else f'{numero} é impar'

print('Usando o ternário: ', resultado)