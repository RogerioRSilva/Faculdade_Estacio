# Tratamento de exceção de uma entrada numerica

try:
    x = int(input("Digite um numero:"))
except ValueError:
    print("Entre com um numero valido.")


# Tratamento de exceção de uma divisão por zero.

def dividir(x, y):
    try:
        resultado = x / y
        print(f'A resposta é: ', resultado)
    except ZeroDivisionError:
        print("Divisão por zero")

dividir(3, 0)