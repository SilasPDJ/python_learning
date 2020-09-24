# set() não respeita ordem.., é quase uma tupla
# FAZER CAST = transformar lista em set, em tupla etc...
s1 = set()
s1.add(1)
s1.add('Python')
print(s1)
print(type(s1))

# NÃO ACEITA ELEMENTOS DUPLICADOS
# EXEMPLO:
l1 = [12,12,12,12,12,12]
print(set(l1))

# FUNÇÕES dele -> union | ; intersection & ; difference - (always in the left) ; symmetric_difference ^ (wherever)

s1 = {1, 2, 3, 4, 5}
s2 = {1, 2, 3, 4, 5, 6}

s3 = s1 | s2
print(s3)
# | -> union
# & -> e
# - > diferença elemento da esquerda
# ^ -> diferença simétrica
print(s2 ^ s1)

l1 = 'Silas', 'Damilys', 'Damilys'
l2 = 'Silas', 'Damilys', 'Silas'
if set(l1) == set(l2):
    print('L1 é igual a L2')
else:
    print('NÃO IGUAL')

# SET é muito bom rpa comparar listas