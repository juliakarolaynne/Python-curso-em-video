import random

aluno1 = input('Digite o nome do aluno: ')
aluno2 = input('Digite o nome de outro aluno: ')
aluno3 = input('Digite o nome de outro aluno: ')
aluno4 = input('Digite o nome de outro aluno: ')

num = random.randint(1, 4)

if num == 1:
    apagar = aluno1
elif num == 2:
    apagar = aluno2
elif num == 3: 
    apagar = aluno3
else:
    apagar = aluno4

print('O aluno(a) escolhido foi: {} - {}'.format(num, apagar))