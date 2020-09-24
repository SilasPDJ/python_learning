"""
São funções/expressões anônimas
"""
from random import randint

print(lambda x, y: x * y)
# print(a(2, 2))

lista = []
for i in range(1, 10+1):
    lista.append([f'P{i}', randint(10, 50)])


lista.sort(key=lambda item: item[1], reverse=False)
# lista alterada
print(lista)

print(sorted(lista, key=lambda e: e[0], reverse=True))
#lista não alterada


def func(item):
    return item[1]
lista = []
for i in range(1, 10+1):
    lista.append([f'P{i}', randint(10, 50)])
lista.sort(key=func, reverse=False)
print(lista)
print('\033[1;31mAQUI EM BAIXO É O QUE O lambda FAZ\033[m')
