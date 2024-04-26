# Desconto usando estrutura de decisão

valor_unitario = 10.00

quantidade_itens = 23

if(quantidade_itens <= 10):
    print(f'Não haverá desconto!')
elif(quantidade_itens > 10 and quantidade_itens <= 20):
    print(f'Vc tem desconto de 10%')
    valor_total = quantidade_itens * valor_unitario
    valor_desconto = valor_total - (valor_total * (10/100))
    print(f'Valor total {valor_total} com desconto de 10%: {valor_desconto}')
else:
    print(f'Vc tem desconto de 20%')
    valor_total = quantidade_itens * valor_unitario
    valor_desconto = valor_total - (valor_total * (20 / 100))
    print(f'Valor total {valor_total} com desconto de 20%: {valor_desconto}')