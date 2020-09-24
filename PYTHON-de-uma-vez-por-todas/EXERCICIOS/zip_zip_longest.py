lista_a = list(range(1, 8))
# lista_a = list(range(1, 100, 10))
lista_b = lista_a[:-3].copy()

# até o tamanho da lista menor
lista_soma = zip(lista_a, lista_b)
final = [sum(tupla) for tupla in lista_soma]
print(final)
# PYTHONIC
lista_soma = [x+y for (x, y) in zip(lista_a, lista_b)]
input(lista_soma)


lista_a = list(range(1, 8))
lista_b = lista_a[:-3].copy()
# unpythonic (not in a bad way, but, it's better to know pythonics way for python)
lista_soma = []
for i in range(len(lista_b)):
    soma = lista_b[i] + lista_a[i]
    lista_soma.append(soma)
print(lista_soma)


# lista_soma = [sum(tupla) for tupla in lista_soma for i in range(2) for e in range(3)]
# zoas

# TOO MANY VALUES TO UNPACK? TRY A ZIP
