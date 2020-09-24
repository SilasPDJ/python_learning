nome = str(input('Digite qual é o seu nome: '))
ln = len(nome)

if ln <= 4:
    print(f'O nome {nome} tem {ln} letras. QUE CURTO!')
elif 5 <= ln <= 6:
    print(f'O nome {nome} tem {ln} letras. NORMAL!')
elif ln > 6:
    print(f'O nome {nome} tem {ln} letras. SEU NOME É MUITO GRANDE!')
