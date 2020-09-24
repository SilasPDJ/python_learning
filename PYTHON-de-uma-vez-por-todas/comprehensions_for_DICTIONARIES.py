L1 = list(range(0, 11))

L2 = [i*2 for i in L1]
print(L2)

lista = [
    ('chave', 2),
    ('chave2', 'valor')
]
d1 = {x: y*2 for x, y in lista}
# d1 = dict(lista)
# mesmas coisas
print(d1)

d1 = {x for x in range(5)}
print(d1, type(d1))
# compreensão de conjuntos

d1 = {f'chave_{x}': x++2 for x in range(5)}
# ++ -> += ; ** -> *= (EM PYTHON)
print(d1)
