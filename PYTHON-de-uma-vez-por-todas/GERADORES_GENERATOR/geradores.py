import sys


lista = list(range(0, 11))
print(hasattr(lista, '__iter__'))

lista = iter(lista)
print(hasattr(lista, '__next__'))
print(next(lista))
# iterável -> objeto que pode iterar sobre ele, mas não necessariamente é um iterador iter()
# iteador -> vai me dar um valor de cada vez

lista = list(range(10))
print(sys.getsizeof(lista))

# a cada vez que eu preciso de um valor o gerador me retorna ele, para que não ocupe tanto espaço da memória

# zip_longest
# TOO MANY VALUES TO UNPACK? TRY A ZIP
# o list(), tuple(), dict() também desempacota um generator

# (v for v in whatever)
# -> iter(whatever)
