"""
count - Itertools

####################################################################################
variavel = ((x, y) for x, y in zip('Alo', 'Hello'))
# gerador acima, GENERATOR EXPRESSION, else -> yield em def p/ geradores

todos os geradores são iteradores, mas nem todos iteradores são geradores
####################################################################################
"""

from types import GeneratorType

# count -> retorna um iterador

# variavel = zip('Alo', 'Alo')
variavel = ((x, y) for x, y in zip('Alo', 'Hello'))
# gerador acima, GENERATOR EXPRESSION, else -> yield p/ geradores

# Gerador, itereradores, iteráveis
print(variavel)
# iter(variavel)
tf = isinstance(variavel, GeneratorType)
print(tf)
input(tf)


from itertools import count
cont = count()
# iterador sem fim
# utilizando, for, while, ou seja o que for, iterador/gerador

# contador = count(start=5, step=.1)

lista = ['Silas', 'Karol', 'Emilia', 'Osiel', 'útil']
e = count()
lista = zip(e, lista)
print(tuple(lista))
