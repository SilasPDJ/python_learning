lista = [1, 2, 3, 5]
print(*lista, sep='\/')

# eu posso tanto receber empacotado quanto enviar empacotado
# def test(*args)
# test(*lista)

# *args, **kwargs

def func(*args, **kwargs):
    print(args)

    nome = kwargs.get('nome')
    # nome kwargs['nome']

    if nome is not None:
        print(nome)

    # Ele pode lanaçr uma exceção dict['test']
    # mas com o get dá pra testar antes...


def dumb(*args, **keyargs):
    for arg in args:
        print(arg)
    for k in keyargs.values(): # etc, legal
        print('keyargs')
        print(k)
# dumb(nome='teste')


def func_1(*args):
    print(args)


def func_2():
    return 'TESTE', 'JETE'


A = func_1(func_2())
b = func_1(*func_2())




