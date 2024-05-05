import math

oposto = int(input('Digite o comprimento do cateto oposto: '))
adjacente = int(input('Digite o comprimento do cateto adjacente: '))
hipotenusa = oposto ** 2 + adjacente ** 2

print('O comprimento da hipotenusa é {}'.format(math.sqrt(hipotenusa)))

