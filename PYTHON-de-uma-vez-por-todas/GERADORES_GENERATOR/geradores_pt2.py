"""
####################################################################################
variavel = ((x, y) for x, y in zip('Alo', 'Hello'))
# gerador acima, GENERATOR EXPRESSION, else -> yield em def p/ geradores

todos os geradores são iteradores, mas nem todos iteradores são geradores
####################################################################################
"""


import sys
from time import sleep
# a cada vez que eu preciso de um valor o gerador me retorna ele, para que não ocupe tanto espaço da memória


def gera():

    for n in range(100):
        yield n
        # gerador
        sleep(0.1)

        # ao inves de esperar por todos os elementos na tela, ele está fazendo uma lazy evaluation
        # um valor de cada vez
        # isso através do yield

        # iteradores tem o método next(), ao contrário dos iteráveis
        ##############################################################  AQUI É UM GERADOR


g = gera()
print(g)

# CRIANDO GERADOR
lista = (x for x in range(1000))
print(type(lista))
print()
