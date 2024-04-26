km = float(input('Quantos quilometros foram percorridos: '))
dia = int(input('Foi alugado por quantos dias: '))
preco_dia = dia * 60
preco_km = km * 0.15

print('Valor a ser pago será R${}'.format(preco_dia + preco_km))