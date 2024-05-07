import math

angulo = int(input('Digite o angulo: '))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangete = math.tan(math.radians(angulo))
print('O ângulo {} tem o valor {:.2f} do seno, {:.2f} do cosseno e {:.2f } da tangente'.format(angulo, seno, cosseno, tangete))