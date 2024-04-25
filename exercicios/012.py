preco = float(input('Digite valor do produto: R$'))
desconto = preco * 0.05

print('O produto custa R${:.2f} com desconto fica R${:.2f}'.format(preco, preco - desconto))