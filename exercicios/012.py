preco = float(input('Digite valor do produto: R$'))
desconto = preco - (preco * 5 / 100)

print('O produto custa R${:.2f} com desconto fica R${:.2f}'.format(preco, desconto))