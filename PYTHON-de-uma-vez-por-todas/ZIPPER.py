"""
Zip - Unindo iteráveis
Zip_longest - Itertools
"""
from itertools import zip_longest

### código
cidades = ['São Paulo', 'Belo Horizonte', 'Salvador', 'Monte Belo', 'zip_NaoMeUne', 'SóZipLongest', 'IterTools']

#código
estados = ['SP', 'MG', 'BA', 'MG']
# ####### O ZIP cria UM iterável

cidades_estados = zip_longest(estados, cidades, fillvalue='Estado')
print(list(cidades_estados))

cidades_estados = zip(cidades, estados)
print(list(cidades_estados))
# print(dict(cidades_estados))

# zip_longest
# TOO MANY VALUES TO UNPACK? TRY A ZIP
# o list(), tuple(), dict() também desempacota um iterável, são iteradores

# (v for v in whatever)
# -> iter(whatever)

# a string é um iterável , zip retorna um iterador
# gerador vem geralmente acompanhado do for, acho que é isso
