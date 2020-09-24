def repilassa(lista_de_letras):
    lista_de_letras = str(lista_de_letras).replace(']', ',')
    lista_de_letras = lista_de_letras.replace('[', '')
    lista_de_letras = lista_de_letras.replace("'", '')

    return lista_de_letras

#pop() remove o último elemento da lista

ldl = []
cont = 5
for i in range(cont):
    while True:
        letra = input('Digite uma letra: ')
        if letra.upper().isalpha():
            if len(letra) == 1:
                ldl.append(letra)
                break
            else:
                print('TENTE NOVAMENTE!')
        else:
            print('Tente novamente')

ldl = repilassa(ldl)

print(f'As letras digitadas foram: {ldl[0:len(ldl)-1].upper()}')


