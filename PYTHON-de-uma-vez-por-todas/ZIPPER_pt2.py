from itertools import zip_longest, count
# os métodos acima são geradores, por isso consomem poucos recursos de memória

"""
zip não une valores a mais de uma lista, ele descarta, zip_longest une

count() com zip_longest() gera loop infinito
"""

# ## código
indices = count()
cidades = ['São Paulo', 'Belo Horizonte', 'Salvador', 'Monte Belo', 'zip_NaoMeUne', 'SóZipLongest', 'IterTools']

#código
estados = ['SP', 'MG', 'BA', 'MG']

# ####### O ZIP cria UM ITERADOR
cidades_estados = zip(indices,
                      estados,
                      cidades)

[print(indice, estado, cidade) for indice, estado, cidade in cidades_estados]
# [print(valor) for valor in cidades_estados]
# ele conta infinito, zip_longest com ITERADOR, as duas funções entram em conflito, nesse caso é melhor a função zip

# TOO MANY VALUES TO UNPACK? TRY A ZIP
