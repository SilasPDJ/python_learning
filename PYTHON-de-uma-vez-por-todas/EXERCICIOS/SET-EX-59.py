from random import randint


def armazena_var(elem, lcont):
    print(elem, '.....', lcont)

lista_de_listas_de_inteiros = []
for i in range(20):
    lista_de_listas_de_inteiros.append([])
    for cont in range(10):
        lista_de_listas_de_inteiros[i].append(randint(1, 10))


def encontra_primeiro_duplicado(param_lista_de_inteiros):
    numeros_checados = set()
    primeiro_duplicado = -1
    for numero in param_lista_de_inteiros:
        if numero in numeros_checados:
            primeiro_duplicado = numero
            break

        numeros_checados.add(numero)

    return primeiro_duplicado

print('~'*40)
for lista in lista_de_listas_de_inteiros:

    print(f'{lista}\nO número duplicado é -> {encontra_primeiro_duplicado(lista)}')
    print('~' * 40)
