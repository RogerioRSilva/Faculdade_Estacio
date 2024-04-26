# estrategia 01

def fatorial_iterativo(n):
    fatorial = 1
    for i in range(1, n+1):
        fatorial *= i

    return fatorial


# estratégia 02

def fatorial_recursivo(n):
    if((n==0) or (n==1)):
        return 1

    return n * fatorial_recursivo(n-1)

numero = 5

print("\n========= Fatorial Iterativo ===========")
print(f'O fatorial do numero {numero} é: {fatorial_iterativo(numero)}')

print("\n========= Fatorial Recursivo ===========")
print(f'O fatorial do numero {numero} é: {fatorial_recursivo(numero)}')