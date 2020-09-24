l1 = list(range(1, 10))
ex1 = [print(var) for var in l1]
# muito legal...

ex2 = [v * 2 for v in l1]
# print(ex2)

ex3 = [(v, v2) for v in l1 for v2 in range(3)]
# print(ex3)

l2 = ['Luiz', 'Mauro', 'Maria']
ex4 = [v.replace('a', '@') for v in l2]
print(ex4)

tupla = (
    ('chave', 'valor'),
    ('chave2', 'valor2')
)
ex5 = [(y, x) for x, y in tupla]
print(ex5)

l3 = list(range(100))
print(l3)
ex6 = [var for var in l3 if var % 2 == 0]
# if vai no final...
print(ex6)

ex7 = [v for v in l3 if v % 3 == 0 if v % 8 == 0]
print(ex7)

ex8 = [v if v % 3 == 0 else 'não tem' for v in l3]
print(ex8)