'''
Como exercício prático, tente escrever um programa para calcular e informar o IMC (índice de massa corpórea) do usuário,
que deverá fornecer seu peso e sua altura.
Lembre-se de que o IMC é calculado pela fórmula: IMC = peso dividio pela altura ao quadrado
'''

peso = eval(input('Digite seu peso: '))
altura = eval(input('Digite sua altura: '))

imc = peso/(altura**2)

print(f'Seu IMC é: {imc}')