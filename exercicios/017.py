import math

"""

forma feita sozinha

oposto = int(input('Digite o comprimento do cateto oposto: '))
adjacente = int(input('Digite o comprimento do cateto adjacente: '))
hipotenusa = oposto ** 2 + adjacente ** 2

print('O comprimento da hipotenusa é {}'.format(math.sqrt(hipotenusa)))
"""

#apresentado na aula

co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = math.hypot(co, ca)
print('A hipotenusa vai medir {:.2f}'.format(hi))