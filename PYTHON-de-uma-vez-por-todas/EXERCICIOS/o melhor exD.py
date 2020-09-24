from random import choice as cho


def chamaIFdaDEF(u):
    if u in selecionada:
        # print(f'UHUUUL, a letra {user} existe na palavra secreta.')
        print(' '*17, f'\033[1;42m!!!\033[m')
    else:
        # print(f'QUE PENA! a letra {user} NÃO EXISTE na palavra secreta.')
        print(' '*17, '\033[1;41m!!!\033[m')
        if len(digitadas) >= 1:
            digitadas.pop()


def continue_if(perg, *respp, separador=True):
    """
    :param perg: é a pergunta
    :param respp: opções de respostas (str)
    :param separador: True -> separa; False -> não separa
    :return: a resposta

    DESENVOLVEDOR: Silas B. Ferreira
    """

    while True:
        esta = 0
        repete = input(perg).upper()
        for r in respp:
            # print(r)
            if repete in r:
                esta = 1
            else:
                esta = 0
                # if len(repete) != 1:
        if esta == 0 or len(repete) != 1:
            if separador:
                print('-='*15)
            print(f'\033[1;33m{"Tente novamente":^30}\033[m')
            if separador:
                print('-='*15)
        else:
            return str(repete)


def intentativas(t):
    t = int(t)
    if t == 1:
        res = 4
    else:
        res = 2
    res *= lenselecionada
    return res


# SORTEAR MAIS PALAVRAS, fazer um appendedor de palavras
palavra_secreta = ['Disforme', 'Beco', 'Sol', 'Aberto', 'Ponte',
                   'Esmagamento', 'Dominoes', 'Clemente', 'Olhos',
                   'Terceiro', 'Oceano', 'Cereais', 'Contrato',
                   'Punido', 'Misto', 'Bebida', 'Odor', 'Cadeira',
                   'Pratos', 'Estufa', 'Atraente', 'Quadrado', 'Sapo',
                   'Cachorro', 'Tigre', 'Labirinto', 'Bolsa de valores'
                   ]
selecionada = cho(palavra_secreta)
lenselecionada = len(selecionada)
# print(selecionada)
selecionada = selecionada.lower()

validou = False
digitadas = []
total = []


tentativasp1 = continue_if('Selecione o modo: [1] FÁCIL, [2] SUGERIDO: ', str([1, 2, 3]))
tentativas = intentativas(tentativasp1)

cont = 1
while cont <= int(tentativas):
    # Retornar a estatistica das tentativas
    print(f'Esta é sua {cont}º tentaiva de {tentativas}')
    user = input('Digite uma letra: '.upper())
    if user.__len__() != 1:
        print('Digite apenas uma única letra. '.upper(), end='')
        # user = input('Digite uma letra: ').upper()
    for i in range(97, 123):
        if user.lower() == chr(i).lower():
            validou = True
            break
        else:
            validou = False

    if user == chr(128) or user == chr(199) or validou:
        digitadas.append(user)
        chamaIFdaDEF(user)

        total.append(user)
        # break
    else:
        print('ERRO, digite uma letra. ')
        validou = False

    # Ç 128 # Ã 199
    if len(total) >= 1:
        sectemporario = ''
        for letra_sec in selecionada:
            if letra_sec in digitadas:
                sectemporario += letra_sec
            else:
                sectemporario += '*'
        if sectemporario == selecionada:
            print('\033[1;42m ' * 40, end='\033[m\n')
            print(f'{"Parabéns, você conseguiu!!!":~^40}')
            print(f'{sectemporario:~^40}'.upper())
            break
        print(f'{"POR ENQUANTO":.^40}')
        print(sectemporario)
        print(f'{"POR ENQUANTO":.^40}')
    cont += 1

# A ESTATÍSTICA TA AQUI
for t in total:
    print(t, end='-')
for t in digitadas:
    print(t, end='..')
# FAZER ESTATÍSTICA, PROMETO QUE É A ÚLTIMA PARTE KKK


# SORTEAR MAIS PALAVRAS, WHILE TRUE
# FAZER UM APPENDEDOR DE PALAVRAS QUE APPENDE SE TIVER COM ESPAÇO