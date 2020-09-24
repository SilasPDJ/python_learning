# lists, tuples, str -> Sequences -> Iterável

# for -> tempo de execução

# for utiliza o next até que esgote o elemento, o for faz o gerador automático

nome = 'Silas Bertholdo Ferreira'
iterador = iter(nome)
other_way_iterador = (letra for letra in nome)
# GENERATOR COMPREHENSION

# Sem compreensão -> yield

with open('../#########################iteradorXgerador.txt') as f:
    print(f.read())

for e, n in enumerate(iterador):
    print(n, end='')
    if e == 5:
        break


# Vou printar o restante doq sobrou/ Consumir o restante do que sobrou do meu gerador
[print(n, end='.') for n in iterador]
# Caso já tenha consumido não tem outros valores e chama excessão StopIteration
