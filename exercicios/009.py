tabuada = int(input('Digite a tabuada que deseja saber: '))

for i in range(11):
    resultado = tabuada * i
    print('{} x {} = {}'.format(tabuada, i, resultado))