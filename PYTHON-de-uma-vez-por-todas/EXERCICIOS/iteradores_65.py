carrinho = []

carrinho.append(('Produto1', 30))
carrinho.append(('Produto2', 20))
carrinho.append(('Produto3', 50))

print(carrinho)

fim = sum([valor for tupla in carrinho for valor in tupla if tupla.index(valor) == 1])
print(fim)

carrinho.append(('Produto4', '100'))
correcao = sum([float(valor) for tupla in carrinho for valor in tupla if tupla.index(valor) == 1])
print(correcao)
