def divide(n1, n2):
    if n2 == 0:
        raise ValueError('n2 não pode ser 0')
    return n1/n2


try:
    a = divide(2, 0)
    print(a)
except ValueError as error:
    print(error)