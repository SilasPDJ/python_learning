import sys

l1 = [i for i in range(10000)]
print(sys.getsizeof(l1))
l2 = (i for i in range(10000))
# GENERATOR COMPREHENSHION -----> ( )

print(sys.getsizeof(l2))
# diferença entre lista e gerador
# Lista retem todos os valores que em mandar nela
# Os geradores não vão salvar todos os valores na memória, só vai entregar quando eu pedir o valor através da função next ou for

# iter() ->
