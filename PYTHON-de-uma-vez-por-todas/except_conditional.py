def converte_numero(n):
    try:
        n = int(n)
    except ValueError:
        try:
            n = float(n)
        except ValueError as erro:
            print(n, erro)
            return None
    return n
    # return final


while True:
    numero = converte_numero(input('Digite um número: '))

    if numero is None:
        print('Isso não é número')
    else:

        print(numero * 5)
    if isinstance(numero, int) and numero == 999:
        break
