"""
For in Python
Iterando strings com for
Função range(start=0, stop, step=1)

a range não depende do for nem o for dela
"""
texto = 'Python'
for i, letra in enumerate(texto):
    print(i, letra)

for numero in range(10, 21, 2):
    print(numero)