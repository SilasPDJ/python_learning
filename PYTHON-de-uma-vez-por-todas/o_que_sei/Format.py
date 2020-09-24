"""
Formatando valores com modificadores - Aula 5

:s - Texto (strings)
:d - Inteiros (int)
:f - Números de ponto flutuante (float)
:.(NÚMERO)f - Quatidade de casas decimais (float)
:(CARACTERE)(> ou < ou ^)(QUANTIDADE)(TIOPO - s, d ou f)

> - Esquerda
< - Direita
^ - Centro

"""
num1 = 19032
print(f'{num1:0>10}')
num2 = 403290
print(f'{num2:0>10}\n')

name = 'Silas'
midle_name = 'Bertholdo'
last_name = 'Ferreira'

print('{n} {m} {ll}'.format(n=name, m=midle_name, ll=last_name))
print('{0} {1} {2}'.format(name, midle_name, last_name))