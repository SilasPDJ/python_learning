lista = [[1, 'Silas'],
         [2, 'Dada'],
         [12, 'SilasDada'],
         [1000, 'Mamãe']
         ]

for indice, valor in lista:
    print(f'{indice} de {valor}')

li = ['Luiz', 'José', 1, 2, 3, 4, 5, 100]
p1, p2, *outro, ultimo_da_lista = li
print(outro)
print(ultimo_da_lista)

li2 = ['Luiz', 'José', 1, 2, 3, 4, 5, 100]

*primeiros, penultimo, ultimo = li2
# *_ significa que não vou utilizar o restante

print(primeiros)