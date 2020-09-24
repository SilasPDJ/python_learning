d1 = dict(chave1='Valor da chave', chave2='Valor da outra chave')
print(d1)

print(d1['chave1'])
print(d1.get('nomedachave'))

# del d1['chave1]

# obj == obj2
# significa que se ambos apontam para o mesmo lugar da memória

lista = [
    ['c1', [1,2]],
    ['c2', [2,3]],
    ['c3', [3,4]]
]

d1 = dict(lista)
# d1.popitem()
# d1.pop('c2')
d1.update(dict(teste='KDSALDLASK', teste2='SAJFSDKJGJSDKFKSAKLDASKLASJ'))
print(d1)
